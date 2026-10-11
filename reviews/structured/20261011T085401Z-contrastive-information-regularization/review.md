# Scientific self-review of CPC, InfoNCE, VAT, RIM and MINE

- Review: 20261011T085401Z-contrastive-information-regularization
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T08:51:15Z
- Finished UTC: 2026-10-11T08:54:01Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain all five identities and their explicit mathematical, algorithmic and mapping boundaries. Issues43/44 corrected VAT section labels/loss weighting and the CPC/InfoNCE Poole footnote locator; MINE gradient wording and RIM locators were refined. No actionable finding remains in these current records. All remain DRAFT.

## Scope And Provenance

Five explicitly selected heterogeneous maintained concepts involving contrastive prediction, information estimation or regularization.

Selection: Exactly ContrastivePredictiveCoding, VirtualAdversarialTraining, RegularizedInformationMaximization, MutualInformationNeuralEstimation and InfoNCE from the discovery ledger; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base 63941e3435a51f4419b1385a24398ab8cdeb9d02.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ContrastivePredictiveCoding | data/curated/ContrastivePredictiveCoding.yaml | maintained | Contrastive predictive coding |
| AIMech:VirtualAdversarialTraining | data/curated/VirtualAdversarialTraining.yaml | maintained | Virtual adversarial training |
| AIMech:RegularizedInformationMaximization | data/curated/RegularizedInformationMaximization.yaml | maintained | Regularized information maximization |
| AIMech:MutualInformationNeuralEstimation | data/curated/MutualInformationNeuralEstimation.yaml | maintained | Mutual information neural estimation |
| AIMech:InfoNCE | data/curated/InfoNCE.yaml | maintained | InfoNCE |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ContrastivePredictiveCoding, AIMech:VirtualAdversarialTraining, AIMech:RegularizedInformationMaximization, AIMech:MutualInformationNeuralEstimation, AIMech:InfoNCE | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 73.08s (0:01:13)<br>Checked 442 record(s); 0 failed.<br>Checked 208 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 43 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 42,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ContrastivePredictiveCoding, AIMech:VirtualAdversarialTraining, AIMech:RegularizedInformationMaximization, AIMech:MutualInformationNeuralEstimation, AIMech:InfoNCE | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, primary support, mechanism, limitations and AIO assessment

evidence: supported. Targets: AIMech:ContrastivePredictiveCoding.

CPC denotes the van den Oord et al. procedure, with configurable encoders and ordered context. It uses InfoNCE but is not identical to that loss. It differs from DIM local-to-global feature matching and from SimCLR augmentation-pair learning. An autoregressive context module is part of the original procedure; a GRU and raw-input reconstruction are not requirements. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts returned 52 worktree and 75 main-checkout lines: existing component discussions and discovery/review references, plus unrelated ignored dependency text in main. Short acronyms were compared in normalized identities. Four nearest maintained mechanisms and eleven exact AIO candidate nodes with direct parent edges were inspected.

Compute z_t=g_enc(x_t) and c_t=g_ar(z_&lt;=t). For each selected future offset k use the positive score f_k(x,c_t)=exp(z(x)^T W_k c_t). Form a candidate set containing one true future observation from the context-conditional distribution and N−1 negatives, ideally drawn independently from the observation marginal. Minimize the expected negative log of the positive score divided by the sum of all N scores, including the positive, over selected prediction horizons. Train the encoder, context module and prediction parameters jointly. With the ideal sampling scheme and a sufficiently expressive optimally fitted score, the optimal score is proportional to the conditional-to-marginal density ratio, with a context-dependent factor cancelling in the categorical probabilities. The expected loss yields the InfoNCE lower bound I(X_future;C)&gt;=log(N)−L_NCE under its sampling assumptions. This is an expectation-level statement, not a guarantee for one minibatch. Learned local representations or context summaries can be used downstream. Limitations: The bound is at most log(N) and depends on the negative proposal. Same-speaker, same-sequence or otherwise conditional negatives used in particular experiments do not automatically satisfy the ideal independent marginal sampling assumptions. The original appendix uses an approximate substitution in its derivation. The population bound is supported here by Poole et al.’s separate proof, not by promoting that approximation to an exact equality. Finite critics, finite samples and incomplete optimization do not guarantee density-ratio recovery or an accurate numerical mutual-information estimate. Future-predictive information can include nuisance factors. Only declared primary passages were inspected. No CPC implementation, training run or benchmark was reproduced.

### Identity, primary support, mechanism, limitations and AIO assessment

evidence: supported. Targets: AIMech:VirtualAdversarialTraining.

VAT denotes the Miyato et al. procedure described in the 2018 manuscript revision. The virtual target is the model’s current prediction. Label-free perturbation construction does not mean the complete supervised or semi-supervised training objective has no labels. VAT is a component of IMSAT but is not that information-maximization framework or a generative adversarial network. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts returned 52 worktree and 75 main-checkout lines: existing component discussions and discovery/review references, plus unrelated ignored dependency text in main. Short acronyms were compared in normalized identities. Four nearest maintained mechanisms and eleven exact AIO candidate nodes with direct parent edges were inspected.

