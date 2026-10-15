# Scientific self-review of FractalNet DropPath, NASNet Scheduled DropPath and Swapout

- Review: 20261015T091809Z-fractalnet-droppath-nasnet-scheduled-droppath-and-swapout
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T09:05:25.347287Z
- Finished UTC: 2026-10-15T09:18:09.623223Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The explicit three-target batch was assessed through 18 source-linked claims, definitions, three declared primary sources, three qualified related mappings and 20 individual limitations. Retain the two source-qualified DropPath procedures and the compatible-tensor Swapout construction separately. Actual capture, root postcapture reading and completed required checks are bound. The separately appended PTN source lead is pending and outside the reviewed records. Records remain DRAFT; no new concrete findings were identified within the declared scope.

## Scope And Provenance

Complete explicitly selected three-procedure batch. Shared path-regularization context does not establish one universal algorithm or a merged identity.

Selection: Exact maintained IDs AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout from actual cohort 337 creation.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base d76936e4e77768d08b0cdd7f505ed34c9f50a5f0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FractalNetDropPath | data/curated/FractalNetDropPath.yaml | maintained | FractalNet DropPath |
| AIMech:NASNetScheduledDropPath | data/curated/NASNetScheduledDropPath.yaml | maintained | NASNet Scheduled DropPath |
| AIMech:Swapout | data/curated/Swapout.yaml | maintained | Swapout |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout | Actual command completed with exit0; exact output is retained. |
| just vendored-check | passed | True | AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout | Actual command completed with exit0; exact output is retained. |
| uv run --locked aimech check-source | passed | True | AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout | Actual command completed with exit0; exact output is retained. |
| just render | passed | True | AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout | Actual command completed with exit0; exact output is retained. |
| just render-check | passed | True | AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout | Actual command completed with exit0; exact output is retained. |
| git diff --check | passed | True | AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout | Actual command completed with exit0; exact output is retained. |

## Scientific And Domain Assessments

### Claim fractal-host-and-procedure

evidence: supported. Targets: AIMech:FractalNetDropPath.

Section 3 defines the fractal join host and explicitly contrasts its unprivileged learned inputs with residual pass-through roles. The scope identifies the protocol without claiming that the entire host is itself a regularizer.

### Claim local-nonempty-join-selection

evidence: supported. Targets: AIMech:FractalNetDropPath.

The local bullet explicitly requires survival of at least one input. The claim preserves that requirement and leaves the unspecified nonempty-mask enforcement law open; it does not assert final Bernoulli independence.

### Claim global-single-column-selection

evidence: supported. Targets: AIMech:FractalNetDropPath.

The global bullet restricts the selected network-wide path to a column. Cross-block coupling follows from that single choice. No uniform column law or exact expected depth is invented.

### Claim mean-over-active-inputs

evidence: supported. Targets: AIMech:FractalNetDropPath.

The source says to average active inputs. The finite-sum form and one-input boundary are direct restatements with nonempty and shape conditions, not an author-code replication or a new stochastic law.

### Claim reported-minibatch-mixture

evidence: supported. Targets: AIMech:FractalNetDropPath.

The 50/50 mode mixture, minibatch refresh and 15% local setting have separate precise locations. Ordinary dropout is retained as a co-used procedure, and the diagram is not elevated to a deterministic mode schedule.

### Claim full-graph-and-extracted-column-use

evidence: supported. Targets: AIMech:FractalNetDropPath.

Tables 1 and 4 and the surrounding text evaluate the full graph and extracted columns. The claim records the available prediction choices and the discussed trade-off without adopting a quantitative benchmark effect or ensemble-equality claim.

### definition assessment

evidence: supported. Targets: AIMech:FractalNetDropPath.

The definition combines the two source-defined sampling modes with their shared active-input mean. It does not equate the regularizer with the host architecture or imply independent repaired masks.

### mapping assessment

grounding: supported. Targets: AIMech:FractalNetDropPath.

The exact pinned TrainingStrategy CLASS and all 15 examined contexts were retained in research. Its preprocessing genus prevents an unqualified subclass reading. The single related match is the root-accepted association; no additional architecture, DropoutLayer or RegularizationLayer mapping is asserted.

### source assessment

provenance: supported. Targets: AIMech:FractalNetDropPath.

Only larsson2017-arxiv-v4 is declared and explicitly cited in the definition and all six claims. The exact source version, original acquisition time and separately attributed research/root reading scopes remain retained. Full-text access does not assert full implementation or benchmark inspection.

### limitations assessment

scope: supported. Targets: AIMech:FractalNetDropPath.

All 7 individual limitations are retained exactly and assessed separately below. They preserve source-specific mask, schedule, inference, implementation and empirical boundaries; no missing controls or universal guarantees are supplied.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:FractalNetDropPath.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 209 and distinct residuals. The supporting historical identity scope is: This candidate denotes the original FractalNet local/global DropPath protocol, not the complete fractal architecture, a trained column, NASNet Scheduled DropPath, stochastic depth or a universal modern library DropPath function. Local and global modes remain within one named procedure. No bare DropPath alias is asserted. The retained research snapshot contained 742 native and 442 pinned AIO records. Normalized IDs, labels, aliases and all scoped synonyms had no queried collision. Four whole-checkout searches included ignored and hidden files and returned 714 occurrences reconstructed into one pending-label content. A separate final-name search returned no hits across the same four checkouts, and a bounded AST identity projection of 200 top-level TEMP content modules found no queried identity match. Research traversed all 908 main and 393 nested frontier objects, read 42 selected full objects, 38 semantic definitions and five full native neighbors, and examined 15 exact AIO CLASS contexts with 84 incident-edge rows. These are dated historical findings, not a fresh creation-time absence or saturation claim. Existing owner 209 supplies the shared discovery context; its old DropBlock-paper URL is preserved as a historical lead, not used as defining evidence for either procedure.

### Retained limitation 1

scope: supported. Targets: AIMech:FractalNetDropPath.

The source states nonempty survival but not the enforcement algorithm. Positive all-drop probability under unconstrained independent draws is an elementary boundary, not a reported source defect.

### Retained limitation 2

scope: supported. Targets: AIMech:FractalNetDropPath.

The limits distinguish unspecified global selection probabilities from the specified experimental mode mixture and local setting.

### Retained limitation 3

scope: supported. Targets: AIMech:FractalNetDropPath.

The preferred hand witness respects nonnegative features after the demonstrated ReLU and applies a permitted subsequent affine/nonlinear composition. Its singleton distribution is explicitly illustrative, not the paper's repaired sampling law. The original generic witness is retained as historical context.

### Retained limitation 4

scope: supported. Targets: AIMech:FractalNetDropPath.

The claim does not equate an absent current gradient path with frozen optimizer or running state. No implementation was inspected, so batching, repair and extracted-network normalization stay open.

### Retained limitation 5

scope: supported. Targets: AIMech:FractalNetDropPath.

The paper jointly uses other training choices and labels its supervision explanation a hypothesis. The limit avoids causal or theorem-level claims beyond this evidence.

### Retained limitation 6

scope: supported. Targets: AIMech:FractalNetDropPath.

The retained v4 identity is explicit. Failed alternate access is not equivalence evidence, and the generic term is not imposed as an alias across distinct procedures.

### Retained limitation 7

scope: supported. Targets: AIMech:FractalNetDropPath.

The source allows possible broader hosts while demonstrating CNNs. Compatibility and nonempty inputs are explicit mathematical prerequisites; the stated reading scope is not an implementation certificate.

### Claim named-cell-training-regularizer

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

The name and training role occur in Section 4 and Appendix A.5. The distinct controller description in Appendix A.2–A.3 supports keeping the regularizer separate from architecture search.

### Claim operation-bearing-cell-edges

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

Appendix A.5 explicitly points to the yellow operation boxes in Figure 4. The claim uses that graph unit without importing an identity-edge exclusion or treating all scalar activations as separate path masks.

### Claim linear-training-time-drop-schedule

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

The defining sentence supplies linear progression over training, contrasted with a fixed rate. Endpoints, progress indexing and depth adjustments are absent from these passages and remain limitations rather than invented formulas.

### Claim paper-level-test-scaling-convention

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

