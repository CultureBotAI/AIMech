# Scientific author self-review of Predictive Entropy Search

- Review: 20261015T012016Z-predictive-entropy-search
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T00:59:15.060081Z
- Finished UTC: 2026-10-15T01:20:16.155510Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The original Predictive Entropy Search identity is supported as a DRAFT algorithm with a qualified ActiveLearning association. Its optimizer sampling and approximate conditional predictive entropy distinguish it from ES operationally. Source notation, finite-feature, Hessian, boundary and hyperparameter scopes remain explicit, without a stronger exactness or performance claim.

## Scope And Provenance

All maintained fields of the selected record. Actual source scope: hernandez2014: Historical root reading: all9 native-text pages and visuals4,5. After both actual captures root reread native-text PDF2–5 and visually inspected fresh renders4,5.. Equations2–3 and Algorithms1–2 confirm shared ideal optimizer information and distinct approximate maximizer sampling/predictive-entropy procedure. C1/C2/EP, C3 comparison, noise and conditional hyperparameter average support the six scoped claims. Negative diagonal does not certify definiteness with nonzero off-diagonals; boundary maxima and undefined stability symbol remain qualified. No author software or performance assertion.; hernandez2014-supplement: Historical root reading: all4 native-text pages and visuals2,4. After both actual captures root reread all4 native-text pages and visually inspected fresh renders2,4.. AppendixA supports finite-feature Gaussian weights but kernel expectation does not commute with conditioning. B.1 declares[z;c]; B.3 printed vector/noise blocks use the opposite order. The record preserves integral and ordering caveat without claiming a repaired implementation. The Gaussian moment approximation is not exact maximizer conditioning; archive-member hash/acquisition distinction is retained.; hennig2012: Historical root reading retained from22:12:24Z: all29 native-text pages and visuals11,13,17. After both actual captures root reread native-text PDF8–13,16,19 and viewed fresh renders11,13.. The postcapture source read confirms nonuniform representers, EP finite minimum probabilities and derivatives, negative KL with fixed-reference/proposal correction, greedy prospective-loss choice and qualified hyperparameter handling. Printed covariance/noise/Taylor ambiguity remains unresolved; finite/measure limits and noncore errors from historical reading remain explicit.

Selection: Exact maintained ID: AIMech:PredictiveEntropySearch
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f1b64ab3aa88a7e8c279cdc6fb6640d9e13a5e92.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PredictiveEntropySearch | data/curated/PredictiveEntropySearch.yaml | maintained | Predictive Entropy Search |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:PredictiveEntropySearch | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 537.40s (0:08:57)<br>Checked 442 record(s); 0 failed.<br>Checked 717 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 401 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 411,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PredictiveEntropySearch | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| just render | passed | True | AIMech:PredictiveEntropySearch | Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages<br>uv run --locked python scripts/render_pages.py<br> |
| just render-check | passed | True | AIMech:PredictiveEntropySearch | pages/ is current<br>uv run --locked python scripts/render_pages.py --check<br> |
| uv run --locked aimech check-source | passed | True | AIMech:PredictiveEntropySearch | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:PredictiveEntropySearch | Actual command exited zero without output. |
| python3 research/discovery/entropy-search-boundaries.py | passed | True | AIMech:PredictiveEntropySearch | {<br>  "boundary_optimizer": {<br>    "derivative_at_maximizer": 1,<br>    "function": "f(x)=x on [0,1]",<br>    "maximizer": 1,<br>    "scope": "Logical domain boundary example, not a sampled stationary GP trajectory."<br>  },<br>  "hessian_negative_control": {<br>    "determinants": [<br>      "5",<br>      "-3"<br>    ],<br>    "eigenvalues_permitted": [<br>      1,<br>      -3<br>    ],<br>    "eigenvalues_sampled": [<br>      -1,<br>      -5<br>    ],<br>    "permitted_after_negative_diagonal_only_constraints": [<br>      [<br>        "-1",<br>        "2"<br>      ],<br>      [<br>        "2",<br>        "-1"<br>      ]<br>    ],<br>    "sampled_negative_definite": [<br>      [<br>        "-3",<br>        "2"<br>      ],<br>      [<br>        "2",<br>        "-3"<br>      ]<br>    ]<br>  },<br>  "hyperparameter_marginalization": {<br>    "construction": "Psi and S independent fair bits, Y=S xor Psi.",<br>    "marginal_mi_nats": 0.0,<br>    "mean_conditional_mi_nats": 0.6931471805599453,<br>    "scope": "Demonstrates a general distinction between averaging conditional acquisitions and mutual information under a marginalized model; not a claim about a particular PES experiment."<br>  },<br>  "kernel_average_boundary": {<br>    "average_conditional_posterior_variance": "5/8",<br>    "noise_variance": 1,<br>    "posterior_variance_at_average_kernel": "2/3",<br>    "random_scalar_kernel_values": [<br>      "1",<br>      "3"<br>    ],<br>    "scope": "Generic covariance example. Unbiased feature inner products do not make finite-feature posterior inference exact."<br>  },<br>  "limits": [<br>    "No universal accuracy, convergence, runtime or regret guarantee.",<br>    "No author code or EP/GP implementation was executed.",<br>    "No claim that the displayed ES innovation/Taylor notation has been fully repaired or numerically reproduced."<br>  ],<br>  "predictive_entropy_is_not_information": {<br>    "informative_binary_outcomes": {<br>      "mutual_information": 0.6931471805599453,<br>      "predictive_entropy": 0.6931471805599453,<br>      "predictive_entropy_drop": 0.6931471805599453,<br>      "target_entropy": 0.6931471805599453,<br>      "target_entropy_drop": 0.6931471805599453<br>    },<br>    "scope": "Finite probability example, not a PES surrogate run.",<br>    "uninformative_four_outcomes": {<br>      "mutual_information": 0.0,<br>      "predictive_entropy": 1.3862943611198906,<br>      "predictive_entropy_drop": 0.0,<br>      "target_entropy": 0.6931471805599453,<br>      "target_entropy_drop": 0.0<br>    }<br>  },<br>  "probability_grid": {<br>    "entropy_and_kl_identity_tolerance": 2e-14,<br>    "exact_posterior_martingale": true,<br>    "max_observed_kl_difference": 1.1102230246251565e-16,<br>    "positive_binary_channels": 27<br>  },<br>  "role": "Supporting curator boundary algebra, not an independent scientific review.",<br>  "supplement_block_order": {<br>    "K_diagonal": [<br>      "2",<br>      "3",<br>      "5",<br>      "7"<br>    ],<br>    "correct_mean_variance": [<br>      "4",<br>      "2/3"<br>    ],<br>    "correct_site_order_values": [<br>      "6",<br>      "12",<br>      "9",<br>      "10"<br>    ],<br>    "declared_order": [<br>      "z1",<br>      "z2",<br>      "c1",<br>      "c2"<br>    ],<br>    "literal_printed_mean_variance": [<br>      "9",<br>      "0"<br>    ],<br>    "prediction": "f=z1",<br>    "printed_order_values": [<br>      "9",<br>      "10",<br>      "6",<br>      "12"<br>    ],<br>    "scope": "Generic Gaussian block calculation; K and Kdag kept in their stated [z;c] order. Reordering every object consistently resolves the notation problem."<br>  }<br>}<br> |

## Scientific And Domain Assessments

### Predictive Entropy Search

identity: supported. Targets: AIMech:PredictiveEntropySearch.

Retain the narrow DRAFT identity within the documented search scope.

PES and ES share ideal optimizer information under a consistent minimum/maximum conversion, but the source PES pipeline samples approximate maximizers and computes optimizer-conditioned predictive entropies instead of directly approximating minimizer probabilities and prospective loss. GP regression, derivative-observation GP models and monotonic virtual-derivative models supply distinct ingredients or constraints, not this acquisition. PESC, parallel PES, max-value entropy methods and the older sampling family are not automatic aliases or newly assessed extensions.

### Definition and source scope

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

The maintained definition is supported within its stated method scope.

The definition identifies the predictive-entropy rearrangement plus approximate maximizer draws and Gaussian constraint inference. It preserves the source maximization convention and does not present maximization of predictive entropy alone as PES or equate the approximation with exact optimizer information. The official main paper supports the iterative acquisition and its approximations; the official extracted appendix supports feature and constraint algebra. The JMLR ES source is explicitly comparative evidence. The appendix ZIP contains the four-page PDF, not executable code. Exact PDF/archive hashes and extraction lineage are retained, while original versus current root calculator executions remain correctly attributed.

