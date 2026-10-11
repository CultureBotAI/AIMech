# Discrepancy search and beam decoding — 2026-10-11T06:29:48Z

Added five concepts; the native collection now has 146 DRAFT records.

| Record | AIO assessment |
| --- | --- |
| [AIMech:LimitedDiscrepancySearch](../../data/curated/LimitedDiscrepancySearch.yaml) | No suitable match in the inspected pin |
| [AIMech:ImprovedLimitedDiscrepancySearch](../../data/curated/ImprovedLimitedDiscrepancySearch.yaml) | No suitable match in the inspected pin |
| [AIMech:FCFSBeamDecoding](../../data/curated/FCFSBeamDecoding.yaml) | Related to Natural Language Processing |
| [AIMech:PatienceControlledBeamDecoding](../../data/curated/PatienceControlledBeamDecoding.yaml) | Related to Natural Language Processing |
| [AIMech:VanillaSequenceBeamDecoding](../../data/curated/VanillaSequenceBeamDecoding.yaml) | Related to Natural Language Processing |

LDS and ILDS differ in discrepancy accounting and repeated maximum-depth paths. The three decoders differ in whether completed outputs occupy beam slots, accumulate separately, or trigger a configurable stopping threshold.

Depth-bounded discrepancy search remains deferred. A portable [curator illustration](../../research/validation/20261011T062948Z-dds-driver-counterexample.py) and [actual result](../../research/validation/20261011T062948Z-dds-driver-counterexample.json) show the printed driver stopping before finding an existing goal on one unbalanced tree. The successful variant is not an author-approved correction or a general proof.

The JSON companion preserves exact reading scopes, identity searches, source caveats, mapping assessments and pending leads. Discovery continues.