The claim attributes the prose scaling convention and its cited-method analogy precisely. Its second sentence preserves the unresolved choice of keep probability when the training schedule changes.

### Claim distinct-from-ordinary-output-dropout

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

Appendix A.7 explicitly places a separate dropout setting at the final softmax matrix. This prevents that reported 0.5 from being misread as the ScheduledDropPath endpoint; no empirical benefit is inferred.

### Claim host-and-empirical-protocol-boundary

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

The source describes multiple NASNet training choices and explicitly states that no residual connections are added between convolutional cells. The claim restricts the named regularizer and does not transfer whole-system performance or efficiency claims.

### definition assessment

evidence: supported. Targets: AIMech:NASNetScheduledDropPath.

The definition isolates the source-named temporal cell-edge regularizer. It avoids inventing schedule endpoints, inference coefficients or a complete architecture-search procedure.

### mapping assessment

grounding: supported. Targets: AIMech:NASNetScheduledDropPath.

The exact pinned TrainingStrategy CLASS and all 15 examined contexts were retained in research. Its preprocessing genus prevents an unqualified subclass reading. The single related match is the root-accepted association; no additional architecture, DropoutLayer or RegularizationLayer mapping is asserted.

### source assessment

provenance: supported. Targets: AIMech:NASNetScheduledDropPath.

Only zoph2018-cvpr is declared and explicitly cited in the definition and all six claims. The exact source version, original acquisition time and separately attributed research/root reading scopes remain retained. Full-text access does not assert full implementation or benchmark inspection.

### limitations assessment

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

All 7 individual limitations are retained exactly and assessed separately below. They preserve source-specific mask, schedule, inference, implementation and empirical boundaries; no missing controls or universal guarantees are supplied.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:NASNetScheduledDropPath.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 209 and distinct residuals. The supporting historical identity scope is: This candidate denotes the original NASNet ScheduledDropPath training procedure, not the NASNet architecture-search controller, a complete NASNet network, FractalNet DropPath, stochastic depth or every schedule called DropPath. The retained identity is qualified by the NASNet source and leaves unspecified replication controls open. No bare DropPath alias is asserted. The retained research snapshot contained 742 native and 442 pinned AIO records. Normalized IDs, labels, aliases and all scoped synonyms had no queried collision. Four whole-checkout searches included ignored and hidden files and returned 714 occurrences reconstructed into one pending-label content. A separate final-name search returned no hits across the same four checkouts, and a bounded AST identity projection of 200 top-level TEMP content modules found no queried identity match. Research traversed all 908 main and 393 nested frontier objects, read 42 selected full objects, 38 semantic definitions and five full native neighbors, and examined 15 exact AIO CLASS contexts with 84 incident-edge rows. These are dated historical findings, not a fresh creation-time absence or saturation claim. Existing owner 209 supplies the shared discovery context; its old DropBlock-paper URL is preserved as a historical lead, not used as defining evidence for either procedure.

### Retained limitation 1

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

The named schedule is clear while its numeric controls are not printed in the inspected method. No endpoints or software defaults are imported.

### Retained limitation 2

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

The paper names operation-bearing edges but not all exceptional or coupled mask cases. The limit avoids silently importing FractalNet's different safeguard.

### Retained limitation 3

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

The prose does not identify a time-indexed inference probability or prove nonlinear ensemble equality. This is an evidence gap rather than a demonstrated implementation failure.

### Retained limitation 4

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

Momentum, weight decay and other state make a blanket frozen-parameter inference unjustified. No specific unseen implementation behavior is asserted.

### Retained limitation 5

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

Training-time progression, graph-mask units and training-example ordering are distinct identities. The contextual comparisons do not become extra source-backed mechanism claims about uninspected later implementations.

### Retained limitation 6

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

The limit keeps the paper's combined NASNet system evidence separate from an isolated causal or universal claim about one regularizer.

### Retained limitation 7

scope: supported. Targets: AIMech:NASNetScheduledDropPath.

The source version and selective reading scope are explicit. Missing replication details remain open; no full-paper or author-code inspection is asserted.

### Claim compatible-stochastic-path-sums

evidence: supported. Targets: AIMech:Swapout.

Section 3 defines already computed F_i and per-tensor iid Bernoulli entries before Equation 2, with a directed acyclic surrounding network. The claim preserves the general tensor scope rather than forcing every contribution to be a function of one input. Compatibility is the domain requirement of the displayed addition.

### Claim unitwise-four-choice-specialization

evidence: supported. Targets: AIMech:Swapout.

Equation 3, Figure 1 and the explicit four outcomes support unitwise zero/input/transformation/sum choices. The distinction concerns selector patterns, and the statement avoids claiming four distinct values or one scalar shared across every unit. Section 3.2 independently defines the scalar whole-block comparison.

### Claim shared-parameter-stochastic-training

evidence: supported. Targets: AIMech:Swapout.

Section 3.1 explicitly describes a randomly sampled family with tied parameters, and the training paragraph names SGD in the reported experiments. The claim does not inherit the defective pointwise step in the generic stability sketch or turn an experimental optimizer into a universal requirement.

### Claim depth-dependent-selector-configuration

evidence: supported. Targets: AIMech:Swapout.

The source permits separate selector probabilities and Table 2 defines Linear(a,b) by position from first to last block. The claim carefully distinguishes depth scheduling from temporal annealing and avoids treating the reported setting as an optimum theorem.

### Claim deterministic-and-stochastic-inference

evidence: supported. Targets: AIMech:Swapout.

The source lists both local expectation replacement and sampled prediction averaging. Its ReLU discussion supports the nonlinear qualification. No fixed number of samples, exact whole-network expectation or accuracy guarantee is asserted.

### Claim coupled-special-cases-and-skipforward

evidence: supported. Targets: AIMech:Swapout.

Section 3.2 states the dropout-on-sum, scalar residual dropout and complementary SkipForward formulas. These require coupled, shared or complementary masks, unlike the studied independent pair. The source comparison supports an operational distinction without forcing aliases or extra concepts.

### definition assessment

evidence: supported. Targets: AIMech:Swapout.

The definition names the general Bernoulli-selected compatible-tensor computation, shared-parameter training and the two source inference choices. It is a procedure identity, broader than the main residual-host experiment but not all neural regularization.

### mapping assessment

grounding: supported. Targets: AIMech:Swapout.

Root accepted only related_match to the exact pinned TrainingStrategy node. Its broad preprocessing wording supports a qualified association, not identity or subclassing. ResidualNeuralNetwork remains an inspected host alternative rather than a required mapping for generic Equation 2; additive penalty and Gaussian/dropout layer targets are not its identity.

### source assessment

provenance: supported. Targets: AIMech:Swapout.

Only singh2016 is declared and is cited by the definition and all six claims. Original raw acquisition precision and initial failures are retained. The official supplementary link returned PTN material, which is excluded; arXiv metadata is context only. Table-caption qualification is a separate pre-draft research correction, not a canonical issue.

### limitations assessment

scope: supported. Targets: AIMech:Swapout.

All 6 individual limitations are retained exactly and assessed separately below. They preserve source-specific mask, schedule, inference, implementation and empirical boundaries; no missing controls or universal guarantees are supplied.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:Swapout.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 227 and distinct residuals. The supporting historical identity scope is: Swapout denotes the original 2016 stochastic compatible-tensor combination procedure, with a studied identity-plus-transformation specialization and explicit deterministic or sampled inference. It is retained separately from whole-branch StochasticDepth, recurrent Zoneout, continuous complementary Shake-Shake and shared-switch ShakeDrop. Restricted SkipForward is comparison context, not a forced alias or separate record. Historical research on 15 October 2026 compared 745 native and 442 pinned AIO records, normalizing all 4,752 ID/local-ID/name/alias/scoped-synonym values without a candidate collision. Four ignored/hidden-inclusive searches accounted for 717 occurrences in seven completely read strings: existing owner227, ordinary-English software comments and neighboring discovery context. All 60 selected definitions, 44 query-selected complete frontier objects, four full native neighbors and 13 exact AIO nodes with 53 incident edge rows were read. The query covered both 908 main and 393 nested frontier entries mechanically, without a claim of reading every unrelated body. Owner227 already represents this lead; its old Zoneout URL is historical discovery context, whereas the acquired official 2016 Swapout PDF supplies primary evidence. This is bounded historical research, not a future creation-time absence or saturation assertion.

