# Point and set architectures — 2026-10-11T04:19:44Z

Added five supported architectures, bringing the native collection to 82 DRAFT concepts.

| Record | Distinction |
| --- | --- |
| [AIMech:PointNet](../../data/curated/PointNet.yaml) | This is the original PointNet architecture, including its classification and segmentation paths. It is distinct from PointNet++'s hierarchical local grouping and from a generic set-pooling model. |
| [AIMech:SetTransformer](../../data/curated/SetTransformer.yaml) | The Set Transformer is a set-input architecture, not the AIO Transformer Language Model class, an individual multihead attention layer, or the later Set Transformer++ encoder revision. |
| [AIMech:PointNetPlusPlus](../../data/curated/PointNetPlusPlus.yaml) | PointNet++ adds hierarchical local set abstraction to PointNet. Multi-scale and multi-resolution grouping are distinct variants within this architecture; the paper also evaluates a single-scale ablation. |
| [AIMech:DeepSetsPlusPlus](../../data/curated/DeepSetsPlusPlus.yaml) | Deep Sets++ is the encoder revision defined by Zhang and colleagues, not an alternate spelling of Deep Sets or a claim that every deeper set network uses this construction. |
| [AIMech:SetTransformerPlusPlus](../../data/curated/SetTransformerPlusPlus.yaml) | Set Transformer++ denotes the specific encoder revision and ISAB++ construction in Zhang and colleagues. It is distinct from the original Set Transformer and from Deep Sets++ despite their shared residual and normalization design principles. |

Fixed the identity normalizer so meaningful plus suffixes survive, retaining duplicate protections and rejecting symbol-only names. The reproduced defect is tracked in [issue #13](https://github.com/CultureBotAI/AIMech/issues/13), with an immutable initial review and a successor disposition after checks.

Primary method text and rendered equations/diagrams were inspected; searches included ignored and hidden files. The JSON companion records variant distinctions, source limitations, the code/paper baseline caveat and pending methods. Discovery remains active.
