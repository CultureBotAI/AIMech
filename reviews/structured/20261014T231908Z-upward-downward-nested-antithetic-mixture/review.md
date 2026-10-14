# Scientific author self-review of Upward-downward nested antithetic mixture

- Review: 20261014T231908Z-upward-downward-nested-antithetic-mixture
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T23:06:17.157100Z
- Finished UTC: 2026-10-14T23:19:08.747828Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The explicit complete-component half mixture is supported as a distinct DRAFT algorithm. Independent valid tie policies, possible positive self mass and joint-scan limitations remain explicit.

## Scope And Provenance

All maintained fields of the selected record. Actual source scope: neal2024: Post-capture root native-text reread PDF pages [2, 3, 10, 15, 24, 28, 29, 49]; relevant additional primary text and selected visuals remain in separately retained earlier root ledgers. No full84-page reading claimed.. Reread the actual finite construction, mixture/order conventions and conditional/uniform-target boundaries against maintained claims. Earlier focal/tail derivations and visual assessments remain attributed; current reading does not expand to empirical or full proof certification.

Selection: Exact maintained ID: AIMech:UpwardDownwardNestedAntitheticMixture
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f80a7e2e48616126ad74f0e53aac6eadac9e9034.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:UpwardDownwardNestedAntitheticMixture | data/curated/UpwardDownwardNestedAntitheticMixture.yaml | maintained | Upward-downward nested antithetic mixture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 361.24s (0:06:01)<br>Checked 442 record(s); 0 failed.<br>Checked 713 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 398 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 404,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| just render | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages<br>uv run --locked python scripts/render_pages.py<br> |
| just render-check | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | pages/ is current<br>uv run --locked python scripts/render_pages.py --check<br> |
| uv run --locked aimech check-source | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | Actual command exited zero without output. |
| python3 research/discovery/tower-boundaries.py | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | {<br>  "arbitrary_shift_shortcut": {<br>    "current_zero_based": 0,<br>    "geometry_row": [<br>      "5/6",<br>      "1/6"<br>    ],<br>    "pi": [<br>      "3/5",<br>      "2/5"<br>    ],<br>    "printed_alg6": [<br>      "1/3",<br>      "2/3"<br>    ],<br>    "shift": "1/10"<br>  },<br>  "closed_endpoint": {<br>    "current_zero_based": 0,<br>    "exact_row": [<br>      "0",<br>      "0",<br>      "1"<br>    ],<br>    "half_open_return_zero_based": 2,<br>    "pi": [<br>      "1/5",<br>      "3/10",<br>      "1/2"<br>    ],<br>    "printed_return_zero_based": 1,<br>    "r": "0",<br>    "shift": "1/2",<br>    "transition_probability": "0"<br>  },<br>  "counts": {<br>    "formula_geometry_orientation_comparisons": 16626,<br>    "interior_shift_cases": 8313,<br>    "maximum_first_2010_cases": 363,<br>    "policy_rows_checked": 3279,<br>    "positive_weight_vectors": 363,<br>    "printed_alg7_integrated_rows": 38487,<br>    "printed_alg7_partition_cells": 70962,<br>    "reverse_paired_order_cases": 363,<br>    "scaling_cases": 8313,<br>    "uniform_integration_rows": 38487,<br>    "uniform_partition_cells": 70962,<br>    "zero_current_rows_left_undefined": 1818,<br>    "zero_extension_shift_cases": 2016,<br>    "zero_extension_vectors": 336<br>  },<br>  "current_dependent_order_counterexample": {<br>    "after": [<br>      "2/3",<br>      "1/3",<br>      "0"<br>    ],<br>    "matrix": [<br>      [<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "orders_zero_based": [<br>      [<br>        0,<br>        1,<br>        2<br>      ],<br>      [<br>        1,<br>        0,<br>        2<br>      ],<br>      [<br>        2,<br>        0,<br>        1<br>      ]<br>    ],<br>    "pi": [<br>      "1/3",<br>      "1/3",<br>      "1/3"<br>    ]<br>  },<br>  "orientation_example": {<br>    "half": [<br>      [<br>        "0",<br>        "1/2",<br>        "1/4",<br>        "1/4"<br>      ],<br>      [<br>        "2/3",<br>        "0",<br>        "0",<br>        "1/3"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1/2",<br>        "1/2",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "negative": [<br>      [<br>        "0",<br>        "1/4",<br>        "1/4",<br>        "1/2"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "pi": [<br>      "2/5",<br>      "3/10",<br>      "1/10",<br>      "1/5"<br>    ],<br>    "positive": [<br>      [<br>        "0",<br>        "3/4",<br>        "1/4",<br>        "0"<br>      ],<br>      [<br>        "1/3",<br>        "0",<br>        "0",<br>        "2/3"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "shift": "2/5"<br>  },<br>  "periodicity": [<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "1"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "1"<br>        ]<br>      ],<br>      "states": 1<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "states": 2<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 3,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 3<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            2<br>          ]<br>        },<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            1,<br>            3<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 4,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 4<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 5,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 5<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            3<br>          ]<br>        },<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            1,<br>            4<br>          ]<br>        },<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            2,<br>            5<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 6,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 6<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 7,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 7<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            4<br>          ]<br>        },<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            1,<br>            5<br>          ]<br>        },<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            2,<br>            6<br>          ]<br>        },<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            3,<br>            7<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 8,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6,<br>            7<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 8<br>    },<br>    {<br>      "half_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6,<br>            7,<br>            8<br>          ]<br>        }<br>      ],<br>      "half_shift": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "maximum_classes": [<br>        {<br>          "closed": true,<br>          "period": 9,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6,<br>            7,<br>            8<br>          ]<br>        }<br>      ],<br>      "maximum_shift": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "states": 9<br>    }<br>  ],<br>  "point_mass": {<br>    "interior": [<br>      [<br>        "1"<br>      ]<br>    ],<br>    "maximum_endpoint_extension": [<br>      [<br>        "1"<br>      ]<br>    ]<br>  },<br>  "qualifications": [<br>    "The printed-source negative controls are retained; no source erratum or universal defect in either orientation is inferred.",<br>    "Only exactly reverse-paired UST/DST orders, including tied labels, justify transpose/equal-mixture checks.",<br>    "Zero current rows and maximum-shift point-mass endpoints are outside the maintained positive/interior specification.",<br>    "The direct lower bound follows because total incoming flow from other states is at most W-w_max; finite checks do not establish efficiency or convergence."<br>  ],<br>  "reversible_local_nonreversible_composition": {<br>    "equal_mixture": [<br>      [<br>        "0",<br>        "1/2",<br>        "1/2",<br>        "0"<br>      ],<br>      [<br>        "1/4",<br>        "1/4",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "1/6",<br>        "0",<br>        "1/3",<br>        "1/2"<br>      ],<br>      [<br>        "0",<br>        "1/4",<br>        "3/8",<br>        "3/8"<br>      ]<br>    ],<br>    "local_updates": [<br>      [<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1/3",<br>          "0",<br>          "2/3",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "0",<br>          "1/2"<br>        ]<br>      ],<br>      [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "3/4",<br>          "1/4"<br>        ]<br>      ]<br>    ],<br>    "ordered_composition": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "3/4",<br>        "1/4"<br>      ],<br>      [<br>        "0",<br>        "1/3",<br>        "0",<br>        "2/3"<br>      ],<br>      [<br>        "1/4",<br>        "1/4",<br>        "3/8",<br>        "1/8"<br>      ]<br>    ],<br>    "states": [<br>      [<br>        0,<br>        0<br>      ],<br>      [<br>        0,<br>        1<br>      ],<br>      [<br>        1,<br>        0<br>      ],<br>      [<br>        1,<br>        1<br>      ]<br>    ],<br>    "target": [<br>      "1/10",<br>      "1/5",<br>      "3/10",<br>      "2/5"<br>    ]<br>  },<br>  "reversible_nonhalf": {<br>    "matrix": [<br>      [<br>        "5/6",<br>        "1/6"<br>      ],<br>      [<br>        "1/4",<br>        "3/4"<br>      ]<br>    ],<br>    "pi": [<br>      "3/5",<br>      "2/5"<br>    ],<br>    "shift": "1/10"<br>  },<br>  "scope": "Exact finite original curator calculations. Positive ordered integer vectors of lengths 1..5 with entries 1..3; duplicates after normalization retained. Shift sets include all cumulative-boundary differences, adjacent midpoints and policy/example shifts. Nonnegative extension and endpoint policies are counted separately. No floating implementation, author-code or benchmark execution.",<br>  "systematic_scan_counterexample": {<br>    "classes": [<br>      {<br>        "closed": true,<br>        "period": 3,<br>        "states_zero_based": [<br>          0,<br>          4,<br>          8<br>        ]<br>      },<br>      {<br>        "closed": true,<br>        "period": 3,<br>        "states_zero_based": [<br>          1,<br>          5,<br>          6<br>        ]<br>      },<br>      {<br>        "closed": true,<br>        "period": 3,<br>        "states_zero_based": [<br>          2,<br>          3,<br>          7<br>        ]<br>      }<br>    ],<br>    "matrix": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "states": [<br>      [<br>        0,<br>        0<br>      ],<br>      [<br>        0,<br>        1<br>      ],<br>      [<br>        0,<br>        2<br>      ],<br>      [<br>        1,<br>        0<br>      ],<br>      [<br>        1,<br>        1<br>      ],<br>      [<br>        1,<br>        2<br>      ],<br>      [<br>        2,<br>        0<br>      ],<br>      [<br>        2,<br>        1<br>      ],<br>      [<br>        2,<br>        2<br>      ]<br>    ],<br>    "target": [<br>      "1/9",<br>      "1/9",<br>      "1/9",<br>      "1/9",<br>      "1/9",<br>      "1/9",<br>      "1/9",<br>      "1/9",<br>      "1/9"<br>    ]<br>  },<br>  "zero_row_nonuniqueness": {<br>    "completions": [<br>      [<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ]<br>      ],<br>      [<br>        [<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ]<br>      ]<br>    ],<br>    "partial_rows": [<br>      null,<br>      [<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "0",<br>        "1/2",<br>        "1/2"<br>      ]<br>    ],<br>    "weights": [<br>      "0",<br>      "1",<br>      "2"<br>    ]<br>  }<br>}<br> |
| python3 research/discovery/mixture-boundaries.py | passed | True | AIMech:UpwardDownwardNestedAntitheticMixture | {<br>  "UDNAM_scope": {<br>    "HST": [<br>      [<br>        "0",<br>        "5/8",<br>        "3/8"<br>      ],<br>      [<br>        "5/6",<br>        "0",<br>        "1/6"<br>      ],<br>      [<br>        "3/4",<br>        "1/4",<br>        "0"<br>      ]<br>    ],<br>    "Liu_modified_Gibbs": [<br>      [<br>        "3/14",<br>        "1/2",<br>        "2/7"<br>      ],<br>      [<br>        "2/3",<br>        "1/21",<br>        "2/7"<br>      ],<br>      [<br>        "4/7",<br>        "3/7",<br>        "0"<br>      ]<br>    ],<br>    "ST": [<br>      [<br>        "0",<br>        "3/4",<br>        "1/4"<br>      ],<br>      [<br>        "2/3",<br>        "0",<br>        "1/3"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "U_then_D": [<br>      [<br>        "23/35",<br>        "1/5",<br>        "1/7"<br>      ],<br>      [<br>        "8/35",<br>        "17/35",<br>        "2/7"<br>      ],<br>      [<br>        "12/35",<br>        "13/35",<br>        "2/7"<br>      ]<br>    ],<br>    "U_then_D_reversible": false,<br>    "ZDNAM": [<br>      [<br>        "0",<br>        "5/8",<br>        "3/8"<br>      ],<br>      [<br>        "5/6",<br>        "0",<br>        "1/6"<br>      ],<br>      [<br>        "3/4",<br>        "1/4",<br>        "0"<br>      ]<br>    ],<br>    "all_six_orders_all_shift_exclusion": [<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "2/9",<br>        "solution": {<br>          "candidate_fraction": "51/28",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "159/140",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "2/9",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "1/3",<br>        "solution": {<br>          "candidate_fraction": "23/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "19/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/3",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "4/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "3/4",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "4/9",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "5/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "5/56"<br>        }<br>      },<br>      {<br>        "left": "5/9",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "2/3",<br>        "solution": {<br>          "candidate_fraction": "5/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-19/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "2/3",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "7/9",<br>        "solution": {<br>          "candidate_fraction": "-9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-89/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "7/9",<br>        "order": [<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "2/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "2/9",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "1/3",<br>        "solution": {<br>          "candidate_fraction": "23/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "159/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/3",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "4/9",<br>        "solution": {<br>          "candidate_fraction": "9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "89/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "4/9",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "5/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "5/56"<br>        }<br>      },<br>      {<br>        "left": "5/9",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "2/3",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "3/4",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "2/3",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "7/9",<br>        "solution": {<br>          "candidate_fraction": "-9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "51/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "7/9",<br>        "order": [<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "-23/28",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-19/140",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "2/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "2/9",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "1/3",<br>        "solution": {<br>          "candidate_fraction": "23/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "159/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/3",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "4/9",<br>        "solution": {<br>          "candidate_fraction": "9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "89/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "4/9",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "5/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "5/56"<br>        }<br>      },<br>      {<br>        "left": "5/9",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "2/3",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "3/4",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "2/3",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "7/9",<br>        "solution": {<br>          "candidate_fraction": "-9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "51/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "7/9",<br>        "order": [<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "-23/28",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-19/140",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "2/9",<br>        "solution": {<br>          "candidate_fraction": "51/28",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "159/140",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "2/9",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "1/3",<br>        "solution": {<br>          "candidate_fraction": "23/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "19/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/3",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "4/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "3/4",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "4/9",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "5/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "5/56"<br>        }<br>      },<br>      {<br>        "left": "5/9",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "2/3",<br>        "solution": {<br>          "candidate_fraction": "5/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-19/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "2/3",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "7/9",<br>        "solution": {<br>          "candidate_fraction": "-9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-89/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "7/9",<br>        "order": [<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "2/9",<br>        "solution": {<br>          "candidate_fraction": "51/28",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "159/140",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "2/9",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "1/3",<br>        "solution": {<br>          "candidate_fraction": "23/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "19/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/3",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "4/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "3/4",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "4/9",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "5/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "5/56"<br>        }<br>      },<br>      {<br>        "left": "5/9",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "2/3",<br>        "solution": {<br>          "candidate_fraction": "5/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-19/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "2/3",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "7/9",<br>        "solution": {<br>          "candidate_fraction": "-9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-89/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "7/9",<br>        "order": [<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "2/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "2/9",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "1/3",<br>        "solution": {<br>          "candidate_fraction": "23/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "159/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/3",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "4/9",<br>        "solution": {<br>          "candidate_fraction": "9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "89/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "4/9",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "5/9",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "5/56"<br>        }<br>      },<br>      {<br>        "left": "5/9",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "2/3",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "3/4",<br>          "matches": false,<br>          "required_value": "159/280"<br>        }<br>      },<br>      {<br>        "left": "2/3",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "7/9",<br>        "solution": {<br>          "candidate_fraction": "-9/14",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "51/70",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "7/9",<br>        "order": [<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "-23/28",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "-19/140",<br>          "matches": false<br>        }<br>      }<br>    ],<br>    "minimum_self_mass": "0",<br>    "mixture": [<br>      [<br>        "5/56",<br>        "159/280",<br>        "12/35"<br>      ],<br>      [<br>        "53/70",<br>        "1/30",<br>        "22/105"<br>      ],<br>      [<br>        "24/35",<br>        "11/35",<br>        "0"<br>      ]<br>    ],<br>    "pi": [<br>      "4/9",<br>      "1/3",<br>      "2/9"<br>    ],<br>    "row_dependent_after": [<br>      "11/21",<br>      "32/105",<br>      "6/35"<br>    ],<br>    "row_dependent_component_choice": [<br>      [<br>        "5/28",<br>        "15/28",<br>        "2/7"<br>      ],<br>      [<br>        "4/5",<br>        "1/15",<br>        "2/15"<br>      ],<br>      [<br>        "4/5",<br>        "1/5",<br>        "0"<br>      ]<br>    ],<br>    "stationary_self_mass": "16/315"<br>  },<br>  "UDST_uniform4": {<br>    "UDNAM": [<br>      [<br>        "0",<br>        "1/3",<br>        "1/3",<br>        "1/3"<br>      ],<br>      [<br>        "1/3",<br>        "0",<br>        "1/3",<br>        "1/3"<br>      ],<br>      [<br>        "1/3",<br>        "1/3",<br>        "0",<br>        "1/3"<br>      ],<br>      [<br>        "1/3",<br>        "1/3",<br>        "1/3",<br>        "0"<br>      ]<br>    ],<br>    "UDST": [<br>      [<br>        "0",<br>        "1/2",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "1/2",<br>        "0",<br>        "1/2",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1/2",<br>        "0",<br>        "1/2"<br>      ],<br>      [<br>        "1/2",<br>        "0",<br>        "1/2",<br>        "0"<br>      ]<br>    ],<br>    "ZDNAM": [<br>      [<br>        "0",<br>        "1/3",<br>        "1/3",<br>        "1/3"<br>      ],<br>      [<br>        "1/3",<br>        "0",<br>        "1/3",<br>        "1/3"<br>      ],<br>      [<br>        "1/3",<br>        "1/3",<br>        "0",<br>        "1/3"<br>      ],<br>      [<br>        "1/3",<br>        "1/3",<br>        "1/3",<br>        "0"<br>      ]<br>    ],<br>    "all_24_orders_all_shift_exclusion": [<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          1,<br>          2,<br>          3<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          0,<br>          1,<br>          2,<br>          3<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          0,<br>          1,<br>          2,<br>          3<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          0,<br>          1,<br>          2,<br>          3<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          1,<br>          3,<br>          2<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          0,<br>          1,<br>          3,<br>          2<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          0,<br>          1,<br>          3,<br>          2<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          0,<br>          1,<br>          3,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          2,<br>          1,<br>          3<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          0,<br>          2,<br>          1,<br>          3<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          0,<br>          2,<br>          1,<br>          3<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          0,<br>          2,<br>          1,<br>          3<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          2,<br>          3,<br>          1<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          0,<br>          2,<br>          3,<br>          1<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          0,<br>          2,<br>          3,<br>          1<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          0,<br>          2,<br>          3,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          3,<br>          1,<br>          2<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          0,<br>          3,<br>          1,<br>          2<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          0,<br>          3,<br>          1,<br>          2<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          0,<br>          3,<br>          1,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          0,<br>          3,<br>          2,<br>          1<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          0,<br>          3,<br>          2,<br>          1<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          0,<br>          3,<br>          2,<br>          1<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          0,<br>          3,<br>          2,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          0,<br>          2,<br>          3<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          1,<br>          0,<br>          2,<br>          3<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          1,<br>          0,<br>          2,<br>          3<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          1,<br>          0,<br>          2,<br>          3<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          0,<br>          3,<br>          2<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          1,<br>          0,<br>          3,<br>          2<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          1,<br>          0,<br>          3,<br>          2<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          1,<br>          0,<br>          3,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          2,<br>          0,<br>          3<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          1,<br>          2,<br>          0,<br>          3<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          1,<br>          2,<br>          0,<br>          3<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          1,<br>          2,<br>          0,<br>          3<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          2,<br>          3,<br>          0<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          1,<br>          2,<br>          3,<br>          0<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          1,<br>          2,<br>          3,<br>          0<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          1,<br>          2,<br>          3,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          3,<br>          0,<br>          2<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          1,<br>          3,<br>          0,<br>          2<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          1,<br>          3,<br>          0,<br>          2<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          1,<br>          3,<br>          0,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          1,<br>          3,<br>          2,<br>          0<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          1,<br>          3,<br>          2,<br>          0<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          1,<br>          3,<br>          2,<br>          0<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          1,<br>          3,<br>          2,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          0,<br>          1,<br>          3<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          2,<br>          0,<br>          1,<br>          3<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          2,<br>          0,<br>          1,<br>          3<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          2,<br>          0,<br>          1,<br>          3<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          0,<br>          3,<br>          1<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          2,<br>          0,<br>          3,<br>          1<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          2,<br>          0,<br>          3,<br>          1<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          2,<br>          0,<br>          3,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          1,<br>          0,<br>          3<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          2,<br>          1,<br>          0,<br>          3<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          2,<br>          1,<br>          0,<br>          3<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          2,<br>          1,<br>          0,<br>          3<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          1,<br>          3,<br>          0<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          2,<br>          1,<br>          3,<br>          0<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          2,<br>          1,<br>          3,<br>          0<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          2,<br>          1,<br>          3,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          3,<br>          0,<br>          1<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          2,<br>          3,<br>          0,<br>          1<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          2,<br>          3,<br>          0,<br>          1<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          2,<br>          3,<br>          0,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          2,<br>          3,<br>          1,<br>          0<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          2,<br>          3,<br>          1,<br>          0<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          2,<br>          3,<br>          1,<br>          0<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          2,<br>          3,<br>          1,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          3,<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          3,<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          3,<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          3,<br>          0,<br>          1,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          3,<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          3,<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          3,<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          3,<br>          0,<br>          2,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          3,<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          3,<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          3,<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          3,<br>          1,<br>          0,<br>          2<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          3,<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          3,<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            2,<br>            0<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          3,<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "0",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          3,<br>          1,<br>          2,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          3,<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "candidate_fraction": "1",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          3,<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            1,<br>            0<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          3,<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          3,<br>          2,<br>          0,<br>          1<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "0",<br>        "order": [<br>          3,<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "1/4",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/4",<br>        "order": [<br>          3,<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "1/2",<br>        "solution": {<br>          "constant_entry_mismatch": [<br>            0,<br>            1<br>          ],<br>          "fixed_value": "0",<br>          "matches": false,<br>          "required_value": "1/2"<br>        }<br>      },<br>      {<br>        "left": "1/2",<br>        "order": [<br>          3,<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "3/4",<br>        "solution": {<br>          "candidate_fraction": "1/2",<br>          "conflict_entry": [<br>            0,<br>            2<br>          ],<br>          "conflicting_fraction": "1",<br>          "matches": false<br>        }<br>      },<br>      {<br>        "left": "3/4",<br>        "order": [<br>          3,<br>          2,<br>          1,<br>          0<br>        ],<br>        "right": "1",<br>        "solution": {<br>          "candidate_fraction": "0",<br>          "conflict_entry": [<br>            0,<br>            1<br>          ],<br>          "conflicting_fraction": "1/2",<br>          "matches": false<br>        }<br>      }<br>    ],<br>    "analytic_certificate": "For equal quarter intervals, any shift has two consecutive cyclic offsets q,q+1 with probabilities 1-t,t. Matching two half-probability outputs requires t=1/2. No pair of consecutive residues modulo4 is closed under negation. Thus this single-shift kernel cannot be reversible in any order, whereas UDST is reversible. Boundary shifts have one supported destination and also cannot match.",<br>    "every_single_NAM_order_equal": true,<br>    "pi": [<br>      "1/4",<br>      "1/4",<br>      "1/4",<br>      "1/4"<br>    ],<br>    "source_uniform_FSS_ZFSS_cycle_example": [<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ]<br>    ]<br>  },<br>  "assumptions": [<br>    "Use one complete positive target and current-independent component-selection probabilities at each fixed conditioning environment.",<br>    "UDNAM mixes two reversible NAM kernels; independent valid ascending and descending tie policies preserve reversibility, although the mixture can change.",<br>    "UDST uses one maximum anchor and a specified ascending tail with its exact reversal, including tied labels. Independent weak sorting does not establish reverse-flow pairing.",<br>    "Equal mixture is part of each named method. Unequal constant weights remain invariant but need not remain reversible for UDST.",<br>    "One-state UDST maximum shift equals total mass; its stay kernel is an explicitly guarded boundary extension.",<br>    "The comparison with uniform FSS/ZFSS uses the source-described deterministic-cycle property; their implementation is not imported or executed here."<br>  ],<br>  "dependency_sha256": {<br>    "nam-boundaries.py": "cb58dd0a41b32a7c4f12dcfc711963b39ff062b12f79d8fe6bf065b777714941",<br>    "tower-boundaries.py": "d8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47"<br>  },<br>  "expanded_counts": {<br>    "arbitrary_fixed_NAM_mixing_weight_cases": 600,<br>    "compatible_NAM_order_cases": 771,<br>    "independent_UDNAM_tie_pairs": 3231,<br>    "one_state_UDST_endpoint_extensions": 3,<br>    "paired_UDST_order_cases": 435,<br>    "positive_target_vectors": 120<br>  },<br>  "fixed_two_binary_coordinate_scan": {<br>    "classes": [<br>      {<br>        "closed": true,<br>        "period": 2,<br>        "states_zero_based": [<br>          0,<br>          3<br>        ]<br>      },<br>      {<br>        "closed": true,<br>        "period": 2,<br>        "states_zero_based": [<br>          1,<br>          2<br>        ]<br>      }<br>    ],<br>    "matrix": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0",<br>        "0"<br>      ]<br>    ],<br>    "states": [<br>      [<br>        0,<br>        0<br>      ],<br>      [<br>        0,<br>        1<br>      ],<br>      [<br>        1,<br>        0<br>      ],<br>      [<br>        1,<br>        1<br>      ]<br>    ]<br>  },<br>  "half_dominant_point_boundaries": [<br>    {<br>      "UDNAM": [<br>        [<br>          "1"<br>        ]<br>      ],<br>      "UDNAM_self_mass": "1",<br>      "UDST": [<br>        [<br>          "1"<br>        ]<br>      ],<br>      "UDST_self_mass": "1",<br>      "minimum_self_mass": "1",<br>      "pi": [<br>        "1"<br>      ],<br>      "weights": [<br>        1<br>      ]<br>    },<br>    {<br>      "UDNAM": [<br>        [<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "UDNAM_self_mass": "0",<br>      "UDST": [<br>        [<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "UDST_self_mass": "0",<br>      "minimum_self_mass": "0",<br>      "pi": [<br>        "1/2",<br>        "1/2"<br>      ],<br>      "weights": [<br>        1,<br>        1<br>      ]<br>    },<br>    {<br>      "UDNAM": [<br>        [<br>          "3/20",<br>          "21/40",<br>          "13/40"<br>        ],<br>        [<br>          "7/8",<br>          "0",<br>          "1/8"<br>        ],<br>        [<br>          "13/16",<br>          "3/16",<br>          "0"<br>        ]<br>      ],<br>      "UDNAM_self_mass": "3/40",<br>      "UDST": [<br>        [<br>          "0",<br>          "3/5",<br>          "2/5"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "UDST_self_mass": "0",<br>      "minimum_self_mass": "0",<br>      "pi": [<br>        "1/2",<br>        "3/10",<br>        "1/5"<br>      ],<br>      "weights": [<br>        5,<br>        3,<br>        2<br>      ]<br>    },<br>    {<br>      "UDNAM": [<br>        [<br>          "7/18",<br>          "17/36",<br>          "5/36"<br>        ],<br>        [<br>          "17/18",<br>          "0",<br>          "1/18"<br>        ],<br>        [<br>          "5/6",<br>          "1/6",<br>          "0"<br>        ]<br>      ],<br>      "UDNAM_self_mass": "7/30",<br>      "UDST": [<br>        [<br>          "1/3",<br>          "1/2",<br>          "1/6"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "UDST_self_mass": "1/5",<br>      "minimum_self_mass": "1/5",<br>      "pi": [<br>        "3/5",<br>        "3/10",<br>        "1/10"<br>      ],<br>      "weights": [<br>        6,<br>        3,<br>        1<br>      ]<br>    },<br>    {<br>      "UDNAM": [<br>        [<br>          "55/72",<br>          "17/144",<br>          "17/144"<br>        ],<br>        [<br>          "17/18",<br>          "0",<br>          "1/18"<br>        ],<br>        [<br>          "17/18",<br>          "1/18",<br>          "0"<br>        ]<br>      ],<br>      "UDNAM_self_mass": "11/18",<br>      "UDST": [<br>        [<br>          "3/4",<br>          "1/8",<br>          "1/8"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "UDST_self_mass": "3/5",<br>      "minimum_self_mass": "3/5",<br>      "pi": [<br>        "4/5",<br>        "1/10",<br>        "1/10"<br>      ],<br>      "weights": [<br>        8,<br>        1,<br>        1<br>      ]<br>    }<br>  ],<br>  "mixture_weight_boundaries": {<br>    "after": [<br>      "1/3",<br>      "2/3",<br>      "0"<br>    ],<br>    "paired_components": [<br>      [<br>        [<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      [<br>        [<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0"<br>        ]<br>      ]<br>    ],<br>    "pi": [<br>      "1/3",<br>      "1/3",<br>      "1/3"<br>    ],<br>    "state_dependent_choice": [<br>      [<br>        "0",<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "1",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1",<br>        "0"<br>      ]<br>    ],<br>    "unequal_fixed_mix": [<br>      [<br>        "0",<br>        "1/4",<br>        "3/4"<br>      ],<br>      [<br>        "3/4",<br>        "0",<br>        "1/4"<br>      ],<br>      [<br>        "1/4",<br>        "3/4",<br>        "0"<br>      ]<br>    ],<br>    "unequal_fixed_mix_reversible": false,<br>    "unequal_fixed_mix_stationary": true<br>  },<br>  "original_witnesses": {<br>    "positive_target_vectors": 120,<br>    "scope": "Original exact Fraction calculations, not author software. Positive integer weights1..3 for lengths1..4 produce120 ordered vectors, including repeated normalized targets. One-state maximum-shift endpoint is a separately recognized identity extension. No float, efficiency, benchmark or general ergodicity claim.",<br>    "udnam_distinction": {<br>      "DNAM": [<br>        [<br>          "0",<br>          "3/5",<br>          "2/5"<br>        ],<br>        [<br>          "4/5",<br>          "1/15",<br>          "2/15"<br>        ],<br>        [<br>          "4/5",<br>          "1/5",<br>          "0"<br>        ]<br>      ],<br>      "UDNAM": [<br>        [<br>          "5/56",<br>          "159/280",<br>          "12/35"<br>        ],<br>        [<br>          "53/70",<br>          "1/30",<br>          "22/105"<br>        ],<br>        [<br>          "24/35",<br>          "11/35",<br>          "0"<br>        ]<br>      ],<br>      "UNAM": [<br>        [<br>          "5/28",<br>          "15/28",<br>          "2/7"<br>        ],<br>        [<br>          "5/7",<br>          "0",<br>          "2/7"<br>        ],<br>        [<br>          "4/7",<br>          "3/7",<br>          "0"<br>        ]<br>      ],<br>      "all_six_single_NAM_orders": [<br>        {<br>          "matrix": [<br>            [<br>              "0",<br>              "3/5",<br>              "2/5"<br>            ],<br>            [<br>              "4/5",<br>              "1/15",<br>              "2/15"<br>            ],<br>            [<br>              "4/5",<br>              "1/5",<br>              "0"<br>            ]<br>          ],<br>          "order": [<br>            0,<br>            1,<br>            2<br>          ]<br>        },<br>        {<br>          "matrix": [<br>            [<br>              "0",<br>              "3/5",<br>              "2/5"<br>            ],<br>            [<br>              "4/5",<br>              "1/15",<br>              "2/15"<br>            ],<br>            [<br>              "4/5",<br>              "1/5",<br>              "0"<br>            ]<br>          ],<br>          "order": [<br>            0,<br>            2,<br>            1<br>          ]<br>        },<br>        {<br>          "matrix": [<br>            [<br>              "1/4",<br>              "1/2",<br>              "1/4"<br>            ],<br>            [<br>              "2/3",<br>              "0",<br>              "1/3"<br>            ],<br>            [<br>              "1/2",<br>              "1/2",<br>              "0"<br>            ]<br>          ],<br>          "order": [<br>            1,<br>            0,<br>            2<br>          ]<br>        },<br>        {<br>          "matrix": [<br>            [<br>              "1/4",<br>              "1/2",<br>              "1/4"<br>            ],<br>            [<br>              "2/3",<br>              "0",<br>              "1/3"<br>            ],<br>            [<br>              "1/2",<br>              "1/2",<br>              "0"<br>            ]<br>          ],<br>          "order": [<br>            1,<br>            2,<br>            0<br>          ]<br>        },<br>        {<br>          "matrix": [<br>            [<br>              "5/28",<br>              "15/28",<br>              "2/7"<br>            ],<br>            [<br>              "5/7",<br>              "0",<br>              "2/7"<br>            ],<br>            [<br>              "4/7",<br>              "3/7",<br>              "0"<br>            ]<br>          ],<br>          "order": [<br>            2,<br>            0,<br>            1<br>          ]<br>        },<br>        {<br>          "matrix": [<br>            [<br>              "5/28",<br>              "15/28",<br>              "2/7"<br>            ],<br>            [<br>              "5/7",<br>              "0",<br>              "2/7"<br>            ],<br>            [<br>              "4/7",<br>              "3/7",<br>              "0"<br>            ]<br>          ],<br>          "order": [<br>            2,<br>            1,<br>            0<br>          ]<br>        }<br>      ],<br>      "down_order": [<br>        0,<br>        1,<br>        2<br>      ],<br>      "interpretation": "The mixture has two positive diagonal entries while each single NAM ordering has at most one; this one target disproves full construction equivalence. It does not assert disjoint kernel sets.",<br>      "pi": [<br>        "4/9",<br>        "1/3",<br>        "2/9"<br>      ],<br>      "positive_diagonals": 2,<br>      "up_order": [<br>        2,<br>        1,<br>        0<br>      ]<br>    },<br>    "udnam_tie_policy": {<br>      "DNAM_choices": [<br>        [<br>          [<br>            "0",<br>            "1/14",<br>            "3/14",<br>            "5/7"<br>          ],<br>          [<br>            "1/42",<br>            "1/21",<br>            "3/14",<br>            "5/7"<br>          ],<br>          [<br>            "1/14",<br>            "3/14",<br>            "0",<br>            "5/7"<br>          ],<br>          [<br>            "1/7",<br>            "3/7",<br>            "3/7",<br>            "0"<br>          ]<br>        ],<br>        [<br>          [<br>            "0",<br>            "3/14",<br>            "1/14",<br>            "5/7"<br>          ],<br>          [<br>            "1/14",<br>            "0",<br>            "3/14",<br>            "5/7"<br>          ],<br>          [<br>            "1/42",<br>            "3/14",<br>            "1/21",<br>            "5/7"<br>          ],<br>          [<br>            "1/7",<br>            "3/7",<br>            "3/7",<br>            "0"<br>          ]<br>        ]<br>      ],<br>      "UDNAM_choices": [<br>        [<br>          [<br>            "0",<br>            "53/308",<br>            "75/308",<br>            "45/77"<br>          ],<br>          [<br>            "53/924",<br>            "1/42",<br>            "171/616",<br>            "395/616"<br>          ],<br>          [<br>            "25/308",<br>            "171/616",<br>            "0",<br>            "395/616"<br>          ],<br>          [<br>            "9/77",<br>            "237/616",<br>            "237/616",<br>            "5/44"<br>          ]<br>        ],<br>        [<br>          [<br>            "0",<br>            "75/308",<br>            "53/308",<br>            "45/77"<br>          ],<br>          [<br>            "25/308",<br>            "0",<br>            "171/616",<br>            "395/616"<br>          ],<br>          [<br>            "53/924",<br>            "171/616",<br>            "1/42",<br>            "395/616"<br>          ],<br>          [<br>            "9/77",<br>            "237/616",<br>            "237/616",<br>            "5/44"<br>          ]<br>        ]<br>      ],<br>      "UNAM": [<br>        [<br>          "0",<br>          "3/11",<br>          "3/11",<br>          "5/11"<br>        ],<br>        [<br>          "1/11",<br>          "0",<br>          "15/44",<br>          "25/44"<br>        ],<br>        [<br>          "1/11",<br>          "15/44",<br>          "0",<br>          "25/44"<br>        ],<br>        [<br>          "1/11",<br>          "15/44",<br>          "15/44",<br>          "5/22"<br>        ]<br>      ],<br>      "down_orders": [<br>        [<br>          3,<br>          2,<br>          1,<br>          0<br>        ],<br>        [<br>          3,<br>          1,<br>          2,<br>          0<br>        ]<br>      ],<br>      "interpretation": "UNAM is unchanged under this tie exchange; DNAM and hence UDNAM change. Each component and mixture remains reversible. A reverse-pair requirement is not needed for UDNAM reversibility.",<br>      "pi": [<br>        "1/12",<br>        "1/4",<br>        "1/4",<br>        "5/12"<br>      ],<br>      "up_orders": [<br>        [<br>          0,<br>          1,<br>          2,<br>          3<br>        ],<br>        [<br>          0,<br>          2,<br>          1,<br>          3<br>        ]<br>      ]<br>    },<br>    "udst_single_circle_distinction": {<br>      "DST_positive_orientation": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "HST_same_order": [<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "UDNAM": [<br>        [<br>          "0",<br>          "1/3",<br>          "1/3",<br>          "1/3"<br>        ],<br>        [<br>          "1/3",<br>          "0",<br>          "1/3",<br>          "1/3"<br>        ],<br>        [<br>          "1/3",<br>          "1/3",<br>          "0",<br>          "1/3"<br>        ],<br>        [<br>          "1/3",<br>          "1/3",<br>          "1/3",<br>          "0"<br>        ]<br>      ],<br>      "UDST": [<br>        [<br>          "0",<br>          "1/2",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "1/2",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0"<br>        ]<br>      ],<br>      "UST_positive_orientation": [<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "all_24_orders_all_shift_certificate": [<br>        {<br>          "left": "0",<br>          "order": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            0,<br>            1,<br>            3,<br>            2<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            0,<br>            1,<br>            3,<br>            2<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            0,<br>            1,<br>            3,<br>            2<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            0,<br>            1,<br>            3,<br>            2<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            0,<br>            2,<br>            1,<br>            3<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            0,<br>            2,<br>            1,<br>            3<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            0,<br>            2,<br>            1,<br>            3<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            0,<br>            2,<br>            1,<br>            3<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            0,<br>            2,<br>            3,<br>            1<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            0,<br>            2,<br>            3,<br>            1<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            0,<br>            2,<br>            3,<br>            1<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            0,<br>            2,<br>            3,<br>            1<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            0,<br>            3,<br>            1,<br>            2<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            0,<br>            3,<br>            1,<br>            2<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            0,<br>            3,<br>            1,<br>            2<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            0,<br>            3,<br>            1,<br>            2<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            0,<br>            3,<br>            2,<br>            1<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            0,<br>            3,<br>            2,<br>            1<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            0,<br>            3,<br>            2,<br>            1<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            0,<br>            3,<br>            2,<br>            1<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            1,<br>            0,<br>            2,<br>            3<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            1,<br>            0,<br>            2,<br>            3<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            1,<br>            0,<br>            2,<br>            3<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            1,<br>            0,<br>            2,<br>            3<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            1,<br>            0,<br>            3,<br>            2<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            1,<br>            0,<br>            3,<br>            2<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            1,<br>            0,<br>            3,<br>            2<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            1,<br>            0,<br>            3,<br>            2<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            1,<br>            2,<br>            0,<br>            3<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            1,<br>            2,<br>            0,<br>            3<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            1,<br>            2,<br>            0,<br>            3<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            1,<br>            2,<br>            0,<br>            3<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            1,<br>            2,<br>            3,<br>            0<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            1,<br>            2,<br>            3,<br>            0<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            1,<br>            2,<br>            3,<br>            0<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            1,<br>            2,<br>            3,<br>            0<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            1,<br>            3,<br>            0,<br>            2<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            1,<br>            3,<br>            0,<br>            2<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            1,<br>            3,<br>            0,<br>            2<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            1,<br>            3,<br>            0,<br>            2<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            1,<br>            3,<br>            2,<br>            0<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            1,<br>            3,<br>            2,<br>            0<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            1,<br>            3,<br>            2,<br>            0<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            1,<br>            3,<br>            2,<br>            0<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            2,<br>            0,<br>            1,<br>            3<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            2,<br>            0,<br>            1,<br>            3<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            2,<br>            0,<br>            1,<br>            3<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            2,<br>            0,<br>            1,<br>            3<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            2,<br>            0,<br>            3,<br>            1<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            2,<br>            0,<br>            3,<br>            1<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            2,<br>            0,<br>            3,<br>            1<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            2,<br>            0,<br>            3,<br>            1<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            2,<br>            1,<br>            0,<br>            3<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            2,<br>            1,<br>            0,<br>            3<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            2,<br>            1,<br>            0,<br>            3<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            2,<br>            1,<br>            0,<br>            3<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            2,<br>            1,<br>            3,<br>            0<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            2,<br>            1,<br>            3,<br>            0<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            2,<br>            1,<br>            3,<br>            0<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            2,<br>            1,<br>            3,<br>            0<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            2,<br>            3,<br>            0,<br>            1<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            2,<br>            3,<br>            0,<br>            1<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            2,<br>            3,<br>            0,<br>            1<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            2,<br>            3,<br>            0,<br>            1<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            2,<br>            3,<br>            1,<br>            0<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            2,<br>            3,<br>            1,<br>            0<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            2,<br>            3,<br>            1,<br>            0<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            2,<br>            3,<br>            1,<br>            0<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            3,<br>            0,<br>            1,<br>            2<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            3,<br>            0,<br>            1,<br>            2<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            3,<br>            0,<br>            1,<br>            2<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            3,<br>            0,<br>            1,<br>            2<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            3,<br>            0,<br>            2,<br>            1<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            3,<br>            0,<br>            2,<br>            1<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            3,<br>            0,<br>            2,<br>            1<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            3,<br>            0,<br>            2,<br>            1<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            3,<br>            1,<br>            0,<br>            2<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            3,<br>            1,<br>            0,<br>            2<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            3,<br>            1,<br>            0,<br>            2<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            3,<br>            1,<br>            0,<br>            2<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            3,<br>            1,<br>            2,<br>            0<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            3,<br>            1,<br>            2,<br>            0<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              2,<br>              0<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            3,<br>            1,<br>            2,<br>            0<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "0",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            3,<br>            1,<br>            2,<br>            0<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            3,<br>            2,<br>            0,<br>            1<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "candidate_fraction": "1",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            3,<br>            2,<br>            0,<br>            1<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              1,<br>              0<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            3,<br>            2,<br>            0,<br>            1<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            3,<br>            2,<br>            0,<br>            1<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "0",<br>          "order": [<br>            3,<br>            2,<br>            1,<br>            0<br>          ],<br>          "right": "1/4",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/4",<br>          "order": [<br>            3,<br>            2,<br>            1,<br>            0<br>          ],<br>          "right": "1/2",<br>          "solution": {<br>            "constant_entry_mismatch": [<br>              0,<br>              1<br>            ],<br>            "fixed_value": "0",<br>            "matches": false,<br>            "required_value": "1/2"<br>          }<br>        },<br>        {<br>          "left": "1/2",<br>          "order": [<br>            3,<br>            2,<br>            1,<br>            0<br>          ],<br>          "right": "3/4",<br>          "solution": {<br>            "candidate_fraction": "1/2",<br>            "conflict_entry": [<br>              0,<br>              2<br>            ],<br>            "conflicting_fraction": "1",<br>            "matches": false<br>          }<br>        },<br>        {<br>          "left": "3/4",<br>          "order": [<br>            3,<br>            2,<br>            1,<br>            0<br>          ],<br>          "right": "1",<br>          "solution": {<br>            "candidate_fraction": "0",<br>            "conflict_entry": [<br>              0,<br>              1<br>            ],<br>            "conflicting_fraction": "1/2",<br>            "matches": false<br>          }<br>        }<br>      ],<br>      "closed_affine_segments": 96,<br>      "down_order": [<br>        0,<br>        3,<br>        2,<br>        1<br>      ],<br>      "interpretation": "For this uniform4 target, no single circular shift in any order gives the UDST kernel. All shifts in [0,1] are covered by four affine pieces per order, including endpoints. Either orientation is covered by the full shift range. This is one counterexample, not a classification of all coincidences.",<br>      "orders": 24,<br>      "pi": [<br>        "1/4",<br>        "1/4",<br>        "1/4",<br>        "1/4"<br>      ],<br>      "up_order": [<br>        0,<br>        1,<br>        2,<br>        3<br>      ]<br>    },<br>    "udst_unpaired_tie_failure": {<br>      "independently_tied_down_order": [<br>        0,<br>        1,<br>        2<br>      ],<br>      "interpretation": "Both same orders satisfy weak upward/downward probability sorting when all masses tie. They are not reverse-paired, so Eq101 and the reversibility conclusion do not follow. The bad mixture remains invariant, demonstrating precisely the missing pairing condition.",<br>      "paired_reverse_mixture": [<br>        [<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0"<br>        ]<br>      ],<br>      "pi": [<br>        "1/3",<br>        "1/3",<br>        "1/3"<br>      ],<br>      "unpaired_mixture": [<br>        [<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "up_order": [<br>        0,<br>        1,<br>        2<br>      ]<br>    }<br>  },<br>  "scope": "Exact positive finite conditional kernels. Original source-agent witness output is retained without runtime metadata. Expanded tie, independent-component, all-shift and exploration checks use pinned unchanged sibling routines. No efficiency, float, author-code, all-target nonintersection or general convergence claim.",<br>  "uniform_periodicity": [<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1<br>          ]<br>        }<br>      ],<br>      "states": 2<br>    },<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2<br>          ]<br>        }<br>      ],<br>      "states": 3<br>    },<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3<br>          ]<br>        }<br>      ],<br>      "states": 4<br>    },<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4<br>          ]<br>        }<br>      ],<br>      "states": 5<br>    },<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5<br>          ]<br>        }<br>      ],<br>      "states": 6<br>    },<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6<br>          ]<br>        }<br>      ],<br>      "states": 7<br>    },<br>    {<br>      "UDNAM_classes": [<br>        {<br>          "closed": true,<br>          "period": 1,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6,<br>            7<br>          ]<br>        }<br>      ],<br>      "UDST_classes": [<br>        {<br>          "closed": true,<br>          "period": 2,<br>          "states_zero_based": [<br>            0,<br>            1,<br>            2,<br>            3,<br>            4,<br>            5,<br>            6,<br>            7<br>          ]<br>        }<br>      ],<br>      "states": 8<br>    }<br>  ]<br>}<br> |

## Scientific And Domain Assessments

### Upward-downward nested antithetic mixture

identity: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Retain the narrow DRAFT identity within the documented search scope.

Neal p28 explicitly names UDNAM. Upward and downward policies belong to the existing NAM construction; their equal mixture has its own specified operation and a two-positive-diagonal witness outside all single NAM orderings on that target. It is not identified with ZDNAM, FSS/ZFSS, Liu correction, a shifted-tower mixture or a predictive model ensemble. No bare acronym or historical whole-framework alias is adopted.

### Definition and source scope

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

The maintained definition is supported within its stated method scope.

The definition identifies an equal mixture of two complete NAM component kernels, with fresh state-independent component choice at each local update. This is distinct from a once-per-chain selection, sequential product or a single supplied-order NAM construction. The record cites only the byte-pinned Neal author report26March2024. Sections5–8 define complete NAM, the upward/downward policies, tie behavior and the explicit p28 equal-mixture construction; pp2–3 and49 give conditional and uniform examples. Earlier FHY original full text remains unobtained. Tjelmeland and companion proof readings remain separately scoped historical context, not a basis for unmaintained efficiency or priority claims.

### Related Markov-process mapping

grounding: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

related_match expresses method-to-process association without equivalence or ontology inheritance.

The related_match to AIO:MarkovChain is a method-to-process association. The pinned CLASS describes a stochastic process/model, with Network and ProbabilisticHiddenLayer context, rather than this finite conditional transition algorithm. Twenty-two exact class contexts support this association and twenty-one rejected alternatives. No equivalence, subclass membership or inherited neural assertion follows.
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
AIO:Preprocessing: These stochastic transitions update a sampled state; they do not preprocess a training dataset.
AIO:Layer: Neural topology/component is a different abstraction.
AIO:HiddenLayer: Nonlinear network transformation is not conditional Markov sampling.
AIO:CausalGraphicalModel: Causal assumptions/graph model are not sampler identity or an entailed application.
AIO:EnsembleLearning: A learning task combining prediction algorithms is not an equal mixture of target-preserving Markov kernels.
AIO:RandomForest: A trained ensemble of decision trees is not a categorical conditional transition algorithm.
AIO:MixtureofExpertsLLM: A language model combining expert submodels is not a fixed-probability mixture of stochastic kernels.
AIO:FactorizedLLM: Factorized language-model components and product-of-experts synonyms do not identify this Markov update.

### complete-upward-and-downward-components

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Supported within the stated assumptions and inspected passages.

Neal Sections5–8, Eq19 and Algorithms2–4 define the full supplied-order construction and its ascending/descending policies. At each focal step the maximal change is r min(q/s,s/q); q&gt;=s terminates the remaining block. The mixture uses the complete components, not one focal correction. One-state targets are identities. Original and existing NAM matrix/row implementations agree in771 compatible finite target/order cases.

### constant-half-mixture-selection

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Supported within the stated assumptions and inspected passages.

Neal p28 defines transition probabilities as(U+D)/2. A fresh fair component choice implements this matrix. The exact(4,3,2)/9 example distinguishes U then D from this average, and a current-state-dependent component selector fails invariance. These are bounded negative controls for excluded implementations, not a prohibition of every adaptive method under additional conditions.

### reversible-mixture-and-conditional-use

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Supported within the stated assumptions and inspected passages.

Both complete NAM components are pi-reversible; linearity of weighted flow yields stochasticity, invariance and detailed balance of the constant half mixture. Full-conditional use preserves the joint target. The calculator checks3231 independently valid ascending/descending tie-order pairs on120 ordered positive integer vectors, retaining normalized duplicates. A fixed full sweep need not inherit reversibility.

### downward-tie-policy

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Supported within the stated assumptions and inspected passages.

Neal Eq75 p24 supports upward equal-probability invariance, while p28 and Figure6 p29 expose downward tie dependence. For(1,3,3,5)/12, two valid downward tie orders yield mixture diagonals(0,1/42,0,5/44) and(0,0,1/42,5/44). Independent valid component tie policies remain reversible; reverse pairing is not required for UDNAM.

### distinct-mixture-and-self-mass

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Supported within the stated assumptions and inspected passages.

For(4,3,2)/9, UDNAM diagonal(5/56,1/30,0) contains two positive entries; every one of the six single NAM orders has only one. Stationary self mass16/315 is positive although max pi&lt;1/2, distinguishing minimum-self constructions on this target. This counterexample rejects whole-construction equivalence without claiming disjoint kernel sets or universal noncoincidence.

### invariance-is-not-convergence

evidence: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Supported within the stated assumptions and inspected passages.

Neal Section2 and Section13 distinguish valid updates from exploration properties. A uniform binary UDNAM update flips deterministically, with period2. Two such coordinate flips in a fixed full sweep leave two proper closed joint classes. The calculator derives the matrix and classes exactly; no mixing-rate, burn-in or efficiency conclusion follows.

### Finite positive conditional kernels, complete component rules, order/tie/orientation qualifications and scan limits

consistency: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Mechanism, scan/parameter limits and identity boundaries remain qualified.

Finite strictly positive normalized targets and complete component kernels are required. Component orders must be consistent across rows, but their tie choices need not be reverse-paired because both components are reversible. Mixture weights are a fresh constant half; arbitrary state-dependent choice is outside scope. Positive self mass is possible even below half maximum. Neither local reversibility nor invariance establishes aperiodicity, joint exploration or reversible full scans. No universal efficiency, infinite-state or floating implementation claim is maintained.

### All captured maintained fields

provenance: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Root reassessed the complete current record after canonical capture; DRAFT remains.

Personally reassessed every actual maintained field and all six claims. The specified complete NAM focal/tail updates and stopping rule agree with the retained derivation and fresh Eq19/28-34 reread. UDNAM is a fresh constant half mixture of completed U/D kernels, not a sequential product or current-label-dependent selector. Independent valid tie policies preserve each component balance; downward tie sensitivity and two-positive-diagonal nonrepresentation witness are explicit. Positive self mass and periodic/joint-scan examples prevent unwarranted convergence claims. The Neal-only primary attribution, FHY access gap and related MarkovChain mapping remain accurately scoped. Rereads: neal2024: Post-capture root native-text reread PDF pages [2, 3, 10, 15, 24, 28, 29, 49]; relevant additional primary text and selected visuals remain in separately retained earlier root ledgers. No full84-page reading claimed.

### Source caveats and original calculation history

provenance: supported. Targets: AIMech:UpwardDownwardNestedAntitheticMixture.

Source interpretation, wording clarification and original-to-expanded calculation lineage remain distinct.

The original curator-written tower and mixture checks and their expanded calculations retain exact code, outputs and execution/comparison receipts. Raw download precision is retained beside schema-compatible source timestamps. Named source caveats do not imply a defective maintained record or an author-issued erratum; finite exact checks do not certify floating implementations or general convergence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json; identity_search and identity_assessment | supports | The actual post317 assessment covers all 442 pinned AIO and 710 native IDs, names, aliases and every scoped synonym, plus four complete checkout searches including ignored and hidden files. Historical 706-native source research, 334 selected ID/name rows, 103 selected definitions, 59 additional mixture definitions, 22 exact AIO node/incident/generated contexts and 18 full native neighbors retain their attributed reading scope. The four actual FSS/ZFSS and NAM/ZDNAM records are freshly assessed. AIO:MarkovChain is related_match between a transition construction and a stochastic process; no equivalent or subclass mapping or neural-layer inheritance is asserted. No aliases adopted. UDNAM is a constant equal choice between complete upward and downward NAM kernels, with consistent independently selected valid tie policies. A mixture is not a single supplied-order NAM modification, sequential U-then-D composition or state-dependent component selection. The finite (4,3,2)/9 two-positive-diagonal witness excludes every single NAM ordering. UNAM tie invariance and DNAM tie sensitivity are distinguished. Shared local reversible kernels or special cases with other samplers do not establish identity. |
| mapping | research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json; mapping_context nodes, historical semantic/native contexts, actual317_neighbors and mapping_assessment | supports | The related_match to AIO:MarkovChain is a method-to-process association. The pinned CLASS describes a stochastic process/model, with Network and ProbabilisticHiddenLayer context, rather than this finite conditional transition algorithm. Twenty-two exact class contexts support this association and twenty-one rejected alternatives. No equivalence, subclass membership or inherited neural assertion follows. |
| actual-record-reading | data/curated/UpwardDownwardNestedAntitheticMixture.yaml | supports | Personally reassessed every actual maintained field and all six claims. The specified complete NAM focal/tail updates and stopping rule agree with the retained derivation and fresh Eq19/28-34 reread. UDNAM is a fresh constant half mixture of completed U/D kernels, not a sequential product or current-label-dependent selector. Independent valid tie policies preserve each component balance; downward tie sensitivity and two-positive-diagonal nonrepresentation witness are explicit. Positive self mass and periodic/joint-scan examples prevent unwarranted convergence claims. The Neal-only primary attribution, FHY access gap and related MarkovChain mapping remain accurately scoped. Actual post-capture source reread: neal2024: Post-capture root native-text reread PDF pages [2, 3, 10, 15, 24, 28, 29, 49]; relevant additional primary text and selected visuals remain in separately retained earlier root ledgers. No full84-page reading claimed. |
| neal2024 | https://glizen.com/radfordneal/ftp/gibbs-self.pdf; Section 8, PDF p. 28, explicit UDNAM equal-mixture definition; Section 5, PDF p. 10, Equation 19; Section 6, pp. 14–17, Equations 28–34 and Algorithm 2; Sections 7–8, pp. 22–29, upward/downward orders and Algorithms 3–4; Section 8, PDF p. 28, equal random choice and averaged transition probabilities; Section 2, pp. 2–3, distinction between mixtures and compositions; Sections 5–6, PDF pp. 10 and 14–20, balance-preserving antithetic construction; Section 8, p. 28, mixture; Section 2, pp. 2–3, Equations 1–4 and composition; Section 7, PDF p. 24, Equation 75 and tie invariance; Section 8, pp. 28–29, tie discussion and Figure 6(a); original exact tie comparison in research/discovery/mixture-boundaries.py; Section 6, PDF pp. 14–20, completed NAM diagonal structure; Section 8, pp. 28–30, mixture and ordering limits; Section 13, pp. 49–51, simple-target comparisons; original six-order calculation in research/discovery/mixture-boundaries.py; Section 5, PDF pp. 13–14 and footnotes 7–8, scan boundaries; Section 8, p. 28, scoped efficiency discussion; Section 13, p. 49, uniform-target behavior; original scan checks in research/discovery/mixture-boundaries.py | supports | Author-hosted technical report dated 26 March 2024; 84 PDF pages. Independently pinned from arXiv:2403.18054v1; byte equivalence between versions is not asserted. Actual root reading: Reread the actual finite construction, mixture/order conventions and conditional/uniform-target boundaries against maintained claims. Earlier focal/tail derivations and visual assessments remain attributed; current reading does not expand to empirical or full proof certification. |
| calculation-tower | research/discovery/tower-boundaries.py; Saved report curator_calculations; scope, counts, orientation_example, reversible_nonhalf, arbitrary_shift_shortcut, closed_endpoint, point_mass | supports | Original bounded exact Fraction curator calculations; actual copied-script outputs checked against the full saved result. The mixture imports hash-pinned existing NAM and copied tower siblings without rerunning their main suites. No author-code execution, benchmark replication or universal proof. Selected results: {"scope": "Exact finite original curator calculations. Positive ordered integer vectors of lengths 1..5 with entries 1..3; duplicates after normalization retained. Shift sets include all cumulative-boundary differences, adjacent midpoints and policy/example shifts. Nonnegative extension and endpoint policies are counted separately. No floating implementation, author-code or benchmark execution.", "counts": {"formula_geometry_orientation_comparisons": 16626, "interior_shift_cases": 8313, "maximum_first_2010_cases": 363, "policy_rows_checked": 3279, "positive_weight_vectors": 363, "printed_alg7_integrated_rows": 38487, "printed_alg7_partition_cells": 70962, "reverse_paired_order_cases": 363, "scaling_cases": 8313, "uniform_integration_rows": 38487, "uniform_partition_cells": 70962, "zero_current_rows_left_undefined": 1818, "zero_extension_shift_cases": 2016, "zero_extension_vectors": 336}, "orientation_example": {"half": [["0", "1/2", "1/4", "1/4"], ["2/3", "0", "0", "1/3"], ["1", "0", "0", "0"], ["1/2", "1/2", "0", "0"]], "negative": [["0", "1/4", "1/4", "1/2"], ["1", "0", "0", "0"], ["1", "0", "0", "0"], ["0", "1", "0", "0"]], "pi": ["2/5", "3/10", "1/10", "1/5"], "positive": [["0", "3/4", "1/4", "0"], ["1/3", "0", "0", "2/3"], ["1", "0", "0", "0"], ["1", "0", "0", "0"]], "shift": "2/5"}, "reversible_nonhalf": {"matrix": [["5/6", "1/6"], ["1/4", "3/4"]], "pi": ["3/5", "2/5"], "shift": "1/10"}, "arbitrary_shift_shortcut": {"current_zero_based": 0, "geometry_row": ["5/6", "1/6"], "pi": ["3/5", "2/5"], "printed_alg6": ["1/3", "2/3"], "shift": "1/10"}, "closed_endpoint": {"current_zero_based": 0, "exact_row": ["0", "0", "1"], "half_open_return_zero_based": 2, "pi": ["1/5", "3/10", "1/2"], "printed_return_zero_based": 1, "r": "0", "shift": "1/2", "transition_probability": "0"}, "point_mass": {"interior": [["1"]], "maximum_endpoint_extension": [["1"]]}} |
| calculation-mixture | research/discovery/mixture-boundaries.py; Saved report curator_calculations; scope, dependency_sha256, expanded_counts, half_dominant_point_boundaries | supports | Original bounded exact Fraction curator calculations; actual copied-script outputs checked against the full saved result. The mixture imports hash-pinned existing NAM and copied tower siblings without rerunning their main suites. No author-code execution, benchmark replication or universal proof. Selected results: {"scope": "Exact positive finite conditional kernels. Original source-agent witness output is retained without runtime metadata. Expanded tie, independent-component, all-shift and exploration checks use pinned unchanged sibling routines. No efficiency, float, author-code, all-target nonintersection or general convergence claim.", "dependency_sha256": {"nam-boundaries.py": "cb58dd0a41b32a7c4f12dcfc711963b39ff062b12f79d8fe6bf065b777714941", "tower-boundaries.py": "d8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47"}, "expanded_counts": {"arbitrary_fixed_NAM_mixing_weight_cases": 600, "compatible_NAM_order_cases": 771, "independent_UDNAM_tie_pairs": 3231, "one_state_UDST_endpoint_extensions": 3, "paired_UDST_order_cases": 435, "positive_target_vectors": 120}, "half_dominant_point_boundaries": [{"UDNAM": [["1"]], "UDNAM_self_mass": "1", "UDST": [["1"]], "UDST_self_mass": "1", "minimum_self_mass": "1", "pi": ["1"], "weights": [1]}, {"UDNAM": [["0", "1"], ["1", "0"]], "UDNAM_self_mass": "0", "UDST": [["0", "1"], ["1", "0"]], "UDST_self_mass": "0", "minimum_self_mass": "0", "pi": ["1/2", "1/2"], "weights": [1, 1]}, {"UDNAM": [["3/20", "21/40", "13/40"], ["7/8", "0", "1/8"], ["13/16", "3/16", "0"]], "UDNAM_self_mass": "3/40", "UDST": [["0", "3/5", "2/5"], ["1", "0", "0"], ["1", "0", "0"]], "UDST_self_mass": "0", "minimum_self_mass": "0", "pi": ["1/2", "3/10", "1/5"], "weights": [5, 3, 2]}, {"UDNAM": [["7/18", "17/36", "5/36"], ["17/18", "0", "1/18"], ["5/6", "1/6", "0"]], "UDNAM_self_mass": "7/30", "UDST": [["1/3", "1/2", "1/6"], ["1", "0", "0"], ["1", "0", "0"]], "UDST_self_mass": "1/5", "minimum_self_mass": "1/5", "pi": ["3/5", "3/10", "1/10"], "weights": [6, 3, 1]}, {"UDNAM": [["55/72", "17/144", "17/144"], ["17/18", "0", "1/18"], ["17/18", "1/18", "0"]], "UDNAM_self_mass": "11/18", "UDST": [["3/4", "1/8", "1/8"], ["1", "0", "0"], ["1", "0", "0"]], "UDST_self_mass": "3/5", "minimum_self_mass": "3/5", "pi": ["4/5", "1/10", "1/10"], "weights": [8, 1, 1]}]} |
| source-math-provenance | research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json; source_analysis.handoffs, root_readings and writer_preparation_reading | supports | Root assessed the separately attributed selective source readings and bounded mathematical research. Supporting agents are in the same author workflow and provide no independent scientific approval. |
| source-error-original-lineage | research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json; calculation_lineage.artifacts, curator_calculations and existing calculator dependency; source_analysis source caveats and raw/canonical access precision | supports | Original curator-written tower and mixture scripts, outputs, expanded counterparts and actual execution/comparison receipts preserve reproducible lineage. The unchanged existing NAM dependency is verified separately from the two copied scripts. Suwa/Neal orientation conventions, the printed arbitrary-shift shortcut, closed endpoint and caption/tie qualifications remain distinct from byte provenance and the tower wording clarification. No author-issued erratum or author-software execution is claimed. |

## Limits And Additional Notes

- Author self-review, not independent scientific approval or DRAFT promotion.
- Finite strictly positive normalized targets and complete component kernels are required. Component orders must be consistent across rows, but their tie choices need not be reverse-paired because both components are reversible. Mixture weights are a fresh constant half; arbitrary state-dependent choice is outside scope. Positive self mass is possible even below half maximum. Neither local reversibility nor invariance establishes aperiodicity, joint exploration or reversible full scans. No universal efficiency, infinite-state or floating implementation claim is maintained.
- The Fraction calculators are original curator-written bounded checks, not author software, empirical replication or universal proofs. Repeated normalized targets and policy/order choices are counted explicitly.
- Source, identity and mathematical agents belong to the same author workflow. This is qualified author self-review, not independent scientific approval.
- Historical 706-native research is attributed separately. Actual prewrite 710-native identity refresh, all scoped synonyms, four complete ignored-inclusive searches and actual FSS/ZFSS/NAM/ZDNAM neighbor assessments govern the addition.
- Two copied calculators retain their exact original-to-expanded provenance. The mixture calculator uses the unchanged, hash-pinned existing NAM sibling and copied tower sibling; this does not rerun the entire earlier NAM suite.
- Raw source download precision and whole-second UTC source timestamps are both preserved; download times are not scientific reading times.
- Empty findings reflect actual root assessment of this selected captured record only; no unrelated finding closure or literature saturation is asserted.
- Source caveats and preserved calculation or wording lineage remain distinct; no maintained-record finding or issue closure is invented from them.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T231908Z-upward-downward-nested-antithetic-mixture
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Upward-downward nested antithetic mixture
started_at: '2026-10-14T23:06:17.157100Z'
finished_at: '2026-10-14T23:19:08.747828Z'
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
summary: The explicit complete-component half mixture is supported as a distinct DRAFT
  algorithm. Independent valid tie policies, possible positive self mass and joint-scan
  limitations remain explicit.
source:
  git_revision: f80a7e2e48616126ad74f0e53aac6eadac9e9034
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
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/FactorizedLLM.yaml
    sha256: f73a5e4d591e4d832f94bfa044d77c5645f585b042f07485f99920527d67b6d5
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
  - path: data/aio/MixtureofExpertsLLM.yaml
    sha256: d9c3edb18f624102f141d1daf27aa0cc055eaf9199faf30abf88d2b87fbc1520
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
  - path: data/aio/RandomForest.yaml
    sha256: cfdce4625131a8da239adf1b3957fadbc5433ddc8fc4ac8a3be5fe9018ce66ab
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
  - path: data/curated/CircularWeightShiftSampler.yaml
    sha256: a2ee967fb51b3b61ddc17f4259d3f79bbe94db4f04df27c55f671684a8d96536
    role: context
  - path: data/curated/ConjugateGradientMonteCarlo.yaml
    sha256: 59c29605048365b38ef298fdd3401bf00a8beb522fc9d4b3c8fe868d6946fa4f
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
  - path: data/curated/IndependenceMetropolisHastings.yaml
    sha256: ca1390f00edca43e94f897e2398b3f7d8edddefadc0a5780e0b470816a7754df
    role: context
  - path: data/curated/LiuModifiedGibbsSampler.yaml
    sha256: b3736d9f8dfb1e8b7e218d2b8fc075f413a719dc1c11cee951af8fa3b4542e54
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
  - path: data/curated/MultipleTryMetropolis.yaml
    sha256: f1d607b598a1baf993a7b4de78e82953fd86a9bb9d367e02553aeda4fe2e354b
    role: context
  - path: data/curated/MultipleTryMetropolisWithinGibbs.yaml
    sha256: 539c4d93eff27f5e064abb16fe3e892406ad5dc3d3a6bceb314f4eee37b2a727
    role: context
  - path: data/curated/NealBacktrackingSuppressedMCMC.yaml
    sha256: 1da524622ec40d25aac45313cdbd6412adf1376c6c8b78eeecaded8eb561a0be
    role: context
  - path: data/curated/NestedAntitheticModification.yaml
    sha256: 129f349463f45710166082b7db00a4caa389c65cf93700b82acbf81334a4a17e
    role: context
  - path: data/curated/NonreversibleMetropolisUniformUpdate.yaml
    sha256: 27dbec2b01a48103d709df4b9ab94bba36083bd27acb69af1e3bc70ab6ab4ecd
    role: context
  - path: data/curated/RejectionSampling.yaml
    sha256: 69e7583098c6dd6cae145d01e3f95ac95424fe1f61436c9ded1b160e58e92d05
    role: context
  - path: data/curated/SliceSampling.yaml
    sha256: a87319788a5d2966dd1484b6672a968642fb5514cc6f81184908576304bf6aaa
    role: context
  - path: data/curated/SteppingOutSliceSampling.yaml
    sha256: 8d2d0155c2e1d462b093935f19f4fe11fefb61e19e3ed93336e30b7257dda4c8
    role: context
  - path: data/curated/UpwardDownwardNestedAntitheticMixture.yaml
    sha256: c7754a4aa39a4f1ce5703c13f225693604ab9cc760af3f45236b64137fc6e9e2
    role: target
  - path: data/curated/UpwardDownwardShiftedTowerMixture.yaml
    sha256: edf53fd84732416ca0ea18919f055eee78aa7902b488ae6898141ce30a484ade
    role: context
  - path: data/curated/ZeroSelfDownwardNestedAntitheticModification.yaml
    sha256: eeda6efb3d9466c8e1ddf592379b303b700462f85a96234e9881a0e2c209cd0b
    role: context
  - path: data/curated/ZeroSelfFlattenedSliceSampling.yaml
    sha256: 7ae035e9d9e4ad3c8a34d705e976ce07abeda8f6c8449d112fbf3e535d496b45
    role: context
  - path: research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json
    sha256: 67c0606e4e22d9ca2d473842632207842effb729628e0a61402e1f9e1f49818b
    role: context
  - path: research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.md
    sha256: fdb94a95a30f76ab24df23f1e17fc654c244551da81bcec3165b4cec917ce25f
    role: context
  - path: research/discovery/mixture-boundaries.py
    sha256: 08aabec98558e43e20983518eb4b28c6ec6f383ad26e980a8e577612638e8125
    role: context
  - path: research/discovery/nam-boundaries.py
    sha256: cb58dd0a41b32a7c4f12dcfc711963b39ff062b12f79d8fe6bf065b777714941
    role: context
  - path: research/discovery/tower-boundaries.py
    sha256: d8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47
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
- target_id: AIMech:UpwardDownwardNestedAntitheticMixture
  path: data/curated/UpwardDownwardNestedAntitheticMixture.yaml
  label: Upward-downward nested antithetic mixture
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/UpwardDownwardNestedAntitheticMixture.yaml
    role: maintained
scope:
  description: 'All maintained fields of the selected record. Actual source scope:
    neal2024: Post-capture root native-text reread PDF pages [2, 3, 10, 15, 24, 28,
    29, 49]; relevant additional primary text and selected visuals remain in separately
    retained earlier root ledgers. No full84-page reading claimed.. Reread the actual
    finite construction, mixture/order conventions and conditional/uniform-target
    boundaries against maintained claims. Earlier focal/tail derivations and visual
    assessments remain attributed; current reading does not expand to empirical or
    full proof certification.'
  selection: 'Exact maintained ID: AIMech:UpwardDownwardNestedAntitheticMixture'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exclusions:
  - target: Other batch entries and neighboring identities
    reason: Read as identity/mapping context, not formal review targets.
  - target: Uninspected source versions, general convergence and runtime claims
    reason: Finite strictly positive normalized targets and complete component kernels
      are required. Component orders must be consistent across rows, but their tie
      choices need not be reverse-paired because both components are reversible. Mixture
      weights are a fresh constant half; arbitrary state-dependent choice is outside
      scope. Positive self mass is possible even below half maximum. Neither local
      reversibility nor invariance establishes aperiodicity, joint exploration or
      reversible full scans. No universal efficiency, infinite-state or floating implementation
      claim is maintained.
  - target: Author implementation and benchmark replication
    reason: Only bounded original calculations and project checks were executed.
checks:
- check_id: gate-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 361.24s (0:06:01)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 713 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 398 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 404,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
  scope_note: Actual execution completed 2026-10-14T23:17:40.430488Z; this generator
    executes no recorded commands.
- check_id: vendor-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
  scope_note: Actual execution completed 2026-10-14T23:06:57.762985Z; this generator
    executes no recorded commands.
- check_id: render-2
  name: just render
  command: just render
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: 'Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages

    uv run --locked python scripts/render_pages.py

    '
  scope_note: Actual execution completed 2026-10-14T23:07:48.474356Z; this generator
    executes no recorded commands.
- check_id: render-3
  name: just render-check
  command: just render-check
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: 'pages/ is current

    uv run --locked python scripts/render_pages.py --check

    '
  scope_note: Actual execution completed 2026-10-14T23:08:07.255889Z; this generator
    executes no recorded commands.
- check_id: additional-4
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
  scope_note: Actual execution completed 2026-10-14T23:07:17.975018Z; this generator
    executes no recorded commands.
- check_id: additional-5
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited zero without output.
  scope_note: Actual execution completed 2026-10-14T23:07:18.089986Z; this generator
    executes no recorded commands.
- check_id: calculation-6
  name: python3 research/discovery/tower-boundaries.py
  command: python3 research/discovery/tower-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"arbitrary_shift_shortcut\": {\n    \"current_zero_based\": 0,\n\
    \    \"geometry_row\": [\n      \"5/6\",\n      \"1/6\"\n    ],\n    \"pi\": [\n\
    \      \"3/5\",\n      \"2/5\"\n    ],\n    \"printed_alg6\": [\n      \"1/3\"\
    ,\n      \"2/3\"\n    ],\n    \"shift\": \"1/10\"\n  },\n  \"closed_endpoint\"\
    : {\n    \"current_zero_based\": 0,\n    \"exact_row\": [\n      \"0\",\n    \
    \  \"0\",\n      \"1\"\n    ],\n    \"half_open_return_zero_based\": 2,\n    \"\
    pi\": [\n      \"1/5\",\n      \"3/10\",\n      \"1/2\"\n    ],\n    \"printed_return_zero_based\"\
    : 1,\n    \"r\": \"0\",\n    \"shift\": \"1/2\",\n    \"transition_probability\"\
    : \"0\"\n  },\n  \"counts\": {\n    \"formula_geometry_orientation_comparisons\"\
    : 16626,\n    \"interior_shift_cases\": 8313,\n    \"maximum_first_2010_cases\"\
    : 363,\n    \"policy_rows_checked\": 3279,\n    \"positive_weight_vectors\": 363,\n\
    \    \"printed_alg7_integrated_rows\": 38487,\n    \"printed_alg7_partition_cells\"\
    : 70962,\n    \"reverse_paired_order_cases\": 363,\n    \"scaling_cases\": 8313,\n\
    \    \"uniform_integration_rows\": 38487,\n    \"uniform_partition_cells\": 70962,\n\
    \    \"zero_current_rows_left_undefined\": 1818,\n    \"zero_extension_shift_cases\"\
    : 2016,\n    \"zero_extension_vectors\": 336\n  },\n  \"current_dependent_order_counterexample\"\
    : {\n    \"after\": [\n      \"2/3\",\n      \"1/3\",\n      \"0\"\n    ],\n \
    \   \"matrix\": [\n      [\n        \"0\",\n        \"1\",\n        \"0\"\n  \
    \    ],\n      [\n        \"1\",\n        \"0\",\n        \"0\"\n      ],\n  \
    \    [\n        \"1\",\n        \"0\",\n        \"0\"\n      ]\n    ],\n    \"\
    orders_zero_based\": [\n      [\n        0,\n        1,\n        2\n      ],\n\
    \      [\n        1,\n        0,\n        2\n      ],\n      [\n        2,\n \
    \       0,\n        1\n      ]\n    ],\n    \"pi\": [\n      \"1/3\",\n      \"\
    1/3\",\n      \"1/3\"\n    ]\n  },\n  \"orientation_example\": {\n    \"half\"\
    : [\n      [\n        \"0\",\n        \"1/2\",\n        \"1/4\",\n        \"1/4\"\
    \n      ],\n      [\n        \"2/3\",\n        \"0\",\n        \"0\",\n      \
    \  \"1/3\"\n      ],\n      [\n        \"1\",\n        \"0\",\n        \"0\",\n\
    \        \"0\"\n      ],\n      [\n        \"1/2\",\n        \"1/2\",\n      \
    \  \"0\",\n        \"0\"\n      ]\n    ],\n    \"negative\": [\n      [\n    \
    \    \"0\",\n        \"1/4\",\n        \"1/4\",\n        \"1/2\"\n      ],\n \
    \     [\n        \"1\",\n        \"0\",\n        \"0\",\n        \"0\"\n     \
    \ ],\n      [\n        \"1\",\n        \"0\",\n        \"0\",\n        \"0\"\n\
    \      ],\n      [\n        \"0\",\n        \"1\",\n        \"0\",\n        \"\
    0\"\n      ]\n    ],\n    \"pi\": [\n      \"2/5\",\n      \"3/10\",\n      \"\
    1/10\",\n      \"1/5\"\n    ],\n    \"positive\": [\n      [\n        \"0\",\n\
    \        \"3/4\",\n        \"1/4\",\n        \"0\"\n      ],\n      [\n      \
    \  \"1/3\",\n        \"0\",\n        \"0\",\n        \"2/3\"\n      ],\n     \
    \ [\n        \"1\",\n        \"0\",\n        \"0\",\n        \"0\"\n      ],\n\
    \      [\n        \"1\",\n        \"0\",\n        \"0\",\n        \"0\"\n    \
    \  ]\n    ],\n    \"shift\": \"2/5\"\n  },\n  \"periodicity\": [\n    {\n    \
    \  \"half_classes\": [\n        {\n          \"closed\": true,\n          \"period\"\
    : 1,\n          \"states_zero_based\": [\n            0\n          ]\n       \
    \ }\n      ],\n      \"half_shift\": [\n        [\n          \"1\"\n        ]\n\
    \      ],\n      \"maximum_classes\": [\n        {\n          \"closed\": true,\n\
    \          \"period\": 1,\n          \"states_zero_based\": [\n            0\n\
    \          ]\n        }\n      ],\n      \"maximum_shift\": [\n        [\n   \
    \       \"1\"\n        ]\n      ],\n      \"states\": 1\n    },\n    {\n     \
    \ \"half_classes\": [\n        {\n          \"closed\": true,\n          \"period\"\
    : 2,\n          \"states_zero_based\": [\n            0,\n            1\n    \
    \      ]\n        }\n      ],\n      \"half_shift\": [\n        [\n          \"\
    0\",\n          \"1\"\n        ],\n        [\n          \"1\",\n          \"0\"\
    \n        ]\n      ],\n      \"maximum_classes\": [\n        {\n          \"closed\"\
    : true,\n          \"period\": 2,\n          \"states_zero_based\": [\n      \
    \      0,\n            1\n          ]\n        }\n      ],\n      \"maximum_shift\"\
    : [\n        [\n          \"0\",\n          \"1\"\n        ],\n        [\n   \
    \       \"1\",\n          \"0\"\n        ]\n      ],\n      \"states\": 2\n  \
    \  },\n    {\n      \"half_classes\": [\n        {\n          \"closed\": true,\n\
    \          \"period\": 1,\n          \"states_zero_based\": [\n            0,\n\
    \            1,\n            2\n          ]\n        }\n      ],\n      \"half_shift\"\
    : [\n        [\n          \"0\",\n          \"1/2\",\n          \"1/2\"\n    \
    \    ],\n        [\n          \"1/2\",\n          \"0\",\n          \"1/2\"\n\
    \        ],\n        [\n          \"1/2\",\n          \"1/2\",\n          \"0\"\
    \n        ]\n      ],\n      \"maximum_classes\": [\n        {\n          \"closed\"\
    : true,\n          \"period\": 3,\n          \"states_zero_based\": [\n      \
    \      0,\n            1,\n            2\n          ]\n        }\n      ],\n \
    \     \"maximum_shift\": [\n        [\n          \"0\",\n          \"1\",\n  \
    \        \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n  \
    \        \"1\"\n        ],\n        [\n          \"1\",\n          \"0\",\n  \
    \        \"0\"\n        ]\n      ],\n      \"states\": 3\n    },\n    {\n    \
    \  \"half_classes\": [\n        {\n          \"closed\": true,\n          \"period\"\
    : 2,\n          \"states_zero_based\": [\n            0,\n            2\n    \
    \      ]\n        },\n        {\n          \"closed\": true,\n          \"period\"\
    : 2,\n          \"states_zero_based\": [\n            1,\n            3\n    \
    \      ]\n        }\n      ],\n      \"half_shift\": [\n        [\n          \"\
    0\",\n          \"0\",\n          \"1\",\n          \"0\"\n        ],\n      \
    \  [\n          \"0\",\n          \"0\",\n          \"0\",\n          \"1\"\n\
    \        ],\n        [\n          \"1\",\n          \"0\",\n          \"0\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"1\",\n\
    \          \"0\",\n          \"0\"\n        ]\n      ],\n      \"maximum_classes\"\
    : [\n        {\n          \"closed\": true,\n          \"period\": 4,\n      \
    \    \"states_zero_based\": [\n            0,\n            1,\n            2,\n\
    \            3\n          ]\n        }\n      ],\n      \"maximum_shift\": [\n\
    \        [\n          \"0\",\n          \"1\",\n          \"0\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"1\"\
    ,\n          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"1\"\n        ],\n        [\n          \"1\",\n\
    \          \"0\",\n          \"0\",\n          \"0\"\n        ]\n      ],\n  \
    \    \"states\": 4\n    },\n    {\n      \"half_classes\": [\n        {\n    \
    \      \"closed\": true,\n          \"period\": 1,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2,\n            3,\n        \
    \    4\n          ]\n        }\n      ],\n      \"half_shift\": [\n        [\n\
    \          \"0\",\n          \"0\",\n          \"1/2\",\n          \"1/2\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"1/2\",\n          \"1/2\"\n        ],\n       \
    \ [\n          \"1/2\",\n          \"0\",\n          \"0\",\n          \"0\",\n\
    \          \"1/2\"\n        ],\n        [\n          \"1/2\",\n          \"1/2\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"1/2\",\n          \"1/2\",\n          \"0\",\n\
    \          \"0\"\n        ]\n      ],\n      \"maximum_classes\": [\n        {\n\
    \          \"closed\": true,\n          \"period\": 5,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2,\n            3,\n        \
    \    4\n          ]\n        }\n      ],\n      \"maximum_shift\": [\n       \
    \ [\n          \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"1\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"1\",\n    \
    \      \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n    \
    \      \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\"\n        ]\n      ],\n      \"states\": 5\n    },\n    {\n      \"half_classes\"\
    : [\n        {\n          \"closed\": true,\n          \"period\": 2,\n      \
    \    \"states_zero_based\": [\n            0,\n            3\n          ]\n  \
    \      },\n        {\n          \"closed\": true,\n          \"period\": 2,\n\
    \          \"states_zero_based\": [\n            1,\n            4\n         \
    \ ]\n        },\n        {\n          \"closed\": true,\n          \"period\"\
    : 2,\n          \"states_zero_based\": [\n            2,\n            5\n    \
    \      ]\n        }\n      ],\n      \"half_shift\": [\n        [\n          \"\
    0\",\n          \"0\",\n          \"0\",\n          \"1\",\n          \"0\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"1\",\n          \"0\"\n     \
    \   ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n    \
    \      \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n        \
    \  \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"1\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\"\n        ]\n      ],\n\
    \      \"maximum_classes\": [\n        {\n          \"closed\": true,\n      \
    \    \"period\": 6,\n          \"states_zero_based\": [\n            0,\n    \
    \        1,\n            2,\n            3,\n            4,\n            5\n \
    \         ]\n        }\n      ],\n      \"maximum_shift\": [\n        [\n    \
    \      \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n        \
    \  \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"0\"\
    ,\n          \"1\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"1\",\n          \"0\"\n        ],\n        [\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"1\"\n        ],\n        [\n          \"1\",\n          \"0\",\n        \
    \  \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ]\n  \
    \    ],\n      \"states\": 6\n    },\n    {\n      \"half_classes\": [\n     \
    \   {\n          \"closed\": true,\n          \"period\": 1,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2,\n            3,\n        \
    \    4,\n            5,\n            6\n          ]\n        }\n      ],\n   \
    \   \"half_shift\": [\n        [\n          \"0\",\n          \"0\",\n       \
    \   \"0\",\n          \"1/2\",\n          \"1/2\",\n          \"0\",\n       \
    \   \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n       \
    \   \"0\",\n          \"0\",\n          \"1/2\",\n          \"1/2\",\n       \
    \   \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n       \
    \   \"0\",\n          \"0\",\n          \"0\",\n          \"1/2\",\n         \
    \ \"1/2\"\n        ],\n        [\n          \"1/2\",\n          \"0\",\n     \
    \     \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n         \
    \ \"1/2\"\n        ],\n        [\n          \"1/2\",\n          \"1/2\",\n   \
    \       \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n       \
    \   \"0\"\n        ],\n        [\n          \"0\",\n          \"1/2\",\n     \
    \     \"1/2\",\n          \"0\",\n          \"0\",\n          \"0\",\n       \
    \   \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n       \
    \   \"1/2\",\n          \"1/2\",\n          \"0\",\n          \"0\",\n       \
    \   \"0\"\n        ]\n      ],\n      \"maximum_classes\": [\n        {\n    \
    \      \"closed\": true,\n          \"period\": 7,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2,\n            3,\n        \
    \    4,\n            5,\n            6\n          ]\n        }\n      ],\n   \
    \   \"maximum_shift\": [\n        [\n          \"0\",\n          \"1\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n        \
    \  \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"0\"\
    ,\n          \"1\",\n          \"0\",\n          \"0\",\n          \"0\"\n   \
    \     ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"1\",\n          \"0\",\n          \"0\"\n       \
    \ ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"1\",\n          \"0\"\n        ],\n\
    \        [\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\",\n          \"0\",\n          \"0\",\n          \"1\"\n        ],\n      \
    \  [\n          \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"0\"\n        ]\n      ],\n  \
    \    \"states\": 7\n    },\n    {\n      \"half_classes\": [\n        {\n    \
    \      \"closed\": true,\n          \"period\": 2,\n          \"states_zero_based\"\
    : [\n            0,\n            4\n          ]\n        },\n        {\n     \
    \     \"closed\": true,\n          \"period\": 2,\n          \"states_zero_based\"\
    : [\n            1,\n            5\n          ]\n        },\n        {\n     \
    \     \"closed\": true,\n          \"period\": 2,\n          \"states_zero_based\"\
    : [\n            2,\n            6\n          ]\n        },\n        {\n     \
    \     \"closed\": true,\n          \"period\": 2,\n          \"states_zero_based\"\
    : [\n            3,\n            7\n          ]\n        }\n      ],\n      \"\
    half_shift\": [\n        [\n          \"0\",\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"0\",\n          \"1\",\n      \
    \    \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\",\n          \"1\",\n          \"0\"\n        ],\n        [\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n  \
    \        \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n\
    \        [\n          \"0\",\n          \"1\",\n          \"0\",\n          \"\
    0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n\
    \        ],\n        [\n          \"0\",\n          \"0\",\n          \"1\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\",\n          \"0\"\n        ]\n      ],\n      \"maximum_classes\": [\n\
    \        {\n          \"closed\": true,\n          \"period\": 8,\n          \"\
    states_zero_based\": [\n            0,\n            1,\n            2,\n     \
    \       3,\n            4,\n            5,\n            6,\n            7\n  \
    \        ]\n        }\n      ],\n      \"maximum_shift\": [\n        [\n     \
    \     \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n         \
    \ \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n  \
    \      [\n          \"0\",\n          \"0\",\n          \"1\",\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n   \
    \     ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"1\",\n          \"0\",\n          \"\
    0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\",\n          \"1\",\n  \
    \        \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"1\",\n          \"0\"\n        ],\n        [\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\",\n          \"0\",\n          \"0\",\n          \"1\"\n        ],\n      \
    \  [\n          \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n     \
    \   ]\n      ],\n      \"states\": 8\n    },\n    {\n      \"half_classes\": [\n\
    \        {\n          \"closed\": true,\n          \"period\": 1,\n          \"\
    states_zero_based\": [\n            0,\n            1,\n            2,\n     \
    \       3,\n            4,\n            5,\n            6,\n            7,\n \
    \           8\n          ]\n        }\n      ],\n      \"half_shift\": [\n   \
    \     [\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\
    ,\n          \"1/2\",\n          \"1/2\",\n          \"0\",\n          \"0\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"1/2\",\n  \
    \        \"1/2\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"1/2\",\n          \"1/2\",\n    \
    \      \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\",\n          \"1/2\",\n          \"1/2\"\n        ],\n        [\n    \
    \      \"1/2\",\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    1/2\"\n        ],\n        [\n          \"1/2\",\n          \"1/2\",\n       \
    \   \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n          \"0\"\
    ,\n          \"1/2\",\n          \"1/2\",\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n     \
    \   ],\n        [\n          \"0\",\n          \"0\",\n          \"1/2\",\n  \
    \        \"1/2\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"1/2\",\n          \"1/2\",\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ]\n\
    \      ],\n      \"maximum_classes\": [\n        {\n          \"closed\": true,\n\
    \          \"period\": 9,\n          \"states_zero_based\": [\n            0,\n\
    \            1,\n            2,\n            3,\n            4,\n            5,\n\
    \            6,\n            7,\n            8\n          ]\n        }\n     \
    \ ],\n      \"maximum_shift\": [\n        [\n          \"0\",\n          \"1\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n  \
    \        \"0\",\n          \"0\",\n          \"1\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"0\"\
    ,\n          \"1\",\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"0\",\n          \"1\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n\
    \        [\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    0\",\n          \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n\
    \          \"0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n    \
    \      \"1\",\n          \"0\",\n          \"0\"\n        ],\n        [\n    \
    \      \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n        \
    \  \"0\",\n          \"0\",\n          \"0\",\n          \"1\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"1\"\n        ],\n        [\n          \"1\",\n  \
    \        \"0\",\n          \"0\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ]\n\
    \      ],\n      \"states\": 9\n    }\n  ],\n  \"point_mass\": {\n    \"interior\"\
    : [\n      [\n        \"1\"\n      ]\n    ],\n    \"maximum_endpoint_extension\"\
    : [\n      [\n        \"1\"\n      ]\n    ]\n  },\n  \"qualifications\": [\n \
    \   \"The printed-source negative controls are retained; no source erratum or\
    \ universal defect in either orientation is inferred.\",\n    \"Only exactly reverse-paired\
    \ UST/DST orders, including tied labels, justify transpose/equal-mixture checks.\"\
    ,\n    \"Zero current rows and maximum-shift point-mass endpoints are outside\
    \ the maintained positive/interior specification.\",\n    \"The direct lower bound\
    \ follows because total incoming flow from other states is at most W-w_max; finite\
    \ checks do not establish efficiency or convergence.\"\n  ],\n  \"reversible_local_nonreversible_composition\"\
    : {\n    \"equal_mixture\": [\n      [\n        \"0\",\n        \"1/2\",\n   \
    \     \"1/2\",\n        \"0\"\n      ],\n      [\n        \"1/4\",\n        \"\
    1/4\",\n        \"0\",\n        \"1/2\"\n      ],\n      [\n        \"1/6\",\n\
    \        \"0\",\n        \"1/3\",\n        \"1/2\"\n      ],\n      [\n      \
    \  \"0\",\n        \"1/4\",\n        \"3/8\",\n        \"3/8\"\n      ]\n    ],\n\
    \    \"local_updates\": [\n      [\n        [\n          \"0\",\n          \"\
    0\",\n          \"1\",\n          \"0\"\n        ],\n        [\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n\
    \          \"1/3\",\n          \"0\",\n          \"2/3\",\n          \"0\"\n \
    \       ],\n        [\n          \"0\",\n          \"1/2\",\n          \"0\",\n\
    \          \"1/2\"\n        ]\n      ],\n      [\n        [\n          \"0\",\n\
    \          \"1\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"1/2\",\n          \"1/2\",\n          \"0\",\n          \"0\"\n \
    \       ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n\
    \          \"1\"\n        ],\n        [\n          \"0\",\n          \"0\",\n\
    \          \"3/4\",\n          \"1/4\"\n        ]\n      ]\n    ],\n    \"ordered_composition\"\
    : [\n      [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\n\
    \      ],\n      [\n        \"0\",\n        \"0\",\n        \"3/4\",\n       \
    \ \"1/4\"\n      ],\n      [\n        \"0\",\n        \"1/3\",\n        \"0\"\
    ,\n        \"2/3\"\n      ],\n      [\n        \"1/4\",\n        \"1/4\",\n  \
    \      \"3/8\",\n        \"1/8\"\n      ]\n    ],\n    \"states\": [\n      [\n\
    \        0,\n        0\n      ],\n      [\n        0,\n        1\n      ],\n \
    \     [\n        1,\n        0\n      ],\n      [\n        1,\n        1\n   \
    \   ]\n    ],\n    \"target\": [\n      \"1/10\",\n      \"1/5\",\n      \"3/10\"\
    ,\n      \"2/5\"\n    ]\n  },\n  \"reversible_nonhalf\": {\n    \"matrix\": [\n\
    \      [\n        \"5/6\",\n        \"1/6\"\n      ],\n      [\n        \"1/4\"\
    ,\n        \"3/4\"\n      ]\n    ],\n    \"pi\": [\n      \"3/5\",\n      \"2/5\"\
    \n    ],\n    \"shift\": \"1/10\"\n  },\n  \"scope\": \"Exact finite original\
    \ curator calculations. Positive ordered integer vectors of lengths 1..5 with\
    \ entries 1..3; duplicates after normalization retained. Shift sets include all\
    \ cumulative-boundary differences, adjacent midpoints and policy/example shifts.\
    \ Nonnegative extension and endpoint policies are counted separately. No floating\
    \ implementation, author-code or benchmark execution.\",\n  \"systematic_scan_counterexample\"\
    : {\n    \"classes\": [\n      {\n        \"closed\": true,\n        \"period\"\
    : 3,\n        \"states_zero_based\": [\n          0,\n          4,\n         \
    \ 8\n        ]\n      },\n      {\n        \"closed\": true,\n        \"period\"\
    : 3,\n        \"states_zero_based\": [\n          1,\n          5,\n         \
    \ 6\n        ]\n      },\n      {\n        \"closed\": true,\n        \"period\"\
    : 3,\n        \"states_zero_based\": [\n          2,\n          3,\n         \
    \ 7\n        ]\n      }\n    ],\n    \"matrix\": [\n      [\n        \"0\",\n\
    \        \"0\",\n        \"0\",\n        \"0\",\n        \"1\",\n        \"0\"\
    ,\n        \"0\",\n        \"0\",\n        \"0\"\n      ],\n      [\n        \"\
    0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n       \
    \ \"1\",\n        \"0\",\n        \"0\",\n        \"0\"\n      ],\n      [\n \
    \       \"0\",\n        \"0\",\n        \"0\",\n        \"1\",\n        \"0\"\
    ,\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\"\n      ],\n \
    \     [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n    \
    \    \"0\",\n        \"0\",\n        \"0\",\n        \"1\",\n        \"0\"\n \
    \     ],\n      [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"\
    0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n       \
    \ \"1\"\n      ],\n      [\n        \"0\",\n        \"0\",\n        \"0\",\n \
    \       \"0\",\n        \"0\",\n        \"0\",\n        \"1\",\n        \"0\"\
    ,\n        \"0\"\n      ],\n      [\n        \"0\",\n        \"1\",\n        \"\
    0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n       \
    \ \"0\",\n        \"0\"\n      ],\n      [\n        \"0\",\n        \"0\",\n \
    \       \"1\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\"\
    ,\n        \"0\",\n        \"0\"\n      ],\n      [\n        \"1\",\n        \"\
    0\",\n        \"0\",\n        \"0\",\n        \"0\",\n        \"0\",\n       \
    \ \"0\",\n        \"0\",\n        \"0\"\n      ]\n    ],\n    \"states\": [\n\
    \      [\n        0,\n        0\n      ],\n      [\n        0,\n        1\n  \
    \    ],\n      [\n        0,\n        2\n      ],\n      [\n        1,\n     \
    \   0\n      ],\n      [\n        1,\n        1\n      ],\n      [\n        1,\n\
    \        2\n      ],\n      [\n        2,\n        0\n      ],\n      [\n    \
    \    2,\n        1\n      ],\n      [\n        2,\n        2\n      ]\n    ],\n\
    \    \"target\": [\n      \"1/9\",\n      \"1/9\",\n      \"1/9\",\n      \"1/9\"\
    ,\n      \"1/9\",\n      \"1/9\",\n      \"1/9\",\n      \"1/9\",\n      \"1/9\"\
    \n    ]\n  },\n  \"zero_row_nonuniqueness\": {\n    \"completions\": [\n     \
    \ [\n        [\n          \"1\",\n          \"0\",\n          \"0\"\n        ],\n\
    \        [\n          \"0\",\n          \"0\",\n          \"1\"\n        ],\n\
    \        [\n          \"0\",\n          \"1/2\",\n          \"1/2\"\n        ]\n\
    \      ],\n      [\n        [\n          \"0\",\n          \"1\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"1\"\
    \n        ],\n        [\n          \"0\",\n          \"1/2\",\n          \"1/2\"\
    \n        ]\n      ]\n    ],\n    \"partial_rows\": [\n      null,\n      [\n\
    \        \"0\",\n        \"0\",\n        \"1\"\n      ],\n      [\n        \"\
    0\",\n        \"1/2\",\n        \"1/2\"\n      ]\n    ],\n    \"weights\": [\n\
    \      \"0\",\n      \"1\",\n      \"2\"\n    ]\n  }\n}\n"
  scope_note: Actual execution completed 2026-10-14T23:08:31.383775Z; this generator
    executes no recorded commands.
- check_id: calculation-7
  name: python3 research/discovery/mixture-boundaries.py
  command: python3 research/discovery/mixture-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"UDNAM_scope\": {\n    \"HST\": [\n      [\n        \"0\",\n   \
    \     \"5/8\",\n        \"3/8\"\n      ],\n      [\n        \"5/6\",\n       \
    \ \"0\",\n        \"1/6\"\n      ],\n      [\n        \"3/4\",\n        \"1/4\"\
    ,\n        \"0\"\n      ]\n    ],\n    \"Liu_modified_Gibbs\": [\n      [\n  \
    \      \"3/14\",\n        \"1/2\",\n        \"2/7\"\n      ],\n      [\n     \
    \   \"2/3\",\n        \"1/21\",\n        \"2/7\"\n      ],\n      [\n        \"\
    4/7\",\n        \"3/7\",\n        \"0\"\n      ]\n    ],\n    \"ST\": [\n    \
    \  [\n        \"0\",\n        \"3/4\",\n        \"1/4\"\n      ],\n      [\n \
    \       \"2/3\",\n        \"0\",\n        \"1/3\"\n      ],\n      [\n       \
    \ \"1\",\n        \"0\",\n        \"0\"\n      ]\n    ],\n    \"U_then_D\": [\n\
    \      [\n        \"23/35\",\n        \"1/5\",\n        \"1/7\"\n      ],\n  \
    \    [\n        \"8/35\",\n        \"17/35\",\n        \"2/7\"\n      ],\n   \
    \   [\n        \"12/35\",\n        \"13/35\",\n        \"2/7\"\n      ]\n    ],\n\
    \    \"U_then_D_reversible\": false,\n    \"ZDNAM\": [\n      [\n        \"0\"\
    ,\n        \"5/8\",\n        \"3/8\"\n      ],\n      [\n        \"5/6\",\n  \
    \      \"0\",\n        \"1/6\"\n      ],\n      [\n        \"3/4\",\n        \"\
    1/4\",\n        \"0\"\n      ]\n    ],\n    \"all_six_orders_all_shift_exclusion\"\
    : [\n      {\n        \"left\": \"0\",\n        \"order\": [\n          0,\n \
    \         1,\n          2\n        ],\n        \"right\": \"2/9\",\n        \"\
    solution\": {\n          \"candidate_fraction\": \"51/28\",\n          \"conflict_entry\"\
    : [\n            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"159/140\",\n          \"matches\": false\n        }\n      },\n      {\n \
    \       \"left\": \"2/9\",\n        \"order\": [\n          0,\n          1,\n\
    \          2\n        ],\n        \"right\": \"1/3\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"23/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"19/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"1/3\",\n        \"order\": [\n          0,\n          1,\n \
    \         2\n        ],\n        \"right\": \"4/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"3/4\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"4/9\",\n        \"order\": [\n          0,\n          1,\n \
    \         2\n        ],\n        \"right\": \"5/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            0\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"5/56\"\n        }\n      },\n      {\n      \
    \  \"left\": \"5/9\",\n        \"order\": [\n          0,\n          1,\n    \
    \      2\n        ],\n        \"right\": \"2/3\",\n        \"solution\": {\n \
    \         \"candidate_fraction\": \"5/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-19/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"2/3\",\n        \"order\": [\n          0,\n          1,\n\
    \          2\n        ],\n        \"right\": \"7/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-89/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"7/9\",\n        \"order\": [\n          0,\n          1,\n\
    \          2\n        ],\n        \"right\": \"1\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"0\",\n        \"order\": [\n          0,\n          2,\n   \
    \       1\n        ],\n        \"right\": \"2/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"2/9\",\n        \"order\": [\n          0,\n          2,\n \
    \         1\n        ],\n        \"right\": \"1/3\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"23/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"159/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"1/3\",\n        \"order\": [\n          0,\n          2,\n\
    \          1\n        ],\n        \"right\": \"4/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"89/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"4/9\",\n        \"order\": [\n          0,\n          2,\n \
    \         1\n        ],\n        \"right\": \"5/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            0\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"5/56\"\n        }\n      },\n      {\n      \
    \  \"left\": \"5/9\",\n        \"order\": [\n          0,\n          2,\n    \
    \      1\n        ],\n        \"right\": \"2/3\",\n        \"solution\": {\n \
    \         \"constant_entry_mismatch\": [\n            0,\n            1\n    \
    \      ],\n          \"fixed_value\": \"3/4\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"2/3\",\n        \"order\": [\n          0,\n          2,\n \
    \         1\n        ],\n        \"right\": \"7/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"51/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"7/9\",\n        \"order\": [\n          0,\n          2,\n \
    \         1\n        ],\n        \"right\": \"1\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-23/28\",\n          \"conflict_entry\":\
    \ [\n            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-19/140\",\n          \"matches\": false\n        }\n      },\n      {\n \
    \       \"left\": \"0\",\n        \"order\": [\n          1,\n          0,\n \
    \         2\n        ],\n        \"right\": \"2/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"2/9\",\n        \"order\": [\n          1,\n          0,\n \
    \         2\n        ],\n        \"right\": \"1/3\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"23/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"159/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"1/3\",\n        \"order\": [\n          1,\n          0,\n\
    \          2\n        ],\n        \"right\": \"4/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"89/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"4/9\",\n        \"order\": [\n          1,\n          0,\n \
    \         2\n        ],\n        \"right\": \"5/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            0\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"5/56\"\n        }\n      },\n      {\n      \
    \  \"left\": \"5/9\",\n        \"order\": [\n          1,\n          0,\n    \
    \      2\n        ],\n        \"right\": \"2/3\",\n        \"solution\": {\n \
    \         \"constant_entry_mismatch\": [\n            0,\n            1\n    \
    \      ],\n          \"fixed_value\": \"3/4\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"2/3\",\n        \"order\": [\n          1,\n          0,\n \
    \         2\n        ],\n        \"right\": \"7/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"51/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"7/9\",\n        \"order\": [\n          1,\n          0,\n \
    \         2\n        ],\n        \"right\": \"1\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-23/28\",\n          \"conflict_entry\":\
    \ [\n            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-19/140\",\n          \"matches\": false\n        }\n      },\n      {\n \
    \       \"left\": \"0\",\n        \"order\": [\n          1,\n          2,\n \
    \         0\n        ],\n        \"right\": \"2/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"51/28\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"159/140\",\n          \"matches\": false\n        }\n      },\n      {\n \
    \       \"left\": \"2/9\",\n        \"order\": [\n          1,\n          2,\n\
    \          0\n        ],\n        \"right\": \"1/3\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"23/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"19/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"1/3\",\n        \"order\": [\n          1,\n          2,\n \
    \         0\n        ],\n        \"right\": \"4/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"3/4\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"4/9\",\n        \"order\": [\n          1,\n          2,\n \
    \         0\n        ],\n        \"right\": \"5/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            0\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"5/56\"\n        }\n      },\n      {\n      \
    \  \"left\": \"5/9\",\n        \"order\": [\n          1,\n          2,\n    \
    \      0\n        ],\n        \"right\": \"2/3\",\n        \"solution\": {\n \
    \         \"candidate_fraction\": \"5/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-19/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"2/3\",\n        \"order\": [\n          1,\n          2,\n\
    \          0\n        ],\n        \"right\": \"7/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-89/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"7/9\",\n        \"order\": [\n          1,\n          2,\n\
    \          0\n        ],\n        \"right\": \"1\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"0\",\n        \"order\": [\n          2,\n          0,\n   \
    \       1\n        ],\n        \"right\": \"2/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"51/28\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"159/140\",\n          \"matches\": false\n        }\n      },\n      {\n \
    \       \"left\": \"2/9\",\n        \"order\": [\n          2,\n          0,\n\
    \          1\n        ],\n        \"right\": \"1/3\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"23/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"19/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"1/3\",\n        \"order\": [\n          2,\n          0,\n \
    \         1\n        ],\n        \"right\": \"4/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"3/4\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"4/9\",\n        \"order\": [\n          2,\n          0,\n \
    \         1\n        ],\n        \"right\": \"5/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            0\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"5/56\"\n        }\n      },\n      {\n      \
    \  \"left\": \"5/9\",\n        \"order\": [\n          2,\n          0,\n    \
    \      1\n        ],\n        \"right\": \"2/3\",\n        \"solution\": {\n \
    \         \"candidate_fraction\": \"5/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-19/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"2/3\",\n        \"order\": [\n          2,\n          0,\n\
    \          1\n        ],\n        \"right\": \"7/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-89/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"7/9\",\n        \"order\": [\n          2,\n          0,\n\
    \          1\n        ],\n        \"right\": \"1\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"0\",\n        \"order\": [\n          2,\n          1,\n   \
    \       0\n        ],\n        \"right\": \"2/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            1\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"2/9\",\n        \"order\": [\n          2,\n          1,\n \
    \         0\n        ],\n        \"right\": \"1/3\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"23/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"159/70\",\n          \"matches\": false\n        }\n      },\n      {\n  \
    \      \"left\": \"1/3\",\n        \"order\": [\n          2,\n          1,\n\
    \          0\n        ],\n        \"right\": \"4/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"89/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"4/9\",\n        \"order\": [\n          2,\n          1,\n \
    \         0\n        ],\n        \"right\": \"5/9\",\n        \"solution\": {\n\
    \          \"constant_entry_mismatch\": [\n            0,\n            0\n   \
    \       ],\n          \"fixed_value\": \"0\",\n          \"matches\": false,\n\
    \          \"required_value\": \"5/56\"\n        }\n      },\n      {\n      \
    \  \"left\": \"5/9\",\n        \"order\": [\n          2,\n          1,\n    \
    \      0\n        ],\n        \"right\": \"2/3\",\n        \"solution\": {\n \
    \         \"constant_entry_mismatch\": [\n            0,\n            1\n    \
    \      ],\n          \"fixed_value\": \"3/4\",\n          \"matches\": false,\n\
    \          \"required_value\": \"159/280\"\n        }\n      },\n      {\n   \
    \     \"left\": \"2/3\",\n        \"order\": [\n          2,\n          1,\n \
    \         0\n        ],\n        \"right\": \"7/9\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-9/14\",\n          \"conflict_entry\": [\n\
    \            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"51/70\",\n          \"matches\": false\n        }\n      },\n      {\n   \
    \     \"left\": \"7/9\",\n        \"order\": [\n          2,\n          1,\n \
    \         0\n        ],\n        \"right\": \"1\",\n        \"solution\": {\n\
    \          \"candidate_fraction\": \"-23/28\",\n          \"conflict_entry\":\
    \ [\n            0,\n            1\n          ],\n          \"conflicting_fraction\"\
    : \"-19/140\",\n          \"matches\": false\n        }\n      }\n    ],\n   \
    \ \"minimum_self_mass\": \"0\",\n    \"mixture\": [\n      [\n        \"5/56\"\
    ,\n        \"159/280\",\n        \"12/35\"\n      ],\n      [\n        \"53/70\"\
    ,\n        \"1/30\",\n        \"22/105\"\n      ],\n      [\n        \"24/35\"\
    ,\n        \"11/35\",\n        \"0\"\n      ]\n    ],\n    \"pi\": [\n      \"\
    4/9\",\n      \"1/3\",\n      \"2/9\"\n    ],\n    \"row_dependent_after\": [\n\
    \      \"11/21\",\n      \"32/105\",\n      \"6/35\"\n    ],\n    \"row_dependent_component_choice\"\
    : [\n      [\n        \"5/28\",\n        \"15/28\",\n        \"2/7\"\n      ],\n\
    \      [\n        \"4/5\",\n        \"1/15\",\n        \"2/15\"\n      ],\n  \
    \    [\n        \"4/5\",\n        \"1/5\",\n        \"0\"\n      ]\n    ],\n \
    \   \"stationary_self_mass\": \"16/315\"\n  },\n  \"UDST_uniform4\": {\n    \"\
    UDNAM\": [\n      [\n        \"0\",\n        \"1/3\",\n        \"1/3\",\n    \
    \    \"1/3\"\n      ],\n      [\n        \"1/3\",\n        \"0\",\n        \"\
    1/3\",\n        \"1/3\"\n      ],\n      [\n        \"1/3\",\n        \"1/3\"\
    ,\n        \"0\",\n        \"1/3\"\n      ],\n      [\n        \"1/3\",\n    \
    \    \"1/3\",\n        \"1/3\",\n        \"0\"\n      ]\n    ],\n    \"UDST\"\
    : [\n      [\n        \"0\",\n        \"1/2\",\n        \"0\",\n        \"1/2\"\
    \n      ],\n      [\n        \"1/2\",\n        \"0\",\n        \"1/2\",\n    \
    \    \"0\"\n      ],\n      [\n        \"0\",\n        \"1/2\",\n        \"0\"\
    ,\n        \"1/2\"\n      ],\n      [\n        \"1/2\",\n        \"0\",\n    \
    \    \"1/2\",\n        \"0\"\n      ]\n    ],\n    \"ZDNAM\": [\n      [\n   \
    \     \"0\",\n        \"1/3\",\n        \"1/3\",\n        \"1/3\"\n      ],\n\
    \      [\n        \"1/3\",\n        \"0\",\n        \"1/3\",\n        \"1/3\"\n\
    \      ],\n      [\n        \"1/3\",\n        \"1/3\",\n        \"0\",\n     \
    \   \"1/3\"\n      ],\n      [\n        \"1/3\",\n        \"1/3\",\n        \"\
    1/3\",\n        \"0\"\n      ]\n    ],\n    \"all_24_orders_all_shift_exclusion\"\
    : [\n      {\n        \"left\": \"0\",\n        \"order\": [\n          0,\n \
    \         1,\n          2,\n          3\n        ],\n        \"right\": \"1/4\"\
    ,\n        \"solution\": {\n          \"candidate_fraction\": \"1\",\n       \
    \   \"conflict_entry\": [\n            0,\n            1\n          ],\n     \
    \     \"conflicting_fraction\": \"1/2\",\n          \"matches\": false\n     \
    \   }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n \
    \         0,\n          1,\n          2,\n          3\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          0,\n          1,\n          2,\n          3\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          0,\n          1,\n          2,\n          3\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          0,\n          1,\n          3,\n          2\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          0,\n          1,\n          3,\n          2\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          0,\n          1,\n          3,\n          2\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          0,\n          1,\n          3,\n          2\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          0,\n          2,\n          1,\n          3\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          0,\n          2,\n          1,\n          3\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          0,\n          2,\n          1,\n          3\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          0,\n          2,\n          1,\n          3\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          0,\n          2,\n          3,\n          1\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          0,\n          2,\n          3,\n          1\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          0,\n          2,\n          3,\n          1\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          0,\n          2,\n          3,\n          1\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\": \"\
    0\",\n          \"conflict_entry\": [\n            0,\n            1\n       \
    \   ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\": false\n\
    \        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          0,\n          3,\n          1,\n          2\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          0,\n          3,\n          1,\n          2\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          0,\n          3,\n          1,\n          2\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          0,\n          3,\n          1,\n          2\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          0,\n          3,\n          2,\n          1\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          0,\n          3,\n          2,\n          1\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          0,\n          3,\n          2,\n          1\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          0,\n          3,\n          2,\n          1\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"0\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\"\
    : [\n          1,\n          0,\n          2,\n          3\n        ],\n     \
    \   \"right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          1,\n          0,\n          2,\n          3\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          1,\n          0,\n          2,\n          3\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          1,\n          0,\n          2,\n          3\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\": \"\
    0\",\n          \"conflict_entry\": [\n            0,\n            1\n       \
    \   ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\": false\n\
    \        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          1,\n          0,\n          3,\n          2\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          1,\n          0,\n          3,\n          2\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          1,\n          0,\n          3,\n          2\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          1,\n          0,\n          3,\n          2\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"0\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\"\
    : [\n          1,\n          2,\n          0,\n          3\n        ],\n     \
    \   \"right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          1,\n          2,\n          0,\n          3\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          1,\n          2,\n          0,\n          3\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          1,\n          2,\n          0,\n          3\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          1,\n          2,\n          3,\n          0\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          1,\n          2,\n          3,\n          0\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          1,\n          2,\n          3,\n          0\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          1,\n          2,\n          3,\n          0\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          1,\n          3,\n          0,\n          2\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          1,\n          3,\n          0,\n          2\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          1,\n          3,\n          0,\n          2\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          1,\n          3,\n          0,\n          2\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          1,\n          3,\n          2,\n          0\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          1,\n          3,\n          2,\n          0\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          1,\n          3,\n          2,\n          0\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          1,\n          3,\n          2,\n          0\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          2,\n          0,\n          1,\n          3\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          2,\n          0,\n          1,\n          3\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          2,\n          0,\n          1,\n          3\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          2,\n          0,\n          1,\n          3\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          2,\n          0,\n          3,\n          1\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          2,\n          0,\n          3,\n          1\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          2,\n          0,\n          3,\n          1\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          2,\n          0,\n          3,\n          1\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          2,\n          1,\n          0,\n          3\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          2,\n          1,\n          0,\n          3\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          2,\n          1,\n          0,\n          3\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          2,\n          1,\n          0,\n          3\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"0\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\"\
    : [\n          2,\n          1,\n          3,\n          0\n        ],\n     \
    \   \"right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          2,\n          1,\n          3,\n          0\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          2,\n          1,\n          3,\n          0\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          2,\n          1,\n          3,\n          0\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          2,\n          3,\n          0,\n          1\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          2,\n          3,\n          0,\n          1\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          2,\n          3,\n          0,\n          1\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          2,\n          3,\n          0,\n          1\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          2,\n          3,\n          1,\n          0\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          2,\n          3,\n          1,\n          0\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          2,\n          3,\n          1,\n          0\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          2,\n          3,\n          1,\n          0\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\": \"\
    0\",\n          \"conflict_entry\": [\n            0,\n            1\n       \
    \   ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\": false\n\
    \        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          3,\n          0,\n          1,\n          2\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          3,\n          0,\n          1,\n          2\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          3,\n          0,\n          1,\n          2\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          3,\n          0,\n          1,\n          2\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          3,\n          0,\n          2,\n          1\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          3,\n          0,\n          2,\n          1\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          3,\n          0,\n          2,\n          1\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          3,\n          0,\n          2,\n          1\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          3,\n          1,\n          0,\n          2\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          3,\n          1,\n          0,\n          2\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          3,\n          1,\n          0,\n          2\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          3,\n          1,\n          0,\n          2\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\": \"\
    0\",\n          \"conflict_entry\": [\n            0,\n            1\n       \
    \   ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\": false\n\
    \        }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          3,\n          1,\n          2,\n          0\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          3,\n          1,\n          2,\n          0\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            2,\n            0\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/2\",\n        \"\
    order\": [\n          3,\n          1,\n          2,\n          0\n        ],\n\
    \        \"right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"0\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          3,\n          1,\n          2,\n          0\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          3,\n          2,\n          0,\n          1\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"1/4\",\n        \"\
    order\": [\n          3,\n          2,\n          0,\n          1\n        ],\n\
    \        \"right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            1,\n            0\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          3,\n          2,\n          0,\n          1\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"3/4\",\n        \"order\": [\n\
    \          3,\n          2,\n          0,\n          1\n        ],\n        \"\
    right\": \"1\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"0\",\n        \"order\": [\n\
    \          3,\n          2,\n          1,\n          0\n        ],\n        \"\
    right\": \"1/4\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/4\",\n        \"order\": [\n\
    \          3,\n          2,\n          1,\n          0\n        ],\n        \"\
    right\": \"1/2\",\n        \"solution\": {\n          \"constant_entry_mismatch\"\
    : [\n            0,\n            1\n          ],\n          \"fixed_value\": \"\
    0\",\n          \"matches\": false,\n          \"required_value\": \"1/2\"\n \
    \       }\n      },\n      {\n        \"left\": \"1/2\",\n        \"order\": [\n\
    \          3,\n          2,\n          1,\n          0\n        ],\n        \"\
    right\": \"3/4\",\n        \"solution\": {\n          \"candidate_fraction\":\
    \ \"1/2\",\n          \"conflict_entry\": [\n            0,\n            2\n \
    \         ],\n          \"conflicting_fraction\": \"1\",\n          \"matches\"\
    : false\n        }\n      },\n      {\n        \"left\": \"3/4\",\n        \"\
    order\": [\n          3,\n          2,\n          1,\n          0\n        ],\n\
    \        \"right\": \"1\",\n        \"solution\": {\n          \"candidate_fraction\"\
    : \"0\",\n          \"conflict_entry\": [\n            0,\n            1\n   \
    \       ],\n          \"conflicting_fraction\": \"1/2\",\n          \"matches\"\
    : false\n        }\n      }\n    ],\n    \"analytic_certificate\": \"For equal\
    \ quarter intervals, any shift has two consecutive cyclic offsets q,q+1 with probabilities\
    \ 1-t,t. Matching two half-probability outputs requires t=1/2. No pair of consecutive\
    \ residues modulo4 is closed under negation. Thus this single-shift kernel cannot\
    \ be reversible in any order, whereas UDST is reversible. Boundary shifts have\
    \ one supported destination and also cannot match.\",\n    \"every_single_NAM_order_equal\"\
    : true,\n    \"pi\": [\n      \"1/4\",\n      \"1/4\",\n      \"1/4\",\n     \
    \ \"1/4\"\n    ],\n    \"source_uniform_FSS_ZFSS_cycle_example\": [\n      [\n\
    \        \"0\",\n        \"1\",\n        \"0\",\n        \"0\"\n      ],\n   \
    \   [\n        \"0\",\n        \"0\",\n        \"1\",\n        \"0\"\n      ],\n\
    \      [\n        \"0\",\n        \"0\",\n        \"0\",\n        \"1\"\n    \
    \  ],\n      [\n        \"1\",\n        \"0\",\n        \"0\",\n        \"0\"\n\
    \      ]\n    ]\n  },\n  \"assumptions\": [\n    \"Use one complete positive target\
    \ and current-independent component-selection probabilities at each fixed conditioning\
    \ environment.\",\n    \"UDNAM mixes two reversible NAM kernels; independent valid\
    \ ascending and descending tie policies preserve reversibility, although the mixture\
    \ can change.\",\n    \"UDST uses one maximum anchor and a specified ascending\
    \ tail with its exact reversal, including tied labels. Independent weak sorting\
    \ does not establish reverse-flow pairing.\",\n    \"Equal mixture is part of\
    \ each named method. Unequal constant weights remain invariant but need not remain\
    \ reversible for UDST.\",\n    \"One-state UDST maximum shift equals total mass;\
    \ its stay kernel is an explicitly guarded boundary extension.\",\n    \"The comparison\
    \ with uniform FSS/ZFSS uses the source-described deterministic-cycle property;\
    \ their implementation is not imported or executed here.\"\n  ],\n  \"dependency_sha256\"\
    : {\n    \"nam-boundaries.py\": \"cb58dd0a41b32a7c4f12dcfc711963b39ff062b12f79d8fe6bf065b777714941\"\
    ,\n    \"tower-boundaries.py\": \"d8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47\"\
    \n  },\n  \"expanded_counts\": {\n    \"arbitrary_fixed_NAM_mixing_weight_cases\"\
    : 600,\n    \"compatible_NAM_order_cases\": 771,\n    \"independent_UDNAM_tie_pairs\"\
    : 3231,\n    \"one_state_UDST_endpoint_extensions\": 3,\n    \"paired_UDST_order_cases\"\
    : 435,\n    \"positive_target_vectors\": 120\n  },\n  \"fixed_two_binary_coordinate_scan\"\
    : {\n    \"classes\": [\n      {\n        \"closed\": true,\n        \"period\"\
    : 2,\n        \"states_zero_based\": [\n          0,\n          3\n        ]\n\
    \      },\n      {\n        \"closed\": true,\n        \"period\": 2,\n      \
    \  \"states_zero_based\": [\n          1,\n          2\n        ]\n      }\n \
    \   ],\n    \"matrix\": [\n      [\n        \"0\",\n        \"0\",\n        \"\
    0\",\n        \"1\"\n      ],\n      [\n        \"0\",\n        \"0\",\n     \
    \   \"1\",\n        \"0\"\n      ],\n      [\n        \"0\",\n        \"1\",\n\
    \        \"0\",\n        \"0\"\n      ],\n      [\n        \"1\",\n        \"\
    0\",\n        \"0\",\n        \"0\"\n      ]\n    ],\n    \"states\": [\n    \
    \  [\n        0,\n        0\n      ],\n      [\n        0,\n        1\n      ],\n\
    \      [\n        1,\n        0\n      ],\n      [\n        1,\n        1\n  \
    \    ]\n    ]\n  },\n  \"half_dominant_point_boundaries\": [\n    {\n      \"\
    UDNAM\": [\n        [\n          \"1\"\n        ]\n      ],\n      \"UDNAM_self_mass\"\
    : \"1\",\n      \"UDST\": [\n        [\n          \"1\"\n        ]\n      ],\n\
    \      \"UDST_self_mass\": \"1\",\n      \"minimum_self_mass\": \"1\",\n     \
    \ \"pi\": [\n        \"1\"\n      ],\n      \"weights\": [\n        1\n      ]\n\
    \    },\n    {\n      \"UDNAM\": [\n        [\n          \"0\",\n          \"\
    1\"\n        ],\n        [\n          \"1\",\n          \"0\"\n        ]\n   \
    \   ],\n      \"UDNAM_self_mass\": \"0\",\n      \"UDST\": [\n        [\n    \
    \      \"0\",\n          \"1\"\n        ],\n        [\n          \"1\",\n    \
    \      \"0\"\n        ]\n      ],\n      \"UDST_self_mass\": \"0\",\n      \"\
    minimum_self_mass\": \"0\",\n      \"pi\": [\n        \"1/2\",\n        \"1/2\"\
    \n      ],\n      \"weights\": [\n        1,\n        1\n      ]\n    },\n   \
    \ {\n      \"UDNAM\": [\n        [\n          \"3/20\",\n          \"21/40\",\n\
    \          \"13/40\"\n        ],\n        [\n          \"7/8\",\n          \"\
    0\",\n          \"1/8\"\n        ],\n        [\n          \"13/16\",\n       \
    \   \"3/16\",\n          \"0\"\n        ]\n      ],\n      \"UDNAM_self_mass\"\
    : \"3/40\",\n      \"UDST\": [\n        [\n          \"0\",\n          \"3/5\"\
    ,\n          \"2/5\"\n        ],\n        [\n          \"1\",\n          \"0\"\
    ,\n          \"0\"\n        ],\n        [\n          \"1\",\n          \"0\",\n\
    \          \"0\"\n        ]\n      ],\n      \"UDST_self_mass\": \"0\",\n    \
    \  \"minimum_self_mass\": \"0\",\n      \"pi\": [\n        \"1/2\",\n        \"\
    3/10\",\n        \"1/5\"\n      ],\n      \"weights\": [\n        5,\n       \
    \ 3,\n        2\n      ]\n    },\n    {\n      \"UDNAM\": [\n        [\n     \
    \     \"7/18\",\n          \"17/36\",\n          \"5/36\"\n        ],\n      \
    \  [\n          \"17/18\",\n          \"0\",\n          \"1/18\"\n        ],\n\
    \        [\n          \"5/6\",\n          \"1/6\",\n          \"0\"\n        ]\n\
    \      ],\n      \"UDNAM_self_mass\": \"7/30\",\n      \"UDST\": [\n        [\n\
    \          \"1/3\",\n          \"1/2\",\n          \"1/6\"\n        ],\n     \
    \   [\n          \"1\",\n          \"0\",\n          \"0\"\n        ],\n     \
    \   [\n          \"1\",\n          \"0\",\n          \"0\"\n        ]\n      ],\n\
    \      \"UDST_self_mass\": \"1/5\",\n      \"minimum_self_mass\": \"1/5\",\n \
    \     \"pi\": [\n        \"3/5\",\n        \"3/10\",\n        \"1/10\"\n     \
    \ ],\n      \"weights\": [\n        6,\n        3,\n        1\n      ]\n    },\n\
    \    {\n      \"UDNAM\": [\n        [\n          \"55/72\",\n          \"17/144\"\
    ,\n          \"17/144\"\n        ],\n        [\n          \"17/18\",\n       \
    \   \"0\",\n          \"1/18\"\n        ],\n        [\n          \"17/18\",\n\
    \          \"1/18\",\n          \"0\"\n        ]\n      ],\n      \"UDNAM_self_mass\"\
    : \"11/18\",\n      \"UDST\": [\n        [\n          \"3/4\",\n          \"1/8\"\
    ,\n          \"1/8\"\n        ],\n        [\n          \"1\",\n          \"0\"\
    ,\n          \"0\"\n        ],\n        [\n          \"1\",\n          \"0\",\n\
    \          \"0\"\n        ]\n      ],\n      \"UDST_self_mass\": \"3/5\",\n  \
    \    \"minimum_self_mass\": \"3/5\",\n      \"pi\": [\n        \"4/5\",\n    \
    \    \"1/10\",\n        \"1/10\"\n      ],\n      \"weights\": [\n        8,\n\
    \        1,\n        1\n      ]\n    }\n  ],\n  \"mixture_weight_boundaries\"\
    : {\n    \"after\": [\n      \"1/3\",\n      \"2/3\",\n      \"0\"\n    ],\n \
    \   \"paired_components\": [\n      [\n        [\n          \"0\",\n         \
    \ \"1\",\n          \"0\"\n        ],\n        [\n          \"0\",\n         \
    \ \"0\",\n          \"1\"\n        ],\n        [\n          \"1\",\n         \
    \ \"0\",\n          \"0\"\n        ]\n      ],\n      [\n        [\n         \
    \ \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n         \
    \ \"1\",\n          \"0\",\n          \"0\"\n        ],\n        [\n         \
    \ \"0\",\n          \"1\",\n          \"0\"\n        ]\n      ]\n    ],\n    \"\
    pi\": [\n      \"1/3\",\n      \"1/3\",\n      \"1/3\"\n    ],\n    \"state_dependent_choice\"\
    : [\n      [\n        \"0\",\n        \"1\",\n        \"0\"\n      ],\n      [\n\
    \        \"1\",\n        \"0\",\n        \"0\"\n      ],\n      [\n        \"\
    0\",\n        \"1\",\n        \"0\"\n      ]\n    ],\n    \"unequal_fixed_mix\"\
    : [\n      [\n        \"0\",\n        \"1/4\",\n        \"3/4\"\n      ],\n  \
    \    [\n        \"3/4\",\n        \"0\",\n        \"1/4\"\n      ],\n      [\n\
    \        \"1/4\",\n        \"3/4\",\n        \"0\"\n      ]\n    ],\n    \"unequal_fixed_mix_reversible\"\
    : false,\n    \"unequal_fixed_mix_stationary\": true\n  },\n  \"original_witnesses\"\
    : {\n    \"positive_target_vectors\": 120,\n    \"scope\": \"Original exact Fraction\
    \ calculations, not author software. Positive integer weights1..3 for lengths1..4\
    \ produce120 ordered vectors, including repeated normalized targets. One-state\
    \ maximum-shift endpoint is a separately recognized identity extension. No float,\
    \ efficiency, benchmark or general ergodicity claim.\",\n    \"udnam_distinction\"\
    : {\n      \"DNAM\": [\n        [\n          \"0\",\n          \"3/5\",\n    \
    \      \"2/5\"\n        ],\n        [\n          \"4/5\",\n          \"1/15\"\
    ,\n          \"2/15\"\n        ],\n        [\n          \"4/5\",\n          \"\
    1/5\",\n          \"0\"\n        ]\n      ],\n      \"UDNAM\": [\n        [\n\
    \          \"5/56\",\n          \"159/280\",\n          \"12/35\"\n        ],\n\
    \        [\n          \"53/70\",\n          \"1/30\",\n          \"22/105\"\n\
    \        ],\n        [\n          \"24/35\",\n          \"11/35\",\n         \
    \ \"0\"\n        ]\n      ],\n      \"UNAM\": [\n        [\n          \"5/28\"\
    ,\n          \"15/28\",\n          \"2/7\"\n        ],\n        [\n          \"\
    5/7\",\n          \"0\",\n          \"2/7\"\n        ],\n        [\n         \
    \ \"4/7\",\n          \"3/7\",\n          \"0\"\n        ]\n      ],\n      \"\
    all_six_single_NAM_orders\": [\n        {\n          \"matrix\": [\n         \
    \   [\n              \"0\",\n              \"3/5\",\n              \"2/5\"\n \
    \           ],\n            [\n              \"4/5\",\n              \"1/15\"\
    ,\n              \"2/15\"\n            ],\n            [\n              \"4/5\"\
    ,\n              \"1/5\",\n              \"0\"\n            ]\n          ],\n\
    \          \"order\": [\n            0,\n            1,\n            2\n     \
    \     ]\n        },\n        {\n          \"matrix\": [\n            [\n     \
    \         \"0\",\n              \"3/5\",\n              \"2/5\"\n            ],\n\
    \            [\n              \"4/5\",\n              \"1/15\",\n            \
    \  \"2/15\"\n            ],\n            [\n              \"4/5\",\n         \
    \     \"1/5\",\n              \"0\"\n            ]\n          ],\n          \"\
    order\": [\n            0,\n            2,\n            1\n          ]\n     \
    \   },\n        {\n          \"matrix\": [\n            [\n              \"1/4\"\
    ,\n              \"1/2\",\n              \"1/4\"\n            ],\n           \
    \ [\n              \"2/3\",\n              \"0\",\n              \"1/3\"\n   \
    \         ],\n            [\n              \"1/2\",\n              \"1/2\",\n\
    \              \"0\"\n            ]\n          ],\n          \"order\": [\n  \
    \          1,\n            0,\n            2\n          ]\n        },\n      \
    \  {\n          \"matrix\": [\n            [\n              \"1/4\",\n       \
    \       \"1/2\",\n              \"1/4\"\n            ],\n            [\n     \
    \         \"2/3\",\n              \"0\",\n              \"1/3\"\n            ],\n\
    \            [\n              \"1/2\",\n              \"1/2\",\n             \
    \ \"0\"\n            ]\n          ],\n          \"order\": [\n            1,\n\
    \            2,\n            0\n          ]\n        },\n        {\n         \
    \ \"matrix\": [\n            [\n              \"5/28\",\n              \"15/28\"\
    ,\n              \"2/7\"\n            ],\n            [\n              \"5/7\"\
    ,\n              \"0\",\n              \"2/7\"\n            ],\n            [\n\
    \              \"4/7\",\n              \"3/7\",\n              \"0\"\n       \
    \     ]\n          ],\n          \"order\": [\n            2,\n            0,\n\
    \            1\n          ]\n        },\n        {\n          \"matrix\": [\n\
    \            [\n              \"5/28\",\n              \"15/28\",\n          \
    \    \"2/7\"\n            ],\n            [\n              \"5/7\",\n        \
    \      \"0\",\n              \"2/7\"\n            ],\n            [\n        \
    \      \"4/7\",\n              \"3/7\",\n              \"0\"\n            ]\n\
    \          ],\n          \"order\": [\n            2,\n            1,\n      \
    \      0\n          ]\n        }\n      ],\n      \"down_order\": [\n        0,\n\
    \        1,\n        2\n      ],\n      \"interpretation\": \"The mixture has\
    \ two positive diagonal entries while each single NAM ordering has at most one;\
    \ this one target disproves full construction equivalence. It does not assert\
    \ disjoint kernel sets.\",\n      \"pi\": [\n        \"4/9\",\n        \"1/3\"\
    ,\n        \"2/9\"\n      ],\n      \"positive_diagonals\": 2,\n      \"up_order\"\
    : [\n        2,\n        1,\n        0\n      ]\n    },\n    \"udnam_tie_policy\"\
    : {\n      \"DNAM_choices\": [\n        [\n          [\n            \"0\",\n \
    \           \"1/14\",\n            \"3/14\",\n            \"5/7\"\n          ],\n\
    \          [\n            \"1/42\",\n            \"1/21\",\n            \"3/14\"\
    ,\n            \"5/7\"\n          ],\n          [\n            \"1/14\",\n   \
    \         \"3/14\",\n            \"0\",\n            \"5/7\"\n          ],\n \
    \         [\n            \"1/7\",\n            \"3/7\",\n            \"3/7\",\n\
    \            \"0\"\n          ]\n        ],\n        [\n          [\n        \
    \    \"0\",\n            \"3/14\",\n            \"1/14\",\n            \"5/7\"\
    \n          ],\n          [\n            \"1/14\",\n            \"0\",\n     \
    \       \"3/14\",\n            \"5/7\"\n          ],\n          [\n          \
    \  \"1/42\",\n            \"3/14\",\n            \"1/21\",\n            \"5/7\"\
    \n          ],\n          [\n            \"1/7\",\n            \"3/7\",\n    \
    \        \"3/7\",\n            \"0\"\n          ]\n        ]\n      ],\n     \
    \ \"UDNAM_choices\": [\n        [\n          [\n            \"0\",\n         \
    \   \"53/308\",\n            \"75/308\",\n            \"45/77\"\n          ],\n\
    \          [\n            \"53/924\",\n            \"1/42\",\n            \"171/616\"\
    ,\n            \"395/616\"\n          ],\n          [\n            \"25/308\"\
    ,\n            \"171/616\",\n            \"0\",\n            \"395/616\"\n   \
    \       ],\n          [\n            \"9/77\",\n            \"237/616\",\n   \
    \         \"237/616\",\n            \"5/44\"\n          ]\n        ],\n      \
    \  [\n          [\n            \"0\",\n            \"75/308\",\n            \"\
    53/308\",\n            \"45/77\"\n          ],\n          [\n            \"25/308\"\
    ,\n            \"0\",\n            \"171/616\",\n            \"395/616\"\n   \
    \       ],\n          [\n            \"53/924\",\n            \"171/616\",\n \
    \           \"1/42\",\n            \"395/616\"\n          ],\n          [\n  \
    \          \"9/77\",\n            \"237/616\",\n            \"237/616\",\n   \
    \         \"5/44\"\n          ]\n        ]\n      ],\n      \"UNAM\": [\n    \
    \    [\n          \"0\",\n          \"3/11\",\n          \"3/11\",\n         \
    \ \"5/11\"\n        ],\n        [\n          \"1/11\",\n          \"0\",\n   \
    \       \"15/44\",\n          \"25/44\"\n        ],\n        [\n          \"1/11\"\
    ,\n          \"15/44\",\n          \"0\",\n          \"25/44\"\n        ],\n \
    \       [\n          \"1/11\",\n          \"15/44\",\n          \"15/44\",\n \
    \         \"5/22\"\n        ]\n      ],\n      \"down_orders\": [\n        [\n\
    \          3,\n          2,\n          1,\n          0\n        ],\n        [\n\
    \          3,\n          1,\n          2,\n          0\n        ]\n      ],\n\
    \      \"interpretation\": \"UNAM is unchanged under this tie exchange; DNAM and\
    \ hence UDNAM change. Each component and mixture remains reversible. A reverse-pair\
    \ requirement is not needed for UDNAM reversibility.\",\n      \"pi\": [\n   \
    \     \"1/12\",\n        \"1/4\",\n        \"1/4\",\n        \"5/12\"\n      ],\n\
    \      \"up_orders\": [\n        [\n          0,\n          1,\n          2,\n\
    \          3\n        ],\n        [\n          0,\n          2,\n          1,\n\
    \          3\n        ]\n      ]\n    },\n    \"udst_single_circle_distinction\"\
    : {\n      \"DST_positive_orientation\": [\n        [\n          \"0\",\n    \
    \      \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n    \
    \      \"1\",\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n\
    \        [\n          \"0\",\n          \"1\",\n          \"0\",\n          \"\
    0\"\n        ],\n        [\n          \"0\",\n          \"0\",\n          \"1\"\
    ,\n          \"0\"\n        ]\n      ],\n      \"HST_same_order\": [\n       \
    \ [\n          \"0\",\n          \"0\",\n          \"1\",\n          \"0\"\n \
    \       ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n\
    \          \"1\"\n        ],\n        [\n          \"1\",\n          \"0\",\n\
    \          \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n\
    \          \"1\",\n          \"0\",\n          \"0\"\n        ]\n      ],\n  \
    \    \"UDNAM\": [\n        [\n          \"0\",\n          \"1/3\",\n         \
    \ \"1/3\",\n          \"1/3\"\n        ],\n        [\n          \"1/3\",\n   \
    \       \"0\",\n          \"1/3\",\n          \"1/3\"\n        ],\n        [\n\
    \          \"1/3\",\n          \"1/3\",\n          \"0\",\n          \"1/3\"\n\
    \        ],\n        [\n          \"1/3\",\n          \"1/3\",\n          \"1/3\"\
    ,\n          \"0\"\n        ]\n      ],\n      \"UDST\": [\n        [\n      \
    \    \"0\",\n          \"1/2\",\n          \"0\",\n          \"1/2\"\n       \
    \ ],\n        [\n          \"1/2\",\n          \"0\",\n          \"1/2\",\n  \
    \        \"0\"\n        ],\n        [\n          \"0\",\n          \"1/2\",\n\
    \          \"0\",\n          \"1/2\"\n        ],\n        [\n          \"1/2\"\
    ,\n          \"0\",\n          \"1/2\",\n          \"0\"\n        ]\n      ],\n\
    \      \"UST_positive_orientation\": [\n        [\n          \"0\",\n        \
    \  \"1\",\n          \"0\",\n          \"0\"\n        ],\n        [\n        \
    \  \"0\",\n          \"0\",\n          \"1\",\n          \"0\"\n        ],\n \
    \       [\n          \"0\",\n          \"0\",\n          \"0\",\n          \"\
    1\"\n        ],\n        [\n          \"1\",\n          \"0\",\n          \"0\"\
    ,\n          \"0\"\n        ]\n      ],\n      \"all_24_orders_all_shift_certificate\"\
    : [\n        {\n          \"left\": \"0\",\n          \"order\": [\n         \
    \   0,\n            1,\n            2,\n            3\n          ],\n        \
    \  \"right\": \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\"\
    : \"1\",\n            \"conflict_entry\": [\n              0,\n              1\n\
    \            ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            0,\n            1,\n            2,\n  \
    \          3\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"0\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            0,\n      \
    \      1,\n            2,\n            3\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            0,\n            1,\n            2,\n        \
    \    3\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            0,\n\
    \            1,\n            3,\n            2\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1\",\n            \"conflict_entry\": [\n              0,\n              1\n \
    \           ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            0,\n            1,\n            3,\n  \
    \          2\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"constant_entry_mismatch\": [\n              1,\n          \
    \    0\n            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            0,\n\
    \            1,\n            3,\n            2\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            0,\n            1,\n            3,\n        \
    \    2\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            0,\n\
    \            2,\n            1,\n            3\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            0,\n            2,\n            1,\n        \
    \    3\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            0,\n      \
    \      2,\n            1,\n            3\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              2,\n              0\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            0,\n            2,\n            1,\n      \
    \      3\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            0,\n\
    \            2,\n            3,\n            1\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            0,\n            2,\n            3,\n        \
    \    1\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            0,\n\
    \            2,\n            3,\n            1\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              1,\n              0\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            0,\n            2,\n            3,\n        \
    \    1\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"0\",\n            \"conflict_entry\": [\n\
    \              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            0,\n        \
    \    3,\n            1,\n            2\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            0,\n            3,\n            1,\n        \
    \    2\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              2,\n              0\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            0,\n      \
    \      3,\n            1,\n            2\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              0,\n              2\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            0,\n            3,\n            1,\n      \
    \      2\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            0,\n\
    \            3,\n            2,\n            1\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            0,\n            3,\n            2,\n        \
    \    1\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            0,\n\
    \            3,\n            2,\n            1\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1/2\",\n            \"conflict_entry\": [\n              0,\n              2\n\
    \            ],\n            \"conflicting_fraction\": \"1\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"3/4\"\
    ,\n          \"order\": [\n            0,\n            3,\n            2,\n  \
    \          1\n          ],\n          \"right\": \"1\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"0\",\n            \"conflict_entry\"\
    : [\n              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            1,\n        \
    \    0,\n            2,\n            3\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            1,\n            0,\n            2,\n        \
    \    3\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            1,\n\
    \            0,\n            2,\n            3\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              1,\n              0\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            1,\n            0,\n            2,\n        \
    \    3\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"0\",\n            \"conflict_entry\": [\n\
    \              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            1,\n        \
    \    0,\n            3,\n            2\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            1,\n            0,\n            3,\n        \
    \    2\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            1,\n\
    \            0,\n            3,\n            2\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1/2\",\n            \"conflict_entry\": [\n              0,\n              2\n\
    \            ],\n            \"conflicting_fraction\": \"1\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"3/4\"\
    ,\n          \"order\": [\n            1,\n            0,\n            3,\n  \
    \          2\n          ],\n          \"right\": \"1\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"0\",\n            \"conflict_entry\"\
    : [\n              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            1,\n        \
    \    2,\n            0,\n            3\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            1,\n            2,\n            0,\n        \
    \    3\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              2,\n              0\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            1,\n      \
    \      2,\n            0,\n            3\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              0,\n              2\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            1,\n            2,\n            0,\n      \
    \      3\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            1,\n\
    \            2,\n            3,\n            0\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1\",\n            \"conflict_entry\": [\n              0,\n              1\n \
    \           ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            1,\n            2,\n            3,\n  \
    \          0\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"0\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            1,\n      \
    \      2,\n            3,\n            0\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            1,\n            2,\n            3,\n        \
    \    0\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            1,\n\
    \            3,\n            0,\n            2\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            1,\n            3,\n            0,\n        \
    \    2\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            1,\n      \
    \      3,\n            0,\n            2\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              2,\n              0\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            1,\n            3,\n            0,\n      \
    \      2\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            1,\n\
    \            3,\n            2,\n            0\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1\",\n            \"conflict_entry\": [\n              0,\n              1\n \
    \           ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            1,\n            3,\n            2,\n  \
    \          0\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"constant_entry_mismatch\": [\n              1,\n          \
    \    0\n            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            1,\n\
    \            3,\n            2,\n            0\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            1,\n            3,\n            2,\n        \
    \    0\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            2,\n\
    \            0,\n            1,\n            3\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1\",\n            \"conflict_entry\": [\n              0,\n              1\n \
    \           ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            2,\n            0,\n            1,\n  \
    \          3\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"constant_entry_mismatch\": [\n              1,\n          \
    \    0\n            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            2,\n\
    \            0,\n            1,\n            3\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            2,\n            0,\n            1,\n        \
    \    3\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            2,\n\
    \            0,\n            3,\n            1\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            2,\n            0,\n            3,\n        \
    \    1\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              2,\n              0\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            2,\n      \
    \      0,\n            3,\n            1\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              0,\n              2\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            2,\n            0,\n            3,\n      \
    \      1\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            2,\n\
    \            1,\n            0,\n            3\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            2,\n            1,\n            0,\n        \
    \    3\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            2,\n\
    \            1,\n            0,\n            3\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1/2\",\n            \"conflict_entry\": [\n              0,\n              2\n\
    \            ],\n            \"conflicting_fraction\": \"1\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"3/4\"\
    ,\n          \"order\": [\n            2,\n            1,\n            0,\n  \
    \          3\n          ],\n          \"right\": \"1\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"0\",\n            \"conflict_entry\"\
    : [\n              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            2,\n        \
    \    1,\n            3,\n            0\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            2,\n            1,\n            3,\n        \
    \    0\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            2,\n      \
    \      1,\n            3,\n            0\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              2,\n              0\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            2,\n            1,\n            3,\n      \
    \      0\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            2,\n\
    \            3,\n            0,\n            1\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1\",\n            \"conflict_entry\": [\n              0,\n              1\n \
    \           ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            2,\n            3,\n            0,\n  \
    \          1\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"0\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            2,\n      \
    \      3,\n            0,\n            1\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            2,\n            3,\n            0,\n        \
    \    1\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            2,\n\
    \            3,\n            1,\n            0\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            2,\n            3,\n            1,\n        \
    \    0\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            2,\n\
    \            3,\n            1,\n            0\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              1,\n              0\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            2,\n            3,\n            1,\n        \
    \    0\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"0\",\n            \"conflict_entry\": [\n\
    \              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            3,\n        \
    \    0,\n            1,\n            2\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1\",\n\
    \            \"conflict_entry\": [\n              0,\n              1\n      \
    \      ],\n            \"conflicting_fraction\": \"1/2\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"1/4\",\n  \
    \        \"order\": [\n            3,\n            0,\n            1,\n      \
    \      2\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"0\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            3,\n      \
    \      0,\n            1,\n            2\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            3,\n            0,\n            1,\n        \
    \    2\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            3,\n\
    \            0,\n            2,\n            1\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            3,\n            0,\n            2,\n        \
    \    1\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              0,\n              2\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            3,\n      \
    \      0,\n            2,\n            1\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              2,\n              0\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            3,\n            0,\n            2,\n      \
    \      1\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            3,\n\
    \            1,\n            0,\n            2\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            3,\n            1,\n            0,\n        \
    \    2\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            3,\n\
    \            1,\n            0,\n            2\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              1,\n              0\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            3,\n            1,\n            0,\n        \
    \    2\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"0\",\n            \"conflict_entry\": [\n\
    \              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"0\",\n          \"order\": [\n            3,\n        \
    \    1,\n            2,\n            0\n          ],\n          \"right\": \"\
    1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\": [\n\
    \              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            3,\n            1,\n            2,\n        \
    \    0\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"candidate_fraction\": \"1/2\",\n            \"conflict_entry\"\
    : [\n              2,\n              0\n            ],\n            \"conflicting_fraction\"\
    : \"1\",\n            \"matches\": false\n          }\n        },\n        {\n\
    \          \"left\": \"1/2\",\n          \"order\": [\n            3,\n      \
    \      1,\n            2,\n            0\n          ],\n          \"right\": \"\
    3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"1/2\"\
    ,\n            \"conflict_entry\": [\n              0,\n              2\n    \
    \        ],\n            \"conflicting_fraction\": \"0\",\n            \"matches\"\
    : false\n          }\n        },\n        {\n          \"left\": \"3/4\",\n  \
    \        \"order\": [\n            3,\n            1,\n            2,\n      \
    \      0\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            3,\n\
    \            2,\n            0,\n            1\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1\",\n            \"conflict_entry\": [\n              0,\n              1\n \
    \           ],\n            \"conflicting_fraction\": \"1/2\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"1/4\"\
    ,\n          \"order\": [\n            3,\n            2,\n            0,\n  \
    \          1\n          ],\n          \"right\": \"1/2\",\n          \"solution\"\
    : {\n            \"constant_entry_mismatch\": [\n              1,\n          \
    \    0\n            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            3,\n\
    \            2,\n            0,\n            1\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"3/4\",\n    \
    \      \"order\": [\n            3,\n            2,\n            0,\n        \
    \    1\n          ],\n          \"right\": \"1\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"0\",\n          \"order\": [\n            3,\n\
    \            2,\n            1,\n            0\n          ],\n          \"right\"\
    : \"1/4\",\n          \"solution\": {\n            \"constant_entry_mismatch\"\
    : [\n              0,\n              1\n            ],\n            \"fixed_value\"\
    : \"0\",\n            \"matches\": false,\n            \"required_value\": \"\
    1/2\"\n          }\n        },\n        {\n          \"left\": \"1/4\",\n    \
    \      \"order\": [\n            3,\n            2,\n            1,\n        \
    \    0\n          ],\n          \"right\": \"1/2\",\n          \"solution\": {\n\
    \            \"constant_entry_mismatch\": [\n              0,\n              1\n\
    \            ],\n            \"fixed_value\": \"0\",\n            \"matches\"\
    : false,\n            \"required_value\": \"1/2\"\n          }\n        },\n \
    \       {\n          \"left\": \"1/2\",\n          \"order\": [\n            3,\n\
    \            2,\n            1,\n            0\n          ],\n          \"right\"\
    : \"3/4\",\n          \"solution\": {\n            \"candidate_fraction\": \"\
    1/2\",\n            \"conflict_entry\": [\n              0,\n              2\n\
    \            ],\n            \"conflicting_fraction\": \"1\",\n            \"\
    matches\": false\n          }\n        },\n        {\n          \"left\": \"3/4\"\
    ,\n          \"order\": [\n            3,\n            2,\n            1,\n  \
    \          0\n          ],\n          \"right\": \"1\",\n          \"solution\"\
    : {\n            \"candidate_fraction\": \"0\",\n            \"conflict_entry\"\
    : [\n              0,\n              1\n            ],\n            \"conflicting_fraction\"\
    : \"1/2\",\n            \"matches\": false\n          }\n        }\n      ],\n\
    \      \"closed_affine_segments\": 96,\n      \"down_order\": [\n        0,\n\
    \        3,\n        2,\n        1\n      ],\n      \"interpretation\": \"For\
    \ this uniform4 target, no single circular shift in any order gives the UDST kernel.\
    \ All shifts in [0,1] are covered by four affine pieces per order, including endpoints.\
    \ Either orientation is covered by the full shift range. This is one counterexample,\
    \ not a classification of all coincidences.\",\n      \"orders\": 24,\n      \"\
    pi\": [\n        \"1/4\",\n        \"1/4\",\n        \"1/4\",\n        \"1/4\"\
    \n      ],\n      \"up_order\": [\n        0,\n        1,\n        2,\n      \
    \  3\n      ]\n    },\n    \"udst_unpaired_tie_failure\": {\n      \"independently_tied_down_order\"\
    : [\n        0,\n        1,\n        2\n      ],\n      \"interpretation\": \"\
    Both same orders satisfy weak upward/downward probability sorting when all masses\
    \ tie. They are not reverse-paired, so Eq101 and the reversibility conclusion\
    \ do not follow. The bad mixture remains invariant, demonstrating precisely the\
    \ missing pairing condition.\",\n      \"paired_reverse_mixture\": [\n       \
    \ [\n          \"0\",\n          \"1/2\",\n          \"1/2\"\n        ],\n   \
    \     [\n          \"1/2\",\n          \"0\",\n          \"1/2\"\n        ],\n\
    \        [\n          \"1/2\",\n          \"1/2\",\n          \"0\"\n        ]\n\
    \      ],\n      \"pi\": [\n        \"1/3\",\n        \"1/3\",\n        \"1/3\"\
    \n      ],\n      \"unpaired_mixture\": [\n        [\n          \"0\",\n     \
    \     \"1\",\n          \"0\"\n        ],\n        [\n          \"0\",\n     \
    \     \"0\",\n          \"1\"\n        ],\n        [\n          \"1\",\n     \
    \     \"0\",\n          \"0\"\n        ]\n      ],\n      \"up_order\": [\n  \
    \      0,\n        1,\n        2\n      ]\n    }\n  },\n  \"scope\": \"Exact positive\
    \ finite conditional kernels. Original source-agent witness output is retained\
    \ without runtime metadata. Expanded tie, independent-component, all-shift and\
    \ exploration checks use pinned unchanged sibling routines. No efficiency, float,\
    \ author-code, all-target nonintersection or general convergence claim.\",\n \
    \ \"uniform_periodicity\": [\n    {\n      \"UDNAM_classes\": [\n        {\n \
    \         \"closed\": true,\n          \"period\": 2,\n          \"states_zero_based\"\
    : [\n            0,\n            1\n          ]\n        }\n      ],\n      \"\
    UDST_classes\": [\n        {\n          \"closed\": true,\n          \"period\"\
    : 2,\n          \"states_zero_based\": [\n            0,\n            1\n    \
    \      ]\n        }\n      ],\n      \"states\": 2\n    },\n    {\n      \"UDNAM_classes\"\
    : [\n        {\n          \"closed\": true,\n          \"period\": 1,\n      \
    \    \"states_zero_based\": [\n            0,\n            1,\n            2\n\
    \          ]\n        }\n      ],\n      \"UDST_classes\": [\n        {\n    \
    \      \"closed\": true,\n          \"period\": 1,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2\n          ]\n        }\n \
    \     ],\n      \"states\": 3\n    },\n    {\n      \"UDNAM_classes\": [\n   \
    \     {\n          \"closed\": true,\n          \"period\": 1,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2,\n            3\n         \
    \ ]\n        }\n      ],\n      \"UDST_classes\": [\n        {\n          \"closed\"\
    : true,\n          \"period\": 2,\n          \"states_zero_based\": [\n      \
    \      0,\n            1,\n            2,\n            3\n          ]\n      \
    \  }\n      ],\n      \"states\": 4\n    },\n    {\n      \"UDNAM_classes\": [\n\
    \        {\n          \"closed\": true,\n          \"period\": 1,\n          \"\
    states_zero_based\": [\n            0,\n            1,\n            2,\n     \
    \       3,\n            4\n          ]\n        }\n      ],\n      \"UDST_classes\"\
    : [\n        {\n          \"closed\": true,\n          \"period\": 1,\n      \
    \    \"states_zero_based\": [\n            0,\n            1,\n            2,\n\
    \            3,\n            4\n          ]\n        }\n      ],\n      \"states\"\
    : 5\n    },\n    {\n      \"UDNAM_classes\": [\n        {\n          \"closed\"\
    : true,\n          \"period\": 1,\n          \"states_zero_based\": [\n      \
    \      0,\n            1,\n            2,\n            3,\n            4,\n  \
    \          5\n          ]\n        }\n      ],\n      \"UDST_classes\": [\n  \
    \      {\n          \"closed\": true,\n          \"period\": 2,\n          \"\
    states_zero_based\": [\n            0,\n            1,\n            2,\n     \
    \       3,\n            4,\n            5\n          ]\n        }\n      ],\n\
    \      \"states\": 6\n    },\n    {\n      \"UDNAM_classes\": [\n        {\n \
    \         \"closed\": true,\n          \"period\": 1,\n          \"states_zero_based\"\
    : [\n            0,\n            1,\n            2,\n            3,\n        \
    \    4,\n            5,\n            6\n          ]\n        }\n      ],\n   \
    \   \"UDST_classes\": [\n        {\n          \"closed\": true,\n          \"\
    period\": 1,\n          \"states_zero_based\": [\n            0,\n           \
    \ 1,\n            2,\n            3,\n            4,\n            5,\n       \
    \     6\n          ]\n        }\n      ],\n      \"states\": 7\n    },\n    {\n\
    \      \"UDNAM_classes\": [\n        {\n          \"closed\": true,\n        \
    \  \"period\": 1,\n          \"states_zero_based\": [\n            0,\n      \
    \      1,\n            2,\n            3,\n            4,\n            5,\n  \
    \          6,\n            7\n          ]\n        }\n      ],\n      \"UDST_classes\"\
    : [\n        {\n          \"closed\": true,\n          \"period\": 2,\n      \
    \    \"states_zero_based\": [\n            0,\n            1,\n            2,\n\
    \            3,\n            4,\n            5,\n            6,\n            7\n\
    \          ]\n        }\n      ],\n      \"states\": 8\n    }\n  ]\n}\n"
  scope_note: Actual execution completed 2026-10-14T23:08:38.396403Z; this generator
    executes no recorded commands.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json
  locator: identity_search and identity_assessment
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: 67c0606e4e22d9ca2d473842632207842effb729628e0a61402e1f9e1f49818b
  support: supports
  summary: The actual post317 assessment covers all 442 pinned AIO and 710 native
    IDs, names, aliases and every scoped synonym, plus four complete checkout searches
    including ignored and hidden files. Historical 706-native source research, 334
    selected ID/name rows, 103 selected definitions, 59 additional mixture definitions,
    22 exact AIO node/incident/generated contexts and 18 full native neighbors retain
    their attributed reading scope. The four actual FSS/ZFSS and NAM/ZDNAM records
    are freshly assessed. AIO:MarkovChain is related_match between a transition construction
    and a stochastic process; no equivalent or subclass mapping or neural-layer inheritance
    is asserted. No aliases adopted. UDNAM is a constant equal choice between complete
    upward and downward NAM kernels, with consistent independently selected valid
    tie policies. A mixture is not a single supplied-order NAM modification, sequential
    U-then-D composition or state-dependent component selection. The finite (4,3,2)/9
    two-positive-diagonal witness excludes every single NAM ordering. UNAM tie invariance
    and DNAM tie sensitivity are distinguished. Shared local reversible kernels or
    special cases with other samplers do not establish identity.
  search_scope: Canonical ID/name/alias/all-scoped-synonym checks and retained four
    complete-checkout searches include ignored and hidden files. Bounded corpus scope,
    not universal absence.
- evidence_id: mapping
  kind: record_content
  reference: research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json
  locator: mapping_context nodes, historical semantic/native contexts, actual317_neighbors
    and mapping_assessment
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: 67c0606e4e22d9ca2d473842632207842effb729628e0a61402e1f9e1f49818b
  support: supports
  summary: The related_match to AIO:MarkovChain is a method-to-process association.
    The pinned CLASS describes a stochastic process/model, with Network and ProbabilisticHiddenLayer
    context, rather than this finite conditional transition algorithm. Twenty-two
    exact class contexts support this association and twenty-one rejected alternatives.
    No equivalence, subclass membership or inherited neural assertion follows.
- evidence_id: actual-record-reading
  kind: record_content
  reference: data/curated/UpwardDownwardNestedAntitheticMixture.yaml
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: c7754a4aa39a4f1ce5703c13f225693604ab9cc760af3f45236b64137fc6e9e2
  support: supports
  summary: 'Personally reassessed every actual maintained field and all six claims.
    The specified complete NAM focal/tail updates and stopping rule agree with the
    retained derivation and fresh Eq19/28-34 reread. UDNAM is a fresh constant half
    mixture of completed U/D kernels, not a sequential product or current-label-dependent
    selector. Independent valid tie policies preserve each component balance; downward
    tie sensitivity and two-positive-diagonal nonrepresentation witness are explicit.
    Positive self mass and periodic/joint-scan examples prevent unwarranted convergence
    claims. The Neal-only primary attribution, FHY access gap and related MarkovChain
    mapping remain accurately scoped. Actual post-capture source reread: neal2024:
    Post-capture root native-text reread PDF pages [2, 3, 10, 15, 24, 28, 29, 49];
    relevant additional primary text and selected visuals remain in separately retained
    earlier root ledgers. No full84-page reading claimed.'
- evidence_id: neal2024
  kind: primary_source
  reference: https://glizen.com/radfordneal/ftp/gibbs-self.pdf
  locator: Section 8, PDF p. 28, explicit UDNAM equal-mixture definition; Section
    5, PDF p. 10, Equation 19; Section 6, pp. 14–17, Equations 28–34 and Algorithm
    2; Sections 7–8, pp. 22–29, upward/downward orders and Algorithms 3–4; Section
    8, PDF p. 28, equal random choice and averaged transition probabilities; Section
    2, pp. 2–3, distinction between mixtures and compositions; Sections 5–6, PDF pp.
    10 and 14–20, balance-preserving antithetic construction; Section 8, p. 28, mixture;
    Section 2, pp. 2–3, Equations 1–4 and composition; Section 7, PDF p. 24, Equation
    75 and tie invariance; Section 8, pp. 28–29, tie discussion and Figure 6(a); original
    exact tie comparison in research/discovery/mixture-boundaries.py; Section 6, PDF
    pp. 14–20, completed NAM diagonal structure; Section 8, pp. 28–30, mixture and
    ordering limits; Section 13, pp. 49–51, simple-target comparisons; original six-order
    calculation in research/discovery/mixture-boundaries.py; Section 5, PDF pp. 13–14
    and footnotes 7–8, scan boundaries; Section 8, p. 28, scoped efficiency discussion;
    Section 13, p. 49, uniform-target behavior; original scan checks in research/discovery/mixture-boundaries.py
  accessed_at: '2026-10-14T20:33:01Z'
  snapshot_sha256: 3d637d3eec046118a4c81d0d3824f387e1077d5ed8bd15d90a4db242c89d8bea
  support: supports
  summary: 'Author-hosted technical report dated 26 March 2024; 84 PDF pages. Independently
    pinned from arXiv:2403.18054v1; byte equivalence between versions is not asserted.
    Actual root reading: Reread the actual finite construction, mixture/order conventions
    and conditional/uniform-target boundaries against maintained claims. Earlier focal/tail
    derivations and visual assessments remain attributed; current reading does not
    expand to empirical or full proof certification.'
- evidence_id: calculation-tower
  kind: record_content
  reference: research/discovery/tower-boundaries.py
  locator: Saved report curator_calculations; scope, counts, orientation_example,
    reversible_nonhalf, arbitrary_shift_shortcut, closed_endpoint, point_mass
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: d8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47
  support: supports
  summary: 'Original bounded exact Fraction curator calculations; actual copied-script
    outputs checked against the full saved result. The mixture imports hash-pinned
    existing NAM and copied tower siblings without rerunning their main suites. No
    author-code execution, benchmark replication or universal proof. Selected results:
    {"scope": "Exact finite original curator calculations. Positive ordered integer
    vectors of lengths 1..5 with entries 1..3; duplicates after normalization retained.
    Shift sets include all cumulative-boundary differences, adjacent midpoints and
    policy/example shifts. Nonnegative extension and endpoint policies are counted
    separately. No floating implementation, author-code or benchmark execution.",
    "counts": {"formula_geometry_orientation_comparisons": 16626, "interior_shift_cases":
    8313, "maximum_first_2010_cases": 363, "policy_rows_checked": 3279, "positive_weight_vectors":
    363, "printed_alg7_integrated_rows": 38487, "printed_alg7_partition_cells": 70962,
    "reverse_paired_order_cases": 363, "scaling_cases": 8313, "uniform_integration_rows":
    38487, "uniform_partition_cells": 70962, "zero_current_rows_left_undefined": 1818,
    "zero_extension_shift_cases": 2016, "zero_extension_vectors": 336}, "orientation_example":
    {"half": [["0", "1/2", "1/4", "1/4"], ["2/3", "0", "0", "1/3"], ["1", "0", "0",
    "0"], ["1/2", "1/2", "0", "0"]], "negative": [["0", "1/4", "1/4", "1/2"], ["1",
    "0", "0", "0"], ["1", "0", "0", "0"], ["0", "1", "0", "0"]], "pi": ["2/5", "3/10",
    "1/10", "1/5"], "positive": [["0", "3/4", "1/4", "0"], ["1/3", "0", "0", "2/3"],
    ["1", "0", "0", "0"], ["1", "0", "0", "0"]], "shift": "2/5"}, "reversible_nonhalf":
    {"matrix": [["5/6", "1/6"], ["1/4", "3/4"]], "pi": ["3/5", "2/5"], "shift": "1/10"},
    "arbitrary_shift_shortcut": {"current_zero_based": 0, "geometry_row": ["5/6",
    "1/6"], "pi": ["3/5", "2/5"], "printed_alg6": ["1/3", "2/3"], "shift": "1/10"},
    "closed_endpoint": {"current_zero_based": 0, "exact_row": ["0", "0", "1"], "half_open_return_zero_based":
    2, "pi": ["1/5", "3/10", "1/2"], "printed_return_zero_based": 1, "r": "0", "shift":
    "1/2", "transition_probability": "0"}, "point_mass": {"interior": [["1"]], "maximum_endpoint_extension":
    [["1"]]}}'
- evidence_id: calculation-mixture
  kind: record_content
  reference: research/discovery/mixture-boundaries.py
  locator: Saved report curator_calculations; scope, dependency_sha256, expanded_counts,
    half_dominant_point_boundaries
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: 08aabec98558e43e20983518eb4b28c6ec6f383ad26e980a8e577612638e8125
  support: supports
  summary: 'Original bounded exact Fraction curator calculations; actual copied-script
    outputs checked against the full saved result. The mixture imports hash-pinned
    existing NAM and copied tower siblings without rerunning their main suites. No
    author-code execution, benchmark replication or universal proof. Selected results:
    {"scope": "Exact positive finite conditional kernels. Original source-agent witness
    output is retained without runtime metadata. Expanded tie, independent-component,
    all-shift and exploration checks use pinned unchanged sibling routines. No efficiency,
    float, author-code, all-target nonintersection or general convergence claim.",
    "dependency_sha256": {"nam-boundaries.py": "cb58dd0a41b32a7c4f12dcfc711963b39ff062b12f79d8fe6bf065b777714941",
    "tower-boundaries.py": "d8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47"},
    "expanded_counts": {"arbitrary_fixed_NAM_mixing_weight_cases": 600, "compatible_NAM_order_cases":
    771, "independent_UDNAM_tie_pairs": 3231, "one_state_UDST_endpoint_extensions":
    3, "paired_UDST_order_cases": 435, "positive_target_vectors": 120}, "half_dominant_point_boundaries":
    [{"UDNAM": [["1"]], "UDNAM_self_mass": "1", "UDST": [["1"]], "UDST_self_mass":
    "1", "minimum_self_mass": "1", "pi": ["1"], "weights": [1]}, {"UDNAM": [["0",
    "1"], ["1", "0"]], "UDNAM_self_mass": "0", "UDST": [["0", "1"], ["1", "0"]], "UDST_self_mass":
    "0", "minimum_self_mass": "0", "pi": ["1/2", "1/2"], "weights": [1, 1]}, {"UDNAM":
    [["3/20", "21/40", "13/40"], ["7/8", "0", "1/8"], ["13/16", "3/16", "0"]], "UDNAM_self_mass":
    "3/40", "UDST": [["0", "3/5", "2/5"], ["1", "0", "0"], ["1", "0", "0"]], "UDST_self_mass":
    "0", "minimum_self_mass": "0", "pi": ["1/2", "3/10", "1/5"], "weights": [5, 3,
    2]}, {"UDNAM": [["7/18", "17/36", "5/36"], ["17/18", "0", "1/18"], ["5/6", "1/6",
    "0"]], "UDNAM_self_mass": "7/30", "UDST": [["1/3", "1/2", "1/6"], ["1", "0", "0"],
    ["1", "0", "0"]], "UDST_self_mass": "1/5", "minimum_self_mass": "1/5", "pi": ["3/5",
    "3/10", "1/10"], "weights": [6, 3, 1]}, {"UDNAM": [["55/72", "17/144", "17/144"],
    ["17/18", "0", "1/18"], ["17/18", "1/18", "0"]], "UDNAM_self_mass": "11/18", "UDST":
    [["3/4", "1/8", "1/8"], ["1", "0", "0"], ["1", "0", "0"]], "UDST_self_mass": "3/5",
    "minimum_self_mass": "3/5", "pi": ["4/5", "1/10", "1/10"], "weights": [8, 1, 1]}]}'
- evidence_id: source-math-provenance
  kind: record_content
  reference: research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json
  locator: source_analysis.handoffs, root_readings and writer_preparation_reading
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: 67c0606e4e22d9ca2d473842632207842effb729628e0a61402e1f9e1f49818b
  support: supports
  summary: Root assessed the separately attributed selective source readings and bounded
    mathematical research. Supporting agents are in the same author workflow and provide
    no independent scientific approval.
- evidence_id: source-error-original-lineage
  kind: record_content
  reference: research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json
  locator: calculation_lineage.artifacts, curator_calculations and existing calculator
    dependency; source_analysis source caveats and raw/canonical access precision
  accessed_at: '2026-10-14T23:08:26.435425Z'
  snapshot_sha256: 67c0606e4e22d9ca2d473842632207842effb729628e0a61402e1f9e1f49818b
  support: supports
  summary: Original curator-written tower and mixture scripts, outputs, expanded counterparts
    and actual execution/comparison receipts preserve reproducible lineage. The unchanged
    existing NAM dependency is verified separately from the two copied scripts. Suwa/Neal
    orientation conventions, the printed arbitrary-shift shortcut, closed endpoint
    and caption/tie qualifications remain distinct from byte provenance and the tower
    wording clarification. No author-issued erratum or author-software execution is
    claimed.
assessments:
- assessment_id: identity
  area: identity
  topic: Upward-downward nested antithetic mixture
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - identity
  - neal2024
  summary: Retain the narrow DRAFT identity within the documented search scope.
  details: Neal p28 explicitly names UDNAM. Upward and downward policies belong to
    the existing NAM construction; their equal mixture has its own specified operation
    and a two-positive-diagonal witness outside all single NAM orderings on that target.
    It is not identified with ZDNAM, FSS/ZFSS, Liu correction, a shifted-tower mixture
    or a predictive model ensemble. No bare acronym or historical whole-framework
    alias is adopted.
- assessment_id: definition
  area: evidence
  topic: Definition and source scope
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - actual-record-reading
  summary: The maintained definition is supported within its stated method scope.
  details: The definition identifies an equal mixture of two complete NAM component
    kernels, with fresh state-independent component choice at each local update. This
    is distinct from a once-per-chain selection, sequential product or a single supplied-order
    NAM construction. The record cites only the byte-pinned Neal author report26March2024.
    Sections5–8 define complete NAM, the upward/downward policies, tie behavior and
    the explicit p28 equal-mixture construction; pp2–3 and49 give conditional and
    uniform examples. Earlier FHY original full text remains unobtained. Tjelmeland
    and companion proof readings remain separately scoped historical context, not
    a basis for unmaintained efficiency or priority claims.
- assessment_id: mapping
  area: grounding
  topic: Related Markov-process mapping
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - mapping
  - neal2024
  summary: related_match expresses method-to-process association without equivalence
    or ontology inheritance.
  details: 'The related_match to AIO:MarkovChain is a method-to-process association.
    The pinned CLASS describes a stochastic process/model, with Network and ProbabilisticHiddenLayer
    context, rather than this finite conditional transition algorithm. Twenty-two
    exact class contexts support this association and twenty-one rejected alternatives.
    No equivalence, subclass membership or inherited neural assertion follows.

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

    AIO:Preprocessing: These stochastic transitions update a sampled state; they do
    not preprocess a training dataset.

    AIO:Layer: Neural topology/component is a different abstraction.

    AIO:HiddenLayer: Nonlinear network transformation is not conditional Markov sampling.

    AIO:CausalGraphicalModel: Causal assumptions/graph model are not sampler identity
    or an entailed application.

    AIO:EnsembleLearning: A learning task combining prediction algorithms is not an
    equal mixture of target-preserving Markov kernels.

    AIO:RandomForest: A trained ensemble of decision trees is not a categorical conditional
    transition algorithm.

    AIO:MixtureofExpertsLLM: A language model combining expert submodels is not a
    fixed-probability mixture of stochastic kernels.

    AIO:FactorizedLLM: Factorized language-model components and product-of-experts
    synonyms do not identify this Markov update.'
- assessment_id: complete-upward-and-downward-components
  area: evidence
  topic: complete-upward-and-downward-components
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  summary: Supported within the stated assumptions and inspected passages.
  details: Neal Sections5–8, Eq19 and Algorithms2–4 define the full supplied-order
    construction and its ascending/descending policies. At each focal step the maximal
    change is r min(q/s,s/q); q>=s terminates the remaining block. The mixture uses
    the complete components, not one focal correction. One-state targets are identities.
    Original and existing NAM matrix/row implementations agree in771 compatible finite
    target/order cases.
- assessment_id: constant-half-mixture-selection
  area: evidence
  topic: constant-half-mixture-selection
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  summary: Supported within the stated assumptions and inspected passages.
  details: Neal p28 defines transition probabilities as(U+D)/2. A fresh fair component
    choice implements this matrix. The exact(4,3,2)/9 example distinguishes U then
    D from this average, and a current-state-dependent component selector fails invariance.
    These are bounded negative controls for excluded implementations, not a prohibition
    of every adaptive method under additional conditions.
- assessment_id: reversible-mixture-and-conditional-use
  area: evidence
  topic: reversible-mixture-and-conditional-use
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  summary: Supported within the stated assumptions and inspected passages.
  details: Both complete NAM components are pi-reversible; linearity of weighted flow
    yields stochasticity, invariance and detailed balance of the constant half mixture.
    Full-conditional use preserves the joint target. The calculator checks3231 independently
    valid ascending/descending tie-order pairs on120 ordered positive integer vectors,
    retaining normalized duplicates. A fixed full sweep need not inherit reversibility.
- assessment_id: downward-tie-policy
  area: evidence
  topic: downward-tie-policy
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  summary: Supported within the stated assumptions and inspected passages.
  details: Neal Eq75 p24 supports upward equal-probability invariance, while p28 and
    Figure6 p29 expose downward tie dependence. For(1,3,3,5)/12, two valid downward
    tie orders yield mixture diagonals(0,1/42,0,5/44) and(0,0,1/42,5/44). Independent
    valid component tie policies remain reversible; reverse pairing is not required
    for UDNAM.
- assessment_id: distinct-mixture-and-self-mass
  area: evidence
  topic: distinct-mixture-and-self-mass
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  summary: Supported within the stated assumptions and inspected passages.
  details: For(4,3,2)/9, UDNAM diagonal(5/56,1/30,0) contains two positive entries;
    every one of the six single NAM orders has only one. Stationary self mass16/315
    is positive although max pi<1/2, distinguishing minimum-self constructions on
    this target. This counterexample rejects whole-construction equivalence without
    claiming disjoint kernel sets or universal noncoincidence.
- assessment_id: invariance-is-not-convergence
  area: evidence
  topic: invariance-is-not-convergence
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  summary: Supported within the stated assumptions and inspected passages.
  details: Neal Section2 and Section13 distinguish valid updates from exploration
    properties. A uniform binary UDNAM update flips deterministically, with period2.
    Two such coordinate flips in a fixed full sweep leave two proper closed joint
    classes. The calculator derives the matrix and classes exactly; no mixing-rate,
    burn-in or efficiency conclusion follows.
- assessment_id: scope-and-boundaries
  area: consistency
  topic: Finite positive conditional kernels, complete component rules, order/tie/orientation
    qualifications and scan limits
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - neal2024
  - calculation-mixture
  - source-math-provenance
  summary: Mechanism, scan/parameter limits and identity boundaries remain qualified.
  details: Finite strictly positive normalized targets and complete component kernels
    are required. Component orders must be consistent across rows, but their tie choices
    need not be reverse-paired because both components are reversible. Mixture weights
    are a fresh constant half; arbitrary state-dependent choice is outside scope.
    Positive self mass is possible even below half maximum. Neither local reversibility
    nor invariance establishes aperiodicity, joint exploration or reversible full
    scans. No universal efficiency, infinite-state or floating implementation claim
    is maintained.
- assessment_id: actual-maintained-fields
  area: provenance
  topic: All captured maintained fields
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - actual-record-reading
  - identity
  - mapping
  - neal2024
  summary: Root reassessed the complete current record after canonical capture; DRAFT
    remains.
  details: 'Personally reassessed every actual maintained field and all six claims.
    The specified complete NAM focal/tail updates and stopping rule agree with the
    retained derivation and fresh Eq19/28-34 reread. UDNAM is a fresh constant half
    mixture of completed U/D kernels, not a sequential product or current-label-dependent
    selector. Independent valid tie policies preserve each component balance; downward
    tie sensitivity and two-positive-diagonal nonrepresentation witness are explicit.
    Positive self mass and periodic/joint-scan examples prevent unwarranted convergence
    claims. The Neal-only primary attribution, FHY access gap and related MarkovChain
    mapping remain accurately scoped. Rereads: neal2024: Post-capture root native-text
    reread PDF pages [2, 3, 10, 15, 24, 28, 29, 49]; relevant additional primary text
    and selected visuals remain in separately retained earlier root ledgers. No full84-page
    reading claimed.'
- assessment_id: source-error-and-original-lineage
  area: provenance
  topic: Source caveats and original calculation history
  outcome: supported
  target_ids:
  - AIMech:UpwardDownwardNestedAntitheticMixture
  evidence_ids:
  - source-error-original-lineage
  summary: Source interpretation, wording clarification and original-to-expanded calculation
    lineage remain distinct.
  details: The original curator-written tower and mixture checks and their expanded
    calculations retain exact code, outputs and execution/comparison receipts. Raw
    download precision is retained beside schema-compatible source timestamps. Named
    source caveats do not imply a defective maintained record or an author-issued
    erratum; finite exact checks do not certify floating implementations or general
    convergence.
findings: []
actions: []
limitations:
- Author self-review, not independent scientific approval or DRAFT promotion.
- Finite strictly positive normalized targets and complete component kernels are required.
  Component orders must be consistent across rows, but their tie choices need not
  be reverse-paired because both components are reversible. Mixture weights are a
  fresh constant half; arbitrary state-dependent choice is outside scope. Positive
  self mass is possible even below half maximum. Neither local reversibility nor invariance
  establishes aperiodicity, joint exploration or reversible full scans. No universal
  efficiency, infinite-state or floating implementation claim is maintained.
- The Fraction calculators are original curator-written bounded checks, not author
  software, empirical replication or universal proofs. Repeated normalized targets
  and policy/order choices are counted explicitly.
- Source, identity and mathematical agents belong to the same author workflow. This
  is qualified author self-review, not independent scientific approval.
- Historical 706-native research is attributed separately. Actual prewrite 710-native
  identity refresh, all scoped synonyms, four complete ignored-inclusive searches
  and actual FSS/ZFSS/NAM/ZDNAM neighbor assessments govern the addition.
- Two copied calculators retain their exact original-to-expanded provenance. The mixture
  calculator uses the unchanged, hash-pinned existing NAM sibling and copied tower
  sibling; this does not rerun the entire earlier NAM suite.
- Raw source download precision and whole-second UTC source timestamps are both preserved;
  download times are not scientific reading times.
notes:
- Empty findings reflect actual root assessment of this selected captured record only;
  no unrelated finding closure or literature saturation is asserted.
- Source caveats and preserved calculation or wording lineage remain distinct; no
  maintained-record finding or issue closure is invented from them.
tags:
- native-concepts
- self-review
- discovery-ongoing
- mcmc
```