### Retained limitation 1

scope: supported. Targets: AIMech:Swapout.

Shape/probability/acyclic prerequisites follow from the displayed tensor operation. Different mask dependence changes its law; the all-zero omission in the Equation 2 set is reconciled with permitted selectors and explicit Equation 3 zero outcome. No uninspected implementation is certified.

### Retained limitation 2

scope: supported. Targets: AIMech:Swapout.

The hand example is inside the generic Equation 2 family, with v explicitly a parameter. The four derivative magnitudes at 2*pi/3 average to 1/2 while the maximum-global-Lipschitz member has zero derivative. This is a bounded failure of that pointwise inference, not a ReLU-residual instability theorem or full review of the cited stability result.

### Retained limitation 3

scope: supported. Targets: AIMech:Swapout.

The finite two-mask hand example directly distinguishes an expectation after ReLU from ReLU after expectation. It does not require a benchmark or code. Sampling predictions is retained as approximation rather than exact finite-sample ensemble inference.

### Retained limitation 4

scope: supported. Targets: AIMech:Swapout.

Independent masks independent of the feature pair give the displayed variance excess. Correlation between X and Y cancels from that difference; interior equality also includes both features vanishing almost surely. Conditional versus unconditional means and alternate mask dependence remain explicit.

### Retained limitation 5

scope: supported. Targets: AIMech:Swapout.

Root corrected the earlier research note that inserted deterministic into the Table 3 caption. The current limitation treats the caption as inference-ambiguous, correctly notes the stochastic column, and uses the first deterministic row only to reject a universal deterministic improvement claim. The paper itself qualifies most settings and reports a weaker preliminary ImageNet result.

### Retained limitation 6

scope: supported. Targets: AIMech:Swapout.

Only the exact official main paper is declared. Its acquired time, build date and publication year are kept distinct. The mismatched PTN supplement is excluded and separately retained as a future source lead; the record does not pretend that an inaccessible correct supplement, preprint PDF, author code or benchmark was inspected.

### Captured bytes, accepted science and frontier accounting

consistency: supported. Targets: AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath, AIMech:Swapout.

All three captured records equal the actual write payloads and report entries. Exact support covers 18 claims and 20 limitations. Only existing owners 209 and 227 changed; all 906 other prior main and 393 nested values remain unchanged. One pending PTN source lead was appended and remains outside the three reviewed records. Six required checks passed. No global exhaustion or DRAFT promotion is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath. FractalNet combines local nonempty join selection and global column selection with active-input averaging. NASNet Scheduled DropPath applies a training-time probability schedule to operation-bearing cell edges. These different selection units and schedules remain two source-qualified procedures within the existing owner 209; neither gets a bare DropPath alias.
- retain: AIMech:Swapout. Swapout is the original stochastic compatible-tensor combination procedure with a unitwise independent two-selector specialization and explicit inference alternatives. Coupled SkipForward, scalar residual dropping and other neighboring regularizers do not become exact aliases. Existing owner 227 is retained.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| captured-inputs | /private/tmp/aimech-droppath-swapout-cohort337-capture.json | context_only | Actual canonical inspect output; all captured input hashes rechecked. Inspection alone is not scientific approval. |
| postcapture-reading | /private/tmp/aimech-droppath-swapout-cohort337-root-postcapture-reading.json | context_only | Actual root full-target assessment after capture and completed checks; selective primary scopes are stated separately. |
| scientific-support | /private/tmp/aimech-droppath-swapout-cohort337-review-preparation-20261015/scientific-support.prepared.json | context_only | Attributed same-author support of all 18 accepted claims and 20 individual limitations. This is preparation DATA, not itself an actual canonical capture. |
| actual-write | /private/tmp/aimech-droppath-swapout-cohort337-write.json | context_only | Actual creation receipt binds three records, report pair and CREATE history. |
| discovery-report | research/discovery/20261015T090241Z-fractalnet-droppath-nasnet-scheduled-droppath-and-swapout.json | context_only | Record mirrors are exact. Only existing owners 209 and 227 changed; all 906 other prior main and 393 nested objects are unchanged. One separately assessed pending PTN source lead was appended; it is not a fourth record or reviewed scientific target. |
| creation-history | history/reports/fractalnet-droppath-nasnet-scheduled-droppath-and-swapout/2026-10-15T090302Z-codex-40b373.yaml | context_only | Actual append-only CREATE sidecar; review and publication are separate later actions. |
| pinned-aio | sources/aio/aio.json; Exact AIO:TrainingStrategy with retained inspected alternatives and incident edges; its preprocessing genus is not imposed as an is-a relation. | context_only | Exact snapshot supports three qualified related mappings; no upstream equivalence or subclass assertion. |
| identity-assessment | /private/tmp/aimech-cohort337-root-decisions.json | context_only | Actual root decisions bind fresh ignored/hidden-inclusive scans and owners 209/227 and one pending source-lead accounting; no manual rereading of every hit by this generator is claimed. |
| droppath-nonnegative-host-addendum | /private/tmp/aimech-droppath-research-20261015/analytic-nonnegative-host-addendum.json; FractalNet limitation 3; Section 3.3, PDF p. 5, and retained analytical addendum. | context_only | The separate pre-draft addendum supplies nonnegative 0/2 features followed by affine shift and ReLU, retaining the original generic witness. The illustrative singleton law is not claimed to be the paper's mask distribution. This is analytical context, not a canonical finding. |
| swapout-caption-qualification | /private/tmp/aimech-swapout-research-20261015/table-caption-correction.json; Official Swapout PDF p. 7, Table 3 caption and first row; nearby PDF p. 6 prose. | context_only | The original curator note inserted deterministic into an inference-unspecified caption. The successor preserves the numerical row but withdraws an unambiguous-caption contradiction, noting the stochastic column and qualified prose. This pre-draft correction preserves original artifacts and is not a canonical finding or author erratum. |
| src-larsson2017-arxiv-v4 | https://arxiv.org/pdf/1605.07648v4; Historical supporting research read all 11 native-text pages and visuals 2, 4 and 5; draft preparation reread text 4–8 and visual 4. Root research read text 1, 4–8 and visuals 4–5, then complete accepted draft/support. Definition and six claims use Sections 3–4, PDF pp. 4–8. Access, source build and version dates remain distinct. No author code or benchmark inspection is claimed. | supports | arXiv:1605.07648v4, submitted 26 May 2017 at 18:53:56 UTC; retained 11-page PDF identifying publication at ICLR 2017. The PDF build date of 30 May 2017 and HTTP Last-Modified date in 2023 are file metadata, not publication dates. Acquisition time is access metadata, not a claim of full reading. |
| src-zoph2018-cvpr | https://openaccess.thecvf.com/content_cvpr_2018/papers/Zoph_Learning_Transferable_Architectures_CVPR_2018_paper.pdf; Historical supporting research read native text 1–5 and 11–12, visuals 5 and 11; draft preparation reread text 4–5 and 11–12 plus visual 11. Root research read text 1, 4–5, 11 and visuals 5/11, then additionally full native text p. 12 during draft assessment. This is selective reading of the official 14-page CVPR PDF, not a full-paper or author-code audit. | supports | Official CVPR 2018 open-access PDF, 14 pages including Appendices A and B, printed pp. 8697–8710. This retained version is distinct from the arXiv:1707.07012 versions; no byte equivalence is assumed. Acquisition time is access metadata, not a claim of full reading. |
| src-singh2016 | https://proceedings.neurips.cc/paper_files/paper/2016/file/c51ce410c124a10e0db5e4b97fc2af39-Paper.pdf; Historical source agent read all nine official main-paper native-text pages and visuals 3–8. Root read text 3–8 and visuals 3–4, then visual p. 7 during draft acceptance. Definition and six claim locators lie in main text 3–6. The mismatched PTN supplement was read only for identification and is excluded from Swapout evidence. No author code or benchmark execution is claimed. | supports | Official NIPS 2016 proceedings PDF, nine local pages; Advances in Neural Information Processing Systems 29, bibliographic pp. 28–36. The PDF modification timestamp of 19 November 2016 is file-build metadata, not an asserted publication day. No equivalence to the separately indexed arXiv preprint is asserted. Acquisition time is access metadata, not a claim of full reading. |
| record-fractal | data/curated/FractalNetDropPath.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| record-nasnet | data/curated/NASNetScheduledDropPath.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| record-swapout | data/curated/Swapout.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| check-gate | /private/tmp/aimech-droppath-swapout-cohort337-check-gate.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-vendor | /private/tmp/aimech-droppath-swapout-cohort337-check-vendor.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-check-source | /private/tmp/aimech-droppath-swapout-cohort337-check-check-source.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-render | /private/tmp/aimech-droppath-swapout-cohort337-check-render.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-render-check | /private/tmp/aimech-droppath-swapout-cohort337-check-render-check.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-diff | /private/tmp/aimech-droppath-swapout-cohort337-check-diff.json | context_only | Actual completed command and retained output before this new review was saved. |