### Related AIO mapping: AIO:ActiveLearning

grounding: supported. Targets: AIMech:PredictiveEntropySearch.

related_match expresses the scoped semantic association without equivalence or ontology inheritance.

The exact pinned ActiveLearning CLASS describes deliberately querying an information source for outputs. Both algorithms select informative black-box objective evaluations to update a surrogate and optimizer-location belief. related_match records that association without equating function optimization with annotation or pool-based classification, asserting subclass membership, or identifying either acquisition with the broad class. All thirteen selected exact node/incident contexts and twelve alternatives retain their original reading attribution.
Alternatives:
AIO:TrainingStrategy: General expensive black-box function optimization is not necessarily model training or preprocessing; training applications do not define these whole algorithms.
AIO:RegressionAnalysis: The GP regression surrogate is a component, not the information-based sequential evaluation rule.
AIO:SupervisedLearning: A generic input-output learning task omits the optimizer-location acquisition.
AIO:UnsupervisedLearning: The methods collect objective-value observations and are not defined by unlabeled pattern learning.
AIO:ReinforcementLearning: Exploration terminology does not identify a policy/environment reward-learning method or cumulative-regret objective.
AIO:BayesianNetwork: A GP posterior and conditional information formula are not a DAG network architecture.
AIO:Model: The records would denote search algorithms, not only a predictive surrogate artifact.
AIO:Network: No interconnected-node architecture defines these acquisition mechanisms.
AIO:MathematicalFunction: An acquisition formula alone does not identify the complete iterative algorithm.
AIO:DeepActiveLearning: The methods do not require a deep neural network or the pinned annotation-focused architecture.
AIO:KernelLayer: Use of covariance kernels does not make either optimizer a neural layer.
AIO:MachineLearningTask: This broad task is less informative than the explicit query-learning association; it does not identify either algorithm.

### optimizer-information-and-entropy-rearrangement

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

Supported within the stated assumptions and inspected passages.

Main Eq2–3 uses mutual-information symmetry at fixed data, candidate and hyperparameters. The record adds the necessary well-defined entropy scope and consistent min/max conversion to ES. Finite channels check both entropy reductions against direct MI; an independent four-outcome observation has higher predictive entropy than an informative binary one, showing why the conditional term cannot be omitted. These are bounded probability examples, not PES GP executions.

### finite-feature-maximizer-samples

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

Supported within the stated assumptions and inspected passages.

Main PDF3 and appendixA derive spectral random features and Gaussian posterior weights before numerical sample-function maximization. The kernel and differentiability qualifications are explicit. A fixed feature map defines a finite-rank GP exactly; expectation of its kernel does not commute through posterior conditioning. The rational scalar example gives average conditional variance5/8 versus2/3 at the mean kernel, supporting that boundary without claiming an observed PES error rate.

### approximate-maximizer-constraint-inference

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

Supported within the stated assumptions and inspected passages.

Main PDF4–5 initially fixes zero gradient/off-diagonals, then substitutes sampled off-diagonal Hessian values; EP approximates remaining negative-diagonal and soft-value factors. The record correctly describes those as approximate constraints. Keeping off-diagonal2 while changing diagonal -3 to -1 turns eigenvalues(-1,-5) into(1,-3), so diagonal signs are insufficient after substitution. A linear objective on[0,1] also has a nonstationary boundary maximum. Neither witness asserts that every PES draw fails.

### candidate-comparison-and-predictive-variance

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

Supported within the stated assumptions and inspected passages.

Main Eq8–9 derives a truncated-Gaussian marginal variance for a valid covariance and strictly positive difference variance, then makes a further Gaussian moment approximation and adds observation noise. The strict comparison degenerates at x=S. Supplement Eq12 provides an integral definition; its later [c;tilde_m]/diag(0,tilde_V) display conflicts with stated [z;c] ordering unless every block is reordered. The exact generic block witness supports the notation caveat, not a tested software patch.

### hyperparameter-conditional-acquisition-average

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

Supported within the stated assumptions and inspected passages.

Algorithm2 and Eq10 average per-draw log-variance differences after pairing hyperparameters and approximate maximizers; noise belongs to each draw. This is a conditional-information average. The exact fair-bit XOR construction has mean conditional MI log2 and marginal MI0, disproving a general equality to the marginalized information objective. Reusing candidate-independent constraints is source-supported; no implementation efficiency measurement is asserted.

### sequential-query-and-final-recommendation

evidence: supported. Targets: AIMech:PredictiveEntropySearch.

Supported within the stated assumptions and inspected passages.

Algorithm1 explicitly maximizes the acquisition, observes the objective, augments data and returns an optimizer of the final GP posterior mean. This separates the sampling rule from the recommendation and from the mode of the optimizer law. Neither approximate acquisition maximization nor a finite evaluation budget certifies the true global optimum.

### Original maximizer-sampling and approximate predictive-entropy Bayesian optimizer, with conditional hyperparameter averaging and interior-constraint limitations

consistency: supported. Targets: AIMech:PredictiveEntropySearch.

Mechanism, parameter assumptions and identity boundaries remain qualified.

Ideal entropy identities require finite terms and appropriate measures. Finite features, numerical maximization, EP and moment matching remain separate approximations. Derivative constraints describe interior stationary points and cannot cover every bounded-domain optimum. Negative diagonals with nonzero off-diagonals need not give a negative-definite Hessian. Main C3 prose reverses an inequality and the stability paragraph uses undefined s; no unstated numerical repair is adopted. The supplement’s K/[z;c] ordering must be reconciled consistently with its displayed vector/noise blocks. Conditional hyperparameter information averaging is not generally marginal information. No general accuracy, regret, speed or convergence comparison with ES is established.

### All captured maintained fields

provenance: supported. Targets: AIMech:PredictiveEntropySearch.

Root reassessed the complete current record after canonical capture; DRAFT remains.

Root reread the complete actual YAML after both canonical captures and reassessed its six claims, locators, definition, kind, related ActiveLearning mapping and limitations against prepared narratives and the freshly reread primary pages. All117 selected definitions and13 exact AIO node/edge contexts were read during current prewrite review. Full actual322 neighbor YAMLs and12 exact content groups were read; all1458 occurrences reconstructed. Supporting all1157 identity fields and898/393 frontier candidate/disposition assessment remains attributed. Source/download timestamps are not review-reading timestamps. Root read the complete copied v2 calculator and current postcapture output; exact rational masses/algebra and floating logs with five absolute-only comparisons remain distinct. The original/successor/root execution lineage and preparation six-versus-five count failure are retained; no mathematical run failure or canonical issue is invented. Supporting audit found no new defect; its primary/source run is precreation and its actual correspondence check is postcapture, with the source and byte-audit roles separated. No independent scientific approval or saturation is claimed. PES approximate random-feature maximizers and Gaussian/EP predictive-entropy inference define this identity. Conditional hyperparameter MI averaging is not generally marginalized MI; the retained XOR construction establishes that limited distinction. Rereads: After capture325 at00:59:15Z: ES native-text8–13,16,19 and visuals11,13; PES main native-text2–5 and visuals4,5; supplement native-text1–4 and visuals2,4. Earlier complete root text scopes remain separately dated. Fresh renders are in /private/tmp/aimech-batch324-root-postcapture-visuals.

### Source caveats and original calculation history

provenance: supported. Targets: AIMech:PredictiveEntropySearch.

Source interpretation, TEMP clarifications and actual calculation lineage remain distinct.

