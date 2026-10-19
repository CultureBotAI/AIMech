# Discovery Report: Round 389 — DIANA Distributed Learning with Compressed Gradient Differences

- **Timestamp**: `2026-10-19T07:52:00Z`
- **Selected Concept**: `AIMech:DianaDistributedLearningWithCompressedGradientDifferences` (*DIANA Distributed Learning with Compressed Gradient Differences*)
- **Record Path**: `data/curated/DianaDistributedLearningWithCompressedGradientDifferences.yaml`
- **Primary Source**: Konstantin Mishchenko, Eduard Gorbunov, Martin Takáč, Peter Richtárik — *Distributed Learning with Compressed Gradient Differences* (`https://doi.org/10.48550/arXiv.1901.09269`).

## Identity & Boundary Resolution

Distinct from QSGD (AIMech:QsgdCommunicationEfficientStochasticGradientQuantization, which quantizes raw gradients g_i^k directly without memory shifts h_i^k and therefore suffers non-vanishing quantization variance at x^* whenever nabla f_i(x^*) != 0, recovered as the special case alpha = 0, h_i^0 = 0, p = 2 of DIANA), from EF21 (AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization, which uses biased contractive compressors on deterministic gradients with error state g_i^{t+1} = g_i^t + C(nabla f_i(x^{t+1}) - g_i^t) rather than unbiased l_p quantization with damping step size alpha <= alpha_p and proximal composite support R(x)), and from Sparsified SGD with Error Memory (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression). No pinned AIO class covers DIANA or compressed gradient-difference shift learning.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 389 DIANA (Mishchenko et al. 2019): alpha_inf(9)=0.5000, diana_x_err=4.53e-31, diana_h_err=4.23e-31 << terngrad_err=6.3809e-02
```