## Limits And Additional Notes

- Author self-review with attributed supporting agents is not independent scientific approval. Full_text describes source access; historical supporting and selective root reading scopes remain individually attributed.
- FractalNet retains nonempty local joins, unspecified enforcement and column-selection laws, experimental mode mixture, and full-graph versus extracted-column use. Active-input averaging does not establish an exact nonlinear ensemble expectation.
- NASNet Scheduled DropPath retains the training-time linear schedule and paper-level inference description while leaving numeric endpoints, sharing, identity-edge exceptions and the inference time index unresolved. No later implementation defaults are imported.
- Swapout retains compatible shapes, mask dependence, conditional variance assumptions, nonlinear inference and the bounded generic Lipschitz counterexample. No universal stability, convergence or benchmark advantage is asserted.
- The FractalNet arXiv v4, official NASNet CVPR 2018 PDF and official Swapout NIPS 2016 PDF are distinct exact sources. The wrongly linked PTN supplement is excluded from Swapout evidence and remains a separately pending lead, not a fourth reviewed target.
- The nonnegative-host illustration addendum and Swapout caption qualification retain their original research artifacts and chronology. They are preparation provenance, not fabricated resolved canonical findings.
- No calculator, author code, model training or benchmark was executed for this review. The three TrainingStrategy mappings are qualified related associations, not equivalence or subclass assertions; the pinned preprocessing genus is not imposed on the procedure definitions.
- Required checks are actual retained completed logs, including historical failed attempts if present. Canonical validation/save/check of this new review remain separate actions. Records stay DRAFT; no upstream change or global exhaustion is inferred.
- Root read complete actual canonical records, report Markdown, CREATE history and owners209/227/pending908, and all prepared claim/individual-limitation assessments. Final postcapture assessment rechecks that these previously read complete bytes equal the captured and accepted payloads. Root primary reading: FractalNet v4 text1,4–8 and visuals4–5; NASNet official text1,4–5,11–12 and visuals5/11; Swapout official text3–8 and visuals3–4/7. Supporting source-agent full or selective reading is separately attributed in retained ledgers. The excluded PTN supplement was identified separately. No author implementation or benchmark execution, and no manual reading of every unrelated inherited frontier body, is claimed.
- Retain all three source-qualified algorithm identities. FractalNet local/global selection uses nonempty active-input means and unspecified enforcement/column laws. NASNet schedules operation-bearing edge suppression over training, without invented endpoints or inference-time index. Swapout combines compatible tensors with explicit selector coupling and inference alternatives; the bounded Lipschitz, conditional variance and nonlinear expectation arguments do not imply a model-instability or universal performance theorem. All18 claims,20 limitations, definitions,3primarysources and related TrainingStrategy mappings are supported at their declared scope. Original pre-curation caption qualification and nonnegative-host addendum remain distinct from canonical findings. Actual owners209/227 resolve these records;906other prior main393nested objects remain exact and PTN remains pending908. Six actual checks passed; records remain DRAFT. No required concrete finding arose.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
title: Scientific self-review of FractalNet DropPath, NASNet Scheduled DropPath and
  Swapout
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author assessment with attributed same-author supporting
    source and mathematical agents. No external or independent scientific approval
    is asserted.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The explicit three-target batch was assessed through 18 source-linked claims,
  definitions, three declared primary sources, three qualified related mappings and
  20 individual limitations. Retain the two source-qualified DropPath procedures and
  the compatible-tensor Swapout construction separately. Actual capture, root postcapture
  reading and completed required checks are bound. The separately appended PTN source
  lead is pending and outside the reviewed records. Records remain DRAFT; no new concrete
  findings were identified within the declared scope.
scope:
  description: Complete explicitly selected three-procedure batch. Shared path-regularization
    context does not establish one universal algorithm or a merged identity.
  selection: Exact maintained IDs AIMech:FractalNetDropPath, AIMech:NASNetScheduledDropPath,
    AIMech:Swapout from actual cohort 337 creation.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  exclusions:
  - target: Perspective Transformer Nets pending source lead
    reason: A separately accounted source lead, not a created record or reviewed scientific
      target in this batch.
  - target: Later generic DropPath implementations, complete FractalNet/NASNet architectures
      and other regularizers
    reason: Context only; no resolution beyond the three specified procedures and
      inspected source versions.
  - target: Author implementations, training and benchmark reproduction
    reason: Outside the retained source-reading and bounded hand-reasoning scopes.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  rationale: FractalNet combines local nonempty join selection and global column selection
    with active-input averaging. NASNet Scheduled DropPath applies a training-time
    probability schedule to operation-bearing cell edges. These different selection
    units and schedules remain two source-qualified procedures within the existing
    owner 209; neither gets a bare DropPath alias.
  evidence_ids:
  - record-fractal
  - record-nasnet
  - src-larsson2017-arxiv-v4
  - src-zoph2018-cvpr
  - identity-assessment
- action: retain
  target_ids:
  - AIMech:Swapout
  rationale: Swapout is the original stochastic compatible-tensor combination procedure
    with a unitwise independent two-selector specialization and explicit inference
    alternatives. Coupled SkipForward, scalar residual dropping and other neighboring
    regularizers do not become exact aliases. Existing owner 227 is retained.
  evidence_ids:
  - record-swapout
  - src-singh2016
  - identity-assessment
  - pinned-aio
limitations:
- Author self-review with attributed supporting agents is not independent scientific
  approval. Full_text describes source access; historical supporting and selective
  root reading scopes remain individually attributed.
- FractalNet retains nonempty local joins, unspecified enforcement and column-selection
  laws, experimental mode mixture, and full-graph versus extracted-column use. Active-input
  averaging does not establish an exact nonlinear ensemble expectation.
- NASNet Scheduled DropPath retains the training-time linear schedule and paper-level
  inference description while leaving numeric endpoints, sharing, identity-edge exceptions
  and the inference time index unresolved. No later implementation defaults are imported.
- Swapout retains compatible shapes, mask dependence, conditional variance assumptions,
  nonlinear inference and the bounded generic Lipschitz counterexample. No universal
  stability, convergence or benchmark advantage is asserted.
- The FractalNet arXiv v4, official NASNet CVPR 2018 PDF and official Swapout NIPS
  2016 PDF are distinct exact sources. The wrongly linked PTN supplement is excluded
  from Swapout evidence and remains a separately pending lead, not a fourth reviewed
  target.
- The nonnegative-host illustration addendum and Swapout caption qualification retain
  their original research artifacts and chronology. They are preparation provenance,
  not fabricated resolved canonical findings.
- No calculator, author code, model training or benchmark was executed for this review.
  The three TrainingStrategy mappings are qualified related associations, not equivalence
  or subclass assertions; the pinned preprocessing genus is not imposed on the procedure
  definitions.
- Required checks are actual retained completed logs, including historical failed
  attempts if present. Canonical validation/save/check of this new review remain separate
  actions. Records stay DRAFT; no upstream change or global exhaustion is inferred.
