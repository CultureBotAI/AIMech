# Stochastic connection, block and state masks — 2026-10-11T12:35:01Z

Added three native DRAFT concepts, bringing the maintained collection to 279.

| Record | Defining procedure |
| --- | --- |
| [AIMech:DropConnect](../../data/curated/DropConnect.yaml) | A stochastic neural-network layer that masks individual weights and biases during training, so each example is processed through a randomly selected subset of the layer’s connections. |
| [AIMech:StochasticDepth](../../data/curated/StochasticDepth.yaml) | A residual-network training procedure that randomly bypasses residual transformations during training and uses all residual transformations with survival-probability scaling during inference. |
| [AIMech:Zoneout](../../data/curated/Zoneout.yaml) | A recurrent-network regularization procedure that randomly preserves selected state components at their previous values instead of applying their proposed updates during training. |

The records distinguish weight/bias masking, residual-block survival and recurrent state preservation. Source-specific mask conventions, inference approximations and architecture boundaries remain explicit.

Each concept carries inspected AIO mappings. The [finite calculation](stochastic-regularization-boundaries.py) illustrates the recorded boundaries. The JSON ledger preserves primary sources, source versions, reading scopes, ignored-inclusive identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