Original and successor curator-written checks retain exact code, first outputs and actual execution/reproduction receipts. The five-site tolerance correction preserves its preimage and identical output; the earlier builder count-preflight failure is not misrepresented as a failed mathematical execution. Raw acquisition and archive extraction remain separate from schema-compatible source timestamps. Source caveats are not author-issued errata or maintained-record issue closures. Bounded algebra and floating entropy checks do not validate the full ES/PES numerical pipeline or general accuracy/convergence claims.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json; identity_search and identity_assessment | supports | This record maintains the original PES approximate maximizer-sampling and predictive-entropy algorithm. Its ideal fixed-hyperparameter information target agrees with ES, but finite-feature maximizer draws and constraint/moment approximations do not identify the ES representer-point/EP-derivative procedure. Direction of optimization alone is not the distinction. General GP regression, derivative observations and generic entropy calculations are components or different methods. Constrained, parallel and max-value methods are not automatically aliases. No acronym alias is adopted; current canonical and ignored-inclusive evidence is refreshed before creation. |
| mapping | research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json; mapping_context per_record nodes/semantic/native contexts, actual322_neighbors and mapping_assessment | supports | The exact pinned ActiveLearning CLASS describes deliberately querying an information source for outputs. Both algorithms select informative black-box objective evaluations to update a surrogate and optimizer-location belief. related_match records that association without equating function optimization with annotation or pool-based classification, asserting subclass membership, or identifying either acquisition with the broad class. All thirteen selected exact node/incident contexts and twelve alternatives retain their original reading attribution. |
| actual-record-reading | data/curated/PredictiveEntropySearch.yaml | supports | Root reread the complete actual YAML after both canonical captures and reassessed its six claims, locators, definition, kind, related ActiveLearning mapping and limitations against prepared narratives and the freshly reread primary pages. All117 selected definitions and13 exact AIO node/edge contexts were read during current prewrite review. Full actual322 neighbor YAMLs and12 exact content groups were read; all1458 occurrences reconstructed. Supporting all1157 identity fields and898/393 frontier candidate/disposition assessment remains attributed. Source/download timestamps are not review-reading timestamps. Root read the complete copied v2 calculator and current postcapture output; exact rational masses/algebra and floating logs with five absolute-only comparisons remain distinct. The original/successor/root execution lineage and preparation six-versus-five count failure are retained; no mathematical run failure or canonical issue is invented. Supporting audit found no new defect; its primary/source run is precreation and its actual correspondence check is postcapture, with the source and byte-audit roles separated. No independent scientific approval or saturation is claimed. PES approximate random-feature maximizers and Gaussian/EP predictive-entropy inference define this identity. Conditional hyperparameter MI averaging is not generally marginalized MI; the retained XOR construction establishes that limited distinction. Actual post-capture source reread: After capture325 at00:59:15Z: ES native-text8–13,16,19 and visuals11,13; PES main native-text2–5 and visuals4,5; supplement native-text1–4 and visuals2,4. Earlier complete root text scopes remain separately dated. Fresh renders are in /private/tmp/aimech-batch324-root-postcapture-visuals. |
| hernandez2014 | https://proceedings.neurips.cc/paper_files/paper/2014/file/6488484c982e9af5c35689523ba1abfe-Paper.pdf; Section 2, PDF pp. 2–5, Equations 2–10 and Algorithm 2; Sections 1–2, PDF pp. 1–3, Equations 1–3; small original finite-channel illustrations in research/discovery/entropy-search-boundaries.py; Section 2.1, PDF p. 3, Equation 5; Section 2.2, PDF pp. 4–5, C1–C2, Equations 6–7 and sampled off-diagonal substitution after Equation 9; original Hessian and boundary examples in research/discovery/entropy-search-boundaries.py; Section 2.2, PDF p. 5, Equations 8–9 and entropy approximation immediately following them; Algorithm 2, PDF p. 2; Section 2.3, PDF p. 5, Equation 10; original finite XOR conditional/marginal information example in research/discovery/entropy-search-boundaries.py; Sections 1–2, PDF pp. 1–3; Algorithms 1–2, PDF p. 2 | supports | Official Advances in Neural Information Processing Systems 27 (2014) proceedings PDF, nine pages; retrieved proceedings.neurips.cc bytes equal the retained papers.nips.cc PDF. Actual root reading: Equations2–3 and Algorithms1–2 confirm shared ideal optimizer information and distinct approximate maximizer sampling/predictive-entropy procedure. C1/C2/EP, C3 comparison, noise and conditional hyperparameter average support the six scoped claims. Negative diagonal does not certify definiteness with nonzero off-diagonals; boundary maxima and undefined stability symbol remain qualified. No author software or performance assertion. |
| hernandez2014-supplement | https://proceedings.neurips.cc/paper_files/paper/2014/file/6488484c982e9af5c35689523ba1abfe-Supplemental.zip; Appendix A, supplement PDF pp. 1–2 / printed pp. 10–11; scalar kernel-conditioning boundary illustration in research/discovery/entropy-search-boundaries.py; Appendices B.1–B.2, supplement PDF pp. 2–3 / printed pp. 11–12; Appendix B.3, supplement PDF pp. 3–4 / printed pp. 12–13, Equation 12 and following Gaussian prediction expressions; original block-order example in research/discovery/entropy-search-boundaries.py | supports | Official 2014 proceedings Supplemental.zip member pes-appendix.pdf; four PDF pages numbered 10–13, Appendices A–B.3. PDF hash is the extracted member; acquisition timestamp is inherited from the separately pinned ZIP download. Actual root reading: AppendixA supports finite-feature Gaussian weights but kernel expectation does not commute with conditioning. B.1 declares[z;c]; B.3 printed vector/noise blocks use the opposite order. The record preserves integral and ordering caveat without claiming a repaired implementation. The Gaussian moment approximation is not exact maximizer conditioning; archive-member hash/acquisition distinction is retained. |
| hennig2012 | https://jmlr.org/papers/volume13/hennig12a/hennig12a.pdf; Sections 2.3 and 2.5–2.6, PDF pp. 8–10, 12–14 / printed pp. 1816–1818, 1820–1822 | supports | Official JMLR 13(57):1809–1837 (2012) journal PDF; 29 PDF pages, submitted December 2011 and published June 2012. Locators distinguish PDF and printed pagination. Actual root reading: The postcapture source read confirms nonuniform representers, EP finite minimum probabilities and derivatives, negative KL with fixed-reference/proposal correction, greedy prospective-loss choice and qualified hyperparameter handling. Printed covariance/noise/Taylor ambiguity remains unresolved; finite/measure limits and noncore errors from historical reading remain explicit. |
| calculation-entropy-search | research/discovery/entropy-search-boundaries.py; Saved report curator_calculations; probability_grid, predictive_entropy_is_not_information, hyperparameter_marginalization, hessian_negative_control, supplement_block_order, kernel_average_boundary, boundary_optimizer | supports | Original bounded rational probability/matrix algebra with floating natural-log entropy; five isclose sites use rel_tol=0 and abs_tol=2e-14; actual copied-script outputs checked against the full saved result. No author-code execution, model training, benchmark replication or universal proof. Selected results: {"probability_grid": {"entropy_and_kl_identity_tolerance": 2e-14, "exact_posterior_martingale": true, "max_observed_kl_difference": 1.1102230246251565e-16, "positive_binary_channels": 27}, "predictive_entropy_is_not_information": {"informative_binary_outcomes": {"mutual_information": 0.6931471805599453, "predictive_entropy": 0.6931471805599453, "predictive_entropy_drop": 0.6931471805599453, "target_entropy": 0.6931471805599453, "target_entropy_drop": 0.6931471805599453}, "scope": "Finite probability example, not a PES surrogate run.", "uninformative_four_outcomes": {"mutual_information": 0.0, "predictive_entropy": 1.3862943611198906, "predictive_entropy_drop": 0.0, "target_entropy": 0.6931471805599453, "target_entropy_drop": 0.0}}, "hyperparameter_marginalization": {"construction": "Psi and S independent fair bits, Y=S xor Psi.", "marginal_mi_nats": 0.0, "mean_conditional_mi_nats": 0.6931471805599453, "scope": "Demonstrates a general distinction between averaging conditional acquisitions and mutual information under a marginalized model; not a claim about a particular PES experiment."}, "hessian_negative_control": {"determinants": ["5", "-3"], "eigenvalues_permitted": [1, -3], "eigenvalues_sampled": [-1, -5], "permitted_after_negative_diagonal_only_constraints": [["-1", "2"], ["2", "-1"]], "sampled_negative_definite": [["-3", "2"], ["2", "-3"]]}, "supplement_block_order": {"K_diagonal": ["2", "3", "5", "7"], "correct_mean_variance": ["4", "2/3"], "correct_site_order_values": ["6", "12", "9", "10"], "declared_order": ["z1", "z2", "c1", "c2"], "literal_printed_mean_variance": ["9", "0"], "prediction": "f=z1", "printed_order_values": ["9", "10", "6", "12"], "scope": "Generic Gaussian block calculation; K and Kdag kept in their stated [z;c] order. Reordering every object consistently resolves the notation problem."}, "kernel_average_boundary": {"average_conditional_posterior_variance": "5/8", "noise_variance": 1, "posterior_variance_at_average_kernel": "2/3", "random_scalar_kernel_values": ["1", "3"], "scope": "Generic covariance example. Unbiased feature inner products do not make finite-feature posterior inference exact."}, "boundary_optimizer": {"derivative_at_maximizer": 1, "function": "f(x)=x on [0,1]", "maximizer": 1, "scope": "Logical domain boundary example, not a sampled stationary GP trajectory."}} |
| source-math-provenance | research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json; source_analysis.handoffs, root_readings and writer_preparation_reading | supports | Root assessed the separately attributed selective source readings and bounded mathematical research. Supporting agents are in the same author workflow and provide no independent scientific approval. |
| source-error-original-lineage | research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json; calculation_lineage.artifacts, curator_calculations, draft_wording_lineage, research_correction_lineage and source_analysis | supports | Original and successor curator-written ES/PES calculators, first outputs and actual root reproductions retain exact bytes. Five explicit relative-tolerance settings changed comparison guards only; mathematical formulas and output bytes did not change. Original and successor mathematical assessments retain their separate execution attribution. Source formula caveats, official supplement extraction and raw acquisition precision remain explicit. These are not author-code execution, fabricated failed mathematical runs or canonical issue closures. |

