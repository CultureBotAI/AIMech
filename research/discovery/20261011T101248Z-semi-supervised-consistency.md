# Semi-supervised consistency — 2026-10-11T10:12:48Z

Added four native DRAFT concepts; the maintained collection now contains 234 records.

| Record | Target construction |
| --- | --- |
| [AIMech:PiModel](../../data/curated/PiModel.yaml) | Two current predictions; gradients through both branches. |
| [AIMech:TemporalEnsembling](../../data/curated/TemporalEnsembling.yaml) | Stored, bias-corrected averages of earlier per-example predictions. |
| [AIMech:MeanTeacher](../../data/curated/MeanTeacher.yaml) | A stopped-gradient teacher updated by averaging student weights. |
| [AIMech:MixMatch](../../data/curated/MixMatch.yaml) | Averaged and sharpened guessed labels followed by input/target interpolation. |

Primary method pages and the Mean Teacher supplement establish the branch-gradient and target-update boundaries. Explicit AIO mappings are related algorithm-to-task associations.

[Review issue #58](https://github.com/CultureBotAI/AIMech/issues/58) records the reproduced Π-model/Model false collision. The fix preserves Unicode letters and combining marks, with regression coverage for real collisions and invalid symbol-only names. Existing identity keys remain unchanged in a 1,348-string audit.

The JSON ledger preserves source hashes, actual reading scope, the issue reproduction and fix, all inherited candidates, and new MixUp/ReMixMatch/consistency leads. Discovery remains active.
