# Literature Discovery Report: Generalized Mean P-Value Merging

- **Report ID**: `20261017T103500Z-generalized-mean-pvalue-merging`
- **Created At**: `2026-10-17T10:35:00Z`
- **Curated Concept**: `AIMech:GeneralizedMeanPValueMerging` (`data/curated/GeneralizedMeanPValueMerging.yaml`, SHA-256 `099a7959a7d93ae42c966e7ca9e54c90581ba3c54218810baead7bd017e58396`)
- **Verification Script**: `research/discovery/generalized-mean-pvalue-merging-boundaries.py` (SHA-256 `44f1931563deeed6236f5c62da4a02520f051ee356d5391c7817918d69090c38`)

## Primary Sources Inspected

1. **Vovk & Wang (2020)** — *Combining p-values via averaging*, `arXiv:1212.4966` (*Biometrika* 107(4):791–808, DOI `https://doi.org/10.1093/biomet/asaa027`). Complete full-text HTML conversion read (`sha256: 795de89f2d3ab8ce1a5c07046cce1fb85a097610b08ba7ffd661ddeae22a16a3`).
2. **Fang, Chang, Park, & Tseng (2023)** — *Heavy-tailed distribution for combining dependent p-values with asymptotic robustness*, `arXiv:2103.12967` (*Statistica Sinica* 33, 1115–1142, DOI `https://doi.org/10.5705/ss.202021.0078`). Complete full-text HTML conversion read (`sha256: 432b18ec119b33e5b3cd66b32bb71015a243bb7dd28362cf7c9557f0e78a8402`).
3. **Gui, Jiang, & Wang (2023)** — *Aggregating Dependent Signals with Heavy-Tailed Combination Tests*, `arXiv:2310.20460v1` (DOI `https://doi.org/10.48550/arXiv.2310.20460`). Complete full-text HTML conversion read (`sha256: 3f487fc6bca4b5db326053b80a172ec71bee5387faa78dc2605e6bf91c795f71`).

## Candidate Decisions

- **`AIMech:GeneralizedMeanPValueMerging`** (`ADD_CURATED`): Statistical $p$-value combination framework (Vovk & Wang 2020) calibrating Kolmogorov / Hardy–Littlewood–Pólya generalized $r$-means $M_{r,K}(p_1,\dots,p_K)$ and simplex-weighted $r$-means $M_{r,\mathbf{w}}(p_1,\dots,p_K)$ with exact and asymptotically precise worst-case dependence multipliers across $r \in [-\infty, +\infty]$.

## Constructed Mathematical Verification Summary

```json
{
  "concept_id": "AIMech:GeneralizedMeanPValueMerging",
  "prop12_eq17_simulation_K50_mu3": {
    "rho_0.1": {
      "mean_arithmetic": 0.03438829586782956,
      "mean_bonferroni": 2.6857250696607493e-05,
      "mean_compound_BA": 5.3714501393214986e-05,
      "mean_compound_BG": 5.3714501393214986e-05,
      "mean_geometric": 0.0027689647881950046
    },
    "rho_0.9": {
      "mean_arithmetic": 0.03601379134003679,
      "mean_bonferroni": 0.13459898203203058,
      "mean_compound_BA": 0.06517145269925724,
      "mean_compound_BG": 0.06841813529520667,
      "mean_geometric": 0.03596571591761933
    }
  },
  "prop4_prop5_prop5w_precision_checks": {
    "eps": 0.1,
    "prob_2_M12_le_eps_under_joint_mixability": 0.1,
    "prob_unscaled_M12_le_eps_under_joint_mixability": 0.2,
    "prop3_k2_r2_asymptotic_multiplier": 1.7320508075688772,
    "prop5_k2_r2_precise_multiplier": 1.4142135623730951,
    "prop5w_dominant_weight_multiplier_w07": 1.4285714285714286,
    "prop5w_merged_p_value": 0.041428571428571426
  },
  "prop8_prop9_harmonic_multipliers": {
    "10": {
      "a_K_H": 4.559778560272899,
      "a_K_H_over_ln_K": 1.9802866674272739,
      "e_ln_K": 6.259075216766395,
      "r_star_minimizer": -1.7677041641106597,
      "y_K": 23.258789671962646
    },
    "1000": {
      "a_K_H": 10.110735846311918,
      "a_K_H_over_ln_K": 1.4636789286782237,
      "e_ln_K": 18.777225650299183,
      "r_star_minimizer": -1.1692690290604408,
      "y_K": 7986.795110324581
    },
    "3": {
      "a_K_H": 2.745643576732724,
      "a_K_H_over_ln_K": 2.499192485878138,
      "e_ln_K": 2.9863378208083255,
      "r_star_minimizer": -11.140723975747152,
      "y_K": 1.8169605355365102
    },
    "5": {
      "a_K_H": 3.5645018084938873,
      "a_K_H_over_ln_K": 2.2147494979181674,
      "e_ln_K": 4.374905831402675,
      "r_star_minimizer": -2.640856237522197,
      "y_K": 6.76088975619874
    },
    "50": {
      "a_K_H": 6.625000924775344,
      "a_K_H_over_ln_K": 1.6934974348521963,
      "e_ln_K": 10.633981048169069,
      "r_star_minimizer": -1.3434038804418624,
      "y_K": 221.45694655270665
    }
  }
}
```
