# Scientific author self-review of Zero-self flattened slice sampling

- Review: 20261014T220151Z-zero-self-flattened-slice-sampling
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T21:41:45.569038Z
- Finished UTC: 2026-10-14T22:01:51.891201Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The finite Zero-self flattened slice sampling record is supported within its stated source and exact-calculation scope. DRAFT is retained; source errors, ordering conventions, boundary behavior and convergence limits remain explicit.

## Scope And Provenance

All maintained fields of the selected record. Actual source scope: Selective primary method/context reading; cumulative root text1–51 of84 pages with recorded selected visual pages. Fresh post-capture text41,43–47,51 and visual42,46.. The bar construction, blocker policy and Algorithms8–9 support the maintained mechanisms. Eq112–114 require positive-support uniqueness. Printed Figure10 and Algorithm9 caveats are retained. Reading does not cover all empirical or antecedent proofs; current exact checks are curator-written mathematical evidence.

Selection: Exact maintained ID: AIMech:ZeroSelfFlattenedSliceSampling
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f7209818aea9b23fad74ee708675f39995941c00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ZeroSelfFlattenedSliceSampling | data/curated/ZeroSelfFlattenedSliceSampling.yaml | maintained | Zero-self flattened slice sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 555.67s (0:09:15)<br>Checked 442 record(s); 0 failed.<br>Checked 708 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 396 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 400,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| just render | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages<br>uv run --locked python scripts/render_pages.py<br> |
| just render-check | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | pages/ is current<br>uv run --locked python scripts/render_pages.py --check<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | Actual command exited zero without output. |
| python3 research/discovery/fss-zfss-boundaries.py | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | {<br>  "case_generation": "All distinct nonnegative rational probability vectors with 1\u20136 states obtained from ordered weak compositions of totals1\u20138; plus explicit Figure10, strict half-neighbors, irregular ties and zero-mass cases.",<br>  "counts": {<br>    "FSS_nonminimal_self": 297,<br>    "FSS_reversible": 2661,<br>    "ZFSS_nonminimal_self": 0,<br>    "ZFSS_reversible": 2661,<br>    "distributions": 4450,<br>    "distributions_FSS_ZFSS_distinct": 297,<br>    "endpoint_checks": 97160,<br>    "endpoint_zero_probability_outputs": 998,<br>    "half_boundary_kernels": 1862,<br>    "integrated_sampler_rows": 48580,<br>    "integrated_uniform_cells": 108028,<br>    "invalid_probability_vectors_rejected": 4,<br>    "kernels": 8900,<br>    "point_mass_kernels": 42,<br>    "sampler_executions": 145176,<br>    "tied_max_kernels": 1810,<br>    "zero_mass_rows": 18792<br>  },<br>  "differences": [],<br>  "endpoint_zero_probability_outputs": [<br>    {<br>      "current_0based": 2,<br>      "method": "FSS",<br>      "range": [<br>        "0",<br>        "1"<br>      ],<br>      "returned_0based": 2,<br>      "row": [<br>        "1/4",<br>        "3/4",<br>        "0"<br>      ],<br>      "target": [<br>        "1/8",<br>        "3/8",<br>        "1/2"<br>      ],<br>      "uniform": "1"<br>    },<br>    {<br>      "current_0based": 2,<br>      "method": "ZFSS",<br>      "range": [<br>        "0",<br>        "1"<br>      ],<br>      "returned_0based": 2,<br>      "row": [<br>        "1/4",<br>        "3/4",<br>        "0"<br>      ],<br>      "target": [<br>        "1/8",<br>        "3/8",<br>        "1/2"<br>      ],<br>      "uniform": "1"<br>    },<br>    {<br>      "current_0based": 2,<br>      "method": "FSS",<br>      "range": [<br>        "0",<br>        "1"<br>      ],<br>      "returned_0based": 2,<br>      "row": [<br>        "1/3",<br>        "2/3",<br>        "0"<br>      ],<br>      "target": [<br>        "1/6",<br>        "1/3",<br>        "1/2"<br>      ],<br>      "uniform": "1"<br>    },<br>    {<br>      "current_0based": 2,<br>      "method": "ZFSS",<br>      "range": [<br>        "0",<br>        "1"<br>      ],<br>      "returned_0based": 2,<br>      "row": [<br>        "1/3",<br>        "2/3",<br>        "0"<br>      ],<br>      "target": [<br>        "1/6",<br>        "1/3",<br>        "1/2"<br>      ],<br>      "uniform": "1"<br>    },<br>    {<br>      "current_0based": 2,<br>      "method": "FSS",<br>      "range": [<br>        "0",<br>        "1"<br>      ],<br>      "returned_0based": 2,<br>      "row": [<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ],<br>      "target": [<br>        "1/4",<br>        "1/4",<br>        "1/2"<br>      ],<br>      "uniform": "1"<br>    },<br>    {<br>      "current_0based": 2,<br>      "method": "ZFSS",<br>      "range": [<br>        "0",<br>        "1"<br>      ],<br>      "returned_0based": 2,<br>      "row": [<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ],<br>      "target": [<br>        "1/4",<br>        "1/4",<br>        "1/2"<br>      ],<br>      "uniform": "1"<br>    }<br>  ],<br>  "figure10": {<br>    "FSS_verified": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1/4",<br>        "0",<br>        "0",<br>        "0",<br>        "3/4"<br>      ],<br>      [<br>        "0",<br>        "1/2",<br>        "0",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1/9",<br>        "2/9",<br>        "4/9",<br>        "1/9",<br>        "1/9"<br>      ]<br>    ],<br>    "SS_printed": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1/2",<br>        "0",<br>        "0",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1/3",<br>        "1/9",<br>        "5/9"<br>      ]<br>    ],<br>    "ZFSS_calculated_three_ways": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1/7",<br>        "0",<br>        "0",<br>        "0",<br>        "6/7"<br>      ],<br>      [<br>        "0",<br>        "2/7",<br>        "0",<br>        "1/14",<br>        "9/14"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "10/63",<br>        "20/63",<br>        "4/9",<br>        "5/63",<br>        "0"<br>      ]<br>    ],<br>    "ZFSS_printed_nonstationary": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1/4",<br>        "0",<br>        "0",<br>        "0",<br>        "3/4"<br>      ],<br>      [<br>        "0",<br>        "1/2",<br>        "0",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "10/63",<br>        "20/63",<br>        "4/9",<br>        "5/63",<br>        "0"<br>      ]<br>    ],<br>    "matrix_rows_in_original_state_order": true,<br>    "printed_ZFSS_stationarity_residual": [<br>      "3/140",<br>      "3/70",<br>      "0",<br>      "-1/70",<br>      "-1/20"<br>    ],<br>    "printed_ZFSS_target_after_one_step": [<br>      "17/140",<br>      "17/70",<br>      "1/5",<br>      "1/28",<br>      "2/5"<br>    ],<br>    "source_caveat": "The printed ZFSS matrix rows2 and3 retain FSS entries and fail stationarity. Its final row agrees with Algorithms8\u20139 and geometric calculation. This script preserves the printed matrix as a negative control, not a valid kernel.",<br>    "stationary_self_correct_kernels": [<br>      "1/4",<br>      "1/20",<br>      "0"<br>    ],<br>    "target": [<br>      "1/10",<br>      "1/5",<br>      "1/5",<br>      "1/20",<br>      "9/20"<br>    ]<br>  },<br>  "first_distinct_kernel": {<br>    "FSS": [<br>      [<br>        "0",<br>        "3/7",<br>        "2/7",<br>        "2/7"<br>      ],<br>      [<br>        "0",<br>        "1/6",<br>        "1/6",<br>        "2/3"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1/4",<br>        "3/4",<br>        "0"<br>      ]<br>    ],<br>    "ZFSS": [<br>      [<br>        "0",<br>        "3/7",<br>        "2/7",<br>        "2/7"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1/3",<br>        "2/3"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ]<br>    ],<br>    "target": [<br>      "0",<br>      "3/7",<br>      "2/7",<br>      "2/7"<br>    ]<br>  },<br>  "sampler_interpretation": "Algorithm9 zero-current CDF branch interpreted without its ambiguous outer For line. Ordinary continuous uniform inputs integrated exactly; closed endpoints checked separately.",<br>  "scope": "Three original exact finite constructions. No author code executed; no general theorem or floating-point implementation verification.",<br>  "uniform_periodicity": {<br>    "2": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 2<br>    },<br>    "3": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 3<br>    },<br>    "4": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 4<br>    },<br>    "5": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 5<br>    },<br>    "6": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 6<br>    },<br>    "7": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 7<br>    },<br>    "8": {<br>      "deterministic_predecessor_cycle": true,<br>      "period": 8<br>    }<br>  }<br>}<br> |
| python3 research/discovery/fss-zfss-extra-boundaries.py | passed | True | AIMech:ZeroSelfFlattenedSliceSampling | {<br>  "endpoint_counterexamples": [<br>    {<br>      "current_state_1based": 3,<br>      "method": "FSS",<br>      "returned_state_1based": 3,<br>      "returned_transition_probability": "0",<br>      "row": [<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ],<br>      "target": [<br>        "1/4",<br>        "1/4",<br>        "1/2"<br>      ],<br>      "uniform_value": "1"<br>    },<br>    {<br>      "current_state_1based": 3,<br>      "method": "ZFSS",<br>      "returned_state_1based": 3,<br>      "returned_transition_probability": "0",<br>      "row": [<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ],<br>      "target": [<br>        "1/4",<br>        "1/4",<br>        "1/2"<br>      ],<br>      "uniform_value": "1"<br>    }<br>  ],<br>  "figure10_simple_slice": {<br>    "agrees_with_printed_matrix": true,<br>    "matrix": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1/2",<br>        "0",<br>        "0",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1/3",<br>        "1/9",<br>        "5/9"<br>      ]<br>    ],<br>    "target": [<br>      "1/10",<br>      "1/5",<br>      "1/5",<br>      "1/20",<br>      "9/20"<br>    ]<br>  },<br>  "joint_compositions": [<br>    {<br>      "both_coordinate_kernels_stationary": true,<br>      "fixed_mixture_matrix": [<br>        [<br>          "0",<br>          "0",<br>          "2/3",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "2/9",<br>          "0",<br>          "4/9",<br>          "0",<br>          "2/15",<br>          "0",<br>          "0",<br>          "1/5",<br>          "0"<br>        ],<br>        [<br>          "1/3",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "1/6",<br>          "0",<br>          "0",<br>          "1/6"<br>        ],<br>        [<br>          "1/9",<br>          "0",<br>          "0",<br>          "0",<br>          "4/9",<br>          "2/9",<br>          "2/9",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0",<br>          "0",<br>          "0",<br>          "1/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/3",<br>          "2/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/9",<br>          "0",<br>          "4/9",<br>          "1/9",<br>          "2/9"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0"<br>        ]<br>      ],<br>      "fixed_mixture_reversible": true,<br>      "fixed_mixture_stationary": true,<br>      "fixed_scan_matrix": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "2/5",<br>          "0",<br>          "0",<br>          "2/5",<br>          "0",<br>          "1/5"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0",<br>          "1/3"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0",<br>          "0",<br>          "2/9",<br>          "0",<br>          "1/9"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "fixed_scan_reversible": false,<br>      "fixed_scan_stationary": true,<br>      "joint_target_row_major_3x3": [<br>        "1/15",<br>        "0",<br>        "2/15",<br>        "1/5",<br>        "2/15",<br>        "1/15",<br>        "2/15",<br>        "1/5",<br>        "1/15"<br>      ],<br>      "method": "FSS"<br>    },<br>    {<br>      "both_coordinate_kernels_stationary": true,<br>      "fixed_mixture_matrix": [<br>        [<br>          "0",<br>          "0",<br>          "2/3",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "2/9",<br>          "0",<br>          "4/9",<br>          "0",<br>          "2/15",<br>          "0",<br>          "0",<br>          "1/5",<br>          "0"<br>        ],<br>        [<br>          "1/3",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "1/6",<br>          "0",<br>          "0",<br>          "1/6"<br>        ],<br>        [<br>          "1/9",<br>          "0",<br>          "0",<br>          "0",<br>          "4/9",<br>          "2/9",<br>          "2/9",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0",<br>          "0",<br>          "0",<br>          "1/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/3",<br>          "2/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/9",<br>          "0",<br>          "4/9",<br>          "1/9",<br>          "2/9"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0"<br>        ]<br>      ],<br>      "fixed_mixture_reversible": true,<br>      "fixed_mixture_stationary": true,<br>      "fixed_scan_matrix": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "2/5",<br>          "0",<br>          "0",<br>          "2/5",<br>          "0",<br>          "1/5"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0",<br>          "1/3"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "1/3",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "2/3",<br>          "0",<br>          "0",<br>          "2/9",<br>          "0",<br>          "1/9"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "fixed_scan_reversible": false,<br>      "fixed_scan_stationary": true,<br>      "joint_target_row_major_3x3": [<br>        "1/15",<br>        "0",<br>        "2/15",<br>        "1/5",<br>        "2/15",<br>        "1/15",<br>        "2/15",<br>        "1/5",<br>        "1/15"<br>      ],<br>      "method": "ZFSS"<br>    }<br>  ],<br>  "scope": "Supplementary curator rational calculations; uses the independently authored algorithms of the base audit, never author software.",<br>  "systematic_scan_counterexample": {<br>    "joint_target": "Uniform independent 3x3 coordinates",<br>    "meaning": "Both FSS and ZFSS preserve the target but a deterministic full scan is reducible. Zero self transitions do not guarantee convergence from every initial state.",<br>    "period_within_class": 3,<br>    "three_closed_classes_0based_row_major": [<br>      [<br>        0,<br>        4,<br>        8<br>      ],<br>      [<br>        2,<br>        3,<br>        7<br>      ],<br>      [<br>        1,<br>        5,<br>        6<br>      ]<br>    ],<br>    "transition": "(a,b) -&gt; (a-1 mod3,b-1 mod3) each full scan"<br>  },<br>  "zero_label_order_effect": {<br>    "FSS_after_deleting_zero_label": [<br>      [<br>        "0",<br>        "1/3",<br>        "2/3"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ]<br>    ],<br>    "FSS_positive_rows_with_zero_label": [<br>      [<br>        "1/6",<br>        "1/6",<br>        "2/3"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1/4",<br>        "3/4",<br>        "0"<br>      ]<br>    ],<br>    "ZFSS_same_after_this_deletion": true,<br>    "meaning": "Do not silently delete zero-probability labels before applying FSS: the immediate predecessor excluded from mass redistribution is part of the specified order. This example distinguishes support preservation from kernel identity.",<br>    "positive_target": [<br>      "3/7",<br>      "2/7",<br>      "2/7"<br>    ],<br>    "target_with_leading_zero": [<br>      "0",<br>      "3/7",<br>      "2/7",<br>      "2/7"<br>    ]<br>  },<br>  "zero_row_nonuniqueness": {<br>    "alternative_invariant_kernel": [<br>      [<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "both_reversible_and_minimal_self": true,<br>    "meaning": "Uniqueness of Eq112 is on positive support; a zero-mass row is not determined by stationarity. Algorithm8 explicitly sets that row to the target law.",<br>    "published_algorithm8_kernel": [<br>      [<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ]<br>    ],<br>    "target": [<br>      "1/2",<br>      "1/2",<br>      "0"<br>    ]<br>  }<br>}<br> |

## Scientific And Domain Assessments

### Zero-self flattened slice sampling

identity: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Retain the narrow DRAFT identity within the documented search scope.

ZFSS is the named ZERO=true blocker policy, rather than every minimum-self conditional kernel or an exact alias of FSS. Shared code and dominant/zero-current branches do not equate the two positive-support kernels in general. It is distinct from generic Gibbs/slice, interval and elliptical methods, Liu conditional exclusion and augmented pair/sign/direction methods. Broader antithetic/NAM source families remain separate open identity research; no source-wide import is implied.

### Definition and source scope

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

The maintained definition is supported within its stated method scope.

The definition identifies finite ZFSS as the specific blocker-relocation policy followed by the flattened-bar predecessor update. Avoidable self transitions are removed, with the dominant-mass exception explicit in the claims. The primary evidence is the independently pinned author-hosted report dated 26 March 2024, 84 PDF pages. Section 11 and Algorithms 8–9 on pp. 41–47 define the finite kernels and their implementations; pp. 2–3 support conditional composition, and pp. 49–51 discuss boundary behavior. Reading is selective. Original source equations and curator analytic deductions are distinguished from bounded exact calculations. The printed Figure 10 ZFSS matrix fails its stated stationarity test; that source discrepancy is preserved rather than silently corrected. Neither arXiv-byte equivalence nor author-code execution is claimed.

### Related Markov-process mapping

grounding: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

related_match expresses method-to-process association without equivalence or ontology inheritance.

The related_match to AIO:MarkovChain is a method-to-process association. The exact pinned CLASS denotes a stochastic process/model, exported under Network with a ProbabilisticHiddenLayer relation. Conditional transition construction supports the association but not equivalence, subclass membership or inherited neural assertions. Eighteen complete AIO class contexts and their generated records ground the selected mapping and seventeen rejected alternatives.
Alternatives:
AIO:Network: Interconnected entities/model superclass; no sampling procedure identity or subtype claim follows.
AIO:ProbabilisticHiddenLayer: Categorical probability estimation in a neural hidden layer differs from a conditional-invariant transition.
AIO:Model: Abstract model superclass is not the specific algorithm; no exact or forced broad mapping.
AIO:MachineLearningTask: General learning task differs from the sampling procedure.
AIO:TrainingStrategy: Training/preprocessing family differs from finite conditional Markov updates.
AIO:MathematicalFunction: Generic rule/function does not identify this stochastic transition algorithm.
AIO:BayesianNetwork: DAG probability model can be an application target, not the sampler.
AIO:ProbabilisticGraphicalModel: Conditional dependence model/task differs from inference updates.
AIO:UnsupervisedLearning: Learning patterns from unlabeled data is not the defining sampling mechanism.
AIO:BoltzmannMachineNetwork: An application/model family rather than the conditional transition procedure.
AIO:RestrictedBoltzmannMachine: Restricted neural energy model is not the algorithm.
AIO:EnergyBasedLLM: Language-model energy construction does not define these generic categorical kernels.
AIO:ImplicitLanguageModel: Sequence scoring/model class rather than a finite conditional update.
AIO:Preprocessing: Rearranging auxiliary probability bars is not dataset preprocessing.
AIO:Layer: Neural topology/component is a different abstraction.
AIO:HiddenLayer: Nonlinear network transformation is not conditional Markov sampling.
AIO:CausalGraphicalModel: Causal assumptions/graph model are not sampler identity or an entailed application.

### blocking-state-and-flattened-bars

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Supported within the stated assumptions and inspected passages.

Algorithm 8 ZERO=true scans backward cyclically for the nearest b satisfying pi(b)&gt;=f*s, recalculating f=(h-s)/(1-h-pi(b)) for each candidate. For h&lt;1/2, 0&lt;=f&lt;1 and a second-largest label qualifies, so the search terminates. Moving b immediately before a retains all remaining relative order. The same height-s original bar and added a-labelled pieces define the transition. This specific blocker policy, rather than arbitrary order optimization, identifies ZFSS.

### invariance-and-avoided-self-transitions

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Supported within the stated assumptions and inspected passages.

The height-preserving bar split and cyclic predecessor permutation establish invariance. Added a pieces are no taller than preceding original bars, so departure from those pieces changes the label. For the original a bar, the relocated blocker catches motion below its height; above it, all added a pieces are inactive because their heights are bounded by f*s&lt;=pi(b). Hence regular-case self probabilities vanish. Valid conditional mixtures/compositions preserve the joint target, without a general reversibility or convergence conclusion.

### dominant-mass-and-zero-state-conventions

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Supported within the stated assumptions and inspected passages.

Algorithm 8 p. 44 checks zero current mass first and assigns the row pi. For h&gt;=1/2 and a supported current label, nonmaximum labels move to a while P(a,a)=(2h-1)/h and P(a,j)=pi(j)/h. Detailed balance holds on positive support, with total self mass 2h-1; h=1/2 and h=1 are explicit boundaries. Eq. 112 uniqueness must be restricted to positive support because invariant weighting does not determine a zero-mass row. The alternative third row(1,0,0) for pi=(1/2,1/2,0) is a concrete check. The term zero-self eliminates avoidable self transitions; dominant h&gt;1/2 requires positive stationary self mass. It does not claim every row diagonal vanishes for every target.

### finite-checks-and-printed-matrix-discrepancy

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Supported within the stated assumptions and inspected passages.

The4,450-target suite verifies target invariance and minimum self mass in each tested ZFSS case. Raw Figure 10 ZFSS rows 2/3 instead produce target pushforward(17/140,17/70,1/5,1/28,2/5), so the printed matrix is a negative control. Algorithm 8 and independent geometry give row 2=(1/7,0,0,0,6/7) and row 3=(0,2/7,0,1/14,9/14); the printed last row agrees. The source error is explicit and does not become an author-issued erratum, universal theorem or runtime-replication claim.

### kernel-distinction-and-periodicity

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Supported within the stated assumptions and inspected passages.

The saved suite finds 297 target inputs with different FSS and ZFSS transition matrices, demonstrating separate kernel identities despite agreement when relocation is unnecessary and in the shared dominant branch. For equal finite weights, predecessor motion forms a deterministic cycle of period m. For two independent uniform three-state coordinates, a fixed full scan subtracts one from both coordinates modulo 3, preserving a-b and leaving three closed classes. The target remains invariant while a single trajectory does not explore all classes. Neither removed self transitions nor invariance alone imply ergodicity, improved finite-run error, asymptotic variance or runtime.

### fast-sampler-interpretation-limits

evidence: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Supported within the stated assumptions and inspected passages.

Algorithm 8 defines the maintained probability kernel. The Algorithm 9 calculation interprets its ambiguous zero-current outer loop as a single inverse-CDF traversal; it is not a claim that literal printed control flow was replicated. At pi=(1/4,1/4,1/2), k=3, r=1, the closed endpoint returns state 3 although P33=0. That event is null under ideal continuous uniform sampling, so it does not refute the ideal law, but it rules out an unconditional closed-endpoint/floating-point guarantee. The original publication remains unmodified.

### Finite conditional kernels, supplied ordering, source-error handling and composed-scan limits

consistency: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Mechanism, scan/parameter limits and identity boundaries remain qualified.

Scope is finite ordered labels and an exact nonnegative normalized conditional law, with the first-maximizer and zero-current conventions retained. A zero-mass current value does not supply an undefined zero-total conditioning law. Countably infinite extensions, adaptive order changes, floating-point stability, general convergence and benchmark superiority are outside scope. Minimum self mass is not a guarantee of aperiodicity, irreducibility or lower asymptotic variance. The 84-page report and its cited antecedent proofs/empirical sections were not wholly read.

### All captured maintained fields

provenance: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

Root reassessed the complete current record after canonical capture; DRAFT remains.

Root fully read both actual maintained YAML records after canonical capture, all prepared claim/mapping narratives, actual report delta, history and integrity result. All six claims and source locators are scoped to exact finite normalized conditional kernels. Related AIO:MarkovChain is a method/process association; no inherited neural assertions or alias equivalence. Original precise retrieval timestamp remains in the raw manifest; canonical source metadata truncates to schema whole seconds, with the prewrite validation failure preserved. Original/portable calculator derivation and failed printed-Figure10 comparison remain explicit. No author implementation, empirical replication, independent approval or saturation claim. Actual DRAFT status and source/version limits retained. No new maintained-record finding found. ZFSS uses the nearest backward qualifying blocker with recomputed factor and preserved remaining order. Added pieces cannot exceed preceding originals; the blocker eliminates regular-case self transitions. Dominant mass requires2h-1 stationary self mass. Printed Figure10 ZFSS rows2/3 are explicitly nonstationary; corrected calculations are curator evidence, not an author erratum. Rereads: Neal author report text PDF pp41,43–47,51 and visual pp42,46. Visual42 confirms actual printed comparison rows; visual46 confirms the ambiguous zero-current outer loop and r&gt;=s endpoint. Earlier text1–51 and selected visual readings are retained, not all claimed freshly reread.

### Raw source discrepancy and exact calculator derivation

provenance: supported. Targets: AIMech:ZeroSelfFlattenedSliceSampling.

The source discrepancy and original-to-portable lineage remain explicit.

Figure 10 printed ZFSS rows are retained as a negative control, not silently replaced or labeled an author erratum. Algorithm 9 loop/endpoint limits are qualified. Original and portable mathematical results agree after only declared metadata exclusions; source reading and execution scopes remain separately attributed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T213822Z-flattened-slice-sampling.json; identity_search and identity_assessment | supports | The post312 assessment covers all 442 pinned AIO and 706 native IDs, names, aliases and scoped synonyms, plus four complete checkout searches including ignored and hidden files. The maintained identity is a finite ordered conditional kernel, distinct from generic slice/Gibbs, interval and elliptical slice procedures, MH-within-Gibbs and persistent-sign/pair-state samplers. Earlier 703-native searches and 18 exact AIO contexts are preserved with their reading scopes; the three actual batch312 native neighbors were assessed for this identity comparison. AIO:MarkovChain is related_match at a different abstraction level; no neural Network or ProbabilisticHiddenLayer inheritance is implied. ZFSS denotes the nearest-qualifying-blocker ZERO=true policy. It differs from FSS for positive-probability transitions, while sharing special cases. Zero-self means removal of avoidable self transitions; it is not an exact alias for arbitrary minimum-self kernels. No aliases are adopted. |
| mapping | research/discovery/20261014T213822Z-flattened-slice-sampling.json; mapping_context nodes, historical semantic/native contexts, actual312_neighbors and mapping_assessment | supports | The related_match to AIO:MarkovChain is a method-to-process association. The exact pinned CLASS denotes a stochastic process/model, exported under Network with a ProbabilisticHiddenLayer relation. Conditional transition construction supports the association but not equivalence, subclass membership or inherited neural assertions. Eighteen complete AIO class contexts and their generated records ground the selected mapping and seventeen rejected alternatives. |
| actual-record-reading | data/curated/ZeroSelfFlattenedSliceSampling.yaml | supports | Root fully read both actual maintained YAML records after canonical capture, all prepared claim/mapping narratives, actual report delta, history and integrity result. All six claims and source locators are scoped to exact finite normalized conditional kernels. Related AIO:MarkovChain is a method/process association; no inherited neural assertions or alias equivalence. Original precise retrieval timestamp remains in the raw manifest; canonical source metadata truncates to schema whole seconds, with the prewrite validation failure preserved. Original/portable calculator derivation and failed printed-Figure10 comparison remain explicit. No author implementation, empirical replication, independent approval or saturation claim. Actual DRAFT status and source/version limits retained. No new maintained-record finding found. ZFSS uses the nearest backward qualifying blocker with recomputed factor and preserved remaining order. Added pieces cannot exceed preceding originals; the blocker eliminates regular-case self transitions. Dominant mass requires2h-1 stationary self mass. Printed Figure10 ZFSS rows2/3 are explicitly nonstationary; corrected calculations are curator evidence, not an author erratum. Actual post-capture source reread: Neal author report text PDF pp41,43–47,51 and visual pp42,46. Visual42 confirms actual printed comparison rows; visual46 confirms the ambiguous zero-current outer loop and r&gt;=s endpoint. Earlier text1–51 and selected visual readings are retained, not all claimed freshly reread. |
| neal2024 | https://glizen.com/radfordneal/ftp/gibbs-self.pdf; Section 11, PDF pp. 42–43, ZFSS reordering; Algorithm 8, pp. 44–45, ZERO true; Section 11, PDF pp. 42–43, blocker construction; Algorithm 8, pp. 44–45, ZERO true; Section 11, PDF pp. 41–43, invariant-slice framework and blocker argument; Section 2, pp. 2–3, Equations 2–4; geometric calculations in research/discovery/fss-zfss-boundaries.py; Algorithm 8 Part 1, PDF p. 44, zero-current and dominant-mass branches; Section 13, p. 51, Equations 112–114; exact support example in research/discovery/fss-zfss-extra-boundaries.py; Figure 10, PDF p. 42, rightmost matrix; Algorithms 8–9, pp. 44–47; original curator calculations in research/discovery/fss-zfss-boundaries.py; Section 11, PDF pp. 42–43, FSS/ZFSS distinction; Section 13, pp. 49–51, uniform cycles and common boundary kernel; exact examples in research/discovery/fss-zfss-boundaries.py and research/discovery/fss-zfss-extra-boundaries.py; Algorithm 9 Part 1, PDF p. 46, output guarantee, zero-current loop and dominant-mass CDF; endpoint checks in research/discovery/fss-zfss-extra-boundaries.py | supports | Author-hosted technical report dated 26 March 2024; 84 PDF pages. Independently pinned from arXiv:2403.18054v1; byte equivalence between versions is not asserted. Actual root reading: The bar construction, blocker policy and Algorithms8–9 support the maintained mechanisms. Eq112–114 require positive-support uniqueness. Printed Figure10 and Algorithm9 caveats are retained. Reading does not cover all empirical or antecedent proofs; current exact checks are curator-written mathematical evidence. |
| calculation-main | research/discovery/fss-zfss-boundaries.py; Saved report curator_calculations; counts, figure10, uniform_periodicity | supports | Exact Fraction original curator calculations, with actual copied-script outputs checked against the full saved results. No author-code execution, benchmark replication or universal proof. Selected results: {"counts": {"FSS_nonminimal_self": 297, "FSS_reversible": 2661, "ZFSS_nonminimal_self": 0, "ZFSS_reversible": 2661, "distributions": 4450, "distributions_FSS_ZFSS_distinct": 297, "endpoint_checks": 97160, "endpoint_zero_probability_outputs": 998, "half_boundary_kernels": 1862, "integrated_sampler_rows": 48580, "integrated_uniform_cells": 108028, "invalid_probability_vectors_rejected": 4, "kernels": 8900, "point_mass_kernels": 42, "sampler_executions": 145176, "tied_max_kernels": 1810, "zero_mass_rows": 18792}, "figure10": {"FSS_verified": [["0", "0", "0", "0", "1"], ["1/4", "0", "0", "0", "3/4"], ["0", "1/2", "0", "0", "1/2"], ["0", "0", "0", "0", "1"], ["1/9", "2/9", "4/9", "1/9", "1/9"]], "SS_printed": [["0", "0", "0", "0", "1"], ["1/2", "0", "0", "0", "1/2"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "1/3", "1/9", "5/9"]], "ZFSS_calculated_three_ways": [["0", "0", "0", "0", "1"], ["1/7", "0", "0", "0", "6/7"], ["0", "2/7", "0", "1/14", "9/14"], ["0", "0", "0", "0", "1"], ["10/63", "20/63", "4/9", "5/63", "0"]], "ZFSS_printed_nonstationary": [["0", "0", "0", "0", "1"], ["1/4", "0", "0", "0", "3/4"], ["0", "1/2", "0", "0", "1/2"], ["0", "0", "0", "0", "1"], ["10/63", "20/63", "4/9", "5/63", "0"]], "matrix_rows_in_original_state_order": true, "printed_ZFSS_stationarity_residual": ["3/140", "3/70", "0", "-1/70", "-1/20"], "printed_ZFSS_target_after_one_step": ["17/140", "17/70", "1/5", "1/28", "2/5"], "source_caveat": "The printed ZFSS matrix rows2 and3 retain FSS entries and fail stationarity. Its final row agrees with Algorithms8–9 and geometric calculation. This script preserves the printed matrix as a negative control, not a valid kernel.", "stationary_self_correct_kernels": ["1/4", "1/20", "0"], "target": ["1/10", "1/5", "1/5", "1/20", "9/20"]}, "uniform_periodicity": {"2": {"deterministic_predecessor_cycle": true, "period": 2}, "3": {"deterministic_predecessor_cycle": true, "period": 3}, "4": {"deterministic_predecessor_cycle": true, "period": 4}, "5": {"deterministic_predecessor_cycle": true, "period": 5}, "6": {"deterministic_predecessor_cycle": true, "period": 6}, "7": {"deterministic_predecessor_cycle": true, "period": 7}, "8": {"deterministic_predecessor_cycle": true, "period": 8}}} |
| calculation-extra | research/discovery/fss-zfss-extra-boundaries.py; Saved report curator_calculations; endpoint_counterexamples, zero_row_nonuniqueness, zero_label_order_effect, systematic_scan_counterexample | supports | Exact Fraction original curator calculations, with actual copied-script outputs checked against the full saved results. No author-code execution, benchmark replication or universal proof. Selected results: {"endpoint_counterexamples": [{"current_state_1based": 3, "method": "FSS", "returned_state_1based": 3, "returned_transition_probability": "0", "row": ["1/2", "1/2", "0"], "target": ["1/4", "1/4", "1/2"], "uniform_value": "1"}, {"current_state_1based": 3, "method": "ZFSS", "returned_state_1based": 3, "returned_transition_probability": "0", "row": ["1/2", "1/2", "0"], "target": ["1/4", "1/4", "1/2"], "uniform_value": "1"}], "zero_row_nonuniqueness": {"alternative_invariant_kernel": [["0", "1", "0"], ["1", "0", "0"], ["1", "0", "0"]], "both_reversible_and_minimal_self": true, "meaning": "Uniqueness of Eq112 is on positive support; a zero-mass row is not determined by stationarity. Algorithm8 explicitly sets that row to the target law.", "published_algorithm8_kernel": [["0", "1", "0"], ["1", "0", "0"], ["1/2", "1/2", "0"]], "target": ["1/2", "1/2", "0"]}, "zero_label_order_effect": {"FSS_after_deleting_zero_label": [["0", "1/3", "2/3"], ["1", "0", "0"], ["1/2", "1/2", "0"]], "FSS_positive_rows_with_zero_label": [["1/6", "1/6", "2/3"], ["1", "0", "0"], ["1/4", "3/4", "0"]], "ZFSS_same_after_this_deletion": true, "meaning": "Do not silently delete zero-probability labels before applying FSS: the immediate predecessor excluded from mass redistribution is part of the specified order. This example distinguishes support preservation from kernel identity.", "positive_target": ["3/7", "2/7", "2/7"], "target_with_leading_zero": ["0", "3/7", "2/7", "2/7"]}, "systematic_scan_counterexample": {"joint_target": "Uniform independent 3x3 coordinates", "meaning": "Both FSS and ZFSS preserve the target but a deterministic full scan is reducible. Zero self transitions do not guarantee convergence from every initial state.", "period_within_class": 3, "three_closed_classes_0based_row_major": [[0, 4, 8], [2, 3, 7], [1, 5, 6]], "transition": "(a,b) -&gt; (a-1 mod3,b-1 mod3) each full scan"}} |
| source-math-provenance | research/discovery/20261014T213822Z-flattened-slice-sampling.json; source_analysis.handoffs.source_math, root_readings and writer_preparation_reading | supports | Root assessed the separately attributed selective source readings and bounded mathematical research. Supporting agents are in the same author workflow and provide no independent scientific approval. |
| source-error-portable-lineage | research/discovery/20261014T213822Z-flattened-slice-sampling.json; calculation_lineage, curator_calculations.original and source_analysis.root_readings.figure10 | supports | The raw printed Figure 10 ZFSS matrix and initial failed comparison are retained as source-error evidence. Algorithms and independently derived geometry give different corrected rows, without an author-issued erratum claim. Original scripts/results, metadata-only portable derivation and recorded executions are preserved; both portable scripts retain their fixed sibling relationship. |

## Limits And Additional Notes

- Author self-review, not independent scientific approval or DRAFT promotion.
- Scope is finite ordered labels and an exact nonnegative normalized conditional law, with the first-maximizer and zero-current conventions retained. A zero-mass current value does not supply an undefined zero-total conditioning law. Countably infinite extensions, adaptive order changes, floating-point stability, general convergence and benchmark superiority are outside scope. Minimum self mass is not a guarantee of aperiodicity, irreducibility or lower asymptotic variance. The 84-page report and its cited antecedent proofs/empirical sections were not wholly read.
- Bounded exact Fraction calculations are original curator checks, not author software or a general proof.
- Source, identity and mathematical supporting agents belong to the same author workflow; this remains author self-review.
- Historical703-native identity/source handoffs remain attributed; current prewrite706-native inventory, searches and actual neighbors govern the added identities.
- The raw failed Figure 10 comparison, corrected negative-control interpretation and original-to-portable calculator lineage remain explicit.
- Empty findings reflect actual root assessment of this selected captured record only; no unrelated finding closure or literature saturation is asserted.
- A publication matrix discrepancy is retained as a source limitation; no maintained-record finding or issue closure is invented from that discrepancy.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T220151Z-zero-self-flattened-slice-sampling
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Zero-self flattened slice sampling
started_at: '2026-10-14T21:41:45.569038Z'
finished_at: '2026-10-14T22:01:51.891201Z'
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
summary: The finite Zero-self flattened slice sampling record is supported within
  its stated source and exact-calculation scope. DRAFT is retained; source errors,
  ordering conventions, boundary behavior and convergence limits remain explicit.
source:
  git_revision: f7209818aea9b23fad74ee708675f39995941c00
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
  - path: data/curated/DiaconisHolmesNealFiberSampler.yaml
    sha256: 2c9a3659fe85b5cb71cc22d7e9198c732aa3bdaed398f2b25793d514eeb0f3a6
    role: context
  - path: data/curated/DoublingSliceSampling.yaml
    sha256: 9de4028afbf3c1217076bf4bc3ae0b228b86545356393dae8d0cc157593b8ac4
    role: context
  - path: data/curated/EllipticalSliceSampling.yaml
    sha256: 6176b40f80f575b805140d402cd370f199c4db2083affd43fad991f1bc07df57
    role: context
  - path: data/curated/FlattenedSliceSampling.yaml
    sha256: c64a3d37ea98c8a43f9e005d34c06b9f5fb0f24381529613a5698d65537bd17a
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/GustafsonGuidedWalkMetropolis.yaml
    sha256: 839d08e76d362a34ead45d72c7e4d31bfbb29833b8638f31ff7c32d26ff5e67d
    role: context
  - path: data/curated/LiuModifiedGibbsSampler.yaml
    sha256: b3736d9f8dfb1e8b7e218d2b8fc075f413a719dc1c11cee951af8fa3b4542e54
    role: context
  - path: data/curated/MetropolisWithinGibbs.yaml
    sha256: 0e9cfedc93c7e46cc6316809d5a9ec9488b33891a9c9862f914a0adf8f7cb140
    role: context
  - path: data/curated/NealBacktrackingSuppressedMCMC.yaml
    sha256: 1da524622ec40d25aac45313cdbd6412adf1376c6c8b78eeecaded8eb561a0be
    role: context
  - path: data/curated/NonreversibleMetropolisUniformUpdate.yaml
    sha256: 27dbec2b01a48103d709df4b9ab94bba36083bd27acb69af1e3bc70ab6ab4ecd
    role: context
  - path: data/curated/SliceSampling.yaml
    sha256: a87319788a5d2966dd1484b6672a968642fb5514cc6f81184908576304bf6aaa
    role: context
  - path: data/curated/SteppingOutSliceSampling.yaml
    sha256: 8d2d0155c2e1d462b093935f19f4fe11fefb61e19e3ed93336e30b7257dda4c8
    role: context
  - path: data/curated/ZeroSelfFlattenedSliceSampling.yaml
    sha256: 7ae035e9d9e4ad3c8a34d705e976ce07abeda8f6c8449d112fbf3e535d496b45
    role: target
  - path: research/discovery/20261014T213822Z-flattened-slice-sampling.json
    sha256: 486d7974d137450ca681cd215dbe344b398da718f03bfc9e39a4238feddba7f6
    role: context
  - path: research/discovery/20261014T213822Z-flattened-slice-sampling.md
    sha256: c0d921d1f47af4491ae398c4508455b3385567e069fa66cb520ed6487458e1b6
    role: context
  - path: research/discovery/fss-zfss-boundaries.py
    sha256: 59ec829118d914392b6810e0171dd6679d821355451378766fff73fcbea89e88
    role: context
  - path: research/discovery/fss-zfss-extra-boundaries.py
    sha256: 3dcc67cdf8405d236e28ff4f6ecea8592531643c5528051b89eacbb0cc2d047a
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
- target_id: AIMech:ZeroSelfFlattenedSliceSampling
  path: data/curated/ZeroSelfFlattenedSliceSampling.yaml
  label: Zero-self flattened slice sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ZeroSelfFlattenedSliceSampling.yaml
    role: maintained
scope:
  description: 'All maintained fields of the selected record. Actual source scope:
    Selective primary method/context reading; cumulative root text1–51 of84 pages
    with recorded selected visual pages. Fresh post-capture text41,43–47,51 and visual42,46..
    The bar construction, blocker policy and Algorithms8–9 support the maintained
    mechanisms. Eq112–114 require positive-support uniqueness. Printed Figure10 and
    Algorithm9 caveats are retained. Reading does not cover all empirical or antecedent
    proofs; current exact checks are curator-written mathematical evidence.'
  selection: 'Exact maintained ID: AIMech:ZeroSelfFlattenedSliceSampling'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exclusions:
  - target: Other batch entries and neighboring identities
    reason: Read as identity/mapping context, not formal review targets.
  - target: Uninspected source versions, general convergence and runtime claims
    reason: Scope is finite ordered labels and an exact nonnegative normalized conditional
      law, with the first-maximizer and zero-current conventions retained. A zero-mass
      current value does not supply an undefined zero-total conditioning law. Countably
      infinite extensions, adaptive order changes, floating-point stability, general
      convergence and benchmark superiority are outside scope. Minimum self mass is
      not a guarantee of aperiodicity, irreducibility or lower asymptotic variance.
      The 84-page report and its cited antecedent proofs/empirical sections were not
      wholly read.
  - target: Author implementation and benchmark replication
    reason: Only bounded original calculations and project checks were executed.
checks:
- check_id: gate-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 555.67s (0:09:15)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 708 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 396 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 400,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
  scope_note: Actual execution completed 2026-10-14T21:59:03.993372Z; this generator
    executes no recorded commands.
- check_id: vendor-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
  scope_note: Actual execution completed 2026-10-14T21:42:16.513720Z; this generator
    executes no recorded commands.
- check_id: render-2
  name: just render
  command: just render
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages

    uv run --locked python scripts/render_pages.py

    '
  scope_note: Actual execution completed 2026-10-14T21:42:40.608648Z; this generator
    executes no recorded commands.
- check_id: render-3
  name: just render-check
  command: just render-check
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'pages/ is current

    uv run --locked python scripts/render_pages.py --check

    '
  scope_note: Actual execution completed 2026-10-14T21:43:12.648181Z; this generator
    executes no recorded commands.
- check_id: additional-4
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
  scope_note: Actual execution completed 2026-10-14T21:42:14.834323Z; this generator
    executes no recorded commands.
- check_id: additional-5
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited zero without output.
  scope_note: Actual execution completed 2026-10-14T21:42:15.393023Z; this generator
    executes no recorded commands.
- check_id: calculation-6
  name: python3 research/discovery/fss-zfss-boundaries.py
  command: python3 research/discovery/fss-zfss-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"case_generation\": \"All distinct nonnegative rational probability\
    \ vectors with 1\\u20136 states obtained from ordered weak compositions of totals1\\\
    u20138; plus explicit Figure10, strict half-neighbors, irregular ties and zero-mass\
    \ cases.\",\n  \"counts\": {\n    \"FSS_nonminimal_self\": 297,\n    \"FSS_reversible\"\
    : 2661,\n    \"ZFSS_nonminimal_self\": 0,\n    \"ZFSS_reversible\": 2661,\n  \
    \  \"distributions\": 4450,\n    \"distributions_FSS_ZFSS_distinct\": 297,\n \
    \   \"endpoint_checks\": 97160,\n    \"endpoint_zero_probability_outputs\": 998,\n\
    \    \"half_boundary_kernels\": 1862,\n    \"integrated_sampler_rows\": 48580,\n\
    \    \"integrated_uniform_cells\": 108028,\n    \"invalid_probability_vectors_rejected\"\
    : 4,\n    \"kernels\": 8900,\n    \"point_mass_kernels\": 42,\n    \"sampler_executions\"\
    : 145176,\n    \"tied_max_kernels\": 1810,\n    \"zero_mass_rows\": 18792\n  },\n\
    \  \"differences\": [],\n  \"endpoint_zero_probability_outputs\": [\n    {\n \
    \     \"current_0based\": 2,\n      \"method\": \"FSS\",\n      \"range\": [\n\
    \        \"0\",\n        \"1\"\n      ],\n      \"returned_0based\": 2,\n    \
    \  \"row\": [\n        \"1/4\",\n        \"3/4\",\n        \"0\"\n      ],\n \
    \     \"target\": [\n        \"1/8\",\n        \"3/8\",\n        \"1/2\"\n   \
    \   ],\n      \"uniform\": \"1\"\n    },\n    {\n      \"current_0based\": 2,\n\
    \      \"method\": \"ZFSS\",\n      \"range\": [\n        \"0\",\n        \"1\"\
    \n      ],\n      \"returned_0based\": 2,\n      \"row\": [\n        \"1/4\",\n\
    \        \"3/4\",\n        \"0\"\n      ],\n      \"target\": [\n        \"1/8\"\
    ,\n        \"3/8\",\n        \"1/2\"\n      ],\n      \"uniform\": \"1\"\n   \
    \ },\n    {\n      \"current_0based\": 2,\n      \"method\": \"FSS\",\n      \"\
    range\": [\n        \"0\",\n        \"1\"\n      ],\n      \"returned_0based\"\
    : 2,\n      \"row\": [\n        \"1/3\",\n        \"2/3\",\n        \"0\"\n  \
    \    ],\n      \"target\": [\n        \"1/6\",\n        \"1/3\",\n        \"1/2\"\
    \n      ],\n      \"uniform\": \"1\"\n    },\n    {\n      \"current_0based\"\
    : 2,\n      \"method\": \"ZFSS\",\n      \"range\": [\n        \"0\",\n      \
    \  \"1\"\n      ],\n      \"returned_0based\": 2,\n      \"row\": [\n        \"\
    1/3\",\n        \"2/3\",\n        \"0\"\n      ],\n      \"target\": [\n     \
    \   \"1/6\",\n        \"1/3\",\n        \"1/2\"\n      ],\n      \"uniform\":\
    \ \"1\"\n    },\n    {\n      \"current_0based\": 2,\n      \"method\": \"FSS\"\
    ,\n      \"range\": [\n        \"0\",\n        \"1\"\n      ],\n      \"returned_0based\"\
    : 2,\n      \"row\": [\n        \"1/2\",\n        \"1/2\",\n        \"0\"\n  \
    \    ],\n      \"target\": [\n        \"1/4\",\n        \"1/4\",\n        \"1/2\"\
    \n      ],\n      \"uniform\": \"1\"\n    },\n    {\n      \"current_0based\"\
    : 2,\n      \"method\": \"ZFSS\",\n      \"range\": [\n        \"0\",\n      \
    \  \"1\"\n      ],\n      \"returned_0based\": 2,\n      \"row\": [\n        \"\
    1/2\",\n        \"1/2\",\n        \"0\"\n      ],\n      \"target\": [\n     \
    \   \"1/4\",\n        \"1/4\",\n        \"1/2\"\n      ],\n      \"uniform\":\
    \ \"1\"\n    }\n  ],\n  \"figure10\": {\n    \"FSS_verified\": [\n      [\n  \
    \      \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\n\
    \      ],\n      [\n        \"1/4\",\n        \"0\",\n        \"0\",\n       \
    \ \"0\",\n        \"3/4\"\n      ],\n      [\n        \"0\",\n        \"1/2\"\
    ,\n        \"0\",\n        \"0\",\n        \"1/2\"\n      ],\n      [\n      \
    \  \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\n   \
    \   ],\n      [\n        \"1/9\",\n        \"2/9\",\n        \"4/9\",\n      \
    \  \"1/9\",\n        \"1/9\"\n      ]\n    ],\n    \"SS_printed\": [\n      [\n\
    \        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\
    \n      ],\n      [\n        \"1/2\",\n        \"0\",\n        \"0\",\n      \
    \  \"0\",\n        \"1/2\"\n      ],\n      [\n        \"0\",\n        \"1\",\n\
    \        \"0\",\n        \"0\",\n        \"0\"\n      ],\n      [\n        \"\
    0\",\n        \"0\",\n        \"1\",\n        \"0\",\n        \"0\"\n      ],\n\
    \      [\n        \"0\",\n        \"0\",\n        \"1/3\",\n        \"1/9\",\n\
    \        \"5/9\"\n      ]\n    ],\n    \"ZFSS_calculated_three_ways\": [\n   \
    \   [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n      \
    \  \"1\"\n      ],\n      [\n        \"1/7\",\n        \"0\",\n        \"0\",\n\
    \        \"0\",\n        \"6/7\"\n      ],\n      [\n        \"0\",\n        \"\
    2/7\",\n        \"0\",\n        \"1/14\",\n        \"9/14\"\n      ],\n      [\n\
    \        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\
    \n      ],\n      [\n        \"10/63\",\n        \"20/63\",\n        \"4/9\",\n\
    \        \"5/63\",\n        \"0\"\n      ]\n    ],\n    \"ZFSS_printed_nonstationary\"\
    : [\n      [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n\
    \        \"1\"\n      ],\n      [\n        \"1/4\",\n        \"0\",\n        \"\
    0\",\n        \"0\",\n        \"3/4\"\n      ],\n      [\n        \"0\",\n   \
    \     \"1/2\",\n        \"0\",\n        \"0\",\n        \"1/2\"\n      ],\n  \
    \    [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n     \
    \   \"1\"\n      ],\n      [\n        \"10/63\",\n        \"20/63\",\n       \
    \ \"4/9\",\n        \"5/63\",\n        \"0\"\n      ]\n    ],\n    \"matrix_rows_in_original_state_order\"\
    : true,\n    \"printed_ZFSS_stationarity_residual\": [\n      \"3/140\",\n   \
    \   \"3/70\",\n      \"0\",\n      \"-1/70\",\n      \"-1/20\"\n    ],\n    \"\
    printed_ZFSS_target_after_one_step\": [\n      \"17/140\",\n      \"17/70\",\n\
    \      \"1/5\",\n      \"1/28\",\n      \"2/5\"\n    ],\n    \"source_caveat\"\
    : \"The printed ZFSS matrix rows2 and3 retain FSS entries and fail stationarity.\
    \ Its final row agrees with Algorithms8\\u20139 and geometric calculation. This\
    \ script preserves the printed matrix as a negative control, not a valid kernel.\"\
    ,\n    \"stationary_self_correct_kernels\": [\n      \"1/4\",\n      \"1/20\"\
    ,\n      \"0\"\n    ],\n    \"target\": [\n      \"1/10\",\n      \"1/5\",\n \
    \     \"1/5\",\n      \"1/20\",\n      \"9/20\"\n    ]\n  },\n  \"first_distinct_kernel\"\
    : {\n    \"FSS\": [\n      [\n        \"0\",\n        \"3/7\",\n        \"2/7\"\
    ,\n        \"2/7\"\n      ],\n      [\n        \"0\",\n        \"1/6\",\n    \
    \    \"1/6\",\n        \"2/3\"\n      ],\n      [\n        \"0\",\n        \"\
    1\",\n        \"0\",\n        \"0\"\n      ],\n      [\n        \"0\",\n     \
    \   \"1/4\",\n        \"3/4\",\n        \"0\"\n      ]\n    ],\n    \"ZFSS\":\
    \ [\n      [\n        \"0\",\n        \"3/7\",\n        \"2/7\",\n        \"2/7\"\
    \n      ],\n      [\n        \"0\",\n        \"0\",\n        \"1/3\",\n      \
    \  \"2/3\"\n      ],\n      [\n        \"0\",\n        \"1\",\n        \"0\",\n\
    \        \"0\"\n      ],\n      [\n        \"0\",\n        \"1/2\",\n        \"\
    1/2\",\n        \"0\"\n      ]\n    ],\n    \"target\": [\n      \"0\",\n    \
    \  \"3/7\",\n      \"2/7\",\n      \"2/7\"\n    ]\n  },\n  \"sampler_interpretation\"\
    : \"Algorithm9 zero-current CDF branch interpreted without its ambiguous outer\
    \ For line. Ordinary continuous uniform inputs integrated exactly; closed endpoints\
    \ checked separately.\",\n  \"scope\": \"Three original exact finite constructions.\
    \ No author code executed; no general theorem or floating-point implementation\
    \ verification.\",\n  \"uniform_periodicity\": {\n    \"2\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 2\n    },\n    \"3\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 3\n    },\n    \"4\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 4\n    },\n    \"5\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 5\n    },\n    \"6\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 6\n    },\n    \"7\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 7\n    },\n    \"8\": {\n      \"deterministic_predecessor_cycle\"\
    : true,\n      \"period\": 8\n    }\n  }\n}\n"
  scope_note: Actual execution completed 2026-10-14T21:42:49.113407Z; this generator
    executes no recorded commands.
- check_id: calculation-7
  name: python3 research/discovery/fss-zfss-extra-boundaries.py
  command: python3 research/discovery/fss-zfss-extra-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"endpoint_counterexamples\": [\n    {\n      \"current_state_1based\"\
    : 3,\n      \"method\": \"FSS\",\n      \"returned_state_1based\": 3,\n      \"\
    returned_transition_probability\": \"0\",\n      \"row\": [\n        \"1/2\",\n\
    \        \"1/2\",\n        \"0\"\n      ],\n      \"target\": [\n        \"1/4\"\
    ,\n        \"1/4\",\n        \"1/2\"\n      ],\n      \"uniform_value\": \"1\"\
    \n    },\n    {\n      \"current_state_1based\": 3,\n      \"method\": \"ZFSS\"\
    ,\n      \"returned_state_1based\": 3,\n      \"returned_transition_probability\"\
    : \"0\",\n      \"row\": [\n        \"1/2\",\n        \"1/2\",\n        \"0\"\n\
    \      ],\n      \"target\": [\n        \"1/4\",\n        \"1/4\",\n        \"\
    1/2\"\n      ],\n      \"uniform_value\": \"1\"\n    }\n  ],\n  \"figure10_simple_slice\"\
    : {\n    \"agrees_with_printed_matrix\": true,\n    \"matrix\": [\n      [\n \
    \       \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\n\
    \      ],\n      [\n        \"1/2\",\n        \"0\",\n        \"0\",\n       \
    \ \"0\",\n        \"1/2\"\n      ],\n      [\n        \"0\",\n        \"1\",\n\
    \        \"0\",\n        \"0\",\n        \"0\"\n      ],\n      [\n        \"\
    0\",\n        \"0\",\n        \"1\",\n        \"0\",\n        \"0\"\n      ],\n\
    \      [\n        \"0\",\n        \"0\",\n        \"1/3\",\n        \"1/9\",\n\
    \        \"5/9\"\n      ]\n    ],\n    \"target\": [\n      \"1/10\",\n      \"\
    1/5\",\n      \"1/5\",\n      \"1/20\",\n      \"9/20\"\n    ]\n  },\n  \"joint_compositions\"\
    : [\n    {\n      \"both_coordinate_kernels_stationary\": true,\n      \"fixed_mixture_matrix\"\
    : [\n        [\n          \"0\",\n          \"0\",\n          \"2/3\",\n     \
    \     \"1/3\",\n          \"0\",\n          \"0\",\n          \"0\",\n       \
    \   \"0\",\n          \"0\"\n        ],\n        [\n          \"2/9\",\n     \
    \     \"0\",\n          \"4/9\",\n          \"0\",\n          \"2/15\",\n    \
    \      \"0\",\n          \"0\",\n          \"1/5\",\n          \"0\"\n       \
    \ ],\n        [\n          \"1/3\",\n          \"0\",\n          \"1/3\",\n  \
    \        \"0\",\n          \"0\",\n          \"1/6\",\n          \"0\",\n    \
    \      \"0\",\n          \"1/6\"\n        ],\n        [\n          \"1/9\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"4/9\",\n  \
    \        \"2/9\",\n          \"2/9\",\n          \"0\",\n          \"0\"\n   \
    \     ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"2/3\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"1/3\",\n          \"0\"\n        ],\n        [\n          \"0\",\n  \
    \        \"0\",\n          \"1/3\",\n          \"2/3\",\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n       \
    \ ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"1/3\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"2/3\",\n          \"0\"\n        ],\n        [\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"2/9\",\n        \
    \  \"0\",\n          \"4/9\",\n          \"1/9\",\n          \"2/9\"\n       \
    \ ],\n        [\n          \"0\",\n          \"0\",\n          \"1/3\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"2/3\",\n          \"0\"\n        ]\n      ],\n      \"fixed_mixture_reversible\"\
    : true,\n      \"fixed_mixture_stationary\": true,\n      \"fixed_scan_matrix\"\
    : [\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n       \
    \   \"0\",\n          \"2/3\",\n          \"1/3\",\n          \"0\",\n       \
    \   \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n       \
    \   \"0\",\n          \"0\",\n          \"2/5\",\n          \"0\",\n         \
    \ \"0\",\n          \"2/5\",\n          \"0\",\n          \"1/5\"\n        ],\n\
    \        [\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    1/2\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"1/2\"\
    ,\n          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"1/3\",\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"2/3\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"2/3\",\n          \"0\",\n      \
    \    \"1/3\"\n        ],\n        [\n          \"1/2\",\n          \"0\",\n  \
    \        \"1/2\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"2/3\",\n          \"1/3\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n        \
    \  \"0\",\n          \"2/3\",\n          \"0\",\n          \"0\",\n          \"\
    2/9\",\n          \"0\",\n          \"1/9\"\n        ],\n        [\n         \
    \ \"1/2\",\n          \"0\",\n          \"1/2\",\n          \"0\",\n         \
    \ \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\
    \n        ]\n      ],\n      \"fixed_scan_reversible\": false,\n      \"fixed_scan_stationary\"\
    : true,\n      \"joint_target_row_major_3x3\": [\n        \"1/15\",\n        \"\
    0\",\n        \"2/15\",\n        \"1/5\",\n        \"2/15\",\n        \"1/15\"\
    ,\n        \"2/15\",\n        \"1/5\",\n        \"1/15\"\n      ],\n      \"method\"\
    : \"FSS\"\n    },\n    {\n      \"both_coordinate_kernels_stationary\": true,\n\
    \      \"fixed_mixture_matrix\": [\n        [\n          \"0\",\n          \"\
    0\",\n          \"2/3\",\n          \"1/3\",\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"2/9\",\n          \"0\",\n          \"4/9\",\n          \"0\",\n\
    \          \"2/15\",\n          \"0\",\n          \"0\",\n          \"1/5\",\n\
    \          \"0\"\n        ],\n        [\n          \"1/3\",\n          \"0\",\n\
    \          \"1/3\",\n          \"0\",\n          \"0\",\n          \"1/6\",\n\
    \          \"0\",\n          \"0\",\n          \"1/6\"\n        ],\n        [\n\
    \          \"1/9\",\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"4/9\",\n          \"2/9\",\n          \"2/9\",\n          \"0\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"2/3\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"1/3\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"1/3\",\n          \"2/3\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"1/3\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"2/3\",\n          \"0\"\n        ],\n        [\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"2/9\",\n          \"0\",\n          \"4/9\",\n          \"1/9\",\n      \
    \    \"2/9\"\n        ],\n        [\n          \"0\",\n          \"0\",\n    \
    \      \"1/3\",\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"2/3\",\n          \"0\"\n        ]\n      ],\n      \"\
    fixed_mixture_reversible\": true,\n      \"fixed_mixture_stationary\": true,\n\
    \      \"fixed_scan_matrix\": [\n        [\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"2/3\",\n          \"1/3\",\n\
    \          \"0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"2/5\",\n  \
    \        \"0\",\n          \"0\",\n          \"2/5\",\n          \"0\",\n    \
    \      \"1/5\"\n        ],\n        [\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"1/2\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"1/2\",\n          \"0\"\n        ],\n        [\n  \
    \        \"0\",\n          \"0\",\n          \"1/3\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"2/3\",\n      \
    \    \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    2/3\",\n          \"0\",\n          \"1/3\"\n        ],\n        [\n         \
    \ \"1/2\",\n          \"0\",\n          \"1/2\",\n          \"0\",\n         \
    \ \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\
    \n        ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"2/3\",\n          \"1/3\",\n          \"0\",\n\
    \          \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"2/3\",\n          \"0\",\n  \
    \        \"0\",\n          \"2/9\",\n          \"0\",\n          \"1/9\"\n   \
    \     ],\n        [\n          \"1/2\",\n          \"0\",\n          \"1/2\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\"\n        ]\n      ],\n      \"fixed_scan_reversible\"\
    : false,\n      \"fixed_scan_stationary\": true,\n      \"joint_target_row_major_3x3\"\
    : [\n        \"1/15\",\n        \"0\",\n        \"2/15\",\n        \"1/5\",\n\
    \        \"2/15\",\n        \"1/15\",\n        \"2/15\",\n        \"1/5\",\n \
    \       \"1/15\"\n      ],\n      \"method\": \"ZFSS\"\n    }\n  ],\n  \"scope\"\
    : \"Supplementary curator rational calculations; uses the independently authored\
    \ algorithms of the base audit, never author software.\",\n  \"systematic_scan_counterexample\"\
    : {\n    \"joint_target\": \"Uniform independent 3x3 coordinates\",\n    \"meaning\"\
    : \"Both FSS and ZFSS preserve the target but a deterministic full scan is reducible.\
    \ Zero self transitions do not guarantee convergence from every initial state.\"\
    ,\n    \"period_within_class\": 3,\n    \"three_closed_classes_0based_row_major\"\
    : [\n      [\n        0,\n        4,\n        8\n      ],\n      [\n        2,\n\
    \        3,\n        7\n      ],\n      [\n        1,\n        5,\n        6\n\
    \      ]\n    ],\n    \"transition\": \"(a,b) -> (a-1 mod3,b-1 mod3) each full\
    \ scan\"\n  },\n  \"zero_label_order_effect\": {\n    \"FSS_after_deleting_zero_label\"\
    : [\n      [\n        \"0\",\n        \"1/3\",\n        \"2/3\"\n      ],\n  \
    \    [\n        \"1\",\n        \"0\",\n        \"0\"\n      ],\n      [\n   \
    \     \"1/2\",\n        \"1/2\",\n        \"0\"\n      ]\n    ],\n    \"FSS_positive_rows_with_zero_label\"\
    : [\n      [\n        \"1/6\",\n        \"1/6\",\n        \"2/3\"\n      ],\n\
    \      [\n        \"1\",\n        \"0\",\n        \"0\"\n      ],\n      [\n \
    \       \"1/4\",\n        \"3/4\",\n        \"0\"\n      ]\n    ],\n    \"ZFSS_same_after_this_deletion\"\
    : true,\n    \"meaning\": \"Do not silently delete zero-probability labels before\
    \ applying FSS: the immediate predecessor excluded from mass redistribution is\
    \ part of the specified order. This example distinguishes support preservation\
    \ from kernel identity.\",\n    \"positive_target\": [\n      \"3/7\",\n     \
    \ \"2/7\",\n      \"2/7\"\n    ],\n    \"target_with_leading_zero\": [\n     \
    \ \"0\",\n      \"3/7\",\n      \"2/7\",\n      \"2/7\"\n    ]\n  },\n  \"zero_row_nonuniqueness\"\
    : {\n    \"alternative_invariant_kernel\": [\n      [\n        \"0\",\n      \
    \  \"1\",\n        \"0\"\n      ],\n      [\n        \"1\",\n        \"0\",\n\
    \        \"0\"\n      ],\n      [\n        \"1\",\n        \"0\",\n        \"\
    0\"\n      ]\n    ],\n    \"both_reversible_and_minimal_self\": true,\n    \"\
    meaning\": \"Uniqueness of Eq112 is on positive support; a zero-mass row is not\
    \ determined by stationarity. Algorithm8 explicitly sets that row to the target\
    \ law.\",\n    \"published_algorithm8_kernel\": [\n      [\n        \"0\",\n \
    \       \"1\",\n        \"0\"\n      ],\n      [\n        \"1\",\n        \"0\"\
    ,\n        \"0\"\n      ],\n      [\n        \"1/2\",\n        \"1/2\",\n    \
    \    \"0\"\n      ]\n    ],\n    \"target\": [\n      \"1/2\",\n      \"1/2\"\
    ,\n      \"0\"\n    ]\n  }\n}\n"
  scope_note: Actual execution completed 2026-10-14T21:42:49.354648Z; this generator
    executes no recorded commands.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T213822Z-flattened-slice-sampling.json
  locator: identity_search and identity_assessment
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 486d7974d137450ca681cd215dbe344b398da718f03bfc9e39a4238feddba7f6
  support: supports
  summary: The post312 assessment covers all 442 pinned AIO and 706 native IDs, names,
    aliases and scoped synonyms, plus four complete checkout searches including ignored
    and hidden files. The maintained identity is a finite ordered conditional kernel,
    distinct from generic slice/Gibbs, interval and elliptical slice procedures, MH-within-Gibbs
    and persistent-sign/pair-state samplers. Earlier 703-native searches and 18 exact
    AIO contexts are preserved with their reading scopes; the three actual batch312
    native neighbors were assessed for this identity comparison. AIO:MarkovChain is
    related_match at a different abstraction level; no neural Network or ProbabilisticHiddenLayer
    inheritance is implied. ZFSS denotes the nearest-qualifying-blocker ZERO=true
    policy. It differs from FSS for positive-probability transitions, while sharing
    special cases. Zero-self means removal of avoidable self transitions; it is not
    an exact alias for arbitrary minimum-self kernels. No aliases are adopted.
  search_scope: Canonical ID/name/alias/all-scoped-synonym checks and retained four
    complete-checkout searches include ignored and hidden files. Bounded corpus scope,
    not universal absence.
- evidence_id: mapping
  kind: record_content
  reference: research/discovery/20261014T213822Z-flattened-slice-sampling.json
  locator: mapping_context nodes, historical semantic/native contexts, actual312_neighbors
    and mapping_assessment
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 486d7974d137450ca681cd215dbe344b398da718f03bfc9e39a4238feddba7f6
  support: supports
  summary: The related_match to AIO:MarkovChain is a method-to-process association.
    The exact pinned CLASS denotes a stochastic process/model, exported under Network
    with a ProbabilisticHiddenLayer relation. Conditional transition construction
    supports the association but not equivalence, subclass membership or inherited
    neural assertions. Eighteen complete AIO class contexts and their generated records
    ground the selected mapping and seventeen rejected alternatives.
- evidence_id: actual-record-reading
  kind: record_content
  reference: data/curated/ZeroSelfFlattenedSliceSampling.yaml
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 7ae035e9d9e4ad3c8a34d705e976ce07abeda8f6c8449d112fbf3e535d496b45
  support: supports
  summary: 'Root fully read both actual maintained YAML records after canonical capture,
    all prepared claim/mapping narratives, actual report delta, history and integrity
    result. All six claims and source locators are scoped to exact finite normalized
    conditional kernels. Related AIO:MarkovChain is a method/process association;
    no inherited neural assertions or alias equivalence. Original precise retrieval
    timestamp remains in the raw manifest; canonical source metadata truncates to
    schema whole seconds, with the prewrite validation failure preserved. Original/portable
    calculator derivation and failed printed-Figure10 comparison remain explicit.
    No author implementation, empirical replication, independent approval or saturation
    claim. Actual DRAFT status and source/version limits retained. No new maintained-record
    finding found. ZFSS uses the nearest backward qualifying blocker with recomputed
    factor and preserved remaining order. Added pieces cannot exceed preceding originals;
    the blocker eliminates regular-case self transitions. Dominant mass requires2h-1
    stationary self mass. Printed Figure10 ZFSS rows2/3 are explicitly nonstationary;
    corrected calculations are curator evidence, not an author erratum. Actual post-capture
    source reread: Neal author report text PDF pp41,43–47,51 and visual pp42,46. Visual42
    confirms actual printed comparison rows; visual46 confirms the ambiguous zero-current
    outer loop and r>=s endpoint. Earlier text1–51 and selected visual readings are
    retained, not all claimed freshly reread.'
- evidence_id: neal2024
  kind: primary_source
  reference: https://glizen.com/radfordneal/ftp/gibbs-self.pdf
  locator: Section 11, PDF pp. 42–43, ZFSS reordering; Algorithm 8, pp. 44–45, ZERO
    true; Section 11, PDF pp. 42–43, blocker construction; Algorithm 8, pp. 44–45,
    ZERO true; Section 11, PDF pp. 41–43, invariant-slice framework and blocker argument;
    Section 2, pp. 2–3, Equations 2–4; geometric calculations in research/discovery/fss-zfss-boundaries.py;
    Algorithm 8 Part 1, PDF p. 44, zero-current and dominant-mass branches; Section
    13, p. 51, Equations 112–114; exact support example in research/discovery/fss-zfss-extra-boundaries.py;
    Figure 10, PDF p. 42, rightmost matrix; Algorithms 8–9, pp. 44–47; original curator
    calculations in research/discovery/fss-zfss-boundaries.py; Section 11, PDF pp.
    42–43, FSS/ZFSS distinction; Section 13, pp. 49–51, uniform cycles and common
    boundary kernel; exact examples in research/discovery/fss-zfss-boundaries.py and
    research/discovery/fss-zfss-extra-boundaries.py; Algorithm 9 Part 1, PDF p. 46,
    output guarantee, zero-current loop and dominant-mass CDF; endpoint checks in
    research/discovery/fss-zfss-extra-boundaries.py
  accessed_at: '2026-10-14T20:33:01Z'
  snapshot_sha256: 3d637d3eec046118a4c81d0d3824f387e1077d5ed8bd15d90a4db242c89d8bea
  support: supports
  summary: 'Author-hosted technical report dated 26 March 2024; 84 PDF pages. Independently
    pinned from arXiv:2403.18054v1; byte equivalence between versions is not asserted.
    Actual root reading: The bar construction, blocker policy and Algorithms8–9 support
    the maintained mechanisms. Eq112–114 require positive-support uniqueness. Printed
    Figure10 and Algorithm9 caveats are retained. Reading does not cover all empirical
    or antecedent proofs; current exact checks are curator-written mathematical evidence.'
- evidence_id: calculation-main
  kind: record_content
  reference: research/discovery/fss-zfss-boundaries.py
  locator: Saved report curator_calculations; counts, figure10, uniform_periodicity
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 59ec829118d914392b6810e0171dd6679d821355451378766fff73fcbea89e88
  support: supports
  summary: 'Exact Fraction original curator calculations, with actual copied-script
    outputs checked against the full saved results. No author-code execution, benchmark
    replication or universal proof. Selected results: {"counts": {"FSS_nonminimal_self":
    297, "FSS_reversible": 2661, "ZFSS_nonminimal_self": 0, "ZFSS_reversible": 2661,
    "distributions": 4450, "distributions_FSS_ZFSS_distinct": 297, "endpoint_checks":
    97160, "endpoint_zero_probability_outputs": 998, "half_boundary_kernels": 1862,
    "integrated_sampler_rows": 48580, "integrated_uniform_cells": 108028, "invalid_probability_vectors_rejected":
    4, "kernels": 8900, "point_mass_kernels": 42, "sampler_executions": 145176, "tied_max_kernels":
    1810, "zero_mass_rows": 18792}, "figure10": {"FSS_verified": [["0", "0", "0",
    "0", "1"], ["1/4", "0", "0", "0", "3/4"], ["0", "1/2", "0", "0", "1/2"], ["0",
    "0", "0", "0", "1"], ["1/9", "2/9", "4/9", "1/9", "1/9"]], "SS_printed": [["0",
    "0", "0", "0", "1"], ["1/2", "0", "0", "0", "1/2"], ["0", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"], ["0", "0", "1/3", "1/9", "5/9"]], "ZFSS_calculated_three_ways":
    [["0", "0", "0", "0", "1"], ["1/7", "0", "0", "0", "6/7"], ["0", "2/7", "0", "1/14",
    "9/14"], ["0", "0", "0", "0", "1"], ["10/63", "20/63", "4/9", "5/63", "0"]], "ZFSS_printed_nonstationary":
    [["0", "0", "0", "0", "1"], ["1/4", "0", "0", "0", "3/4"], ["0", "1/2", "0", "0",
    "1/2"], ["0", "0", "0", "0", "1"], ["10/63", "20/63", "4/9", "5/63", "0"]], "matrix_rows_in_original_state_order":
    true, "printed_ZFSS_stationarity_residual": ["3/140", "3/70", "0", "-1/70", "-1/20"],
    "printed_ZFSS_target_after_one_step": ["17/140", "17/70", "1/5", "1/28", "2/5"],
    "source_caveat": "The printed ZFSS matrix rows2 and3 retain FSS entries and fail
    stationarity. Its final row agrees with Algorithms8–9 and geometric calculation.
    This script preserves the printed matrix as a negative control, not a valid kernel.",
    "stationary_self_correct_kernels": ["1/4", "1/20", "0"], "target": ["1/10", "1/5",
    "1/5", "1/20", "9/20"]}, "uniform_periodicity": {"2": {"deterministic_predecessor_cycle":
    true, "period": 2}, "3": {"deterministic_predecessor_cycle": true, "period": 3},
    "4": {"deterministic_predecessor_cycle": true, "period": 4}, "5": {"deterministic_predecessor_cycle":
    true, "period": 5}, "6": {"deterministic_predecessor_cycle": true, "period": 6},
    "7": {"deterministic_predecessor_cycle": true, "period": 7}, "8": {"deterministic_predecessor_cycle":
    true, "period": 8}}}'
- evidence_id: calculation-extra
  kind: record_content
  reference: research/discovery/fss-zfss-extra-boundaries.py
  locator: Saved report curator_calculations; endpoint_counterexamples, zero_row_nonuniqueness,
    zero_label_order_effect, systematic_scan_counterexample
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 3dcc67cdf8405d236e28ff4f6ecea8592531643c5528051b89eacbb0cc2d047a
  support: supports
  summary: 'Exact Fraction original curator calculations, with actual copied-script
    outputs checked against the full saved results. No author-code execution, benchmark
    replication or universal proof. Selected results: {"endpoint_counterexamples":
    [{"current_state_1based": 3, "method": "FSS", "returned_state_1based": 3, "returned_transition_probability":
    "0", "row": ["1/2", "1/2", "0"], "target": ["1/4", "1/4", "1/2"], "uniform_value":
    "1"}, {"current_state_1based": 3, "method": "ZFSS", "returned_state_1based": 3,
    "returned_transition_probability": "0", "row": ["1/2", "1/2", "0"], "target":
    ["1/4", "1/4", "1/2"], "uniform_value": "1"}], "zero_row_nonuniqueness": {"alternative_invariant_kernel":
    [["0", "1", "0"], ["1", "0", "0"], ["1", "0", "0"]], "both_reversible_and_minimal_self":
    true, "meaning": "Uniqueness of Eq112 is on positive support; a zero-mass row
    is not determined by stationarity. Algorithm8 explicitly sets that row to the
    target law.", "published_algorithm8_kernel": [["0", "1", "0"], ["1", "0", "0"],
    ["1/2", "1/2", "0"]], "target": ["1/2", "1/2", "0"]}, "zero_label_order_effect":
    {"FSS_after_deleting_zero_label": [["0", "1/3", "2/3"], ["1", "0", "0"], ["1/2",
    "1/2", "0"]], "FSS_positive_rows_with_zero_label": [["1/6", "1/6", "2/3"], ["1",
    "0", "0"], ["1/4", "3/4", "0"]], "ZFSS_same_after_this_deletion": true, "meaning":
    "Do not silently delete zero-probability labels before applying FSS: the immediate
    predecessor excluded from mass redistribution is part of the specified order.
    This example distinguishes support preservation from kernel identity.", "positive_target":
    ["3/7", "2/7", "2/7"], "target_with_leading_zero": ["0", "3/7", "2/7", "2/7"]},
    "systematic_scan_counterexample": {"joint_target": "Uniform independent 3x3 coordinates",
    "meaning": "Both FSS and ZFSS preserve the target but a deterministic full scan
    is reducible. Zero self transitions do not guarantee convergence from every initial
    state.", "period_within_class": 3, "three_closed_classes_0based_row_major": [[0,
    4, 8], [2, 3, 7], [1, 5, 6]], "transition": "(a,b) -> (a-1 mod3,b-1 mod3) each
    full scan"}}'
- evidence_id: source-math-provenance
  kind: record_content
  reference: research/discovery/20261014T213822Z-flattened-slice-sampling.json
  locator: source_analysis.handoffs.source_math, root_readings and writer_preparation_reading
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 486d7974d137450ca681cd215dbe344b398da718f03bfc9e39a4238feddba7f6
  support: supports
  summary: Root assessed the separately attributed selective source readings and bounded
    mathematical research. Supporting agents are in the same author workflow and provide
    no independent scientific approval.
- evidence_id: source-error-portable-lineage
  kind: record_content
  reference: research/discovery/20261014T213822Z-flattened-slice-sampling.json
  locator: calculation_lineage, curator_calculations.original and source_analysis.root_readings.figure10
  accessed_at: '2026-10-14T21:43:21Z'
  snapshot_sha256: 486d7974d137450ca681cd215dbe344b398da718f03bfc9e39a4238feddba7f6
  support: supports
  summary: The raw printed Figure 10 ZFSS matrix and initial failed comparison are
    retained as source-error evidence. Algorithms and independently derived geometry
    give different corrected rows, without an author-issued erratum claim. Original
    scripts/results, metadata-only portable derivation and recorded executions are
    preserved; both portable scripts retain their fixed sibling relationship.
assessments:
- assessment_id: identity
  area: identity
  topic: Zero-self flattened slice sampling
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - identity
  - neal2024
  summary: Retain the narrow DRAFT identity within the documented search scope.
  details: ZFSS is the named ZERO=true blocker policy, rather than every minimum-self
    conditional kernel or an exact alias of FSS. Shared code and dominant/zero-current
    branches do not equate the two positive-support kernels in general. It is distinct
    from generic Gibbs/slice, interval and elliptical methods, Liu conditional exclusion
    and augmented pair/sign/direction methods. Broader antithetic/NAM source families
    remain separate open identity research; no source-wide import is implied.
- assessment_id: definition
  area: evidence
  topic: Definition and source scope
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - actual-record-reading
  summary: The maintained definition is supported within its stated method scope.
  details: The definition identifies finite ZFSS as the specific blocker-relocation
    policy followed by the flattened-bar predecessor update. Avoidable self transitions
    are removed, with the dominant-mass exception explicit in the claims. The primary
    evidence is the independently pinned author-hosted report dated 26 March 2024,
    84 PDF pages. Section 11 and Algorithms 8–9 on pp. 41–47 define the finite kernels
    and their implementations; pp. 2–3 support conditional composition, and pp. 49–51
    discuss boundary behavior. Reading is selective. Original source equations and
    curator analytic deductions are distinguished from bounded exact calculations.
    The printed Figure 10 ZFSS matrix fails its stated stationarity test; that source
    discrepancy is preserved rather than silently corrected. Neither arXiv-byte equivalence
    nor author-code execution is claimed.
- assessment_id: mapping
  area: grounding
  topic: Related Markov-process mapping
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - mapping
  - neal2024
  summary: related_match expresses method-to-process association without equivalence
    or ontology inheritance.
  details: 'The related_match to AIO:MarkovChain is a method-to-process association.
    The exact pinned CLASS denotes a stochastic process/model, exported under Network
    with a ProbabilisticHiddenLayer relation. Conditional transition construction
    supports the association but not equivalence, subclass membership or inherited
    neural assertions. Eighteen complete AIO class contexts and their generated records
    ground the selected mapping and seventeen rejected alternatives.

    Alternatives:

    AIO:Network: Interconnected entities/model superclass; no sampling procedure identity
    or subtype claim follows.

    AIO:ProbabilisticHiddenLayer: Categorical probability estimation in a neural hidden
    layer differs from a conditional-invariant transition.

    AIO:Model: Abstract model superclass is not the specific algorithm; no exact or
    forced broad mapping.

    AIO:MachineLearningTask: General learning task differs from the sampling procedure.

    AIO:TrainingStrategy: Training/preprocessing family differs from finite conditional
    Markov updates.

    AIO:MathematicalFunction: Generic rule/function does not identify this stochastic
    transition algorithm.

    AIO:BayesianNetwork: DAG probability model can be an application target, not the
    sampler.

    AIO:ProbabilisticGraphicalModel: Conditional dependence model/task differs from
    inference updates.

    AIO:UnsupervisedLearning: Learning patterns from unlabeled data is not the defining
    sampling mechanism.

    AIO:BoltzmannMachineNetwork: An application/model family rather than the conditional
    transition procedure.

    AIO:RestrictedBoltzmannMachine: Restricted neural energy model is not the algorithm.

    AIO:EnergyBasedLLM: Language-model energy construction does not define these generic
    categorical kernels.

    AIO:ImplicitLanguageModel: Sequence scoring/model class rather than a finite conditional
    update.

    AIO:Preprocessing: Rearranging auxiliary probability bars is not dataset preprocessing.

    AIO:Layer: Neural topology/component is a different abstraction.

    AIO:HiddenLayer: Nonlinear network transformation is not conditional Markov sampling.

    AIO:CausalGraphicalModel: Causal assumptions/graph model are not sampler identity
    or an entailed application.'
- assessment_id: blocking-state-and-flattened-bars
  area: evidence
  topic: blocking-state-and-flattened-bars
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  summary: Supported within the stated assumptions and inspected passages.
  details: Algorithm 8 ZERO=true scans backward cyclically for the nearest b satisfying
    pi(b)>=f*s, recalculating f=(h-s)/(1-h-pi(b)) for each candidate. For h<1/2, 0<=f<1
    and a second-largest label qualifies, so the search terminates. Moving b immediately
    before a retains all remaining relative order. The same height-s original bar
    and added a-labelled pieces define the transition. This specific blocker policy,
    rather than arbitrary order optimization, identifies ZFSS.
- assessment_id: invariance-and-avoided-self-transitions
  area: evidence
  topic: invariance-and-avoided-self-transitions
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  summary: Supported within the stated assumptions and inspected passages.
  details: The height-preserving bar split and cyclic predecessor permutation establish
    invariance. Added a pieces are no taller than preceding original bars, so departure
    from those pieces changes the label. For the original a bar, the relocated blocker
    catches motion below its height; above it, all added a pieces are inactive because
    their heights are bounded by f*s<=pi(b). Hence regular-case self probabilities
    vanish. Valid conditional mixtures/compositions preserve the joint target, without
    a general reversibility or convergence conclusion.
- assessment_id: dominant-mass-and-zero-state-conventions
  area: evidence
  topic: dominant-mass-and-zero-state-conventions
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  summary: Supported within the stated assumptions and inspected passages.
  details: Algorithm 8 p. 44 checks zero current mass first and assigns the row pi.
    For h>=1/2 and a supported current label, nonmaximum labels move to a while P(a,a)=(2h-1)/h
    and P(a,j)=pi(j)/h. Detailed balance holds on positive support, with total self
    mass 2h-1; h=1/2 and h=1 are explicit boundaries. Eq. 112 uniqueness must be restricted
    to positive support because invariant weighting does not determine a zero-mass
    row. The alternative third row(1,0,0) for pi=(1/2,1/2,0) is a concrete check.
    The term zero-self eliminates avoidable self transitions; dominant h>1/2 requires
    positive stationary self mass. It does not claim every row diagonal vanishes for
    every target.
- assessment_id: finite-checks-and-printed-matrix-discrepancy
  area: evidence
  topic: finite-checks-and-printed-matrix-discrepancy
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  summary: Supported within the stated assumptions and inspected passages.
  details: The4,450-target suite verifies target invariance and minimum self mass
    in each tested ZFSS case. Raw Figure 10 ZFSS rows 2/3 instead produce target pushforward(17/140,17/70,1/5,1/28,2/5),
    so the printed matrix is a negative control. Algorithm 8 and independent geometry
    give row 2=(1/7,0,0,0,6/7) and row 3=(0,2/7,0,1/14,9/14); the printed last row
    agrees. The source error is explicit and does not become an author-issued erratum,
    universal theorem or runtime-replication claim.
- assessment_id: kernel-distinction-and-periodicity
  area: evidence
  topic: kernel-distinction-and-periodicity
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  summary: Supported within the stated assumptions and inspected passages.
  details: The saved suite finds 297 target inputs with different FSS and ZFSS transition
    matrices, demonstrating separate kernel identities despite agreement when relocation
    is unnecessary and in the shared dominant branch. For equal finite weights, predecessor
    motion forms a deterministic cycle of period m. For two independent uniform three-state
    coordinates, a fixed full scan subtracts one from both coordinates modulo 3, preserving
    a-b and leaving three closed classes. The target remains invariant while a single
    trajectory does not explore all classes. Neither removed self transitions nor
    invariance alone imply ergodicity, improved finite-run error, asymptotic variance
    or runtime.
- assessment_id: fast-sampler-interpretation-limits
  area: evidence
  topic: fast-sampler-interpretation-limits
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  summary: Supported within the stated assumptions and inspected passages.
  details: Algorithm 8 defines the maintained probability kernel. The Algorithm 9
    calculation interprets its ambiguous zero-current outer loop as a single inverse-CDF
    traversal; it is not a claim that literal printed control flow was replicated.
    At pi=(1/4,1/4,1/2), k=3, r=1, the closed endpoint returns state 3 although P33=0.
    That event is null under ideal continuous uniform sampling, so it does not refute
    the ideal law, but it rules out an unconditional closed-endpoint/floating-point
    guarantee. The original publication remains unmodified.
- assessment_id: scope-and-boundaries
  area: consistency
  topic: Finite conditional kernels, supplied ordering, source-error handling and
    composed-scan limits
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - neal2024
  - calculation-main
  - calculation-extra
  - source-math-provenance
  summary: Mechanism, scan/parameter limits and identity boundaries remain qualified.
  details: Scope is finite ordered labels and an exact nonnegative normalized conditional
    law, with the first-maximizer and zero-current conventions retained. A zero-mass
    current value does not supply an undefined zero-total conditioning law. Countably
    infinite extensions, adaptive order changes, floating-point stability, general
    convergence and benchmark superiority are outside scope. Minimum self mass is
    not a guarantee of aperiodicity, irreducibility or lower asymptotic variance.
    The 84-page report and its cited antecedent proofs/empirical sections were not
    wholly read.
- assessment_id: actual-maintained-fields
  area: provenance
  topic: All captured maintained fields
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - actual-record-reading
  - identity
  - mapping
  - neal2024
  summary: Root reassessed the complete current record after canonical capture; DRAFT
    remains.
  details: 'Root fully read both actual maintained YAML records after canonical capture,
    all prepared claim/mapping narratives, actual report delta, history and integrity
    result. All six claims and source locators are scoped to exact finite normalized
    conditional kernels. Related AIO:MarkovChain is a method/process association;
    no inherited neural assertions or alias equivalence. Original precise retrieval
    timestamp remains in the raw manifest; canonical source metadata truncates to
    schema whole seconds, with the prewrite validation failure preserved. Original/portable
    calculator derivation and failed printed-Figure10 comparison remain explicit.
    No author implementation, empirical replication, independent approval or saturation
    claim. Actual DRAFT status and source/version limits retained. No new maintained-record
    finding found. ZFSS uses the nearest backward qualifying blocker with recomputed
    factor and preserved remaining order. Added pieces cannot exceed preceding originals;
    the blocker eliminates regular-case self transitions. Dominant mass requires2h-1
    stationary self mass. Printed Figure10 ZFSS rows2/3 are explicitly nonstationary;
    corrected calculations are curator evidence, not an author erratum. Rereads: Neal
    author report text PDF pp41,43–47,51 and visual pp42,46. Visual42 confirms actual
    printed comparison rows; visual46 confirms the ambiguous zero-current outer loop
    and r>=s endpoint. Earlier text1–51 and selected visual readings are retained,
    not all claimed freshly reread.'
- assessment_id: source-error-and-portable-lineage
  area: provenance
  topic: Raw source discrepancy and exact calculator derivation
  outcome: supported
  target_ids:
  - AIMech:ZeroSelfFlattenedSliceSampling
  evidence_ids:
  - source-error-portable-lineage
  summary: The source discrepancy and original-to-portable lineage remain explicit.
  details: Figure 10 printed ZFSS rows are retained as a negative control, not silently
    replaced or labeled an author erratum. Algorithm 9 loop/endpoint limits are qualified.
    Original and portable mathematical results agree after only declared metadata
    exclusions; source reading and execution scopes remain separately attributed.
findings: []
actions: []
limitations:
- Author self-review, not independent scientific approval or DRAFT promotion.
- Scope is finite ordered labels and an exact nonnegative normalized conditional law,
  with the first-maximizer and zero-current conventions retained. A zero-mass current
  value does not supply an undefined zero-total conditioning law. Countably infinite
  extensions, adaptive order changes, floating-point stability, general convergence
  and benchmark superiority are outside scope. Minimum self mass is not a guarantee
  of aperiodicity, irreducibility or lower asymptotic variance. The 84-page report
  and its cited antecedent proofs/empirical sections were not wholly read.
- Bounded exact Fraction calculations are original curator checks, not author software
  or a general proof.
- Source, identity and mathematical supporting agents belong to the same author workflow;
  this remains author self-review.
- Historical703-native identity/source handoffs remain attributed; current prewrite706-native
  inventory, searches and actual neighbors govern the added identities.
- The raw failed Figure 10 comparison, corrected negative-control interpretation and
  original-to-portable calculator lineage remain explicit.
notes:
- Empty findings reflect actual root assessment of this selected captured record only;
  no unrelated finding closure or literature saturation is asserted.
- A publication matrix discrepancy is retained as a source limitation; no maintained-record
  finding or issue closure is invented from that discrepancy.
tags:
- native-concepts
- self-review
- discovery-ongoing
- mcmc
```