## Limits And Additional Notes

- Author self-review, not independent scientific approval or DRAFT promotion.
- Ideal entropy identities require finite terms and appropriate measures. Finite features, numerical maximization, EP and moment matching remain separate approximations. Derivative constraints describe interior stationary points and cannot cover every bounded-domain optimum. Negative diagonals with nonzero off-diagonals need not give a negative-definite Hessian. Main C3 prose reverses an inequality and the stability paragraph uses undefined s; no unstated numerical repair is adopted. The supplement’s K/[z;c] ordering must be reconciled consistently with its displayed vector/noise blocks. Conditional hyperparameter information averaging is not generally marginal information. No general accuracy, regret, speed or convergence comparison with ES is established.
- This is qualified author self-review with supporting agents in the same author workflow; no independent scientific approval or DRAFT promotion is implied.
- Historical research covered 708 native and 442 AIO records, 117 selected definitions and nine full native neighbors. The actual prewrite scope is 715 native and 442 AIO records, all scoped synonyms, four ignored/hidden-inclusive whole-checkout searches and two freshly assessed batch322 neighbors; historical reading is not relabeled as fresh root reading.
- The original curator-written calculator uses exact rational probability masses and matrix examples with floating natural logarithms. The successor explicitly sets rel_tol=0 and abs_tol=2e-14 at five comparison sites; original and successor code, actual first/root executions and unchanged result bytes remain distinct. No GP fitting, EP loop, random-feature sampling, acquisition optimization or author-code replication was performed by those checks.
- The tolerance clarification occurred in TEMP before curation and preserves its earlier count-preflight failure. It is not a fabricated failed mathematical run, canonical finding, author erratum or issue closure.
- Raw source acquisition/extraction precision is retained beside whole-second record metadata. Download dates and bibliography are distinct from actual source-reading scope.
- Empty findings reflect actual root assessment of this selected captured record only; no unrelated finding closure or literature saturation is asserted.
- Source caveats and preserved calculation or wording lineage remain distinct; no maintained-record finding or issue closure is invented from them.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T012016Z-predictive-entropy-search
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Predictive Entropy Search
started_at: '2026-10-15T00:59:15.060081Z'
finished_at: '2026-10-15T01:20:16.155510Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author reassessment with supporting source, mathematical
    and integrity agents in the same author workflow; no independent scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The original Predictive Entropy Search identity is supported as a DRAFT algorithm
  with a qualified ActiveLearning association. Its optimizer sampling and approximate
  conditional predictive entropy distinguish it from ES operationally. Source notation,
  finite-feature, Hessian, boundary and hyperparameter scopes remain explicit, without
  a stronger exactness or performance claim.
source:
  git_revision: f1b64ab3aa88a7e8c279cdc6fb6640d9e13a5e92
  state: working_tree
  inputs:
  - path: data/aio/ActiveLearning.yaml
    sha256: a4d5b2c82df6f586fedc7290261bc978e7c8d17f1d844c5ee9efc8243e46bbaf
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/DeepActiveLearning.yaml
    sha256: b04c9aa74728adbe1bd907cb3f0e15b263bda18ed29660babce092daeed2b4f9
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/BOHB.yaml
    sha256: bb965b104107d30a9d74f4ac4eaa0aa72023cdf676afb53528d3a1b41bebf291
    role: context
  - path: data/curated/BarberAgakovBound.yaml
    sha256: ac947a28b3c48611fdbf557cc0bca656e2e93db0d8e158785c579fbc8868076c
    role: context
  - path: data/curated/ContinuousTimeBayesianNetwork.yaml
    sha256: 0d1266ecc3e05dcd8baaf1c76e9fd7f4a447b5353001f7438754514ebb1bd975
    role: context
  - path: data/curated/CrossEntropyOptimization.yaml
    sha256: b2d993224f56b48738bbecc23df28fe0bc1e16e54c658979fdd28fc1924ba269
    role: context
  - path: data/curated/DerivativeObservationGaussianProcessRegression.yaml
    sha256: 888850faa100e14b96057c516e7d65d01ed2932a142577d101660c73dbf90905
    role: context
  - path: data/curated/EntropySearch.yaml
    sha256: 786a3633b1212b280a7d65b37c7c408ac267554f218daa68d70101651019fafd
    role: context
  - path: data/curated/FABOLAS.yaml
    sha256: 800fb7787896a6cd3f0c2ced22fd70543a79d3a59502ff2c52cf4ae4f8ba0cb9
    role: context
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/KSVD.yaml
    sha256: 9614c37762bbcc13f22585eac13e6e9e9c4a4cc651a26c52bee80fa94be21aa9
    role: context
  - path: data/curated/MonotonicGaussianProcessWithVirtualDerivatives.yaml
    sha256: 9b72af4401c813c1fb3d51aa894a080ca96b86b37a051d8e7bb86a73b54e9cfd
    role: context
  - path: data/curated/PredictiveEntropySearch.yaml
    sha256: 359a11bbbb1efb522df8b3652ffe308ff20564e94fc5e20638b418c29b69de5d
    role: target
  - path: data/curated/RandomSearchHyperparameterOptimization.yaml
    sha256: 24dde2b9d19169c383b403742ea355727c2f167ae8aa21970fbda34e832c89fd
    role: context
  - path: data/curated/TreeStructuredParzenEstimator.yaml
    sha256: bdd8130958b93502ecd3bf0cd73f411dfb4aecb5d6d2ab2e01454dee9bae2737
    role: context
  - path: research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json
    sha256: ac133b0577888e01971897d94138e2a737302bc3613ac2f3bf344f359e173be2
    role: context
  - path: research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.md
    sha256: 5e94acf437d2a48b17aa4bfdf6f374a8d262a0acde6318fa051eaada68300f28
    role: context
  - path: research/discovery/entropy-search-boundaries.py
    sha256: e69b30a010c8eebe5ebe8eacb9ffa8a38b4b5393dc4eb31fb4b21ca7434a98d6
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/history.py
    sha256: 4ff83e818c7f50ea25bfc6b8f2cae7ab29c814310b8b361a6f7af8160055aa91
    role: context
  - path: src/aimech/importer.py
    sha256: 7c2dd8e12f18b76cfb5ed4acc7e1901ae9a968b3a6c7a9d62cb260bc2f1ad3ab
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
  - path: src/aimech/validation.py
    sha256: 274ed5e6bc97440515a1964b9b21927135a2e9a5a4808ae8daebccd3e172ffcc
    role: context
targets:
- target_id: AIMech:PredictiveEntropySearch
  path: data/curated/PredictiveEntropySearch.yaml
  label: Predictive Entropy Search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PredictiveEntropySearch.yaml
    role: maintained
