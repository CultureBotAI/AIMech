# Reinforcement-learning discovery — 2026-10-11T03:45:28Z

Added TRPO, generalized advantage estimation, DDPG and the 2015 DQN learning procedure. All four have inspected full primary method descriptions, exact source versions/hashes and selected rendered-page checks. The native collection now contains 64 DRAFT records.

| Record | Scope retained |
| --- | --- |
| [AIMech:TrustRegionPolicyOptimization](../../data/curated/TrustRegionPolicyOptimization.yaml) | TRPO's constrained policy update differs from PPO's clipped surrogate or adaptive penalty variants. It is an optimization procedure, not a trained policy instance. |
| [AIMech:GeneralizedAdvantageEstimation](../../data/curated/GeneralizedAdvantageEstimation.yaml) | GAE estimates advantages used in a policy-gradient update; it is not itself a complete policy optimizer and is distinct from estimating the value function with TD(lambda). |
| [AIMech:DeepDeterministicPolicyGradient](../../data/curated/DeepDeterministicPolicyGradient.yaml) | DDPG combines deterministic policy gradients with deep actor/critic approximators, replay and target networks. It is distinct from stochastic maximum-entropy SAC and discrete-action DQN. |
| [AIMech:DeepQNetwork](../../data/curated/DeepQNetwork.yaml) | This record denotes the 2015 DQN learning procedure, not any arbitrary neural Q-function, one Atari checkpoint, or later Double DQN/Rainbow variants. |

Ignored and hidden files were included in identity searches. Related AIO mappings connect methods to the reinforcement-learning task without equating those abstraction levels.

The review distinguishes practical TRPO approximations from theoretical improvement guarantees, GAE from a complete policy optimizer, continuous deterministic DDPG from discrete-action DQN, and benchmark claims from general competence.

Additional method/component and learned-algorithm leads remain on the frontier. The JSON companion records queries, abstract interpretation, source hashes, method locators, visual inspection and pending dispositions. Discovery has not saturated.