- 'Root read complete actual canonical records, report Markdown, CREATE history and
  owners209/227/pending908, and all prepared claim/individual-limitation assessments.
  Final postcapture assessment rechecks that these previously read complete bytes
  equal the captured and accepted payloads. Root primary reading: FractalNet v4 text1,4–8
  and visuals4–5; NASNet official text1,4–5,11–12 and visuals5/11; Swapout official
  text3–8 and visuals3–4/7. Supporting source-agent full or selective reading is separately
  attributed in retained ledgers. The excluded PTN supplement was identified separately.
  No author implementation or benchmark execution, and no manual reading of every
  unrelated inherited frontier body, is claimed.'
tags:
- scientific-review
- self-review
- heterogeneous-batch
- source-scoped
schema_version: 1.0.0
review_id: 20261015T091809Z-fractalnet-droppath-nasnet-scheduled-droppath-and-swapout
kind: batch
repository: CultureBotAI/AIMech
started_at: '2026-10-15T09:05:25.347287Z'
finished_at: '2026-10-15T09:18:09.623223Z'
source:
  git_revision: d76936e4e77768d08b0cdd7f505ed34c9f50a5f0
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/ResidualNeuralNetwork.yaml
    sha256: 46855f48bc672169007ca212c92ee049f8089e649db9cfa272a3df61fa98ab3e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/DropBlock.yaml
    sha256: 8eaba0fedfe78562a162b7b4a4777a3657dac700dd497e97b06b5218061ae3d5
    role: context
  - path: data/curated/FractalNetDropPath.yaml
    sha256: 1c828a06ae90f7b2c9a1c7082f3a4e09dcc213039254a41dc2918f7bfc65979c
    role: target
  - path: data/curated/NASNetScheduledDropPath.yaml
    sha256: dcd438ea0e444bae67b4e8855dd7f315d1f333da556ab31b649e494e09209d99
    role: target
  - path: data/curated/ShakeDropRegularization.yaml
    sha256: f5653331df1b4469c49ed4a78b422aeadd16617a16fadea8ca4c42422c1236ff
    role: context
  - path: data/curated/ShakeShakeRegularization.yaml
    sha256: 184f2d3694ce8e98d8a55d3948ef4ffafed0ad345231e88ae27832d792da4883
    role: context
  - path: data/curated/StochasticDepth.yaml
    sha256: 32a0f2baac7ebf1c7f08c81f54710df74e56044bbf36e0df1ac7a05f4d925852
    role: context
  - path: data/curated/Swapout.yaml
    sha256: 77edc1d36b4f82f540fe071414f4f0f77e0ed042c99243ef487e03e78831c61e
    role: target
  - path: data/curated/Zoneout.yaml
    sha256: 25f1c0e8bfaa491a871c780730358be99aa37f44933aefc466b1ca0024563ae6
    role: context
  - path: docs/curated-concepts.md
    sha256: 1a3db0915791b0e90b02cd1f83c35850bfc3c97b18edfd8b946c91030578ccb8
    role: context
  - path: docs/record-review-profile.md
    sha256: 2d3e3a73264523c78930d17b0812e2d22887e25423fe7c38e0ddce922d9cec9d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/reports/fractalnet-droppath-nasnet-scheduled-droppath-and-swapout/2026-10-15T090302Z-codex-40b373.yaml
    sha256: 3a8784da205a40fa03bc347219cd1059b301e17a69d6ccc590568785795e574a
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261015T090241Z-fractalnet-droppath-nasnet-scheduled-droppath-and-swapout.json
    sha256: face837430606d9a267281ea1bc0b0749c9fa2d378a8b307f771fe99430c617f
    role: context
  - path: research/discovery/20261015T090241Z-fractalnet-droppath-nasnet-scheduled-droppath-and-swapout.md
    sha256: 1784e193279fec7ee550c91da41ebc54e34eb59d87c71974fc1969bf2ad66ee9
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:FractalNetDropPath
  path: data/curated/FractalNetDropPath.yaml
  label: FractalNet DropPath
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FractalNetDropPath.yaml
    role: maintained native concept record
- target_id: AIMech:NASNetScheduledDropPath
  path: data/curated/NASNetScheduledDropPath.yaml
  label: NASNet Scheduled DropPath
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NASNetScheduledDropPath.yaml
    role: maintained native concept record
- target_id: AIMech:Swapout
  path: data/curated/Swapout.yaml
  label: Swapout
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Swapout.yaml
    role: maintained native concept record
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  command: uv run --locked aimech check-source
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  command: just render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-diff
evidence:
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-droppath-swapout-cohort337-capture.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Actual canonical inspect output; all captured input hashes rechecked. Inspection
    alone is not scientific approval.
  snapshot_sha256: f43761e7e3e15ab9827c4cb28c2b22c91585185d0c057bd282ad086d4ede6d8e
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-droppath-swapout-cohort337-root-postcapture-reading.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Actual root full-target assessment after capture and completed checks;
    selective primary scopes are stated separately.
  snapshot_sha256: 3f08d64489136670238fe48f8a4ee94b0834df5d70da3a7d0172dbc72e2073e7
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-droppath-swapout-cohort337-review-preparation-20261015/scientific-support.prepared.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Attributed same-author support of all 18 accepted claims and 20 individual
    limitations. This is preparation DATA, not itself an actual canonical capture.
  snapshot_sha256: e509d6c4051ca4d4d62ac1f5ebc54a7945405c7c1b23084aa28ba87b19ef0218
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-droppath-swapout-cohort337-write.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Actual creation receipt binds three records, report pair and CREATE history.
  snapshot_sha256: 224acab4217607cad5658e7b4aaba6f1cb5a636bf154b72244fb0d6bf906fa97
- evidence_id: discovery-report
  kind: record_content
  reference: research/discovery/20261015T090241Z-fractalnet-droppath-nasnet-scheduled-droppath-and-swapout.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Record mirrors are exact. Only existing owners 209 and 227 changed; all
    906 other prior main and 393 nested objects are unchanged. One separately assessed
    pending PTN source lead was appended; it is not a fourth record or reviewed scientific
    target.
  snapshot_sha256: face837430606d9a267281ea1bc0b0749c9fa2d378a8b307f771fe99430c617f
- evidence_id: creation-history
  kind: record_content
  reference: history/reports/fractalnet-droppath-nasnet-scheduled-droppath-and-swapout/2026-10-15T090302Z-codex-40b373.yaml
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Actual append-only CREATE sidecar; review and publication are separate
    later actions.
  snapshot_sha256: 3a8784da205a40fa03bc347219cd1059b301e17a69d6ccc590568785795e574a
- evidence_id: pinned-aio
  kind: database
  reference: sources/aio/aio.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Exact snapshot supports three qualified related mappings; no upstream equivalence
    or subclass assertion.
  locator: Exact AIO:TrainingStrategy with retained inspected alternatives and incident
    edges; its preprocessing genus is not imposed as an is-a relation.
  snapshot_sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
- evidence_id: identity-assessment
  kind: search
  reference: /private/tmp/aimech-cohort337-root-decisions.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: Actual root decisions bind fresh ignored/hidden-inclusive scans and owners
    209/227 and one pending source-lead accounting; no manual rereading of every hit
    by this generator is claimed.
  snapshot_sha256: d573bafdfdd09e6f1f9d2aa1347a89102e17b5c7d17a75e83f1ba3aad15d82e0
  search_scope: Exact captured inventory, full carried frontier and four retained
    checkouts searched including ignored and hidden files; no worldwide absence or
    exhaustion claim.
- evidence_id: droppath-nonnegative-host-addendum
  kind: record_content
  reference: /private/tmp/aimech-droppath-research-20261015/analytic-nonnegative-host-addendum.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: The separate pre-draft addendum supplies nonnegative 0/2 features followed
    by affine shift and ReLU, retaining the original generic witness. The illustrative
    singleton law is not claimed to be the paper's mask distribution. This is analytical
    context, not a canonical finding.
  locator: FractalNet limitation 3; Section 3.3, PDF p. 5, and retained analytical
    addendum.
  snapshot_sha256: b700deb86a0a75e55884418e4d2c0a759ed847eb73af6f3aba77a18b934120bb