scope:
  description: 'All maintained fields of the selected record. Actual source scope:
    hernandez2014: Historical root reading: all9 native-text pages and visuals4,5.
    After both actual captures root reread native-text PDF2–5 and visually inspected
    fresh renders4,5.. Equations2–3 and Algorithms1–2 confirm shared ideal optimizer
    information and distinct approximate maximizer sampling/predictive-entropy procedure.
    C1/C2/EP, C3 comparison, noise and conditional hyperparameter average support
    the six scoped claims. Negative diagonal does not certify definiteness with nonzero
    off-diagonals; boundary maxima and undefined stability symbol remain qualified.
    No author software or performance assertion.; hernandez2014-supplement: Historical
    root reading: all4 native-text pages and visuals2,4. After both actual captures
    root reread all4 native-text pages and visually inspected fresh renders2,4.. AppendixA
    supports finite-feature Gaussian weights but kernel expectation does not commute
    with conditioning. B.1 declares[z;c]; B.3 printed vector/noise blocks use the
    opposite order. The record preserves integral and ordering caveat without claiming
    a repaired implementation. The Gaussian moment approximation is not exact maximizer
    conditioning; archive-member hash/acquisition distinction is retained.; hennig2012:
    Historical root reading retained from22:12:24Z: all29 native-text pages and visuals11,13,17.
    After both actual captures root reread native-text PDF8–13,16,19 and viewed fresh
    renders11,13.. The postcapture source read confirms nonuniform representers, EP
    finite minimum probabilities and derivatives, negative KL with fixed-reference/proposal
    correction, greedy prospective-loss choice and qualified hyperparameter handling.
    Printed covariance/noise/Taylor ambiguity remains unresolved; finite/measure limits
    and noncore errors from historical reading remain explicit.'
  selection: 'Exact maintained ID: AIMech:PredictiveEntropySearch'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:PredictiveEntropySearch
  exclusions:
  - target: Other batch entries and neighboring identities
    reason: Read as identity/mapping context, not formal review targets.
  - target: Uninspected source versions, general convergence and runtime claims
    reason: Ideal entropy identities require finite terms and appropriate measures.
      Finite features, numerical maximization, EP and moment matching remain separate
      approximations. Derivative constraints describe interior stationary points and
      cannot cover every bounded-domain optimum. Negative diagonals with nonzero off-diagonals
      need not give a negative-definite Hessian. Main C3 prose reverses an inequality
      and the stability paragraph uses undefined s; no unstated numerical repair is
      adopted. The supplement’s K/[z;c] ordering must be reconciled consistently with
      its displayed vector/noise blocks. Conditional hyperparameter information averaging
      is not generally marginal information. No general accuracy, regret, speed or
      convergence comparison with ES is established.
  - target: Author implementation and benchmark replication
    reason: Only bounded original calculations and project checks were executed.
checks:
- check_id: gate-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 537.40s (0:08:57)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 717 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 401 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 411,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
  scope_note: Actual execution completed 2026-10-15T01:17:58.442944Z; this generator
    executes no recorded commands.
- check_id: vendor-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
  scope_note: Actual execution completed 2026-10-15T01:00:49.498706Z; this generator
    executes no recorded commands.
- check_id: render-2
  name: just render
  command: just render
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages

    uv run --locked python scripts/render_pages.py

    '
  scope_note: Actual execution completed 2026-10-15T00:59:51.877426Z; this generator
    executes no recorded commands.
- check_id: render-3
  name: just render-check
  command: just render-check
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'pages/ is current

    uv run --locked python scripts/render_pages.py --check

    '
  scope_note: Actual execution completed 2026-10-15T01:00:16.551841Z; this generator
    executes no recorded commands.
- check_id: additional-4
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
  scope_note: Actual execution completed 2026-10-15T01:00:43.387374Z; this generator
    executes no recorded commands.
- check_id: additional-5
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited zero without output.
  scope_note: Actual execution completed 2026-10-15T01:00:44.351721Z; this generator
    executes no recorded commands.
- check_id: calculation-6
  name: python3 research/discovery/entropy-search-boundaries.py
  command: python3 research/discovery/entropy-search-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PredictiveEntropySearch
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"boundary_optimizer\": {\n    \"derivative_at_maximizer\": 1,\n\
    \    \"function\": \"f(x)=x on [0,1]\",\n    \"maximizer\": 1,\n    \"scope\"\
    : \"Logical domain boundary example, not a sampled stationary GP trajectory.\"\
    \n  },\n  \"hessian_negative_control\": {\n    \"determinants\": [\n      \"5\"\
    ,\n      \"-3\"\n    ],\n    \"eigenvalues_permitted\": [\n      1,\n      -3\n\
    \    ],\n    \"eigenvalues_sampled\": [\n      -1,\n      -5\n    ],\n    \"permitted_after_negative_diagonal_only_constraints\"\
    : [\n      [\n        \"-1\",\n        \"2\"\n      ],\n      [\n        \"2\"\
    ,\n        \"-1\"\n      ]\n    ],\n    \"sampled_negative_definite\": [\n   \
    \   [\n        \"-3\",\n        \"2\"\n      ],\n      [\n        \"2\",\n   \
    \     \"-3\"\n      ]\n    ]\n  },\n  \"hyperparameter_marginalization\": {\n\
    \    \"construction\": \"Psi and S independent fair bits, Y=S xor Psi.\",\n  \
    \  \"marginal_mi_nats\": 0.0,\n    \"mean_conditional_mi_nats\": 0.6931471805599453,\n\
    \    \"scope\": \"Demonstrates a general distinction between averaging conditional\
    \ acquisitions and mutual information under a marginalized model; not a claim\
    \ about a particular PES experiment.\"\n  },\n  \"kernel_average_boundary\": {\n\
    \    \"average_conditional_posterior_variance\": \"5/8\",\n    \"noise_variance\"\
    : 1,\n    \"posterior_variance_at_average_kernel\": \"2/3\",\n    \"random_scalar_kernel_values\"\
    : [\n      \"1\",\n      \"3\"\n    ],\n    \"scope\": \"Generic covariance example.\
    \ Unbiased feature inner products do not make finite-feature posterior inference\
    \ exact.\"\n  },\n  \"limits\": [\n    \"No universal accuracy, convergence, runtime\
    \ or regret guarantee.\",\n    \"No author code or EP/GP implementation was executed.\"\
    ,\n    \"No claim that the displayed ES innovation/Taylor notation has been fully\
    \ repaired or numerically reproduced.\"\n  ],\n  \"predictive_entropy_is_not_information\"\
    : {\n    \"informative_binary_outcomes\": {\n      \"mutual_information\": 0.6931471805599453,\n\
    \      \"predictive_entropy\": 0.6931471805599453,\n      \"predictive_entropy_drop\"\
    : 0.6931471805599453,\n      \"target_entropy\": 0.6931471805599453,\n      \"\
    target_entropy_drop\": 0.6931471805599453\n    },\n    \"scope\": \"Finite probability\
    \ example, not a PES surrogate run.\",\n    \"uninformative_four_outcomes\": {\n\
    \      \"mutual_information\": 0.0,\n      \"predictive_entropy\": 1.3862943611198906,\n\
    \      \"predictive_entropy_drop\": 0.0,\n      \"target_entropy\": 0.6931471805599453,\n\
    \      \"target_entropy_drop\": 0.0\n    }\n  },\n  \"probability_grid\": {\n\
    \    \"entropy_and_kl_identity_tolerance\": 2e-14,\n    \"exact_posterior_martingale\"\
    : true,\n    \"max_observed_kl_difference\": 1.1102230246251565e-16,\n    \"positive_binary_channels\"\
    : 27\n  },\n  \"role\": \"Supporting curator boundary algebra, not an independent\
    \ scientific review.\",\n  \"supplement_block_order\": {\n    \"K_diagonal\":\
    \ [\n      \"2\",\n      \"3\",\n      \"5\",\n      \"7\"\n    ],\n    \"correct_mean_variance\"\
    : [\n      \"4\",\n      \"2/3\"\n    ],\n    \"correct_site_order_values\": [\n\
    \      \"6\",\n      \"12\",\n      \"9\",\n      \"10\"\n    ],\n    \"declared_order\"\
    : [\n      \"z1\",\n      \"z2\",\n      \"c1\",\n      \"c2\"\n    ],\n    \"\
    literal_printed_mean_variance\": [\n      \"9\",\n      \"0\"\n    ],\n    \"\
    prediction\": \"f=z1\",\n    \"printed_order_values\": [\n      \"9\",\n     \
    \ \"10\",\n      \"6\",\n      \"12\"\n    ],\n    \"scope\": \"Generic Gaussian\
    \ block calculation; K and Kdag kept in their stated [z;c] order. Reordering every\
    \ object consistently resolves the notation problem.\"\n  }\n}\n"
  scope_note: Actual execution completed 2026-10-15T01:00:40.335075Z; this generator
    executes no recorded commands.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json
  locator: identity_search and identity_assessment
  accessed_at: '2026-10-15T01:02:50.291440Z'
  snapshot_sha256: ac133b0577888e01971897d94138e2a737302bc3613ac2f3bf344f359e173be2
  support: supports
  summary: This record maintains the original PES approximate maximizer-sampling and
    predictive-entropy algorithm. Its ideal fixed-hyperparameter information target
    agrees with ES, but finite-feature maximizer draws and constraint/moment approximations
    do not identify the ES representer-point/EP-derivative procedure. Direction of
    optimization alone is not the distinction. General GP regression, derivative observations
    and generic entropy calculations are components or different methods. Constrained,
    parallel and max-value methods are not automatically aliases. No acronym alias
    is adopted; current canonical and ignored-inclusive evidence is refreshed before
    creation.
  search_scope: Canonical ID/name/alias/all-scoped-synonym checks and retained four
    complete-checkout searches include ignored and hidden files. Bounded corpus scope,
    not universal absence.
