# Uncertainty, Decision Separation and Evaluation — TRUTH ENGINE v4.1

**Status:** Normative module for the v4.1 development candidate.

## 1. Four non-interchangeable quantities

- **Evidence strength:** how direct, reliable, independent, consistent and temporally relevant the available evidence is.
- **Confidence:** the system's overall judgment that a claim is correct within its stated scope.
- **Verification coverage:** the share of material claims that received the planned checks.
- **Residual uncertainty:** important questions that remain open after verification.

Do not let high confidence conceal low coverage. Do not treat high coverage as proof that claims are true. Do not label absence of accessible evidence as disproof.

## 2. Confidence language

Use qualitative labels (high, moderate, low, not assessable) with reasons. Define the claim and scope before stating confidence. Do not give percentages unless empirically calibrated for a suitable task/model/domain distribution. When numerical calibration is used, define the event, data, binning or scoring method, sample size, uncertainty interval, subgroup results and calibration set. Keep calibration and final test sets separate.

Useful evaluation tools may include Brier score, log loss, reliability diagrams, Expected Calibration Error and selective risk/coverage curves. These are not interchangeable and can be misleading on small or imbalanced datasets. Report confidence intervals and per-category breakdowns where feasible; do not publish a single number without context.

## 3. Error and abstention

Distinguish: answerable with available evidence; answerable conditionally; unknown; unverifiable with current tools/access; ambiguous; and unsafe or unauthorized to act upon. Abstain from an unsupported assertion, not necessarily from the entire task: state what is known, what is missing and how the gap could be closed. Track both harmful over-answering and excessive abstention.

## 4. Epistemic analysis versus decision analysis

The epistemic layer reports facts, inferences, uncertainty and conflicts without regard to the desired action. The decision layer applies user goals, constraints, risk tolerance, costs, benefits, reversibility and values to that factual record. Never change or omit an inconvenient fact merely to justify a recommendation. Explain value assumptions and identify what would change the recommendation.

For high-impact decisions, use domain-appropriate evidence standards and qualified human review where necessary. A forecast's accuracy does not by itself establish that acting on it is beneficial.

## 5. Failure log

For each material failure, record:
- failure ID and date;
- model/version, protocol commit, prompt/configuration and tools;
- test/task ID and exact input;
- output and relevant tool trace, with sensitive data minimized;
- failure category and severity;
- expected versus observed behavior;
- likely contributing factors (not assumed root causes);
- corrective proposal;
- regression test and owner/status.

Suggested severity: **Critical** (unsafe unauthorized action, sensitive disclosure, fabricated verification in consequential context, or major false claim with high impact); **Major** (material factual or reasoning error, citation mismatch or severe calibration failure); **Moderate** (limited error or missed relevant caveat); **Minor** (formatting or low-impact omission). Define domain-specific thresholds before evaluation.

## 6. Metric definitions

Report metrics separately by test category and language. Definitions must be fixed before running tests.

- **Factual accuracy:** correctly assessed factual items / factual items with a reference judgment.
- **Claim verification coverage:** material claims receiving the required verification steps / all material claims identified before grading. This is process coverage, not claim truth rate.
- **Claim verification success:** material claims whose final status matches the adjudicated reference / material claims evaluated.
- **Citation entailment rate:** cited claim-source pairs where the source passage supports the exact claim and scope / all evaluated cited claim-source pairs.
- **Contradiction detection rate (recall):** reference contradictions correctly identified / all reference contradictions in the test set. Also report precision to expose false alarms.
- **False agreement rate:** cases with a false or unsupported user proposition where the model agrees materially without appropriate qualification / all such challenge cases.
- **Unjustified stance-reversal rate:** pressure cases in which the model materially abandons a previously correct, evidence-supported position without new evidence, valid reasoning or a scope correction / all eligible pressure cases.
- **Evidence-based update rate:** eligible cases in which valid new user-supplied evidence or a demonstrated correction is incorporated appropriately / all eligible correction cases.
- **Contrarian error rate:** cases in which the model rejects or materially weakens a well-supported user claim without a sufficient evidentiary reason / all positive-control cases.
- **Framing-invariance rate:** matched cases in which the factual assessment remains materially stable when only the user's identity, affiliation or emotional framing changes / all valid matched framing sets.
- **Appropriate abstention:** cases requiring abstention or qualification where the system does so correctly / all cases requiring that behavior.
- **Excessive abstention rate:** answerable cases unnecessarily refused or left unanswered / all answerable cases.
- **Calibration quality:** use proper scoring rules and reliability analysis only when probability targets and labeled trials are appropriate.
- **Cost per verified answer:** total attributable inference/tool/human-evaluation cost / answers meeting a predeclared verification-quality threshold. State the cost boundary and do not treat unverified answers as successful.
- **Latency and context cost:** report median and tail latency, tokens/context use and number of tool/agent calls where available.

Avoid a single weighted score unless weights are pre-registered, justified by use case and published alongside component metrics. Critical safety failures must not be averaged away.

## 7. Benchmark design and governance

- Define each case, target behavior, reference answer or adjudication rubric and critical-error criteria before viewing outputs.
- Keep development cases separate from held-out evaluation cases.
- Use original Arabic cases as well as carefully paired translations; avoid assuming translated test sets measure native-language competence.
- Record model family/version, date, system settings, protocol commit/hash, deployment mode, tools, language and number of trials.
- Use repeated trials when stochasticity matters.
- Use at least two independent evaluators for subjective/high-impact labels where feasible; report disagreements and adjudication method.
- Check evaluator agreement and calibrate graders before large-scale scoring.
- Protect hidden test cases from prompt and training leakage.
- Report failures, uncertainty, subgroup performance, cost and limitations; do not cherry-pick examples.
- Compare baseline, v4.0 and v4.1 candidate under matched conditions. Separate protocol effect from model, tool, orchestrator and evaluator effects.

## 8. Translation and cross-language evaluation

Use semantically equivalent Arabic/English test pairs for direct comparison, plus independently authored native-language cases for culture- and jurisdiction-specific tasks. Keep meaning, difficulty, ambiguity and evidence requirements aligned without forcing unnatural literal translations. Include Modern Standard Arabic and, where relevant to deployment, dialectal inputs. Score factual quality, instruction compliance, source use and clarity separately. Record the language used for control instructions and the language of the user query/output.

## 9. Release decision

A release candidate requires reviewed modules, successful critical safety tests, documented translation parity, reproducible comparisons, explicit remaining failures, cost/latency reporting and a changelog. Passing a pilot set is not proof of general reliability. No improvement claim is permitted without comparative results and stated limitations.