- evidence_id: swapout-caption-qualification
  kind: record_content
  reference: /private/tmp/aimech-swapout-research-20261015/table-caption-correction.json
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: context_only
  summary: The original curator note inserted deterministic into an inference-unspecified
    caption. The successor preserves the numerical row but withdraws an unambiguous-caption
    contradiction, noting the stochastic column and qualified prose. This pre-draft
    correction preserves original artifacts and is not a canonical finding or author
    erratum.
  locator: Official Swapout PDF p. 7, Table 3 caption and first row; nearby PDF p.
    6 prose.
  snapshot_sha256: e61a76841f5bbefb2fc05c0791bee63bf7f4236c9aa33e95fce7991fae7a278d
- evidence_id: src-larsson2017-arxiv-v4
  kind: primary_source
  reference: https://arxiv.org/pdf/1605.07648v4
  accessed_at: '2026-10-15T08:15:59Z'
  support: supports
  summary: arXiv:1605.07648v4, submitted 26 May 2017 at 18:53:56 UTC; retained 11-page
    PDF identifying publication at ICLR 2017. The PDF build date of 30 May 2017 and
    HTTP Last-Modified date in 2023 are file metadata, not publication dates. Acquisition
    time is access metadata, not a claim of full reading.
  locator: Historical supporting research read all 11 native-text pages and visuals
    2, 4 and 5; draft preparation reread text 4–8 and visual 4. Root research read
    text 1, 4–8 and visuals 4–5, then complete accepted draft/support. Definition
    and six claims use Sections 3–4, PDF pp. 4–8. Access, source build and version
    dates remain distinct. No author code or benchmark inspection is claimed.
  snapshot_sha256: 6d75803a1a74624d2dda0b62baf76bc3a628062717e03797f44a241cea5d468f
- evidence_id: src-zoph2018-cvpr
  kind: primary_source
  reference: https://openaccess.thecvf.com/content_cvpr_2018/papers/Zoph_Learning_Transferable_Architectures_CVPR_2018_paper.pdf
  accessed_at: '2026-10-15T08:16:02Z'
  support: supports
  summary: Official CVPR 2018 open-access PDF, 14 pages including Appendices A and
    B, printed pp. 8697–8710. This retained version is distinct from the arXiv:1707.07012
    versions; no byte equivalence is assumed. Acquisition time is access metadata,
    not a claim of full reading.
  locator: Historical supporting research read native text 1–5 and 11–12, visuals
    5 and 11; draft preparation reread text 4–5 and 11–12 plus visual 11. Root research
    read text 1, 4–5, 11 and visuals 5/11, then additionally full native text p. 12
    during draft assessment. This is selective reading of the official 14-page CVPR
    PDF, not a full-paper or author-code audit.
  snapshot_sha256: 0a0c3e5396d7cf1428a513cbea62a1e2acacc98b59035566af28868e42336354
- evidence_id: src-singh2016
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2016/file/c51ce410c124a10e0db5e4b97fc2af39-Paper.pdf
  accessed_at: '2026-10-15T08:18:14Z'
  support: supports
  summary: Official NIPS 2016 proceedings PDF, nine local pages; Advances in Neural
    Information Processing Systems 29, bibliographic pp. 28–36. The PDF modification
    timestamp of 19 November 2016 is file-build metadata, not an asserted publication
    day. No equivalence to the separately indexed arXiv preprint is asserted. Acquisition
    time is access metadata, not a claim of full reading.
  locator: Historical source agent read all nine official main-paper native-text pages
    and visuals 3–8. Root read text 3–8 and visuals 3–4, then visual p. 7 during draft
    acceptance. Definition and six claim locators lie in main text 3–6. The mismatched
    PTN supplement was read only for identification and is excluded from Swapout evidence.
    No author code or benchmark execution is claimed.
  snapshot_sha256: 8de0db45edbe61d6384be915e7a9ea5b55c66bbc9df3e9b46cde71a1fc29a8e4
- evidence_id: record-fractal
  kind: record_content
  reference: data/curated/FractalNetDropPath.yaml
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: 1c828a06ae90f7b2c9a1c7082f3a4e09dcc213039254a41dc2918f7bfc65979c
- evidence_id: record-nasnet
  kind: record_content
  reference: data/curated/NASNetScheduledDropPath.yaml
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: dcd438ea0e444bae67b4e8855dd7f315d1f333da556ab31b649e494e09209d99
- evidence_id: record-swapout
  kind: record_content
  reference: data/curated/Swapout.yaml
  accessed_at: '2026-10-15T09:17:48.309612Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: 77edc1d36b4f82f540fe071414f4f0f77e0ed042c99243ef487e03e78831c61e
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-droppath-swapout-cohort337-check-gate.json
  accessed_at: '2026-10-15T09:16:32.291633Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 84a5a6926f938749210fe876cbd1e98e23b145489d99dc91ca26c5b104369a77
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-droppath-swapout-cohort337-check-vendor.json
  accessed_at: '2026-10-15T09:16:35.967769Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: f9cbbbab68b07cc9540e8ad30061a6c041741c85d21982c0eca76d58b68920de
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-droppath-swapout-cohort337-check-check-source.json
  accessed_at: '2026-10-15T09:16:38.584049Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 238f5e032c5a08de28675f109482122f392422e069561bb9816630ffe6cae75b
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-droppath-swapout-cohort337-check-render.json
  accessed_at: '2026-10-15T09:04:08.824377Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 48d591ad52876d971aae11bd132351626b5e320f15c61ce418d74bc557c4de2b
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-droppath-swapout-cohort337-check-render-check.json
  accessed_at: '2026-10-15T09:16:49.350101Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 1ba81df1f56a664f5520e986bf11f849735444d69bf27734b0e858d0eb8feecb
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-droppath-swapout-cohort337-check-diff.json
  accessed_at: '2026-10-15T09:16:49.522713Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: ff3455c127e203ae05ddeaef23d2338aaba7f5ac340bb76bc4e401fcc32f37a4
assessments:
- assessment_id: fractal-fractal-host-and-procedure
  area: evidence
  topic: Claim fractal-host-and-procedure
  outcome: supported
  summary: Section 3 defines the fractal join host and explicitly contrasts its unprivileged
    learned inputs with residual pass-through roles. The scope identifies the protocol
    without claiming that the entire host is itself a regularizer.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-local-nonempty-join-selection
  area: evidence
  topic: Claim local-nonempty-join-selection
  outcome: supported
  summary: The local bullet explicitly requires survival of at least one input. The
    claim preserves that requirement and leaves the unspecified nonempty-mask enforcement
    law open; it does not assert final Bernoulli independence.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-global-single-column-selection
  area: evidence
  topic: Claim global-single-column-selection
  outcome: supported
  summary: The global bullet restricts the selected network-wide path to a column.
    Cross-block coupling follows from that single choice. No uniform column law or
    exact expected depth is invented.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-mean-over-active-inputs
  area: evidence
  topic: Claim mean-over-active-inputs
  outcome: supported
  summary: The source says to average active inputs. The finite-sum form and one-input
    boundary are direct restatements with nonempty and shape conditions, not an author-code
    replication or a new stochastic law.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-reported-minibatch-mixture
  area: evidence
  topic: Claim reported-minibatch-mixture
  outcome: supported
  summary: The 50/50 mode mixture, minibatch refresh and 15% local setting have separate
    precise locations. Ordinary dropout is retained as a co-used procedure, and the
    diagram is not elevated to a deterministic mode schedule.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-full-graph-and-extracted-column-use
  area: evidence
  topic: Claim full-graph-and-extracted-column-use
  outcome: supported
  summary: Tables 1 and 4 and the surrounding text evaluate the full graph and extracted
    columns. The claim records the available prediction choices and the discussed
    trade-off without adopting a quantitative benchmark effect or ensemble-equality
    claim.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The definition combines the two source-defined sampling modes with their
    shared active-input mean. It does not equate the regularizer with the host architecture
    or imply independent repaired masks.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The exact pinned TrainingStrategy CLASS and all 15 examined contexts were
    retained in research. Its preprocessing genus prevents an unqualified subclass
    reading. The single related match is the root-accepted association; no additional
    architecture, DropoutLayer or RegularizationLayer mapping is asserted.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - pinned-aio