- evidence_id: mapping
  kind: record_content
  reference: research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json
  locator: mapping_context per_record nodes/semantic/native contexts, actual322_neighbors
    and mapping_assessment
  accessed_at: '2026-10-15T01:02:50.291440Z'
  snapshot_sha256: ac133b0577888e01971897d94138e2a737302bc3613ac2f3bf344f359e173be2
  support: supports
  summary: The exact pinned ActiveLearning CLASS describes deliberately querying an
    information source for outputs. Both algorithms select informative black-box objective
    evaluations to update a surrogate and optimizer-location belief. related_match
    records that association without equating function optimization with annotation
    or pool-based classification, asserting subclass membership, or identifying either
    acquisition with the broad class. All thirteen selected exact node/incident contexts
    and twelve alternatives retain their original reading attribution.
- evidence_id: actual-record-reading
  kind: record_content
  reference: data/curated/PredictiveEntropySearch.yaml
  accessed_at: '2026-10-15T01:02:50.291440Z'
  snapshot_sha256: 359a11bbbb1efb522df8b3652ffe308ff20564e94fc5e20638b418c29b69de5d
  support: supports
  summary: 'Root reread the complete actual YAML after both canonical captures and
    reassessed its six claims, locators, definition, kind, related ActiveLearning
    mapping and limitations against prepared narratives and the freshly reread primary
    pages. All117 selected definitions and13 exact AIO node/edge contexts were read
    during current prewrite review. Full actual322 neighbor YAMLs and12 exact content
    groups were read; all1458 occurrences reconstructed. Supporting all1157 identity
    fields and898/393 frontier candidate/disposition assessment remains attributed.
    Source/download timestamps are not review-reading timestamps. Root read the complete
    copied v2 calculator and current postcapture output; exact rational masses/algebra
    and floating logs with five absolute-only comparisons remain distinct. The original/successor/root
    execution lineage and preparation six-versus-five count failure are retained;
    no mathematical run failure or canonical issue is invented. Supporting audit found
    no new defect; its primary/source run is precreation and its actual correspondence
    check is postcapture, with the source and byte-audit roles separated. No independent
    scientific approval or saturation is claimed. PES approximate random-feature maximizers
    and Gaussian/EP predictive-entropy inference define this identity. Conditional
    hyperparameter MI averaging is not generally marginalized MI; the retained XOR
    construction establishes that limited distinction. Actual post-capture source
    reread: After capture325 at00:59:15Z: ES native-text8–13,16,19 and visuals11,13;
    PES main native-text2–5 and visuals4,5; supplement native-text1–4 and visuals2,4.
    Earlier complete root text scopes remain separately dated. Fresh renders are in
    /private/tmp/aimech-batch324-root-postcapture-visuals.'
- evidence_id: hernandez2014
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2014/file/6488484c982e9af5c35689523ba1abfe-Paper.pdf
  locator: Section 2, PDF pp. 2–5, Equations 2–10 and Algorithm 2; Sections 1–2, PDF
    pp. 1–3, Equations 1–3; small original finite-channel illustrations in research/discovery/entropy-search-boundaries.py;
    Section 2.1, PDF p. 3, Equation 5; Section 2.2, PDF pp. 4–5, C1–C2, Equations
    6–7 and sampled off-diagonal substitution after Equation 9; original Hessian and
    boundary examples in research/discovery/entropy-search-boundaries.py; Section
    2.2, PDF p. 5, Equations 8–9 and entropy approximation immediately following them;
    Algorithm 2, PDF p. 2; Section 2.3, PDF p. 5, Equation 10; original finite XOR
    conditional/marginal information example in research/discovery/entropy-search-boundaries.py;
    Sections 1–2, PDF pp. 1–3; Algorithms 1–2, PDF p. 2
  accessed_at: '2026-10-14T22:00:05Z'
  snapshot_sha256: 82eb9e614937fe9e90273705bd0c5379fafbd5dc76e7227992246af5c52ca658
  support: supports
  summary: 'Official Advances in Neural Information Processing Systems 27 (2014) proceedings
    PDF, nine pages; retrieved proceedings.neurips.cc bytes equal the retained papers.nips.cc
    PDF. Actual root reading: Equations2–3 and Algorithms1–2 confirm shared ideal
    optimizer information and distinct approximate maximizer sampling/predictive-entropy
    procedure. C1/C2/EP, C3 comparison, noise and conditional hyperparameter average
    support the six scoped claims. Negative diagonal does not certify definiteness
    with nonzero off-diagonals; boundary maxima and undefined stability symbol remain
    qualified. No author software or performance assertion.'
- evidence_id: hernandez2014-supplement
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2014/file/6488484c982e9af5c35689523ba1abfe-Supplemental.zip
  locator: Appendix A, supplement PDF pp. 1–2 / printed pp. 10–11; scalar kernel-conditioning
    boundary illustration in research/discovery/entropy-search-boundaries.py; Appendices
    B.1–B.2, supplement PDF pp. 2–3 / printed pp. 11–12; Appendix B.3, supplement
    PDF pp. 3–4 / printed pp. 12–13, Equation 12 and following Gaussian prediction
    expressions; original block-order example in research/discovery/entropy-search-boundaries.py
  accessed_at: '2026-10-14T22:00:05Z'
  snapshot_sha256: c8cdec73f845ed101aefec04f6d21427bb095b7a4346bd5651d376b31801f4dc
  support: supports
  summary: 'Official 2014 proceedings Supplemental.zip member pes-appendix.pdf; four
    PDF pages numbered 10–13, Appendices A–B.3. PDF hash is the extracted member;
    acquisition timestamp is inherited from the separately pinned ZIP download. Actual
    root reading: AppendixA supports finite-feature Gaussian weights but kernel expectation
    does not commute with conditioning. B.1 declares[z;c]; B.3 printed vector/noise
    blocks use the opposite order. The record preserves integral and ordering caveat
    without claiming a repaired implementation. The Gaussian moment approximation
    is not exact maximizer conditioning; archive-member hash/acquisition distinction
    is retained.'
- evidence_id: hennig2012
  kind: primary_source
  reference: https://jmlr.org/papers/volume13/hennig12a/hennig12a.pdf
  locator: Sections 2.3 and 2.5–2.6, PDF pp. 8–10, 12–14 / printed pp. 1816–1818,
    1820–1822
  accessed_at: '2026-10-14T21:42:10Z'
  snapshot_sha256: c1141315e0cee37ebb2de1e6a87e1e7a64cd7bb54e4812b591fef57031e8e5f2
  support: supports
  summary: 'Official JMLR 13(57):1809–1837 (2012) journal PDF; 29 PDF pages, submitted
    December 2011 and published June 2012. Locators distinguish PDF and printed pagination.
    Actual root reading: The postcapture source read confirms nonuniform representers,
    EP finite minimum probabilities and derivatives, negative KL with fixed-reference/proposal
    correction, greedy prospective-loss choice and qualified hyperparameter handling.
    Printed covariance/noise/Taylor ambiguity remains unresolved; finite/measure limits
    and noncore errors from historical reading remain explicit.'
