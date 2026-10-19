# Discovery Report: Round 415 — Natural Compression and Natural Dithering for Distributed Optimization

- **Timestamp**: `2026-10-19T08:18:00Z`
- **Selected Concept**: `AIMech:NaturalCompressionAndNaturalDitheringForDistributedOptimization` (*Natural Compression and Natural Dithering for Distributed Optimization*)
- **Record Path**: `data/curated/NaturalCompressionAndNaturalDitheringForDistributedOptimization.yaml`
- **Primary Source**: Samuel Horváth, Chen-Yu Ho, Ľudovít Horváth, Atal Narayan Sahu, Marco Canini, Peter Richtárik — *Natural Compression for Distributed Deep Learning* (`https://doi.org/10.1007/s12532-022-00221-9`).

## Identity & Boundary Resolution

Distinct from QSGD / Standard Random Dithering D_sta^{p,s} (AIMech:QSGDQuantizedStochasticGradientDescent, Alistarh et al. 2017, which uses uniformly spaced linear levels {0, 1/s, 2/s, ..., 1} rather than geometric power-of-two levels {2^{1-s}, ..., 1} and requires float multiplication rather than integer bit-shift addition), from TernGrad (AIMech:TernGradTernaryGradientsForDistributedDeepLearning, which uses a single l_infinity ternary level), and from biased Top-k / SignSGD compressors requiring error-feedback memory.

## Constructed Boundary & Regime Verification

```text
[PASS] Natural Compression boundaries verified: omega(C_nat)=0.125000 (1/8), omega(C_nat o S^q)=3.5000, var_nat=0.00785 < var_sta=0.03689
```