- assessment_id: fractal-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Only larsson2017-arxiv-v4 is declared and explicitly cited in the definition
    and all six claims. The exact source version, original acquisition time and separately
    attributed research/root reading scopes remain retained. Full-text access does
    not assert full implementation or benchmark inspection.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All 7 individual limitations are retained exactly and assessed separately
    below. They preserve source-specific mask, schedule, inference, implementation
    and empirical boundaries; no missing controls or universal guarantees are supplied.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 209 and distinct residuals.
    The supporting historical identity scope is: This candidate denotes the original
    FractalNet local/global DropPath protocol, not the complete fractal architecture,
    a trained column, NASNet Scheduled DropPath, stochastic depth or a universal modern
    library DropPath function. Local and global modes remain within one named procedure.
    No bare DropPath alias is asserted. The retained research snapshot contained 742
    native and 442 pinned AIO records. Normalized IDs, labels, aliases and all scoped
    synonyms had no queried collision. Four whole-checkout searches included ignored
    and hidden files and returned 714 occurrences reconstructed into one pending-label
    content. A separate final-name search returned no hits across the same four checkouts,
    and a bounded AST identity projection of 200 top-level TEMP content modules found
    no queried identity match. Research traversed all 908 main and 393 nested frontier
    objects, read 42 selected full objects, 38 semantic definitions and five full
    native neighbors, and examined 15 exact AIO CLASS contexts with 84 incident-edge
    rows. These are dated historical findings, not a fresh creation-time absence or
    saturation claim. Existing owner 209 supplies the shared discovery context; its
    old DropBlock-paper URL is preserved as a historical lead, not used as defining
    evidence for either procedure.'
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - identity-assessment
  - postcapture-reading
- assessment_id: fractal-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The source states nonempty survival but not the enforcement algorithm.
    Positive all-drop probability under unconstrained independent draws is an elementary
    boundary, not a reported source defect.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The limits distinguish unspecified global selection probabilities from
    the specified experimental mode mixture and local setting.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: The preferred hand witness respects nonnegative features after the demonstrated
    ReLU and applies a permitted subsequent affine/nonlinear composition. Its singleton
    distribution is explicitly illustrative, not the paper's repaired sampling law.
    The original generic witness is retained as historical context.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
  - droppath-nonnegative-host-addendum
- assessment_id: fractal-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: The claim does not equate an absent current gradient path with frozen optimizer
    or running state. No implementation was inspected, so batching, repair and extracted-network
    normalization stay open.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: The paper jointly uses other training choices and labels its supervision
    explanation a hypothesis. The limit avoids causal or theorem-level claims beyond
    this evidence.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: The retained v4 identity is explicit. Failed alternate access is not equivalence
    evidence, and the generic term is not imposed as an alias across distinct procedures.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: fractal-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: The source allows possible broader hosts while demonstrating CNNs. Compatibility
    and nonempty inputs are explicit mathematical prerequisites; the stated reading
    scope is not an implementation certificate.
  target_ids:
  - AIMech:FractalNetDropPath
  evidence_ids:
  - record-fractal
  - scientific-support
  - src-larsson2017-arxiv-v4
- assessment_id: nasnet-named-cell-training-regularizer
  area: evidence
  topic: Claim named-cell-training-regularizer
  outcome: supported
  summary: The name and training role occur in Section 4 and Appendix A.5. The distinct
    controller description in Appendix A.2–A.3 supports keeping the regularizer separate
    from architecture search.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-operation-bearing-cell-edges
  area: evidence
  topic: Claim operation-bearing-cell-edges
  outcome: supported
  summary: Appendix A.5 explicitly points to the yellow operation boxes in Figure
    4. The claim uses that graph unit without importing an identity-edge exclusion
    or treating all scalar activations as separate path masks.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-linear-training-time-drop-schedule
  area: evidence
  topic: Claim linear-training-time-drop-schedule
  outcome: supported
  summary: The defining sentence supplies linear progression over training, contrasted
    with a fixed rate. Endpoints, progress indexing and depth adjustments are absent
    from these passages and remain limitations rather than invented formulas.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-paper-level-test-scaling-convention
  area: evidence
  topic: Claim paper-level-test-scaling-convention
  outcome: supported
  summary: The claim attributes the prose scaling convention and its cited-method
    analogy precisely. Its second sentence preserves the unresolved choice of keep
    probability when the training schedule changes.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-distinct-from-ordinary-output-dropout
  area: evidence
  topic: Claim distinct-from-ordinary-output-dropout
  outcome: supported
  summary: Appendix A.7 explicitly places a separate dropout setting at the final
    softmax matrix. This prevents that reported 0.5 from being misread as the ScheduledDropPath
    endpoint; no empirical benefit is inferred.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-host-and-empirical-protocol-boundary
  area: evidence
  topic: Claim host-and-empirical-protocol-boundary
  outcome: supported
  summary: The source describes multiple NASNet training choices and explicitly states
    that no residual connections are added between convolutional cells. The claim
    restricts the named regularizer and does not transfer whole-system performance
    or efficiency claims.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The definition isolates the source-named temporal cell-edge regularizer.
    It avoids inventing schedule endpoints, inference coefficients or a complete architecture-search
    procedure.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The exact pinned TrainingStrategy CLASS and all 15 examined contexts were
    retained in research. Its preprocessing genus prevents an unqualified subclass
    reading. The single related match is the root-accepted association; no additional
    architecture, DropoutLayer or RegularizationLayer mapping is asserted.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - pinned-aio
- assessment_id: nasnet-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Only zoph2018-cvpr is declared and explicitly cited in the definition and
    all six claims. The exact source version, original acquisition time and separately
    attributed research/root reading scopes remain retained. Full-text access does
    not assert full implementation or benchmark inspection.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All 7 individual limitations are retained exactly and assessed separately
    below. They preserve source-specific mask, schedule, inference, implementation
    and empirical boundaries; no missing controls or universal guarantees are supplied.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 209 and distinct residuals.
    The supporting historical identity scope is: This candidate denotes the original
    NASNet ScheduledDropPath training procedure, not the NASNet architecture-search
    controller, a complete NASNet network, FractalNet DropPath, stochastic depth or
    every schedule called DropPath. The retained identity is qualified by the NASNet
    source and leaves unspecified replication controls open. No bare DropPath alias
    is asserted. The retained research snapshot contained 742 native and 442 pinned
    AIO records. Normalized IDs, labels, aliases and all scoped synonyms had no queried
    collision. Four whole-checkout searches included ignored and hidden files and
    returned 714 occurrences reconstructed into one pending-label content. A separate
    final-name search returned no hits across the same four checkouts, and a bounded
    AST identity projection of 200 top-level TEMP content modules found no queried
    identity match. Research traversed all 908 main and 393 nested frontier objects,
    read 42 selected full objects, 38 semantic definitions and five full native neighbors,
    and examined 15 exact AIO CLASS contexts with 84 incident-edge rows. These are
    dated historical findings, not a fresh creation-time absence or saturation claim.
    Existing owner 209 supplies the shared discovery context; its old DropBlock-paper
    URL is preserved as a historical lead, not used as defining evidence for either
    procedure.'
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - identity-assessment
  - postcapture-reading
- assessment_id: nasnet-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The named schedule is clear while its numeric controls are not printed
    in the inspected method. No endpoints or software defaults are imported.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The paper names operation-bearing edges but not all exceptional or coupled
    mask cases. The limit avoids silently importing FractalNet's different safeguard.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: The prose does not identify a time-indexed inference probability or prove
    nonlinear ensemble equality. This is an evidence gap rather than a demonstrated
    implementation failure.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: Momentum, weight decay and other state make a blanket frozen-parameter
    inference unjustified. No specific unseen implementation behavior is asserted.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Training-time progression, graph-mask units and training-example ordering
    are distinct identities. The contextual comparisons do not become extra source-backed
    mechanism claims about uninspected later implementations.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: The limit keeps the paper's combined NASNet system evidence separate from
    an isolated causal or universal claim about one regularizer.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: nasnet-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: The source version and selective reading scope are explicit. Missing replication
    details remain open; no full-paper or author-code inspection is asserted.
  target_ids:
  - AIMech:NASNetScheduledDropPath
  evidence_ids:
  - record-nasnet
  - scientific-support
  - src-zoph2018-cvpr