For a fixed parameter snapshot theta_hat, approximately maximize D(p_theta_hat(y&#124;x)&#124;&#124;p_theta_hat(y&#124;x+r)) over &#124;&#124;r&#124;&#124;_2&lt;=epsilon; the reported classifier implementation uses KL divergence. At r=0 the smooth KL objective has zero value and first derivative. Its local quadratic approximation gives a dominant-Hessian-eigenvector direction. Approximate that direction by initializing a random unit vector, taking the gradient with respect to r at a small displacement xi*d, normalizing it, and optionally repeating this power-iteration approximation. Scale the resulting direction by epsilon. For a model update, hold both the teacher prediction and the selected perturbation fixed while minimizing D(p_theta_hat(y&#124;x)&#124;&#124;p_theta(y&#124;x+r_vadv)). Average this regularizer over available inputs to obtain R_VAT, and minimize supervised negative log likelihood plus alpha times R_VAT. The general formulation can use labeled and unlabeled inputs; the inspected semi-supervised driver applies its VAT branch to the unlabeled-input tensor. The pinned code defaults to one iteration, detaches the teacher and perturbation construction, and computes KL from softmax probabilities and stable log-softmax values. Its vatent branch separately adds conditional entropy minimization. Limitations: The Hessian direction relies on a local quadratic approximation and finite-difference power iteration. One iteration does not solve the exact finite-radius maximization and provides no certified adversarial robustness. The perturbation radius, norm, input representation and regularization weight affect which prediction changes are penalized. Semantic label preservation is not guaranteed for arbitrary perturbations. A constant classifier can have zero consistency loss; VAT alone does not identify meaningful classes. The task loss or other learning signals remain material. The author code uses epsilon-stabilized vector normalization, so its returned vector need not have exactly the ideal radius. Batch-normalization handling and finite arithmetic also belong to implementation scope. Three source files were inspected at the declared ranges without execution. The earlier 2015 precursor was identified but its full methods were not compared; no historical-version equivalence or benchmark reproduction is asserted.

### Identity, primary support, mechanism, limitations and AIO assessment

evidence: supported. Targets: AIMech:RegularizedInformationMaximization.

RIM denotes Gomes et al.’s named clustering framework. This record keeps its linear, kernel, nonuniform-prior and semi-supervised configurations explicit. It differs from IMSAT’s augmentation-consistency regularizer and from IIC’s information between paired assignment variables. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts returned 52 worktree and 75 main-checkout lines: existing component discussions and discovery/review references, plus unrelated ignored dependency text in main. Short acronyms were compared in normalized identities. Four nearest maintained mechanisms and eleven exact AIO candidate nodes with direct parent edges were inspected.

For N unlabeled inputs let p_theta(y&#124;x_i) be conditional cluster probabilities and q(y)=N^−1 sum_i p_theta(y&#124;x_i). Maximize H(q)−N^−1 sum_i H(p_theta(.&#124;x_i))−R(theta). The linear configuration uses softmax(w_y^T x+b_y), R=lambda sum_y &#124;&#124;w_y&#124;&#124;², and unpenalized biases, optimized with L-BFGS. Initialize by oversegmenting the data, fitting a multinomial logistic classifier to the resulting pseudo-labels, then optimizing the regularized information objective. Redundant categories can shrink toward zero marginal probability as their weights decay and biases become negative. The kernel configuration replaces linear scores with sum_i alpha_yi K(x_i,x)+b_y and penalizes RKHS squared norms alpha_y^T K alpha_y, with a regularization coefficient. A nonuniform-prior variant instead maximizes −mean conditional entropy−KL(q&#124;&#124;D)−R for a chosen class prior D. A semi-supervised extension adds labeled log likelihood and weights the unlabeled information term separately. Limitations: The information objective is nonconcave. Finite L-BFGS optimization and a regularization sweep do not guarantee a global optimum or a true cluster count. Softmax probabilities are positive at finite parameters; exact class deletion is an ideal limiting description. The uniform empirical input distribution and class-balance preference implicit in marginal entropy may not fit the desired population. The nonuniform-prior variant changes the objective and requires compatible prior support. Kernel scores require an appropriate positive-semidefinite kernel for the stated RKHS penalty. Equation (8) omits the regularization coefficient while the following derivative includes it; this record makes that coefficient explicit. The paper reports ground-truth adjusted-Rand scores across regularization settings. Those plots are not evidence for an automatic label-free hyperparameter or true-cluster-count selection rule. Primary methods and declared experimental context were inspected; no RIM implementation, optimizer behavior or benchmark was reproduced.

### Identity, primary support, mechanism, limitations and AIO assessment

evidence: supported. Targets: AIMech:MutualInformationNeuralEstimation.

MINE denotes the original neural Donsker–Varadhan estimator and its moving-average training heuristic. The paper’s alternative MINE-f objective is a different variational bound and is not silently equated with this record. MINE estimates dependence; DIM is a representation-learning framework that can use dependence critics, and InfoNCE is a different finite-candidate objective. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts returned 52 worktree and 75 main-checkout lines: existing component discussions and discovery/review references, plus unrelated ignored dependency text in main. Short acronyms were compared in normalized identities. Four nearest maintained mechanisms and eleven exact AIO candidate nodes with direct parent edges were inspected.

For a neural statistics function T_theta(x,z), optimize J(theta)=E_joint[T_theta]−log(E_product[exp(T_theta)]). Under the variational representation’s integrability assumptions, each population J(theta) is a lower bound on I(X;Z); optimizing within a neural family yields its restricted supremum. Estimate expectations from observed joint pairs and samples approximating the product of marginals, such as mismatched or shuffled pairs. The minibatch gradient contains a ratio of product-sample means and is generally biased. The original training heuristic replaces its exponential-moment denominator by an exponential moving average to reduce this bias. Poole et al. show that, when a positive running denominator is held fixed for an update, the resulting update has an interpretation as the gradient of a different unnormalized variational bound. This interpretation does not make the moving-average update a generally unbiased gradient estimator of the population Donsker–Varadhan objective. After fitting a critic, evaluating sample means in the Donsker–Varadhan expression gives a finite estimate, not a certified mutual-information lower bound for that sample. Limitations: Finite-sample log-moment estimation is biased, can be unstable for large critic scores, and need not remain below true mutual information. Reusing samples for critic fitting adds selection effects. The moving-average denominator is a bias-reduction heuristic. Its fixed-denominator alternative-bound interpretation does not prove that a same-batch updated running statistic is independent of the current samples or that the original Donsker–Varadhan gradient is unbiased. Strong-consistency arguments separate neural approximation from empirical estimation under compactness, continuity and measure assumptions. The fixed-family uniform-convergence result is not a proof that stochastic gradient optimization reaches the required supremum. Bounded/Lipschitz critic sample-complexity assumptions do not hold automatically for arbitrary networks and distributions. Shuffling one finite batch can include fixed points and dependent pairs; it is not literally independent sampling from the population product distribution. Sampling construction must be stated when interpreting estimates. As a mathematical consequence of a loose lower bound, reducing a poorly optimized estimated lower bound does not certify a reduction in true mutual information. No author implementation or numerical estimator experiment was audited.

### Identity, primary support, mechanism, limitations and AIO assessment

evidence: supported. Targets: AIMech:InfoNCE.

InfoNCE is the loss introduced in contrastive predictive coding, separable from the CPC encoder/context/prediction procedure. It does not by itself prescribe cosine similarity, temperature, augmentation pairs, symmetric losses or an autoregressive architecture. Named configurations such as SimCLR NT-Xent and DIM’s finite-masking implementation require their own sampling and numerical qualifications. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts returned 52 worktree and 75 main-checkout lines: existing component discussions and discovery/review references, plus unrelated ignored dependency text in main. Short acronyms were compared in normalized identities. Four nearest maintained mechanisms and eleven exact AIO candidate nodes with direct parent edges were inspected.

Given a context c, draw one positive x_+ jointly with c and N−1 negative candidates independently from the marginal p(x), with N&gt;=2. For real scores s(x,c), define ell=−log[exp(s(x_+,c))/sum_(j=1)^N exp(s(x_j,c))], including the positive in the denominator, and minimize L_NCE=E[ell]. For the ideal sampling scheme, log(N)−L_NCE&lt;=I(X;C); since ell&gt;=0, the bound is at most log(N) and may itself be negative. An expressive optimum scores the conditional-to-marginal density ratio up to a context-dependent multiplicative constant in exp(s). The categorical objective remains definable with other candidate constructions, but its stated mutual-information interpretation then requires a separate argument. Poole et al. provide an independent rigorous derivation of the expected bound beyond the approximate step in the original CPC appendix. Limitations: The lower bound holds for an expectation under its specified joint and independent marginal sampling. A realized finite-batch number is not certified to be below true mutual information. The log(N) ceiling limits estimation of high mutual information at a fixed candidate count. Optimizing a finite, restricted critic need not recover the density ratio or true information. False semantic negatives, conditional negative proposals and correlated in-batch candidates can change the learned representation and invalidate an unqualified use of the ideal sampling proof. Semantic usefulness is not guaranteed by the loss. Finite masking values contribute nonzero denominator mass and are not algebraically identical to removing candidates. No numerical implementation or training experiment was run for this loss record.

### CPC and InfoNCE remain distinct

scope: supported. Targets: AIMech:ContrastivePredictiveCoding, AIMech:InfoNCE.

Retain CPC as an algorithm and InfoNCE as its separable mathematical objective.

CPC specifies observation encoding, autoregressive context and future-horizon discrimination. InfoNCE specifies categorical candidate discrimination without prescribing an architecture, cosine score, temperature or augmentation pair. The positive belongs in the denominator. The rigorous expected-information bound requires its ideal sampling scheme; a finite batch is not a certified bound, the bound has a log(N) ceiling, and the original appendix approximate substitution is explicitly distinguished from the follow-up proof.

### VAT and RIM versus IMSAT

representation: supported. Targets: AIMech:VirtualAdversarialTraining, AIMech:RegularizedInformationMaximization.

Retain label-free perturbation smoothing and regularized discriminative clustering as distinct procedures.

VAT holds teacher and perturbation fixed for the parameter update and uses an approximate dominant-Hessian direction; one power iteration is not an exact adversary. The code confirms stable log-softmax KL and numerical vector normalization. The corrected objective is NLL plus alpha times VAT. RIM regularizes classifier complexity and encourages informative categorical assignments; linear/kernel, prior and semi-supervised configurations remain explicit. Finite softmax outputs do not literally delete categories, and nonconvex optimization does not certify true cluster-count recovery. IMSAT combines different information and consistency components rather than establishing equivalence to either component.

### MINE population bounds, empirical estimates and moving averages

representation: supported. Targets: AIMech:MutualInformationNeuralEstimation, AIMech:InfoNCE.

Retain distinct DV neural estimation and finite-candidate contrastive objectives with conditional theory.

MINE distinguishes a population variational lower bound, a neural-family supremum, an empirical estimator and finite stochastic optimization. The log-moment ratio produces biased minibatch gradients; a fixed positive EMA denominator has a different-bound gradient interpretation, not generic unbiasedness for the population DV objective. The supplement’s approximation and uniform-convergence assumptions do not imply SGD convergence. InfoNCE has a different sampling construction and log-count ceiling. Neither estimator proves semantic quality or certifies true information from one sample.

### Positive mappings and explicit no-match decisions

scope: supported. Targets: AIMech:ContrastivePredictiveCoding, AIMech:VirtualAdversarialTraining, AIMech:RegularizedInformationMaximization, AIMech:MutualInformationNeuralEstimation, AIMech:InfoNCE.

Retain qualified related matches for CPC, RIM and InfoNCE and bounded no-match assessments for VAT and MINE.

Eleven exact AIO nodes, definitions/scoped synonyms and direct parents were inspected. CPC relates to SelfsupervisedLearning and ContrastiveLearning; RIM relates to UnsupervisedClustering; InfoNCE relates to ContrastiveLearning. These are qualified procedure-to-task/approach or loss-to-approach relations, not is-a assertions. VAT and MINE have bounded no-match assessments with six and four individually rejected targets respectively. Network components, LLM-specific classes and incidental applications do not establish mapping identity.

### Prepublication issue43 correction

provenance: supported. Targets: AIMech:VirtualAdversarialTraining.

Current locator and loss wording match the inspected primary revision.

The draft used nonexistent section labels III–IV and V-A and left alpha placement grammatically ambiguous. The current record cites Sections3.2–3.4 and Section4, including Equation8, and says NLL plus alpha times R_VAT. The ledger preserves the original draft and correction provenance. This is a current-state review; no prior saved finding or independent reviewer is invented.

### Current Poole locator after issue44

provenance: supported. Targets: AIMech:ContrastivePredictiveCoding, AIMech:InfoNCE.

Both current records cite footnote2 on PDF page4, visually verified.

The initial review is a historical working-tree observation, not rewritten to hide a missed finding. The original discovery ledger preserves its initial locators; the appended correction ledger and current record bytes establish the corrected state. No mathematical claim or mapping changed. No earlier structured finding is invented, so this current-state assessment does not claim formal finding-lineage resolution.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:ContrastivePredictiveCoding, AIMech:VirtualAdversarialTraining, AIMech:RegularizedInformationMaximization, AIMech:MutualInformationNeuralEstimation, AIMech:InfoNCE. Predictive representation learning, its contrastive objective, virtual perturbation smoothing, discriminative information clustering and neural DV estimation differ in inputs, outputs and optimization targets. Shared losses or components do not establish identity. RIM configurations remain explicit within its framework; no upstream AIO mutation follows from these decisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T084632Z-contrastive-information-regularization.json | supports | No normalized identity match among all 442 AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches of the full worktree and main checkout returned 52 and 75 lines respectively. Worktree hits are DIM component discussions or prior discovery/review references; the 23 extra main hits are unrelated ignored dependency text (mine pronouns or PDBj /mine/ URLs). Short CPC/VAT/RIM aliases were included in normalized identities, not broad text search. DIM, IMSAT, IIC and SimCLR remain distinct neighbors. |
| mapping | sources/aio/aio.json; Eleven exact CLASS nodes with definitions, scoped synonyms and direct parents listed in source_analysis.aio_mapping_inspection | supports | Eleven exact AIO nodes, definitions/scoped synonyms and direct parents were inspected. CPC relates to SelfsupervisedLearning and ContrastiveLearning; RIM relates to UnsupervisedClustering; InfoNCE relates to ContrastiveLearning. These are qualified procedure-to-task/approach or loss-to-approach relations, not is-a assertions. VAT and MINE have bounded no-match assessments with six and four individually rejected targets respectively. Network components, LLM-specific classes and incidental applications do not establish mapping identity. |
| neighbors | data/curated/DeepInfoMax.yaml; Definitions, claims and mapping assessments in DeepInfoMax, InformationMaximizingSelfAugmentedTraining, InvariantInformationClustering and SimCLR | supports | DIM learns local/global feature dependence; IMSAT combines discrete information with augmentation consistency; IIC uses paired assignment information; SimCLR uses augmentation-pair contrastive training. Shared components or information terminology do not establish identity. |
| contrastivepredictivecoding-source | https://arxiv.org/pdf/1807.03748v2; Sections 2.1–2.3, Equations (1)–(3), PDF pp. 2–4; Appendix A.1, p. 13, read with the independent bound derivation below | supports | A representation-learning procedure that encodes observations, summarizes preceding representations as context, and jointly trains these components to distinguish future representations from sampled alternatives using InfoNCE. Version: arXiv:1807.03748v2, 2019-01-22; originally submitted 2018-07-10; 13 pages. Complete local text pages read: 1, 2, 3, 4, 13. Actual image pages viewed: 3, 4, 13. Partial/web reads are separately declared in the ledger. No training or benchmark execution. |
| contrastivepredictivecoding-source-1 | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.3, PDF p. 4, Equations (8)–(10) and footnote 2: rigorous expected InfoNCE bound and log-number-of-samples ceiling | supports | Inspected source: On Variational Bounds of Mutual Information. ICML 2019, PMLR 97:5171–5180; ten-page main PDF. Primary follow-up proof passages were inspected; no empirical results are inferred. |
| virtualadversarialtraining-source | https://arxiv.org/pdf/1704.03976v2; Sections 3.2–3.4, PDF pp. 4–6, especially Equation (8) and Algorithm 1; Section 4, p. 7, Equation (17) and implementation setup | supports | A prediction-smoothing regularization procedure that trains a model to preserve its current output distribution under approximately worst-case small input perturbations, constructing those perturbations without using target labels. Version: arXiv:1704.03976v2, 2018-06-27; 16 pages. Complete local text pages read: . Actual image pages viewed: 3, 4, 5, 6. Partial/web reads are separately declared in the ledger. No training or benchmark execution. |
| virtualadversarialtraining-source-1 | https://raw.githubusercontent.com/takerum/vat_tf/c5125d267531ce0f10b2238cf95604d287de63c8/vat.py; Lines 1–72: numerical normalization, finite-difference power iteration, detached teacher and VAT loss | supports | Inspected source: takerum/vat_tf author implementation: vat.py. takerum/vat_tf commit c5125d267531ce0f10b2238cf95604d287de63c8. Pinned author code read at the cited ranges without execution. |
| virtualadversarialtraining-source-2 | https://raw.githubusercontent.com/takerum/vat_tf/c5125d267531ce0f10b2238cf95604d287de63c8/train_semisup.py; Lines 45–75: labeled NLL, unlabeled VAT branch, optional entropy term and optimizer setup | supports | Inspected source: takerum/vat_tf author implementation: train_semisup.py. takerum/vat_tf commit c5125d267531ce0f10b2238cf95604d287de63c8. Pinned author code read at the cited ranges without execution. |
| virtualadversarialtraining-source-3 | https://raw.githubusercontent.com/takerum/vat_tf/c5125d267531ce0f10b2238cf95604d287de63c8/layers.py; Lines 130–149: stable log-softmax, KL divergence and conditional entropy | supports | Inspected source: takerum/vat_tf author implementation: layers.py. takerum/vat_tf commit c5125d267531ce0f10b2238cf95604d287de63c8. Pinned author code read at the cited ranges without execution. |
| regularizedinformationmaximization-source | https://proceedings.neurips.cc/paper_files/paper/2010/file/42998cf32d552343bc8e460416382dca-Paper.pdf; Sections 2–5, PDF pp. 2–5, Equations (1)–(10); Section 6.1, p. 6 for initialization and regularization-sweep context | supports | A discriminative clustering framework that fits conditional class probabilities by maximizing empirical input–assignment mutual information penalized by classifier complexity, with linear and kernel softmax configurations. Version: NIPS 2010; nine-page proceedings PDF; author order follows PDF title page. Complete local text pages read: 1, 2, 4, 5. Actual image pages viewed: 3, 4, 5. Partial/web reads are separately declared in the ledger. No training or benchmark execution. |
| mutualinformationneuralestimation-source | https://proceedings.mlr.press/v80/belghazi18a/belghazi18a.pdf; Sections 2–3, PDF pp. 2–4, Equations (2)–(6), Algorithm 1 and estimator-consistency discussion | supports | A mutual-information estimation procedure that trains a neural statistics function to maximize a Donsker–Varadhan objective contrasting joint samples with product-of-marginals samples, using stochastic optimization and an optional moving-average denominator for gradient estimation. Version: ICML 2018, PMLR 80:531–540; ten-page main PDF. Complete local text pages read: . Actual image pages viewed: 2, 3, 4. Partial/web reads are separately declared in the ledger. No training or benchmark execution. |
| mutualinformationneuralestimation-source-1 | https://proceedings.mlr.press/v80/belghazi18a/belghazi18a-supp.zip; Sections 8.2.1–8.2.3, supplementary PDF pp. 4–7: Donsker–Varadhan proof, approximation/estimation assumptions and bounded Lipschitz critic sample-complexity result | supports | Inspected source: Mutual Information Neural Estimation — Supplementary Material. ICML 2018 publisher supplementary ZIP member mine_appendix.pdf; eight pages; sha256 identifies extracted PDF, not ZIP. Exact page/image scope is recorded in source_analysis; the ZIP source hash identifies its extracted PDF member as stated in version metadata. |
| mutualinformationneuralestimation-source-2 | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.2, PDF pp. 2–4, Equations (3)–(7): Monte Carlo bias of the log-partition term and moving-average-gradient interpretation | supports | Inspected source: On Variational Bounds of Mutual Information. ICML 2019, PMLR 97:5171–5180; ten-page main PDF. Primary follow-up proof passages were inspected; no empirical results are inferred. |
| infonce-source | https://arxiv.org/pdf/1807.03748v2; Section 2.3, PDF pp. 3–4, Equation (2) and density-ratio discussion; Appendix A.1 p. 13, with its approximation explicitly qualified | supports | A contrastive log-softmax objective that identifies a joint positive among sampled candidates and, under independent marginal-negative sampling, gives an expectation-level lower bound on mutual information. Version: arXiv:1807.03748v2, 2019-01-22; originally submitted 2018-07-10; 13 pages. Complete local text pages read: 1, 2, 3, 4, 13. Actual image pages viewed: 3, 4, 13. Partial/web reads are separately declared in the ledger. No training or benchmark execution. |
| infonce-source-1 | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.3, PDF p. 4, Equations (8)–(10), footnote 2 and log(K) ceiling discussion | supports | Inspected source: On Variational Bounds of Mutual Information. ICML 2019, PMLR 97:5171–5180; ten-page main PDF. Primary follow-up proof passages were inspected; no empirical results are inferred. |
| corrections | research/discovery/20261011T084632Z-contrastive-information-regularization.json; review_refinements | supports | Original draft statements/locators and hashes, exact correction time and final hashes preserve the issue43 VAT correction, MINE population-gradient clarification and RIM locator expansion. |
| citation-correction | research/discovery/20261011T085047Z-contrastive-citation-correction.json; changes and visual_reinspection | supports | Issue44 corrects the Poole footnote locator from4 to2 in both CPC and InfoNCE. Original/final record hashes and actual correction time are preserved. The initial saved review missed the minor locator defect and is retained unchanged. |
| initial-review | reviews/structured/20261011T084915Z-contrastive-information-regularization/review.yaml | context_only | Initial author self-review of the precorrection working-tree records; its no-actionable-findings conclusion missed the footnote locator. This new review assesses all five current records and explicitly acknowledges that miss. |

## Limits And Additional Notes

- The initial review and original ledger are preserved with their precorrection locators; the appended issue44 correction and this current review state the final values.
- Adversarial author self-review only; all five records remain DRAFT.
- Full-text access and extraction do not imply every page was read. Exact page/image/code scope is saved in the discovery ledger.
- Only declared VAT implementation ranges were inspected; no CPC/RIM/MINE code equivalence, training or benchmark reproduction is asserted.
- Expected information bounds, approximation assumptions and uniform convergence do not certify finite samples or optimizer outputs.
- Positive mappings and no-match decisions are curator assessments bounded to the pinned AIO snapshot.
- Positive discoveries and outstanding leads keep the goal active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T085401Z-contrastive-information-regularization
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of CPC, InfoNCE, VAT, RIM and MINE
started_at: '2026-10-11T08:51:15Z'
finished_at: '2026-10-11T08:54:01Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all five current
    YAMLs against primary methods, visible equations, MINE supplement, Poole follow-up
    proof, three pinned VAT source files, four native neighbors and eleven exact AIO
    nodes. Corrected statements and locators were reread and reinspected, including
    the page4 image check after the initial review missed footnote2. No independent
    approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain all five identities and their explicit mathematical, algorithmic and
  mapping boundaries. Issues43/44 corrected VAT section labels/loss weighting and
  the CPC/InfoNCE Poole footnote locator; MINE gradient wording and RIM locators were
  refined. No actionable finding remains in these current records. All remain DRAFT.
source:
  git_revision: 63941e3435a51f4419b1385a24398ab8cdeb9d02
  state: working_tree
  inputs:
  - path: data/aio/ActivityRegularizationLayer.yaml
    sha256: cfa728f34098132a63278a471d0e1632f34c9dbc60167f22936e8cd3059725c8
    role: context
  - path: data/aio/ContrastiveLearning.yaml
    sha256: f8100e15621b6dd3335dc0bc8253da0197719faf6ac00f1369ebbc455a6fa645
    role: context
  - path: data/aio/DeepNeuralNetwork.yaml
    sha256: f5c4c7764ea05631bb6396200141eb8ba124725d2dc27919c7efe89e5e30b19e
    role: context
  - path: data/aio/GenerativeAdversarialNetwork.yaml
    sha256: 4f5080d92af8eaea513deed39c60679f0eb7a62d03e5be0d0d8d5c966a9a4544
    role: context
  - path: data/aio/GenerativeAdversarialNetworkAugmentedLLM.yaml
    sha256: d3816d7bd1a3f08e85650e82c1fee6091a8ec8635fb26fec429248a5602cc0de
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SelfSupervisedLLM.yaml
    sha256: 731765c79bcb75a97893e68751033365dcc1e36dc5794de1485ca72ea326e3d4
    role: context
  - path: data/aio/SelfsupervisedLearning.yaml
    sha256: ad9a98dfee5629f6433f13470f56e333316f8f03847df2c5678faf023d979c0e
    role: context
  - path: data/aio/SemiSupervisedLLM.yaml
    sha256: 4ee601313a6cdaa7134207fa384702f0e92d2b93906e379c2b0ef5cfe6eef9ee
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/ContrastivePredictiveCoding.yaml
    sha256: 847880d0f9c8724f50585ab687c9b9a25de6e6f7f9e87d254401275b4ab2f3e7
    role: target
  - path: data/curated/DeepInfoMax.yaml
    sha256: ebda53a216420e7455b5435a380e383d78569acf9b3e0031ae036f8c25b23fb1
    role: context
  - path: data/curated/InfoNCE.yaml
    sha256: b202ebcafc444df533d78ae82c3618d821ce4c5081a99ffe744deb644a6957da
    role: target
  - path: data/curated/InformationMaximizingSelfAugmentedTraining.yaml
    sha256: cd1a3bf10ff09203c9ac3271d82257aeb14ec0bb43064e5a604a0e5eef47196a
    role: context
  - path: data/curated/InvariantInformationClustering.yaml
    sha256: e70989718b3aefcd6a76f96ba225c17319bcc5975276290a239bdcec3d7c5da9
    role: context
  - path: data/curated/MutualInformationNeuralEstimation.yaml
    sha256: bc60c4ec4f58081b8875f0f585cb6a27a85bda74853668e5830949d8bfb9708a
    role: target
  - path: data/curated/RegularizedInformationMaximization.yaml
    sha256: d46bd458678d2a6cd3ae56c41bb14356ee8316c2c4110494e95a42ec60021c34
    role: target
  - path: data/curated/SimCLR.yaml
    sha256: e00dbf707a274e02df684ad09ae679b9dda832ba42e4aea7db5a157e25385e3d
    role: context
  - path: data/curated/VirtualAdversarialTraining.yaml
    sha256: 448041d823d47b52bb5ea340e84257dbf09f20659d5c2f1e2dfd1c36a29799ec
    role: target
  - path: research/discovery/20261011T084632Z-contrastive-information-regularization.json
    sha256: 1814b5565be8579c9c3fbf2130a7b113f75b5523acaf04f3e6ac5986b6ee6626
    role: context
  - path: research/discovery/20261011T085047Z-contrastive-citation-correction.json
    sha256: 8bd96c21936af7c2c1290cfd01003661c40b9676f825ce562c818bb2365952f8
    role: context
  - path: reviews/structured/20261011T084915Z-contrastive-information-regularization/review.yaml
    sha256: b35dbaa008409a58b909d5c6be503314c3221d252d234318321d4be141603aca
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:ContrastivePredictiveCoding
  path: data/curated/ContrastivePredictiveCoding.yaml
  label: Contrastive predictive coding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ContrastivePredictiveCoding.yaml
    role: maintained
- target_id: AIMech:VirtualAdversarialTraining
  path: data/curated/VirtualAdversarialTraining.yaml
  label: Virtual adversarial training
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VirtualAdversarialTraining.yaml
    role: maintained
- target_id: AIMech:RegularizedInformationMaximization
  path: data/curated/RegularizedInformationMaximization.yaml
  label: Regularized information maximization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RegularizedInformationMaximization.yaml
    role: maintained
- target_id: AIMech:MutualInformationNeuralEstimation
  path: data/curated/MutualInformationNeuralEstimation.yaml
  label: Mutual information neural estimation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MutualInformationNeuralEstimation.yaml
    role: maintained
- target_id: AIMech:InfoNCE
  path: data/curated/InfoNCE.yaml
  label: InfoNCE
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/InfoNCE.yaml
    role: maintained
scope:
  description: Five explicitly selected heterogeneous maintained concepts involving
    contrastive prediction, information estimation or regularization.
  selection: Exactly ContrastivePredictiveCoding, VirtualAdversarialTraining, RegularizedInformationMaximization,
    MutualInformationNeuralEstimation and InfoNCE from the discovery ledger; no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:VirtualAdversarialTraining
  - AIMech:RegularizedInformationMaximization
  - AIMech:MutualInformationNeuralEstimation
  - AIMech:InfoNCE
  exclusions:
  - target: NT-Xent, MINE-f/NWJ, TUBA/interpolated bounds, random perturbation training,
      graph clustering components and previous leads
    reason: Independent identity and source inspections remain in the continuing frontier.
  - target: Uninspected paper pages, Poole supplementary formulas and numerical implementations
      beyond declared VAT source ranges
    reason: Only actual inspected passages support the review; no training or estimator
      experiment was run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:VirtualAdversarialTraining
  - AIMech:RegularizedInformationMaximization
  - AIMech:MutualInformationNeuralEstimation
  - AIMech:InfoNCE
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 73.08s (0:01:13)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 208 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 43 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 42,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:VirtualAdversarialTraining
  - AIMech:RegularizedInformationMaximization
  - AIMech:MutualInformationNeuralEstimation
  - AIMech:InfoNCE
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T084632Z-contrastive-information-regularization.json
  accessed_at: '2026-10-11T08:51:15Z'
  support: supports
  summary: No normalized identity match among all 442 AIO labels/scoped synonyms and
    203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches
    of the full worktree and main checkout returned 52 and 75 lines respectively.
    Worktree hits are DIM component discussions or prior discovery/review references;
    the 23 extra main hits are unrelated ignored dependency text (mine pronouns or
    PDBj /mine/ URLs). Short CPC/VAT/RIM aliases were included in normalized identities,
    not broad text search. DIM, IMSAT, IIC and SimCLR remain distinct neighbors.
  search_scope: All 442 AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases;
    both full checkouts including hidden and ignored files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T08:51:15Z'
  support: supports
  locator: Eleven exact CLASS nodes with definitions, scoped synonyms and direct parents
    listed in source_analysis.aio_mapping_inspection
  summary: Eleven exact AIO nodes, definitions/scoped synonyms and direct parents
    were inspected. CPC relates to SelfsupervisedLearning and ContrastiveLearning;
    RIM relates to UnsupervisedClustering; InfoNCE relates to ContrastiveLearning.
    These are qualified procedure-to-task/approach or loss-to-approach relations,
    not is-a assertions. VAT and MINE have bounded no-match assessments with six and
    four individually rejected targets respectively. Network components, LLM-specific
    classes and incidental applications do not establish mapping identity.
- evidence_id: neighbors
  kind: record_content
  reference: data/curated/DeepInfoMax.yaml
  accessed_at: '2026-10-11T08:51:15Z'
  support: supports
  locator: Definitions, claims and mapping assessments in DeepInfoMax, InformationMaximizingSelfAugmentedTraining,
    InvariantInformationClustering and SimCLR
  summary: DIM learns local/global feature dependence; IMSAT combines discrete information
    with augmentation consistency; IIC uses paired assignment information; SimCLR
    uses augmentation-pair contrastive training. Shared components or information
    terminology do not establish identity.
- evidence_id: contrastivepredictivecoding-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1807.03748v2
  locator: Sections 2.1–2.3, Equations (1)–(3), PDF pp. 2–4; Appendix A.1, p. 13,
    read with the independent bound derivation below
  accessed_at: '2026-10-11T08:34:36Z'
  snapshot_sha256: 5ef5e1ab47d2273f418f01f66fb8eb1431ba9b185b7cba45e9955f0fee36427d
  support: supports
  summary: 'A representation-learning procedure that encodes observations, summarizes
    preceding representations as context, and jointly trains these components to distinguish
    future representations from sampled alternatives using InfoNCE. Version: arXiv:1807.03748v2,
    2019-01-22; originally submitted 2018-07-10; 13 pages. Complete local text pages
    read: 1, 2, 3, 4, 13. Actual image pages viewed: 3, 4, 13. Partial/web reads are
    separately declared in the ledger. No training or benchmark execution.'
- evidence_id: contrastivepredictivecoding-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: 'Section 2.3, PDF p. 4, Equations (8)–(10) and footnote 2: rigorous expected
    InfoNCE bound and log-number-of-samples ceiling'
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information. ICML 2019,
    PMLR 97:5171–5180; ten-page main PDF. Primary follow-up proof passages were inspected;
    no empirical results are inferred.'
- evidence_id: virtualadversarialtraining-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1704.03976v2
  locator: Sections 3.2–3.4, PDF pp. 4–6, especially Equation (8) and Algorithm 1;
    Section 4, p. 7, Equation (17) and implementation setup
  accessed_at: '2026-10-11T08:34:36Z'
  snapshot_sha256: e1ccc4b18f17c7b76ef33f018703c8d7a45113cbb1b3a7282e682d8816add8d8
  support: supports
  summary: 'A prediction-smoothing regularization procedure that trains a model to
    preserve its current output distribution under approximately worst-case small
    input perturbations, constructing those perturbations without using target labels.
    Version: arXiv:1704.03976v2, 2018-06-27; 16 pages. Complete local text pages read:
    . Actual image pages viewed: 3, 4, 5, 6. Partial/web reads are separately declared
    in the ledger. No training or benchmark execution.'
- evidence_id: virtualadversarialtraining-source-1
  kind: primary_source
  reference: https://raw.githubusercontent.com/takerum/vat_tf/c5125d267531ce0f10b2238cf95604d287de63c8/vat.py
  locator: 'Lines 1–72: numerical normalization, finite-difference power iteration,
    detached teacher and VAT loss'
  accessed_at: '2026-10-11T08:39:00Z'
  snapshot_sha256: 2d7e42b5afcfa9a7efdf5b9f9328a4cb72dcff1359f71304d26e900674e5cd16
  support: supports
  summary: 'Inspected source: takerum/vat_tf author implementation: vat.py. takerum/vat_tf
    commit c5125d267531ce0f10b2238cf95604d287de63c8. Pinned author code read at the
    cited ranges without execution.'
- evidence_id: virtualadversarialtraining-source-2
  kind: primary_source
  reference: https://raw.githubusercontent.com/takerum/vat_tf/c5125d267531ce0f10b2238cf95604d287de63c8/train_semisup.py
  locator: 'Lines 45–75: labeled NLL, unlabeled VAT branch, optional entropy term
    and optimizer setup'
  accessed_at: '2026-10-11T08:39:00Z'
  snapshot_sha256: 9936e7353823eac91e5ec869d165c4839526e2a7235d40262c12de5a37c4f49b
  support: supports
  summary: 'Inspected source: takerum/vat_tf author implementation: train_semisup.py.
    takerum/vat_tf commit c5125d267531ce0f10b2238cf95604d287de63c8. Pinned author
    code read at the cited ranges without execution.'
- evidence_id: virtualadversarialtraining-source-3
  kind: primary_source
  reference: https://raw.githubusercontent.com/takerum/vat_tf/c5125d267531ce0f10b2238cf95604d287de63c8/layers.py
  locator: 'Lines 130–149: stable log-softmax, KL divergence and conditional entropy'
  accessed_at: '2026-10-11T08:39:37Z'
  snapshot_sha256: a2fde9dadc19b5d214fe9f89794160e504f793bd23ede2c1161f4eb589e1f47a
  support: supports
  summary: 'Inspected source: takerum/vat_tf author implementation: layers.py. takerum/vat_tf
    commit c5125d267531ce0f10b2238cf95604d287de63c8. Pinned author code read at the
    cited ranges without execution.'
- evidence_id: regularizedinformationmaximization-source
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2010/file/42998cf32d552343bc8e460416382dca-Paper.pdf
  locator: Sections 2–5, PDF pp. 2–5, Equations (1)–(10); Section 6.1, p. 6 for initialization
    and regularization-sweep context
  accessed_at: '2026-10-11T08:34:36Z'
  snapshot_sha256: 9da080bfdbab78fc03b89f5970b045b779386c79c73f82c474d2ad7fc420e33e
  support: supports
  summary: 'A discriminative clustering framework that fits conditional class probabilities
    by maximizing empirical input–assignment mutual information penalized by classifier
    complexity, with linear and kernel softmax configurations. Version: NIPS 2010;
    nine-page proceedings PDF; author order follows PDF title page. Complete local
    text pages read: 1, 2, 4, 5. Actual image pages viewed: 3, 4, 5. Partial/web reads
    are separately declared in the ledger. No training or benchmark execution.'
- evidence_id: mutualinformationneuralestimation-source
  kind: primary_source
  reference: https://proceedings.mlr.press/v80/belghazi18a/belghazi18a.pdf
  locator: Sections 2–3, PDF pp. 2–4, Equations (2)–(6), Algorithm 1 and estimator-consistency
    discussion
  accessed_at: '2026-10-11T08:34:36Z'
  snapshot_sha256: 8fd7e622220a5995e47230971d383a737ac12e10ced30d48734fd513f8c0d3be
  support: supports
  summary: 'A mutual-information estimation procedure that trains a neural statistics
    function to maximize a Donsker–Varadhan objective contrasting joint samples with
    product-of-marginals samples, using stochastic optimization and an optional moving-average
    denominator for gradient estimation. Version: ICML 2018, PMLR 80:531–540; ten-page
    main PDF. Complete local text pages read: . Actual image pages viewed: 2, 3, 4.
    Partial/web reads are separately declared in the ledger. No training or benchmark
    execution.'
- evidence_id: mutualinformationneuralestimation-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v80/belghazi18a/belghazi18a-supp.zip
  locator: 'Sections 8.2.1–8.2.3, supplementary PDF pp. 4–7: Donsker–Varadhan proof,
    approximation/estimation assumptions and bounded Lipschitz critic sample-complexity
    result'
  accessed_at: '2026-10-11T08:36:13Z'
  snapshot_sha256: 327266969da08050035408ffd27ae1125105469da0ed3e4c653ba13dd3d71425
  support: supports
  summary: 'Inspected source: Mutual Information Neural Estimation — Supplementary
    Material. ICML 2018 publisher supplementary ZIP member mine_appendix.pdf; eight
    pages; sha256 identifies extracted PDF, not ZIP. Exact page/image scope is recorded
    in source_analysis; the ZIP source hash identifies its extracted PDF member as
    stated in version metadata.'
- evidence_id: mutualinformationneuralestimation-source-2
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: 'Section 2.2, PDF pp. 2–4, Equations (3)–(7): Monte Carlo bias of the log-partition
    term and moving-average-gradient interpretation'
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information. ICML 2019,
    PMLR 97:5171–5180; ten-page main PDF. Primary follow-up proof passages were inspected;
    no empirical results are inferred.'
- evidence_id: infonce-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1807.03748v2
  locator: Section 2.3, PDF pp. 3–4, Equation (2) and density-ratio discussion; Appendix
    A.1 p. 13, with its approximation explicitly qualified
  accessed_at: '2026-10-11T08:34:36Z'
  snapshot_sha256: 5ef5e1ab47d2273f418f01f66fb8eb1431ba9b185b7cba45e9955f0fee36427d
  support: supports
  summary: 'A contrastive log-softmax objective that identifies a joint positive among
    sampled candidates and, under independent marginal-negative sampling, gives an
    expectation-level lower bound on mutual information. Version: arXiv:1807.03748v2,
    2019-01-22; originally submitted 2018-07-10; 13 pages. Complete local text pages
    read: 1, 2, 3, 4, 13. Actual image pages viewed: 3, 4, 13. Partial/web reads are
    separately declared in the ledger. No training or benchmark execution.'
- evidence_id: infonce-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: Section 2.3, PDF p. 4, Equations (8)–(10), footnote 2 and log(K) ceiling
    discussion
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information. ICML 2019,
    PMLR 97:5171–5180; ten-page main PDF. Primary follow-up proof passages were inspected;
    no empirical results are inferred.'
- evidence_id: corrections
  kind: record_content
  reference: research/discovery/20261011T084632Z-contrastive-information-regularization.json
  accessed_at: '2026-10-11T08:51:15Z'
  support: supports
  locator: review_refinements
  summary: Original draft statements/locators and hashes, exact correction time and
    final hashes preserve the issue43 VAT correction, MINE population-gradient clarification
    and RIM locator expansion.
- evidence_id: citation-correction
  kind: record_content
  reference: research/discovery/20261011T085047Z-contrastive-citation-correction.json
  accessed_at: '2026-10-11T08:51:15Z'
  support: supports
  locator: changes and visual_reinspection
  summary: Issue44 corrects the Poole footnote locator from4 to2 in both CPC and InfoNCE.
    Original/final record hashes and actual correction time are preserved. The initial
    saved review missed the minor locator defect and is retained unchanged.
- evidence_id: initial-review
  kind: record_content
  reference: reviews/structured/20261011T084915Z-contrastive-information-regularization/review.yaml
  accessed_at: '2026-10-11T08:51:15Z'
  support: context_only
  summary: Initial author self-review of the precorrection working-tree records; its
    no-actionable-findings conclusion missed the footnote locator. This new review
    assesses all five current records and explicitly acknowledges that miss.
assessments:
- assessment_id: contrastivepredictivecoding
  area: evidence
  topic: Identity, primary support, mechanism, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - contrastivepredictivecoding-source
  - contrastivepredictivecoding-source-1
  summary: 'CPC denotes the van den Oord et al. procedure, with configurable encoders
    and ordered context. It uses InfoNCE but is not identical to that loss. It differs
    from DIM local-to-global feature matching and from SimCLR augmentation-pair learning.
    An autoregressive context module is part of the original procedure; a GRU and
    raw-input reconstruction are not requirements. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native
    IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts
    returned 52 worktree and 75 main-checkout lines: existing component discussions
    and discovery/review references, plus unrelated ignored dependency text in main.
    Short acronyms were compared in normalized identities. Four nearest maintained
    mechanisms and eleven exact AIO candidate nodes with direct parent edges were
    inspected.'
  details: 'Compute z_t=g_enc(x_t) and c_t=g_ar(z_<=t). For each selected future offset
    k use the positive score f_k(x,c_t)=exp(z(x)^T W_k c_t). Form a candidate set
    containing one true future observation from the context-conditional distribution
    and N−1 negatives, ideally drawn independently from the observation marginal.
    Minimize the expected negative log of the positive score divided by the sum of
    all N scores, including the positive, over selected prediction horizons. Train
    the encoder, context module and prediction parameters jointly. With the ideal
    sampling scheme and a sufficiently expressive optimally fitted score, the optimal
    score is proportional to the conditional-to-marginal density ratio, with a context-dependent
    factor cancelling in the categorical probabilities. The expected loss yields the
    InfoNCE lower bound I(X_future;C)>=log(N)−L_NCE under its sampling assumptions.
    This is an expectation-level statement, not a guarantee for one minibatch. Learned
    local representations or context summaries can be used downstream. Limitations:
    The bound is at most log(N) and depends on the negative proposal. Same-speaker,
    same-sequence or otherwise conditional negatives used in particular experiments
    do not automatically satisfy the ideal independent marginal sampling assumptions.
    The original appendix uses an approximate substitution in its derivation. The
    population bound is supported here by Poole et al.’s separate proof, not by promoting
    that approximation to an exact equality. Finite critics, finite samples and incomplete
    optimization do not guarantee density-ratio recovery or an accurate numerical
    mutual-information estimate. Future-predictive information can include nuisance
    factors. Only declared primary passages were inspected. No CPC implementation,
    training run or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified procedure, or for InfoNCE a reusable mathematical objective;
      not a checkpoint or benchmark outcome.
    evidence_ids:
    - contrastivepredictivecoding-source
  - name: aio-assessment
    value: 'related_match: AIO:SelfsupervisedLearning; related_match: AIO:ContrastiveLearning'
    definition: CPC constructs prediction targets from ordered observations without
      manual target labels. This relates an algorithm to a self-supervised task, not
      an is-a claim or equivalence. CPC learns representations by positive-versus-negative
      discrimination. The AIO target is modeled under DeepNeuralNetwork; the relation
      links a procedure to that representation-learning approach without treating
      the algorithm as a network class.
    evidence_ids:
    - identity
    - mapping
- assessment_id: virtualadversarialtraining
  area: evidence
  topic: Identity, primary support, mechanism, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:VirtualAdversarialTraining
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - virtualadversarialtraining-source
  - virtualadversarialtraining-source-1
  - virtualadversarialtraining-source-2
  - virtualadversarialtraining-source-3
  summary: 'VAT denotes the Miyato et al. procedure described in the 2018 manuscript
    revision. The virtual target is the model’s current prediction. Label-free perturbation
    construction does not mean the complete supervised or semi-supervised training
    objective has no labels. VAT is a component of IMSAT but is not that information-maximization
    framework or a generative adversarial network. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native
    IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts
    returned 52 worktree and 75 main-checkout lines: existing component discussions
    and discovery/review references, plus unrelated ignored dependency text in main.
    Short acronyms were compared in normalized identities. Four nearest maintained
    mechanisms and eleven exact AIO candidate nodes with direct parent edges were
    inspected.'
  details: 'For a fixed parameter snapshot theta_hat, approximately maximize D(p_theta_hat(y|x)||p_theta_hat(y|x+r))
    over ||r||_2<=epsilon; the reported classifier implementation uses KL divergence.
    At r=0 the smooth KL objective has zero value and first derivative. Its local
    quadratic approximation gives a dominant-Hessian-eigenvector direction. Approximate
    that direction by initializing a random unit vector, taking the gradient with
    respect to r at a small displacement xi*d, normalizing it, and optionally repeating
    this power-iteration approximation. Scale the resulting direction by epsilon.
    For a model update, hold both the teacher prediction and the selected perturbation
    fixed while minimizing D(p_theta_hat(y|x)||p_theta(y|x+r_vadv)). Average this
    regularizer over available inputs to obtain R_VAT, and minimize supervised negative
    log likelihood plus alpha times R_VAT. The general formulation can use labeled
    and unlabeled inputs; the inspected semi-supervised driver applies its VAT branch
    to the unlabeled-input tensor. The pinned code defaults to one iteration, detaches
    the teacher and perturbation construction, and computes KL from softmax probabilities
    and stable log-softmax values. Its vatent branch separately adds conditional entropy
    minimization. Limitations: The Hessian direction relies on a local quadratic approximation
    and finite-difference power iteration. One iteration does not solve the exact
    finite-radius maximization and provides no certified adversarial robustness. The
    perturbation radius, norm, input representation and regularization weight affect
    which prediction changes are penalized. Semantic label preservation is not guaranteed
    for arbitrary perturbations. A constant classifier can have zero consistency loss;
    VAT alone does not identify meaningful classes. The task loss or other learning
    signals remain material. The author code uses epsilon-stabilized vector normalization,
    so its returned vector need not have exactly the ideal radius. Batch-normalization
    handling and finite arithmetic also belong to implementation scope. Three source
    files were inspected at the declared ranges without execution. The earlier 2015
    precursor was identified but its full methods were not compared; no historical-version
    equivalence or benchmark reproduction is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified procedure, or for InfoNCE a reusable mathematical objective;
      not a checkpoint or benchmark outcome.
    evidence_ids:
    - virtualadversarialtraining-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected AIO candidates describe layers, LLM-specific tasks
      or generative adversarial architectures rather than label-free worst-case prediction
      smoothing. A shared regularization or adversarial word does not provide a sufficiently
      scoped mapping. AIO:RegularizationLayer: A layer applying parameter/activity
      penalties is not this whole-model input-perturbation training procedure. AIO:ActivityRegularizationLayer:
      Output activity penalties do not specify distributional consistency under a
      virtual adversarial input. AIO:SemiSupervisedLLM: The class describes an LLM-specific
      learning arrangement; VAT is a general prediction regularizer. AIO:GenerativeAdversarialNetwork:
      Competing generator/discriminator training is not VAT’s local input-perturbation
      procedure. AIO:GenerativeAdversarialNetworkAugmentedLLM: Its related adversarial-training
      synonym is attached to an LLM-specific generative-adversarial class and does
      not establish VAT identity. AIO:SelfsupervisedLearning: The class describes
      self-supervised prediction tasks. VAT by itself specifies a consistency penalty,
      not a missing-input prediction task.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: regularizedinformationmaximization
  area: evidence
  topic: Identity, primary support, mechanism, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:RegularizedInformationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - regularizedinformationmaximization-source
  summary: 'RIM denotes Gomes et al.’s named clustering framework. This record keeps
    its linear, kernel, nonuniform-prior and semi-supervised configurations explicit.
    It differs from IMSAT’s augmentation-consistency regularizer and from IIC’s information
    between paired assignment variables. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 203 preceding native IDs/names/aliases.
    Ignored-inclusive word-delimited searches of both full checkouts returned 52 worktree
    and 75 main-checkout lines: existing component discussions and discovery/review
    references, plus unrelated ignored dependency text in main. Short acronyms were
    compared in normalized identities. Four nearest maintained mechanisms and eleven
    exact AIO candidate nodes with direct parent edges were inspected.'
  details: 'For N unlabeled inputs let p_theta(y|x_i) be conditional cluster probabilities
    and q(y)=N^−1 sum_i p_theta(y|x_i). Maximize H(q)−N^−1 sum_i H(p_theta(.|x_i))−R(theta).
    The linear configuration uses softmax(w_y^T x+b_y), R=lambda sum_y ||w_y||², and
    unpenalized biases, optimized with L-BFGS. Initialize by oversegmenting the data,
    fitting a multinomial logistic classifier to the resulting pseudo-labels, then
    optimizing the regularized information objective. Redundant categories can shrink
    toward zero marginal probability as their weights decay and biases become negative.
    The kernel configuration replaces linear scores with sum_i alpha_yi K(x_i,x)+b_y
    and penalizes RKHS squared norms alpha_y^T K alpha_y, with a regularization coefficient.
    A nonuniform-prior variant instead maximizes −mean conditional entropy−KL(q||D)−R
    for a chosen class prior D. A semi-supervised extension adds labeled log likelihood
    and weights the unlabeled information term separately. Limitations: The information
    objective is nonconcave. Finite L-BFGS optimization and a regularization sweep
    do not guarantee a global optimum or a true cluster count. Softmax probabilities
    are positive at finite parameters; exact class deletion is an ideal limiting description.
    The uniform empirical input distribution and class-balance preference implicit
    in marginal entropy may not fit the desired population. The nonuniform-prior variant
    changes the objective and requires compatible prior support. Kernel scores require
    an appropriate positive-semidefinite kernel for the stated RKHS penalty. Equation
    (8) omits the regularization coefficient while the following derivative includes
    it; this record makes that coefficient explicit. The paper reports ground-truth
    adjusted-Rand scores across regularization settings. Those plots are not evidence
    for an automatic label-free hyperparameter or true-cluster-count selection rule.
    Primary methods and declared experimental context were inspected; no RIM implementation,
    optimizer behavior or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified procedure, or for InfoNCE a reusable mathematical objective;
      not a checkpoint or benchmark outcome.
    evidence_ids:
    - regularizedinformationmaximization-source
  - name: aio-assessment
    value: 'related_match: AIO:UnsupervisedClustering'
    definition: The unlabeled RIM configuration learns cluster assignments. The AIO
      target is the clustering task; this is an algorithm-to-task association, not
      an is-a assertion. The optional semi-supervised extension is stated separately.
    evidence_ids:
    - identity
    - mapping
- assessment_id: mutualinformationneuralestimation
  area: evidence
  topic: Identity, primary support, mechanism, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:MutualInformationNeuralEstimation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - mutualinformationneuralestimation-source
  - mutualinformationneuralestimation-source-1
  - mutualinformationneuralestimation-source-2
  summary: 'MINE denotes the original neural Donsker–Varadhan estimator and its moving-average
    training heuristic. The paper’s alternative MINE-f objective is a different variational
    bound and is not silently equated with this record. MINE estimates dependence;
    DIM is a representation-learning framework that can use dependence critics, and
    InfoNCE is a different finite-candidate objective. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 203 preceding native
    IDs/names/aliases. Ignored-inclusive word-delimited searches of both full checkouts
    returned 52 worktree and 75 main-checkout lines: existing component discussions
    and discovery/review references, plus unrelated ignored dependency text in main.
    Short acronyms were compared in normalized identities. Four nearest maintained
    mechanisms and eleven exact AIO candidate nodes with direct parent edges were
    inspected.'
  details: 'For a neural statistics function T_theta(x,z), optimize J(theta)=E_joint[T_theta]−log(E_product[exp(T_theta)]).
    Under the variational representation’s integrability assumptions, each population
    J(theta) is a lower bound on I(X;Z); optimizing within a neural family yields
    its restricted supremum. Estimate expectations from observed joint pairs and samples
    approximating the product of marginals, such as mismatched or shuffled pairs.
    The minibatch gradient contains a ratio of product-sample means and is generally
    biased. The original training heuristic replaces its exponential-moment denominator
    by an exponential moving average to reduce this bias. Poole et al. show that,
    when a positive running denominator is held fixed for an update, the resulting
    update has an interpretation as the gradient of a different unnormalized variational
    bound. This interpretation does not make the moving-average update a generally
    unbiased gradient estimator of the population Donsker–Varadhan objective. After
    fitting a critic, evaluating sample means in the Donsker–Varadhan expression gives
    a finite estimate, not a certified mutual-information lower bound for that sample.
    Limitations: Finite-sample log-moment estimation is biased, can be unstable for
    large critic scores, and need not remain below true mutual information. Reusing
    samples for critic fitting adds selection effects. The moving-average denominator
    is a bias-reduction heuristic. Its fixed-denominator alternative-bound interpretation
    does not prove that a same-batch updated running statistic is independent of the
    current samples or that the original Donsker–Varadhan gradient is unbiased. Strong-consistency
    arguments separate neural approximation from empirical estimation under compactness,
    continuity and measure assumptions. The fixed-family uniform-convergence result
    is not a proof that stochastic gradient optimization reaches the required supremum.
    Bounded/Lipschitz critic sample-complexity assumptions do not hold automatically
    for arbitrary networks and distributions. Shuffling one finite batch can include
    fixed points and dependent pairs; it is not literally independent sampling from
    the population product distribution. Sampling construction must be stated when
    interpreting estimates. As a mathematical consequence of a loose lower bound,
    reducing a poorly optimized estimated lower bound does not certify a reduction
    in true mutual information. No author implementation or numerical estimator experiment
    was audited.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified procedure, or for InfoNCE a reusable mathematical objective;
      not a checkpoint or benchmark outcome.
    evidence_ids:
    - mutualinformationneuralestimation-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected snapshot has no suitable class for this neural statistical
      estimator. A critic architecture or downstream representation-learning/GAN use
      is not sufficient to map the estimator itself. AIO:DeepNeuralNetwork: A neural
      network is the parameterized critic component, not the joint-versus-product
      estimation algorithm. AIO:RepresentationLearning: Learning reusable features
      is a possible application; it is not the definition of mutual-information estimation.
      AIO:ContrastiveLearning: This network/representation-learning class does not
      specify the Donsker–Varadhan estimator or its stochastic-gradient correction.
      AIO:GenerativeAdversarialNetwork: An optional downstream use in generative training
      does not make MINE a generator/discriminator architecture.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: infonce
  area: evidence
  topic: Identity, primary support, mechanism, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:InfoNCE
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - infonce-source
  - infonce-source-1
  summary: 'InfoNCE is the loss introduced in contrastive predictive coding, separable
    from the CPC encoder/context/prediction procedure. It does not by itself prescribe
    cosine similarity, temperature, augmentation pairs, symmetric losses or an autoregressive
    architecture. Named configurations such as SimCLR NT-Xent and DIM’s finite-masking
    implementation require their own sampling and numerical qualifications. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    203 preceding native IDs/names/aliases. Ignored-inclusive word-delimited searches
    of both full checkouts returned 52 worktree and 75 main-checkout lines: existing
    component discussions and discovery/review references, plus unrelated ignored
    dependency text in main. Short acronyms were compared in normalized identities.
    Four nearest maintained mechanisms and eleven exact AIO candidate nodes with direct
    parent edges were inspected.'
  details: 'Given a context c, draw one positive x_+ jointly with c and N−1 negative
    candidates independently from the marginal p(x), with N>=2. For real scores s(x,c),
    define ell=−log[exp(s(x_+,c))/sum_(j=1)^N exp(s(x_j,c))], including the positive
    in the denominator, and minimize L_NCE=E[ell]. For the ideal sampling scheme,
    log(N)−L_NCE<=I(X;C); since ell>=0, the bound is at most log(N) and may itself
    be negative. An expressive optimum scores the conditional-to-marginal density
    ratio up to a context-dependent multiplicative constant in exp(s). The categorical
    objective remains definable with other candidate constructions, but its stated
    mutual-information interpretation then requires a separate argument. Poole et
    al. provide an independent rigorous derivation of the expected bound beyond the
    approximate step in the original CPC appendix. Limitations: The lower bound holds
    for an expectation under its specified joint and independent marginal sampling.
    A realized finite-batch number is not certified to be below true mutual information.
    The log(N) ceiling limits estimation of high mutual information at a fixed candidate
    count. Optimizing a finite, restricted critic need not recover the density ratio
    or true information. False semantic negatives, conditional negative proposals
    and correlated in-batch candidates can change the learned representation and invalidate
    an unqualified use of the ideal sampling proof. Semantic usefulness is not guaranteed
    by the loss. Finite masking values contribute nonzero denominator mass and are
    not algebraically identical to removing candidates. No numerical implementation
    or training experiment was run for this loss record.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A specified procedure, or for InfoNCE a reusable mathematical objective;
      not a checkpoint or benchmark outcome.
    evidence_ids:
    - infonce-source
  - name: aio-assessment
    value: 'related_match: AIO:ContrastiveLearning'
    definition: InfoNCE is an objective used for positive-versus-negative discrimination
      in contrastive representation learning. The AIO target is modeled as a network/learning
      approach, so this mathematical-method-to-approach association is not an is-a
      relation or an exact match.
    evidence_ids:
    - identity
    - mapping
- assessment_id: procedure-loss-boundary
  area: scope
  topic: CPC and InfoNCE remain distinct
  outcome: supported
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:InfoNCE
  evidence_ids:
  - contrastivepredictivecoding-source
  - infonce-source
  - infonce-source-1
  - neighbors
  summary: Retain CPC as an algorithm and InfoNCE as its separable mathematical objective.
  details: CPC specifies observation encoding, autoregressive context and future-horizon
    discrimination. InfoNCE specifies categorical candidate discrimination without
    prescribing an architecture, cosine score, temperature or augmentation pair. The
    positive belongs in the denominator. The rigorous expected-information bound requires
    its ideal sampling scheme; a finite batch is not a certified bound, the bound
    has a log(N) ceiling, and the original appendix approximate substitution is explicitly
    distinguished from the follow-up proof.
- assessment_id: regularization-boundaries
  area: representation
  topic: VAT and RIM versus IMSAT
  outcome: supported
  target_ids:
  - AIMech:VirtualAdversarialTraining
  - AIMech:RegularizedInformationMaximization
  evidence_ids:
  - virtualadversarialtraining-source
  - virtualadversarialtraining-source-1
  - virtualadversarialtraining-source-2
  - virtualadversarialtraining-source-3
  - regularizedinformationmaximization-source
  - neighbors
  summary: Retain label-free perturbation smoothing and regularized discriminative
    clustering as distinct procedures.
  details: VAT holds teacher and perturbation fixed for the parameter update and uses
    an approximate dominant-Hessian direction; one power iteration is not an exact
    adversary. The code confirms stable log-softmax KL and numerical vector normalization.
    The corrected objective is NLL plus alpha times VAT. RIM regularizes classifier
    complexity and encourages informative categorical assignments; linear/kernel,
    prior and semi-supervised configurations remain explicit. Finite softmax outputs
    do not literally delete categories, and nonconvex optimization does not certify
    true cluster-count recovery. IMSAT combines different information and consistency
    components rather than establishing equivalence to either component.
- assessment_id: estimator-boundaries
  area: representation
  topic: MINE population bounds, empirical estimates and moving averages
  outcome: supported
  target_ids:
  - AIMech:MutualInformationNeuralEstimation
  - AIMech:InfoNCE
  evidence_ids:
  - mutualinformationneuralestimation-source
  - mutualinformationneuralestimation-source-1
  - mutualinformationneuralestimation-source-2
  - infonce-source-1
  - neighbors
  summary: Retain distinct DV neural estimation and finite-candidate contrastive objectives
    with conditional theory.
  details: MINE distinguishes a population variational lower bound, a neural-family
    supremum, an empirical estimator and finite stochastic optimization. The log-moment
    ratio produces biased minibatch gradients; a fixed positive EMA denominator has
    a different-bound gradient interpretation, not generic unbiasedness for the population
    DV objective. The supplement’s approximation and uniform-convergence assumptions
    do not imply SGD convergence. InfoNCE has a different sampling construction and
    log-count ceiling. Neither estimator proves semantic quality or certifies true
    information from one sample.
- assessment_id: mapping-boundaries
  area: scope
  topic: Positive mappings and explicit no-match decisions
  outcome: supported
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:VirtualAdversarialTraining
  - AIMech:RegularizedInformationMaximization
  - AIMech:MutualInformationNeuralEstimation
  - AIMech:InfoNCE
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain qualified related matches for CPC, RIM and InfoNCE and bounded no-match
    assessments for VAT and MINE.
  details: Eleven exact AIO nodes, definitions/scoped synonyms and direct parents
    were inspected. CPC relates to SelfsupervisedLearning and ContrastiveLearning;
    RIM relates to UnsupervisedClustering; InfoNCE relates to ContrastiveLearning.
    These are qualified procedure-to-task/approach or loss-to-approach relations,
    not is-a assertions. VAT and MINE have bounded no-match assessments with six and
    four individually rejected targets respectively. Network components, LLM-specific
    classes and incidental applications do not establish mapping identity.
- assessment_id: vat-correction
  area: provenance
  topic: Prepublication issue43 correction
  outcome: supported
  target_ids:
  - AIMech:VirtualAdversarialTraining
  evidence_ids:
  - virtualadversarialtraining-source
  - corrections
  summary: Current locator and loss wording match the inspected primary revision.
  details: The draft used nonexistent section labels III–IV and V-A and left alpha
    placement grammatically ambiguous. The current record cites Sections3.2–3.4 and
    Section4, including Equation8, and says NLL plus alpha times R_VAT. The ledger
    preserves the original draft and correction provenance. This is a current-state
    review; no prior saved finding or independent reviewer is invented.
- assessment_id: citation-correction
  area: provenance
  topic: Current Poole locator after issue44
  outcome: supported
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:InfoNCE
  evidence_ids:
  - contrastivepredictivecoding-source-1
  - infonce-source-1
  - citation-correction
  - initial-review
  summary: Both current records cite footnote2 on PDF page4, visually verified.
  details: The initial review is a historical working-tree observation, not rewritten
    to hide a missed finding. The original discovery ledger preserves its initial
    locators; the appended correction ledger and current record bytes establish the
    corrected state. No mathematical claim or mapping changed. No earlier structured
    finding is invented, so this current-state assessment does not claim formal finding-lineage
    resolution.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:ContrastivePredictiveCoding
  - AIMech:VirtualAdversarialTraining
  - AIMech:RegularizedInformationMaximization
  - AIMech:MutualInformationNeuralEstimation
  - AIMech:InfoNCE
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - contrastivepredictivecoding-source
  - contrastivepredictivecoding-source-1
  - virtualadversarialtraining-source
  - virtualadversarialtraining-source-1
  - virtualadversarialtraining-source-2
  - virtualadversarialtraining-source-3
  - regularizedinformationmaximization-source
  - mutualinformationneuralestimation-source
  - mutualinformationneuralestimation-source-1
  - mutualinformationneuralestimation-source-2
  - infonce-source
  - infonce-source-1
  - corrections
  - citation-correction
  - initial-review
  rationale: Predictive representation learning, its contrastive objective, virtual
    perturbation smoothing, discriminative information clustering and neural DV estimation
    differ in inputs, outputs and optimization targets. Shared losses or components
    do not establish identity. RIM configurations remain explicit within its framework;
    no upstream AIO mutation follows from these decisions.
limitations:
- The initial review and original ledger are preserved with their precorrection locators;
  the appended issue44 correction and this current review state the final values.
- Adversarial author self-review only; all five records remain DRAFT.
- Full-text access and extraction do not imply every page was read. Exact page/image/code
  scope is saved in the discovery ledger.
- Only declared VAT implementation ranges were inspected; no CPC/RIM/MINE code equivalence,
  training or benchmark reproduction is asserted.
- Expected information bounds, approximation assumptions and uniform convergence do
  not certify finite samples or optimizer outputs.
- Positive mappings and no-match decisions are curator assessments bounded to the
  pinned AIO snapshot.
- Positive discoveries and outstanding leads keep the goal active.
tags:
- native-concepts
- contrastive-learning
- mutual-information
- regularization
- self-review
- discovery-ongoing
```
