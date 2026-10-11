# Spatial transformers and non-local attention — 2026-10-11T12:54:15Z

Added three native DRAFT concepts, bringing the maintained collection to 285.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:SpatialTransformer](../../data/curated/SpatialTransformer.yaml) | A learnable neural-network component that predicts an input-dependent spatial transformation and uses the resulting sampling grid to warp an image or feature tensor. |
| [AIMech:ResidualAttentionNetwork](../../data/curated/ResidualAttentionNetwork.yaml) | A convolutional-network architecture that stacks attention modules combining trunk features with learned bottom-up and top-down masks through residual attention gating. |
| [AIMech:NonLocalBlock](../../data/curated/NonLocalBlock.yaml) | A neural-network component that aggregates input-dependent pairwise contributions from positions across a representation, projects the aggregate and adds it to the original features through a residual connection. |

The records distinguish geometric resampling, stacked multiscale residual attention and global pairwise feature aggregation. Input/feature alignment limits, residual conventions and normalized versus signed weights remain explicit.

Each concept carries inspected AIO mappings. The [finite calculation](spatial-and-nonlocal-boundaries.py) illustrates the recorded boundaries. The JSON ledger preserves primary sources, source versions, reading scopes, ignored-inclusive identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
