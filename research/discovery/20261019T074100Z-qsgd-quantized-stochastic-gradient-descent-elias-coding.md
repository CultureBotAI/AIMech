# Discovery Report: Round 378 — QSGD (Quantized Stochastic Gradient Descent) with Elias Coding

- **Timestamp**: `2026-10-19T07:41:00Z`
- **Selected Concept**: `AIMech:QsgdQuantizedStochasticGradientDescentWithEliasCoding` (*QSGD (Quantized Stochastic Gradient Descent) with Elias Coding*)
- **Record Path**: `data/curated/QsgdQuantizedStochasticGradientDescentWithEliasCoding.yaml`
- **Primary Source**: Dan Alistarh, Demjan Grubic, Jerry Li, Ryota Tomioka, Milan Vojnovic — *QSGD: Communication-Efficient SGD via Gradient Quantization and Encoding* (`https://papers.nips.cc/paper/2017/hash/6c340f25839e6acdc73414517203f5f0-Abstract.html`).

## Identity & Boundary Resolution

Distinct from biased 1-bit sign compression signSGD (Bernstein et al. 2018, AIMech:SignSgdAndMajorityVoteCompressedNonconvexOptimization), which discards the l_2 norm ||v||_2 and uses deterministic sign(v_i) without unbiased stochastic rounding or Elias run-length coding; from 1-bit SGD with error feedback (Seide et al. 2014; Karimireddy et al. 2019), which maintains a local residual memory e_t; and from post-training neural weight quantization (such as GPTQ or AWQ), which quantizes trained model weights for inference rather than stochastically quantizing and Elias-coding gradients during distributed SGD/SVRG training.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 378 QSGD (Alistarh et al. 2017): s=sqrt(n)=8, avg_bits=200.4 <= theo_bound=212.4 << raw_32bit=2048 (10.2x compression)
```
