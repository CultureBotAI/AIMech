# Discovery Report: Round 811 — Teacher Assistant Knowledge Distillation (TAKD)

- **Timestamp**: `2026-10-19T14:54:00Z`
- **Selected Concept**: `AIMech:TAKDTeacherAssistantKnowledgeDistillation` (*Teacher Assistant Knowledge Distillation (TAKD)*)
- **Record Path**: `data/curated/TAKDTeacherAssistantKnowledgeDistillation.yaml`
- **Primary Source**: Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Ang Li, Nir Levine, Akihiro Matsukawa, Hassan Ghasemzadeh — *Improved Knowledge Distillation via Teacher Assistant* (`https://arxiv.org/bibtex/1902.03393`).

## Identity & Boundary Resolution

Introduced by Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Ang Li, Nir Levine, Akihiro Matsukawa, and Hassan Ghasemzadeh (AAAI 2020, Vol. 34, No. 04, pp. 5191-5198, arXiv:1902.03393, doi:10.1609/aaai.v34i04.5963). Distinct from direct single-step Baseline Knowledge Distillation (BLKD, Hinton et al. 2015), from multi-teacher ensemble distillation (which averages parallel teachers of similar large capacity), and from online Deep Mutual Learning (which co-trains peer networks simultaneously): TAKD proves both empirically and via VC generalization bounds (Eqs. 4-12) that an overly large teacher degrades a fixed small student, and resolves this by sequential capacity-ordered intermediary distillation.

## Constructed Boundary & Regime Verification

```text
{"concept": "TAKDTeacherAssistantKnowledgeDistillation", "vc_bound_takd": 0.057555, "vc_bound_blkd": 0.085616, "vc_bound_nokd": 0.1, "num_paths_to_s2": 8, "best_unconstrained_path": [10, 8, 6, 4, 2], "best_unconstrained_acc": 45.14, "best_2ta_path": [10, 6, 4, 2], "status": "ok"}
```
