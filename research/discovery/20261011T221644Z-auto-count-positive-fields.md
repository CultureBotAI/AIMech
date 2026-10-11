# Auto-binomial, auto-Poisson and auto-exponential fields — 2026-10-11T22:16:44Z

Added three native DRAFT concepts, bringing the maintained collection to 406.

| Record | Definition |
| --- | --- |
| [AIMech:AutoBinomialMarkovRandomField](../../data/curated/AutoBinomialMarkovRandomField.yaml) | A finite pairwise Markov-field model for bounded site counts whose full conditionals are binomial with fixed trial counts and log odds linear in neighboring counts, using symmetric interaction coefficients. |
| [AIMech:AutoPoissonMarkovRandomField](../../data/curated/AutoPoissonMarkovRandomField.yaml) | A finite pairwise Markov-field model for unbounded nonnegative integer counts whose full conditionals are Poisson with log means linear in neighboring counts and whose symmetric interaction coefficients are nonpositive. |
| [AIMech:AutoExponentialMarkovRandomField](../../data/curated/AutoExponentialMarkovRandomField.yaml) | A finite pairwise Markov-field model for nonnegative continuous site values with exponential full conditionals whose rates are positive baseline terms plus nonnegative symmetric linear neighbor interactions. |

The [original finite checks](auto-count-positive-boundaries.py) examine binomial base measures, compatible conditional laws, Poisson support and summability, and exponential rate signs. The primary PDF was reused with its verified checksum after prior complete visual reading; seven pages were freshly reread. Five newer abstracts supply explicitly provisional context and research leads.

The ledger records ignored-inclusive identity searches, directional AIO mappings, evidence scope and access limitations. Adversarial author self-review is required. Discovery remains active with 237 pending inspection leads and carried unresolved dispositions.
