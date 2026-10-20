# Discovery Report: Round 534 — Kardam Lipschitz- and Frequency-Filtered Asynchronous Byzantine Stochastic Gradient Descent

- **Timestamp**: `2026-10-19T10:17:00Z`
- **Selected Concept**: `AIMech:KardamLipschitzAndFrequencyFilteredAsynchronousByzantineStochasticGradientDescent` (*Kardam Lipschitz- and Frequency-Filtered Asynchronous Byzantine Stochastic Gradient Descent*)
- **Record Path**: `data/curated/KardamLipschitzAndFrequencyFilteredAsynchronousByzantineStochasticGradientDescent.yaml`
- **Primary Source**: Georgios Damaskinos, El Mahdi El Mhamdi, Rachid Guerraoui, Rhicheek Patra, Mahsa Taziki — *Asynchronous Byzantine Machine Learning (the case of SGD)* (`https://dblp.org/rec/conf/icml/DamaskinosMGPT18.xml`).

## Identity & Boundary Resolution

Distinct from Zeno++ (AIMech:ZenoPlusPlusRobustFullyAsynchronousStochasticGradientDescent, which scores candidate asynchronous updates using a server validation mini-batch loss descent test without worker frequency bounds or empirical Lipschitz quantiles) and from synchronous Byzantine aggregators such as Krum (AIMech:KrumAndMultiKrumByzantineResilientGradientAggregation), Bulyan (AIMech:BulyanTwoStageMetaAggregationForByzantineResilientDistributedLearning), and Geometric Median / RFA (AIMech:RobustFederatedAggregationViaSmoothedWeiszfeldGeometricMedian). Kardam (Damaskinos et al., ICML 2018, PMLR 80:1153-1162, Section 3.1-3.2, Definitions 3-5, pp. 3-6) comprises two coupled components on the parameter server: (1) the Dampening component scales any accepted gradient g_{tl} computed on stale model x_l (with staleness tau_{tl} = t - l) by a strictly decreasing bijective staleness decay function Lambda(tau_{tl}) satisfying Lambda(0) = 1 (such as exponential dampening Lambda(tau) = exp(-alpha * tau^(1/beta))) with adaptive step size gamma_t = gamma * M / sum_{lambda in Lambda_t} lambda |G_{t,lambda}|; and (2) the Filtering component accepts a candidate gradient g_p from worker p only if it simultaneously passes the Frequency Filter—which maintains the list L of workers for the last 2f accepted gradients and rejects worker q if the top-f most frequent workers in (L; q) appear more than f times in total (Definition 4, Lemma 1)—and the Empirical Lipschitz Filter—which checks whether the server-side empirical Lipschitz ratio hat{K}_t^p = ||g_p - g_q||_2 / ||x_t - x_{t-1}||_2 is at most the (n-f)/n quantile hat{K}_t of all workers' local empirical Lipschitz coefficients hat{K}_p = ||g_p - g_p^{prev}||_2 / ||x_{l_p} - x_{l_p}^{prev}||_2 (Definition 5).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 534 Kardam verified: SL_bounds=[0.600, 0.714], K_hat_t=1.85, k_t_honest=1.48 <= K_hat_t < k_t_byz=389.1, final_err=0.000000
```
