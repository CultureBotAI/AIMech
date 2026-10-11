# Optimizer discovery — 2026-10-11T03:26:15Z

Added twelve evidence-backed native concepts after resolving identities against 442 AIO and 44 existing native records. The maintained collection now contains 56 records. All new records remain DRAFT.

Official PyTorch 2.9 documentation HTML downloads returned HTTP 403. The public documentation source link identified v2.9.1; inspected source files are pinned to commit `d38164a545b4a4e4e0cf73ce67173f70574890b6`. This fallback supplies method documentation, not experimental proof.

| Concept | Inspected mechanism |
| --- | --- |
| [AIMech:AdamW](../../data/curated/AdamW.yaml) | Parameters receive a weight-decay shrinkage step, while first and second gradient moments are updated from the objective gradient and used for the adaptive step. |
| [AIMech:Adagrad](../../data/curated/Adagrad.yaml) | The diagonal variant accumulates squared gradients over iterations and divides the current gradient by the square root of that accumulator plus a numerical stabilizer. |
| [AIMech:RMSprop](../../data/curated/RMSprop.yaml) | An exponential moving average of squared gradients supplies the update denominator; the documented centered option subtracts a squared mean-gradient estimate, and momentum is optional. |
| [AIMech:Adadelta](../../data/curated/Adadelta.yaml) | The update multiplies the gradient by the stabilized root-mean-square of prior updates divided by the stabilized root-mean-square of current gradient history, then updates the squared-update average. |
| [AIMech:Adafactor](../../data/curated/Adafactor.yaml) | For matrix parameters, row and column statistics reconstruct a factored second-moment estimate used to normalize gradients; the inspected implementation also clips update RMS and scales steps using parameter RMS. |
| [AIMech:AdaMax](../../data/curated/AdaMax.yaml) | The first-moment estimate is bias-corrected, while the denominator takes the coordinatewise maximum of the decayed prior scale and the current absolute gradient with the implementation's stabilizer. |
| [AIMech:NAdam](../../data/curated/NAdam.yaml) | The documented update combines a scheduled, bias-adjusted first-moment term with a current-gradient term and divides the combination by a stabilized, bias-corrected second-moment scale. |
| [AIMech:RAdam](../../data/curated/RAdam.yaml) | The cited implementation computes a rectification term when its effective-history statistic exceeds five; before that threshold it takes a bias-corrected first-moment step without adaptive second-moment scaling. |
| [AIMech:AveragedStochasticGradientDescent](../../data/curated/AveragedStochasticGradientDescent.yaml) | The inspected implementation updates the current parameters by a scheduled gradient step and maintains an auxiliary parameter average, with averaging weights controlled by the iteration count and a configurable starting point. |
| [AIMech:LBFGS](../../data/curated/LBFGS.yaml) | The implementation retains a bounded set of curvature pairs and applies a two-loop recursion to obtain a direction from the gradient without storing a dense inverse Hessian. |
| [AIMech:ResilientBackpropagation](../../data/curated/ResilientBackpropagation.yaml) | Repeated gradient signs increase a coordinate's bounded step size, while a sign reversal decreases it; in the cited variant the reversal also suppresses that coordinate's current update. |
| [AIMech:Muon](../../data/curated/Muon.yaml) | The inspected implementation forms a momentum update, optionally uses a Nesterov combination, applies iterative matrix orthogonalization, and scales the resulting update for the parameter shape while applying decoupled weight decay. |

Searches included ignored and hidden files in both checkouts. Matching mentions were previous discovery leads and related-method notes. The AIO mapping is related to TrainingStrategy because its pinned preprocessing definition does not establish an optimizer superclass.

The JSON companion retains source hashes, exact method locators, queries, failed requests and identity-search results. No full third-party source or paper text is redistributed.

The frontier remains nonempty: AMSGrad, A-star and STRIPS need full-method assessment; additional generative-method search results and predecessor leads remain accounted for in the ledgers. Finding twelve additions does not establish saturation.
