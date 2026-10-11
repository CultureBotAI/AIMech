# Conditional and recurrent output architectures — 2026-10-11T18:54:23Z

Added three native DRAFT records, bringing the maintained collection to 367.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:RecurrentNeuralNetworkRestrictedBoltzmannMachine](../../data/curated/RecurrentNeuralNetworkRestrictedBoltzmannMachine.yaml) | A neural sequence architecture in which a deterministic recurrent network with its own hidden state supplies parameters of a conditional RBM that models each next visible vector. |
| [AIMech:RecurrentNeuralNetworkNeuralAutoregressiveDistributionEstimator](../../data/curated/RecurrentNeuralNetworkNeuralAutoregressiveDistributionEstimator.yaml) | A neural sequence architecture in which a deterministic recurrent state supplies parameters of a NADE output distribution, combining temporal recurrence with normalized within-frame autoregressive conditionals. |
| [AIMech:ConditionalRestrictedBoltzmannMachine](../../data/curated/ConditionalRestrictedBoltzmannMachine.yaml) | A conditional neural probability model that represents an output vector with an RBM whose biases or interactions are determined by a supplied conditioning vector. |

RNN-RBM and RNN-NADE broadly map to RecurrentNeuralNetwork; the fully visible RNN-NADE factorization also maps broadly to BayesianNetwork. Generic CRBM broadly maps to ArtificialNeuralNetwork. Conditional RBM relationships are explicitly related mappings, with recurrent, generic and autoregressive identities kept distinct.

The [finite examples](conditional-sequence-boundaries.py) and JSON ledger document actual source reading, identity and mapping checks, source sign and transpose qualifications, conditional normalization and exact versus approximate gradient conventions, and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 200 pending inspection leads.
