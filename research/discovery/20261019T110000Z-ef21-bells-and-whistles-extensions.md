# Discovery Report: Round 577 — EF21 Algorithmic Extensions (EF21-SGD, EF21-PAGE, EF21-PP, EF21-BC, EF21-HB, EF21-Prox)

- **Timestamp**: `2026-10-19T11:00:00Z`
- **Selected Concept**: `AIMech:Ef21ExtensionsStochasticVarianceReducedPartialParticipationBidirectionalAndProximalErrorFeedback` (*EF21 Algorithmic Extensions (EF21-SGD, EF21-PAGE, EF21-PP, EF21-BC, EF21-HB, EF21-Prox)*)
- **Record Path**: `data/curated/Ef21ExtensionsStochasticVarianceReducedPartialParticipationBidirectionalAndProximalErrorFeedback.yaml`
- **Primary Source**: Ilyas Fatkhullin, Igor Sokolov, Eduard Gorbunov, Zhize Li, Peter Richtarik — *EF21 with Bells & Whistles: Practical Algorithmic Extensions of Modern Error Feedback* (`https://dblp.org/search/publ/api?q=EF21+with+Bells+Whistles&format=json`).

## Identity & Boundary Resolution

Distinct from baseline EF21 (which requires full-batch local gradients, full client participation, uncompressed server broadcasts, no momentum, and smooth unconstrained objectives) and from EF-BV (which decomposes compressors into bias and variance parameters using an auxiliary scaling lambda). The EF21 extensions directly generalize the Markov compression recursion g_i^{t+1} = g_i^t + C_i^t(u_i^{t+1} - g_i^t) across six orthogonal operational axes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 577 EF21-Bells-Whistles verified: gn_page=5.093e-32 << gn_sgd=1.136e-01, gn_bc=2.126e-31, grad_map_prox=4.702e-34
```
