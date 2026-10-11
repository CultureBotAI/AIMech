# Channel and spatial feature gating — 2026-10-11T12:43:35Z

Added three native DRAFT concepts, bringing the maintained collection to 282.

| Record | Defining component |
| --- | --- |
| [AIMech:SqueezeAndExcitationBlock](../../data/curated/SqueezeAndExcitationBlock.yaml) | A neural-network feature recalibration component that globally averages each channel, transforms the resulting descriptor through a learned bottleneck, and applies sigmoid-derived channel weights to the input feature maps. |
| [AIMech:ConvolutionalBlockAttentionModule](../../data/curated/ConvolutionalBlockAttentionModule.yaml) | A convolutional feature refinement component that sequentially applies learned channel attention and then spatial attention to an intermediate feature tensor. |
| [AIMech:BottleneckAttentionModule](../../data/curated/BottleneckAttentionModule.yaml) | A convolutional feature refinement component that combines parallel channel and spatial attention branches and adds the resulting gated features back to its input, originally proposed for network downsampling bottlenecks. |

The records distinguish channel-only recalibration, sequential channel/spatial gates and parallel residual attention. Paper/code fusion differences, bounded gates, acronym scope and architecture boundaries remain explicit.

Each concept carries inspected AIO mappings. The [finite calculation](channel-spatial-gating-boundaries.py) illustrates the recorded boundaries. The JSON ledger preserves primary sources, source versions, reading scopes, ignored-inclusive identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