- assessment_id: swapout-compatible-stochastic-path-sums
  area: evidence
  topic: Claim compatible-stochastic-path-sums
  outcome: supported
  summary: Section 3 defines already computed F_i and per-tensor iid Bernoulli entries
    before Equation 2, with a directed acyclic surrounding network. The claim preserves
    the general tensor scope rather than forcing every contribution to be a function
    of one input. Compatibility is the domain requirement of the displayed addition.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-unitwise-four-choice-specialization
  area: evidence
  topic: Claim unitwise-four-choice-specialization
  outcome: supported
  summary: Equation 3, Figure 1 and the explicit four outcomes support unitwise zero/input/transformation/sum
    choices. The distinction concerns selector patterns, and the statement avoids
    claiming four distinct values or one scalar shared across every unit. Section
    3.2 independently defines the scalar whole-block comparison.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-shared-parameter-stochastic-training
  area: evidence
  topic: Claim shared-parameter-stochastic-training
  outcome: supported
  summary: Section 3.1 explicitly describes a randomly sampled family with tied parameters,
    and the training paragraph names SGD in the reported experiments. The claim does
    not inherit the defective pointwise step in the generic stability sketch or turn
    an experimental optimizer into a universal requirement.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-depth-dependent-selector-configuration
  area: evidence
  topic: Claim depth-dependent-selector-configuration
  outcome: supported
  summary: The source permits separate selector probabilities and Table 2 defines
    Linear(a,b) by position from first to last block. The claim carefully distinguishes
    depth scheduling from temporal annealing and avoids treating the reported setting
    as an optimum theorem.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-deterministic-and-stochastic-inference
  area: evidence
  topic: Claim deterministic-and-stochastic-inference
  outcome: supported
  summary: The source lists both local expectation replacement and sampled prediction
    averaging. Its ReLU discussion supports the nonlinear qualification. No fixed
    number of samples, exact whole-network expectation or accuracy guarantee is asserted.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-coupled-special-cases-and-skipforward
  area: evidence
  topic: Claim coupled-special-cases-and-skipforward
  outcome: supported
  summary: Section 3.2 states the dropout-on-sum, scalar residual dropout and complementary
    SkipForward formulas. These require coupled, shared or complementary masks, unlike
    the studied independent pair. The source comparison supports an operational distinction
    without forcing aliases or extra concepts.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The definition names the general Bernoulli-selected compatible-tensor computation,
    shared-parameter training and the two source inference choices. It is a procedure
    identity, broader than the main residual-host experiment but not all neural regularization.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: Root accepted only related_match to the exact pinned TrainingStrategy node.
    Its broad preprocessing wording supports a qualified association, not identity
    or subclassing. ResidualNeuralNetwork remains an inspected host alternative rather
    than a required mapping for generic Equation 2; additive penalty and Gaussian/dropout
    layer targets are not its identity.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - pinned-aio
- assessment_id: swapout-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Only singh2016 is declared and is cited by the definition and all six claims.
    Original raw acquisition precision and initial failures are retained. The official
    supplementary link returned PTN material, which is excluded; arXiv metadata is
    context only. Table-caption qualification is a separate pre-draft research correction,
    not a canonical issue.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All 6 individual limitations are retained exactly and assessed separately
    below. They preserve source-specific mask, schedule, inference, implementation
    and empirical boundaries; no missing controls or universal guarantees are supplied.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 227 and distinct residuals.
    The supporting historical identity scope is: Swapout denotes the original 2016
    stochastic compatible-tensor combination procedure, with a studied identity-plus-transformation
    specialization and explicit deterministic or sampled inference. It is retained
    separately from whole-branch StochasticDepth, recurrent Zoneout, continuous complementary
    Shake-Shake and shared-switch ShakeDrop. Restricted SkipForward is comparison
    context, not a forced alias or separate record. Historical research on 15 October
    2026 compared 745 native and 442 pinned AIO records, normalizing all 4,752 ID/local-ID/name/alias/scoped-synonym
    values without a candidate collision. Four ignored/hidden-inclusive searches accounted
    for 717 occurrences in seven completely read strings: existing owner227, ordinary-English
    software comments and neighboring discovery context. All 60 selected definitions,
    44 query-selected complete frontier objects, four full native neighbors and 13
    exact AIO nodes with 53 incident edge rows were read. The query covered both 908
    main and 393 nested frontier entries mechanically, without a claim of reading
    every unrelated body. Owner227 already represents this lead; its old Zoneout URL
    is historical discovery context, whereas the acquired official 2016 Swapout PDF
    supplies primary evidence. This is bounded historical research, not a future creation-time
    absence or saturation assertion.'
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - identity-assessment
  - postcapture-reading
- assessment_id: swapout-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: Shape/probability/acyclic prerequisites follow from the displayed tensor
    operation. Different mask dependence changes its law; the all-zero omission in
    the Equation 2 set is reconciled with permitted selectors and explicit Equation
    3 zero outcome. No uninspected implementation is certified.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The hand example is inside the generic Equation 2 family, with v explicitly
    a parameter. The four derivative magnitudes at 2*pi/3 average to 1/2 while the
    maximum-global-Lipschitz member has zero derivative. This is a bounded failure
    of that pointwise inference, not a ReLU-residual instability theorem or full review
    of the cited stability result.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: The finite two-mask hand example directly distinguishes an expectation
    after ReLU from ReLU after expectation. It does not require a benchmark or code.
    Sampling predictions is retained as approximation rather than exact finite-sample
    ensemble inference.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: Independent masks independent of the feature pair give the displayed variance
    excess. Correlation between X and Y cancels from that difference; interior equality
    also includes both features vanishing almost surely. Conditional versus unconditional
    means and alternate mask dependence remain explicit.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: swapout-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Root corrected the earlier research note that inserted deterministic into
    the Table 3 caption. The current limitation treats the caption as inference-ambiguous,
    correctly notes the stochastic column, and uses the first deterministic row only
    to reject a universal deterministic improvement claim. The paper itself qualifies
    most settings and reports a weaker preliminary ImageNet result.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
  - swapout-caption-qualification
- assessment_id: swapout-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Only the exact official main paper is declared. Its acquired time, build
    date and publication year are kept distinct. The mismatched PTN supplement is
    excluded and separately retained as a future source lead; the record does not
    pretend that an inaccessible correct supplement, preprint PDF, author code or
    benchmark was inspected.
  target_ids:
  - AIMech:Swapout
  evidence_ids:
  - record-swapout
  - scientific-support
  - src-singh2016
- assessment_id: actual-correspondence
  area: consistency
  topic: Captured bytes, accepted science and frontier accounting
  outcome: supported
  summary: All three captured records equal the actual write payloads and report entries.
    Exact support covers 18 claims and 20 limitations. Only existing owners 209 and
    227 changed; all 906 other prior main and 393 nested values remain unchanged.
    One pending PTN source lead was appended and remains outside the three reviewed
    records. Six required checks passed. No global exhaustion or DRAFT promotion is
    inferred.
  target_ids:
  - AIMech:FractalNetDropPath
  - AIMech:NASNetScheduledDropPath
  - AIMech:Swapout
  evidence_ids:
  - captured-inputs
  - postcapture-reading
  - discovery-report
  - creation-history
  - droppath-nonnegative-host-addendum
  - swapout-caption-qualification
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
findings: []
actions: []
notes:
- Retain all three source-qualified algorithm identities. FractalNet local/global
  selection uses nonempty active-input means and unspecified enforcement/column laws.
  NASNet schedules operation-bearing edge suppression over training, without invented
  endpoints or inference-time index. Swapout combines compatible tensors with explicit
  selector coupling and inference alternatives; the bounded Lipschitz, conditional
  variance and nonlinear expectation arguments do not imply a model-instability or
  universal performance theorem. All18 claims,20 limitations, definitions,3primarysources
  and related TrainingStrategy mappings are supported at their declared scope. Original
  pre-curation caption qualification and nonnegative-host addendum remain distinct
  from canonical findings. Actual owners209/227 resolve these records;906other prior
  main393nested objects remain exact and PTN remains pending908. Six actual checks
  passed; records remain DRAFT. No required concrete finding arose.
```
