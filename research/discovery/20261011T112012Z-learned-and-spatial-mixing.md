# Learned and spatial mixing — 2026-10-11T11:20:12Z

Added three native DRAFT concepts, bringing the maintained collection to 256.

| Record | Defining procedure |
| --- | --- |
| [AIMech:SmartAugmentation](../../data/curated/SmartAugmentation.yaml) | A learned augmentation procedure that trains a network to synthesize examples from same-class inputs while receiving both a within-class reference loss and feedback through the target classifier’s training loss. |
| [AIMech:SamplePairing](../../data/curated/SamplePairing.yaml) | An image-classification augmentation procedure that averages an anchor image with a randomly selected training image using equal pixel weights and trains against the anchor image’s label, with a training schedule that includes phases without pairing. |
| [AIMech:CutMix](../../data/curated/CutMix.yaml) | A training augmentation procedure that replaces a rectangular region of one image with the corresponding region of another and mixes their class targets in proportion to the retained and pasted image areas. |

The records distinguish learned same-class synthesis, equal averaging with an anchor target, and patch replacement with area-weighted targets. Source qualifications preserve SamplePairing’s expected-loss relationship to half-weight target mixing and CutMix’s recomputation of target weights after integer clipping.

An [original finite calculation](example-mixing-boundaries.py) checks these boundaries and the limits of a reference MSE objective. The JSON ledger records exact source versions, actual reading scopes, ignored-inclusive identity searches, mappings and remaining leads.

Review is adversarial author self-review. Discovery remains active.
