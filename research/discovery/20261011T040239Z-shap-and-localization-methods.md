# SHAP and localization methods — 2026-10-11T04:02:39Z

Added six distinct methods after primary-source and rendered-page inspection, bringing the native collection to 74 DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:KernelSHAP](../../data/curated/KernelSHAP.yaml) | Kernel SHAP is a specific estimator within the SHAP framework. Its Shapley kernel and constraints distinguish it from an arbitrary LIME regression surrogate. |
| [AIMech:DeepSHAP](../../data/curated/DeepSHAP.yaml) | Deep SHAP adapts DeepLIFT-style propagation with component SHAP values; it is a distinct approximation method, not the general SHAP definition or a synonym for all DeepLIFT rules. |
| [AIMech:SPLIME](../../data/curated/SPLIME.yaml) | SP-LIME selects representative local explanations; it is separate from fitting each LIME surrogate and does not produce a globally faithful surrogate model. |
| [AIMech:TreeSHAP](../../data/curated/TreeSHAP.yaml) | This record denotes the original tree-traversal SHAP algorithm, not the TreeExplainer software package, all its later modes, or Independent Tree SHAP. |
| [AIMech:GradCAM](../../data/curated/GradCAM.yaml) | Grad-CAM computes a coarse activation-space localization map. It differs from architecture-restricted CAM and from Guided Grad-CAM's additional input-space fusion. |
| [AIMech:GuidedGradCAM](../../data/curated/GuidedGradCAM.yaml) | Guided Grad-CAM is a specific fusion of two visualization methods, not a synonym for Grad-CAM or guided backpropagation alone. |

SHAP and LIME mappings were refined from a theme-only ExplainableLLM link to the predictive-model object directly analyzed by the methods. The original finding is preserved in a structured review and tracked in [issue #10](https://github.com/CultureBotAI/AIMech/issues/10); a successor review will record the checked disposition.

Identity searches included ignored and hidden files. Tree SHAP exactness is bounded to its defined subset-evaluation function; Deep SHAP remains a compositional approximation; SP-LIME selects explanations; Grad-CAM and Guided Grad-CAM retain distinct constructions.

The JSON companion records actual queries, inspected passages, retained source hashes, mapping changes and pending candidates. Discovery remains active.
