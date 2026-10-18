# Discovery Report: Round 210 (`AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency`)

- **Report ID**: `20261017T171500Z-simes-closed-testing-concentration-shortcut-and-fdp-consistency`
- **Created At**: `2026-10-17T17:15:00Z`
- **Corpus State**: `442` AIO records, `604 -> 605` curated records
- **Stopping Status**: `CONTINUE_DISCOVERY`

## 1. Candidate Curated in Round 210

### `AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency` — Simes closed-testing concentration-set shortcut and double-asymptotic false discovery proportion consistency
- **Concept Kind**: `mathematical_method`
- **Record Path**: `data/curated/SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml` (SHA-256 `41cef06cda3799d6493029160b8fbfce2e2d6ede43cb8250c851eb18216a078d`)
- **Primary Sources Inspected in Full Text**:
  1. Jelle J. Goeman, Rosa J. Meijer, Thijmen J. P. Krebs, & Aldo Solari (2019), *Simultaneous control of all false discovery proportions in large-scale multiple hypothesis testing*, *Biometrika* 106(4):841–856 (`arXiv:1611.06739v2` full-text 27-page PDF, SHA-256 `a3f4992cffde630eb0dedf047efbce6bab4b4ece682962bd544b5f5321dcce41`, `291067` bytes; `DOI:10.1093/biomet/asz041`).
  2. Crossref bibliographic record (`https://api.crossref.org/works/10.1093/biomet/asz041`, SHA-256 `ab62d4953d0e0bedf41c737d839e36bdcfa05a646895787d897bbfb48a47856a`).
  3. arXiv abstract record (`https://arxiv.org/abs/1611.06739`, SHA-256 `c162b611101e90effd5b25886112940e1997dd1f3967429f85e3f81245c55d7f`).

## 2. Constructed Boundary & Numerical Verification

Executed `python3 research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py` (SHA-256 `636fe24ef831b4609c4b9524df6d94b5eb64b278711b4876eb6a094175aa2c4e`):
- **Section 3 Figure 1 Non-Consonant Rejections & Goeman–Solari (2011) Shortcut Gap**:
  - Verified $h_\alpha = 2, R_\alpha = \emptyset, t_\alpha(L_3) = 1 < |L_3 \setminus R_\alpha| = 3$, and $t_\alpha(L_2) = 1 < t_\alpha^{\mathrm{GS2011}}(L_2) = 2$.
- **Sections 4 & 5 Exact Shortcut & Concentration Set $Z_\alpha$**:
  - Exhaustively verified Lemmas 1–4 and Theorem 1 across all `256` subsets of an 8-hypothesis problem ($h_\alpha = 4, z_\alpha = 5 \le b_\alpha = 6, d_\alpha(Z_\alpha) = 4, q_\alpha(B_\alpha) = 0.333333$, with strict non-consonant gains $d_\alpha(S) > |S \cap R_\alpha|$ on `128` subsets) and Lemma 5 BH bounds.
- **Sections 6 & 7 Simes-Detectability & Double-Limit Consistency**:
  - Verified Lemma 6 convergence $\hat{\pi}_{\alpha,4000} = 0.9235 \approx \bar{\pi}_\alpha = 0.929996$, vanishing Hommel FWER fraction `0.01575` vs. non-vanishing Theorem 2 fraction $|J_{4000}|/4000 = 0.0905$ with $q_\alpha(J_{4000}) = 0.232044 \le \bar{\pi}_\alpha q = 0.232499$, and Theorem 3 double-limit trajectory $q_{\alpha,m,n}(S_m) \to \gamma_S = 0.6$ (`{'m=200,n=16': 0.9, 'm=1000,n=36': 0.712, 'm=4000,n=81': 0.609}`).
