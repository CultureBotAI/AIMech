# Minority synthesis and feature masks — 2026-10-11T12:27:02Z

Added three native DRAFT concepts, bringing the maintained collection to 276.

| Record | Defining procedure |
| --- | --- |
| [AIMech:SyntheticMinorityOversamplingTechnique](../../data/curated/SyntheticMinorityOversamplingTechnique.yaml) | A minority-class oversampling method that generates synthetic labeled feature vectors by interpolating between an observed minority example and selected neighbors from the same class. |
| [AIMech:DropBlock](../../data/curated/DropBlock.yaml) | A training-time feature-map transformation for convolutional networks that suppresses randomly placed contiguous spatial blocks of activations and rescales retained activations. |
| [AIMech:AttentionBasedDropoutLayer](../../data/curated/AttentionBasedDropoutLayer.yaml) | A training-time convolutional feature-map layer that stochastically applies either a thresholded spatial drop mask or sigmoid importance weights derived from channel-averaged activations, developed for weakly supervised object localization. |

The records distinguish within-class feature synthesis, random contiguous activation suppression and activation-dependent spatial gating. SMOTE interpolation conventions, DropBlock mask polarity/normalization and ADL threshold/background limits are explicit.

Each concept carries inspected AIO mappings. The [finite calculation](augmentation-mask-boundaries.py) illustrates the recorded boundaries. The JSON ledger preserves primary sources, static-code provenance, reading scopes, ignored-inclusive identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
