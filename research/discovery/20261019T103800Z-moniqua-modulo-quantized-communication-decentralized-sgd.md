# Discovery Report: Round 555 — Moniqua Modulo Quantized Communication for Decentralized SGD

- **Timestamp**: `2026-10-19T10:38:00Z`
- **Selected Concept**: `AIMech:MoniquaModuloQuantizedCommunicationForDecentralizedSgd` (*Moniqua Modulo Quantized Communication for Decentralized SGD*)
- **Record Path**: `data/curated/MoniquaModuloQuantizedCommunicationForDecentralizedSgd.yaml`
- **Primary Source**: Yucheng Lu, Christopher De Sa — *Moniqua: Modulo Quantized Communication in Decentralized SGD* (`https://dblp.org/rec/conf/icml/LuS20`).

## Identity & Boundary Resolution

Introduced by Yucheng Lu and Christopher De Sa (ICML 2020, PMLR Vol. 119, pp. 6415-6425; arXiv:2002.11787). Distinct from Choco-SGD (Koloskova et al., ICML 2019) and DCD/ECD-PSGD (Tang et al., NeurIPS 2018), which maintain neighbor model replicas incurring Theta(m * d) additional memory overhead; and distinct from DeepSqueeze / DoubleSqueeze (Tang et al., 2019), which maintain error-compensation buffers incurring Theta(n * d) memory overhead rather than memoryless modular-arithmetic residue quantization.

## Constructed Boundary & Regime Verification

```text
[PASS] Moniqua boundaries verified: Lemma 1&2 exact, err_moniqua=0.0019 << err_naive=0.2372
```