- evidence_id: calculation-entropy-search
  kind: record_content
  reference: research/discovery/entropy-search-boundaries.py
  locator: Saved report curator_calculations; probability_grid, predictive_entropy_is_not_information,
    hyperparameter_marginalization, hessian_negative_control, supplement_block_order,
    kernel_average_boundary, boundary_optimizer
  accessed_at: '2026-10-15T01:02:50.291440Z'
  snapshot_sha256: e69b30a010c8eebe5ebe8eacb9ffa8a38b4b5393dc4eb31fb4b21ca7434a98d6
  support: supports
  summary: 'Original bounded rational probability/matrix algebra with floating natural-log
    entropy; five isclose sites use rel_tol=0 and abs_tol=2e-14; actual copied-script
    outputs checked against the full saved result. No author-code execution, model
    training, benchmark replication or universal proof. Selected results: {"probability_grid":
    {"entropy_and_kl_identity_tolerance": 2e-14, "exact_posterior_martingale": true,
    "max_observed_kl_difference": 1.1102230246251565e-16, "positive_binary_channels":
    27}, "predictive_entropy_is_not_information": {"informative_binary_outcomes":
    {"mutual_information": 0.6931471805599453, "predictive_entropy": 0.6931471805599453,
    "predictive_entropy_drop": 0.6931471805599453, "target_entropy": 0.6931471805599453,
    "target_entropy_drop": 0.6931471805599453}, "scope": "Finite probability example,
    not a PES surrogate run.", "uninformative_four_outcomes": {"mutual_information":
    0.0, "predictive_entropy": 1.3862943611198906, "predictive_entropy_drop": 0.0,
    "target_entropy": 0.6931471805599453, "target_entropy_drop": 0.0}}, "hyperparameter_marginalization":
    {"construction": "Psi and S independent fair bits, Y=S xor Psi.", "marginal_mi_nats":
    0.0, "mean_conditional_mi_nats": 0.6931471805599453, "scope": "Demonstrates a
    general distinction between averaging conditional acquisitions and mutual information
    under a marginalized model; not a claim about a particular PES experiment."},
    "hessian_negative_control": {"determinants": ["5", "-3"], "eigenvalues_permitted":
    [1, -3], "eigenvalues_sampled": [-1, -5], "permitted_after_negative_diagonal_only_constraints":
    [["-1", "2"], ["2", "-1"]], "sampled_negative_definite": [["-3", "2"], ["2", "-3"]]},
    "supplement_block_order": {"K_diagonal": ["2", "3", "5", "7"], "correct_mean_variance":
    ["4", "2/3"], "correct_site_order_values": ["6", "12", "9", "10"], "declared_order":
    ["z1", "z2", "c1", "c2"], "literal_printed_mean_variance": ["9", "0"], "prediction":
    "f=z1", "printed_order_values": ["9", "10", "6", "12"], "scope": "Generic Gaussian
    block calculation; K and Kdag kept in their stated [z;c] order. Reordering every
    object consistently resolves the notation problem."}, "kernel_average_boundary":
    {"average_conditional_posterior_variance": "5/8", "noise_variance": 1, "posterior_variance_at_average_kernel":
    "2/3", "random_scalar_kernel_values": ["1", "3"], "scope": "Generic covariance
    example. Unbiased feature inner products do not make finite-feature posterior
    inference exact."}, "boundary_optimizer": {"derivative_at_maximizer": 1, "function":
    "f(x)=x on [0,1]", "maximizer": 1, "scope": "Logical domain boundary example,
    not a sampled stationary GP trajectory."}}'
- evidence_id: source-math-provenance
  kind: record_content
  reference: research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json
  locator: source_analysis.handoffs, root_readings and writer_preparation_reading
  accessed_at: '2026-10-15T01:02:50.291440Z'
  snapshot_sha256: ac133b0577888e01971897d94138e2a737302bc3613ac2f3bf344f359e173be2
  support: supports
  summary: Root assessed the separately attributed selective source readings and bounded
    mathematical research. Supporting agents are in the same author workflow and provide
    no independent scientific approval.
- evidence_id: source-error-original-lineage
  kind: record_content
  reference: research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json
  locator: calculation_lineage.artifacts, curator_calculations, draft_wording_lineage,
    research_correction_lineage and source_analysis
  accessed_at: '2026-10-15T01:02:50.291440Z'
  snapshot_sha256: ac133b0577888e01971897d94138e2a737302bc3613ac2f3bf344f359e173be2
  support: supports
  summary: Original and successor curator-written ES/PES calculators, first outputs
    and actual root reproductions retain exact bytes. Five explicit relative-tolerance
    settings changed comparison guards only; mathematical formulas and output bytes
    did not change. Original and successor mathematical assessments retain their separate
    execution attribution. Source formula caveats, official supplement extraction
    and raw acquisition precision remain explicit. These are not author-code execution,
    fabricated failed mathematical runs or canonical issue closures.
assessments:
- assessment_id: identity
  area: identity
  topic: Predictive Entropy Search
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - identity
  - hernandez2014
  - hernandez2014-supplement
  - hennig2012
  summary: Retain the narrow DRAFT identity within the documented search scope.
  details: PES and ES share ideal optimizer information under a consistent minimum/maximum
    conversion, but the source PES pipeline samples approximate maximizers and computes
    optimizer-conditioned predictive entropies instead of directly approximating minimizer
    probabilities and prospective loss. GP regression, derivative-observation GP models
    and monotonic virtual-derivative models supply distinct ingredients or constraints,
    not this acquisition. PESC, parallel PES, max-value entropy methods and the older
    sampling family are not automatic aliases or newly assessed extensions.
- assessment_id: definition
  area: evidence
  topic: Definition and source scope
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - hernandez2014-supplement
  - hennig2012
  - actual-record-reading
  summary: The maintained definition is supported within its stated method scope.
  details: The definition identifies the predictive-entropy rearrangement plus approximate
    maximizer draws and Gaussian constraint inference. It preserves the source maximization
    convention and does not present maximization of predictive entropy alone as PES
    or equate the approximation with exact optimizer information. The official main
    paper supports the iterative acquisition and its approximations; the official
    extracted appendix supports feature and constraint algebra. The JMLR ES source
    is explicitly comparative evidence. The appendix ZIP contains the four-page PDF,
    not executable code. Exact PDF/archive hashes and extraction lineage are retained,
    while original versus current root calculator executions remain correctly attributed.
- assessment_id: mapping
  area: grounding
  topic: 'Related AIO mapping: AIO:ActiveLearning'
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - mapping
  - hernandez2014
  - hernandez2014-supplement
  - hennig2012
  summary: related_match expresses the scoped semantic association without equivalence
    or ontology inheritance.
  details: 'The exact pinned ActiveLearning CLASS describes deliberately querying
    an information source for outputs. Both algorithms select informative black-box
    objective evaluations to update a surrogate and optimizer-location belief. related_match
    records that association without equating function optimization with annotation
    or pool-based classification, asserting subclass membership, or identifying either
    acquisition with the broad class. All thirteen selected exact node/incident contexts
    and twelve alternatives retain their original reading attribution.

    Alternatives:

    AIO:TrainingStrategy: General expensive black-box function optimization is not
    necessarily model training or preprocessing; training applications do not define
    these whole algorithms.

    AIO:RegressionAnalysis: The GP regression surrogate is a component, not the information-based
    sequential evaluation rule.

    AIO:SupervisedLearning: A generic input-output learning task omits the optimizer-location
    acquisition.

    AIO:UnsupervisedLearning: The methods collect objective-value observations and
    are not defined by unlabeled pattern learning.

    AIO:ReinforcementLearning: Exploration terminology does not identify a policy/environment
    reward-learning method or cumulative-regret objective.

    AIO:BayesianNetwork: A GP posterior and conditional information formula are not
    a DAG network architecture.

    AIO:Model: The records would denote search algorithms, not only a predictive surrogate
    artifact.

    AIO:Network: No interconnected-node architecture defines these acquisition mechanisms.

    AIO:MathematicalFunction: An acquisition formula alone does not identify the complete
    iterative algorithm.

    AIO:DeepActiveLearning: The methods do not require a deep neural network or the
    pinned annotation-focused architecture.

    AIO:KernelLayer: Use of covariance kernels does not make either optimizer a neural
    layer.

    AIO:MachineLearningTask: This broad task is less informative than the explicit
    query-learning association; it does not identify either algorithm.'
- assessment_id: optimizer-information-and-entropy-rearrangement
  area: evidence
  topic: optimizer-information-and-entropy-rearrangement
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - hennig2012
  - calculation-entropy-search
  summary: Supported within the stated assumptions and inspected passages.
  details: Main Eq2–3 uses mutual-information symmetry at fixed data, candidate and
    hyperparameters. The record adds the necessary well-defined entropy scope and
    consistent min/max conversion to ES. Finite channels check both entropy reductions
    against direct MI; an independent four-outcome observation has higher predictive
    entropy than an informative binary one, showing why the conditional term cannot
    be omitted. These are bounded probability examples, not PES GP executions.
- assessment_id: finite-feature-maximizer-samples
  area: evidence
  topic: finite-feature-maximizer-samples
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - hernandez2014-supplement
  - calculation-entropy-search
  summary: Supported within the stated assumptions and inspected passages.
  details: Main PDF3 and appendixA derive spectral random features and Gaussian posterior
    weights before numerical sample-function maximization. The kernel and differentiability
    qualifications are explicit. A fixed feature map defines a finite-rank GP exactly;
    expectation of its kernel does not commute through posterior conditioning. The
    rational scalar example gives average conditional variance5/8 versus2/3 at the
    mean kernel, supporting that boundary without claiming an observed PES error rate.
- assessment_id: approximate-maximizer-constraint-inference
  area: evidence
  topic: approximate-maximizer-constraint-inference
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - hernandez2014-supplement
  - calculation-entropy-search
  summary: Supported within the stated assumptions and inspected passages.
  details: Main PDF4–5 initially fixes zero gradient/off-diagonals, then substitutes
    sampled off-diagonal Hessian values; EP approximates remaining negative-diagonal
    and soft-value factors. The record correctly describes those as approximate constraints.
    Keeping off-diagonal2 while changing diagonal -3 to -1 turns eigenvalues(-1,-5)
    into(1,-3), so diagonal signs are insufficient after substitution. A linear objective
    on[0,1] also has a nonstationary boundary maximum. Neither witness asserts that
    every PES draw fails.
- assessment_id: candidate-comparison-and-predictive-variance
  area: evidence
  topic: candidate-comparison-and-predictive-variance
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - hernandez2014-supplement
  - calculation-entropy-search
  summary: Supported within the stated assumptions and inspected passages.
  details: Main Eq8–9 derives a truncated-Gaussian marginal variance for a valid covariance
    and strictly positive difference variance, then makes a further Gaussian moment
    approximation and adds observation noise. The strict comparison degenerates at
    x=S. Supplement Eq12 provides an integral definition; its later [c;tilde_m]/diag(0,tilde_V)
    display conflicts with stated [z;c] ordering unless every block is reordered.
    The exact generic block witness supports the notation caveat, not a tested software
    patch.
- assessment_id: hyperparameter-conditional-acquisition-average
  area: evidence
  topic: hyperparameter-conditional-acquisition-average
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - calculation-entropy-search
  summary: Supported within the stated assumptions and inspected passages.
  details: Algorithm2 and Eq10 average per-draw log-variance differences after pairing
    hyperparameters and approximate maximizers; noise belongs to each draw. This is
    a conditional-information average. The exact fair-bit XOR construction has mean
    conditional MI log2 and marginal MI0, disproving a general equality to the marginalized
    information objective. Reusing candidate-independent constraints is source-supported;
    no implementation efficiency measurement is asserted.
- assessment_id: sequential-query-and-final-recommendation
  area: evidence
  topic: sequential-query-and-final-recommendation
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  summary: Supported within the stated assumptions and inspected passages.
  details: Algorithm1 explicitly maximizes the acquisition, observes the objective,
    augments data and returns an optimizer of the final GP posterior mean. This separates
    the sampling rule from the recommendation and from the mode of the optimizer law.
    Neither approximate acquisition maximization nor a finite evaluation budget certifies
    the true global optimum.
- assessment_id: scope-and-boundaries
  area: consistency
  topic: Original maximizer-sampling and approximate predictive-entropy Bayesian optimizer,
    with conditional hyperparameter averaging and interior-constraint limitations
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - hernandez2014
  - hernandez2014-supplement
  - hennig2012
  - calculation-entropy-search
  - source-math-provenance
  summary: Mechanism, parameter assumptions and identity boundaries remain qualified.
  details: Ideal entropy identities require finite terms and appropriate measures.
    Finite features, numerical maximization, EP and moment matching remain separate
    approximations. Derivative constraints describe interior stationary points and
    cannot cover every bounded-domain optimum. Negative diagonals with nonzero off-diagonals
    need not give a negative-definite Hessian. Main C3 prose reverses an inequality
    and the stability paragraph uses undefined s; no unstated numerical repair is
    adopted. The supplement’s K/[z;c] ordering must be reconciled consistently with
    its displayed vector/noise blocks. Conditional hyperparameter information averaging
    is not generally marginal information. No general accuracy, regret, speed or convergence
    comparison with ES is established.
- assessment_id: actual-maintained-fields
  area: provenance
  topic: All captured maintained fields
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - actual-record-reading
  - identity
  - mapping
  - hernandez2014
  - hernandez2014-supplement
  - hennig2012
  summary: Root reassessed the complete current record after canonical capture; DRAFT
    remains.
  details: 'Root reread the complete actual YAML after both canonical captures and
    reassessed its six claims, locators, definition, kind, related ActiveLearning
    mapping and limitations against prepared narratives and the freshly reread primary
    pages. All117 selected definitions and13 exact AIO node/edge contexts were read
    during current prewrite review. Full actual322 neighbor YAMLs and12 exact content
    groups were read; all1458 occurrences reconstructed. Supporting all1157 identity
    fields and898/393 frontier candidate/disposition assessment remains attributed.
    Source/download timestamps are not review-reading timestamps. Root read the complete
    copied v2 calculator and current postcapture output; exact rational masses/algebra
    and floating logs with five absolute-only comparisons remain distinct. The original/successor/root
    execution lineage and preparation six-versus-five count failure are retained;
    no mathematical run failure or canonical issue is invented. Supporting audit found
    no new defect; its primary/source run is precreation and its actual correspondence
    check is postcapture, with the source and byte-audit roles separated. No independent
    scientific approval or saturation is claimed. PES approximate random-feature maximizers
    and Gaussian/EP predictive-entropy inference define this identity. Conditional
    hyperparameter MI averaging is not generally marginalized MI; the retained XOR
    construction establishes that limited distinction. Rereads: After capture325 at00:59:15Z:
    ES native-text8–13,16,19 and visuals11,13; PES main native-text2–5 and visuals4,5;
    supplement native-text1–4 and visuals2,4. Earlier complete root text scopes remain
    separately dated. Fresh renders are in /private/tmp/aimech-batch324-root-postcapture-visuals.'
- assessment_id: source-error-and-original-lineage
  area: provenance
  topic: Source caveats and original calculation history
  outcome: supported
  target_ids:
  - AIMech:PredictiveEntropySearch
  evidence_ids:
  - source-error-original-lineage
  summary: Source interpretation, TEMP clarifications and actual calculation lineage
    remain distinct.
  details: Original and successor curator-written checks retain exact code, first
    outputs and actual execution/reproduction receipts. The five-site tolerance correction
    preserves its preimage and identical output; the earlier builder count-preflight
    failure is not misrepresented as a failed mathematical execution. Raw acquisition
    and archive extraction remain separate from schema-compatible source timestamps.
    Source caveats are not author-issued errata or maintained-record issue closures.
    Bounded algebra and floating entropy checks do not validate the full ES/PES numerical
    pipeline or general accuracy/convergence claims.
findings: []
actions: []
limitations:
- Author self-review, not independent scientific approval or DRAFT promotion.
- Ideal entropy identities require finite terms and appropriate measures. Finite features,
  numerical maximization, EP and moment matching remain separate approximations. Derivative
  constraints describe interior stationary points and cannot cover every bounded-domain
  optimum. Negative diagonals with nonzero off-diagonals need not give a negative-definite
  Hessian. Main C3 prose reverses an inequality and the stability paragraph uses undefined
  s; no unstated numerical repair is adopted. The supplement’s K/[z;c] ordering must
  be reconciled consistently with its displayed vector/noise blocks. Conditional hyperparameter
  information averaging is not generally marginal information. No general accuracy,
  regret, speed or convergence comparison with ES is established.
- This is qualified author self-review with supporting agents in the same author workflow;
  no independent scientific approval or DRAFT promotion is implied.
- Historical research covered 708 native and 442 AIO records, 117 selected definitions
  and nine full native neighbors. The actual prewrite scope is 715 native and 442
  AIO records, all scoped synonyms, four ignored/hidden-inclusive whole-checkout searches
  and two freshly assessed batch322 neighbors; historical reading is not relabeled
  as fresh root reading.
- The original curator-written calculator uses exact rational probability masses and
  matrix examples with floating natural logarithms. The successor explicitly sets
  rel_tol=0 and abs_tol=2e-14 at five comparison sites; original and successor code,
  actual first/root executions and unchanged result bytes remain distinct. No GP fitting,
  EP loop, random-feature sampling, acquisition optimization or author-code replication
  was performed by those checks.
- The tolerance clarification occurred in TEMP before curation and preserves its earlier
  count-preflight failure. It is not a fabricated failed mathematical run, canonical
  finding, author erratum or issue closure.
- Raw source acquisition/extraction precision is retained beside whole-second record
  metadata. Download dates and bibliography are distinct from actual source-reading
  scope.
notes:
- Empty findings reflect actual root assessment of this selected captured record only;
  no unrelated finding closure or literature saturation is asserted.
- Source caveats and preserved calculation or wording lineage remain distinct; no
  maintained-record finding or issue closure is invented from them.
tags:
- native-concepts
- self-review
- discovery-ongoing
- bayesian-optimization
- information-acquisition
- predictive-entropy-search
```
