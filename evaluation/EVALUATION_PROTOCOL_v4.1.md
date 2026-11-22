# TRUTH ENGINE v4.1 — Evaluation Protocol

**Status:** Draft procedure for candidate testing; not a benchmark certification.

## 1. Evaluation questions

The evaluation must answer distinct questions rather than collapse them:
1. Does v4.1 improve the targeted behaviors relative to the base model and v4.0?
2. Does it introduce regressions in accuracy, helpfulness, language quality, abstention, safety or latency?
3. Does the change work across Arabic and English, and across the tested model/platform configurations?
4. Does the benefit justify additional tokens, tools, agent calls, review time and operational complexity?

## 2. Conditions

The current run matrix contains **52 stimuli**: 24 matched English/Arabic pairs (48 prompts) plus four native-Arabic cases. Each stimulus has three planned conditions:
- `BASE_MODEL`: the base model without TRUTH ENGINE instructions.
- `V4_0`: the same model configured with the repository's v4.0 protocol.
- `V4_1_CANDIDATE`: the same model configured with the v4.1 candidate prompt and relevant modules.

This produces **156 planned run slots** before any repeated trials. A slot is not a completed run. The CSV template must be populated only after an actual execution; do not fill missing outputs, scores, model identity or costs with estimates. Use a fixed model snapshot and matched runtime settings across conditions where possible. The v4.1 and v4.0 prompts should not silently receive different tools or context budgets.

Run, where feasible:
- Base model without TRUTH ENGINE.
- TRUTH ENGINE v4.0 using the existing installation method.
- v4.1 candidate using the Master Prompt and relevant modules.
- Optional v4.1 with tools and actual independent agents, only if available.

Do not call simulated roles independent agents. Keep model snapshot, temperature/sampling, context, tools, source packet, task prompt and evaluator rubric matched as closely as possible. Record every deviation.

## 3. Case lifecycle

For each case:
1. Define the failure mode and target behavior.
2. Write the exact input, context, source packet and allowed tools.
3. Define reference answer or adjudication rubric before running models.
4. Define material claims and critical-error conditions.
5. Mark whether the right behavior is answer, qualify, ask one necessary question, abstain from a claim, or stop an action.
6. Run the same case on all conditions.
7. Preserve raw outputs and tool traces subject to privacy controls.
8. Score each criterion and explain the score.
9. Record errors and create regression cases from failures.

## 4. Scoring

Use 0/1/2 for the current pilot set: fail/partial/pass. A case may have multiple criteria; score each separately where practical. Critical errors are flags, not merely deductions. Do not compare raw sums across different case sets or rubrics.

## 5. Inter-rater review

Use at least two evaluators for subjective or consequential cases when feasible. Give evaluators the rubric before they see model identity where practical. Record their independent scores, disagreement and adjudication. Report agreement method and limitations. A model must not be the only grader of its own output.

## 6. Metrics and denominators

Use definitions in `protocol/v4.1/UNCERTAINTY_DECISION_AND_EVALUATION_EN.md`. Report metrics per category and language. Always state the denominator, exclusions, missing observations and whether repeated trials are independent. Report precision and recall where the measure is a detection task. For calibration, report the calibration dataset, proper scoring rule, reliability plot or equivalent, number of samples and uncertainty. Do not infer calibrated confidence from verbal hedges.

## 7. Statistical caution

For paired comparisons, preserve case pairing. Report raw counts and uncertainty intervals; use an appropriate paired analysis if sample size and design justify it. Do not claim improvement from one or two successful demonstrations. Do not claim equivalence because a small test found no significant difference. Keep a held-out set that is not used to edit the prompt.

## 8. Multilingual comparison

Use three complementary groups:
- Paired Arabic/English translations with aligned meaning and difficulty.
- Native-authored Arabic tasks, especially local context, language nuance and jurisdictional matters.
- English-native tasks where the evidence and reference data originate in English.

Track control-prompt language, user-input language, source language and answer language separately. Use qualified bilingual evaluators for semantic parity. Include dialectal Arabic only when in scope and identify the variety used.

## 9. Security testing

Use harmless dummy data and sandboxed tools. Test direct and indirect prompt injection, tool permission escalation, destination substitution, persuasive false agents, repeated-source laundering, agent-to-agent pressure, sensitive action ambiguity and hidden/untrusted content. Include benign controls in every tested language and report false positives. Prompt-only success is not evidence of technical security if the application lacks permission enforcement.

## 10. Reporting template

Report at minimum:
- protocol commit/hash and files loaded;
- model/provider/platform/version and date;
- control prompt language, user language, output language;
- tools, context and agent execution level;
- dataset/case-set version, cases and trials;
- rubric version, evaluator count and agreement;
- per-category and per-language scores;
- critical errors and failure examples;
- accuracy, false agreement, unjustified stance reversal, evidence-based update, contrarian error, framing invariance, citation entailment, verification coverage, abstention and calibration metrics as applicable;
- latency, tokens, tool calls and cost boundary;
- limitations, missing conditions and known confounders.

## 11. Release gate

The candidate may progress only when the owners can show:
- all normative modules reviewed;
- no unresolved critical mismatch between Arabic and English versions;
- critical safety cases pass in the tested configuration;
- v4.1's intended behaviors improve or remain acceptably stable under predeclared thresholds;
- no unacceptable regression in direct factual accuracy, language behavior, over-abstention or user utility;
- costs and complexity are reported;
- a held-out test confirms the result;
- a reviewer approves the final change log.

Passing the gate authorizes a release candidate for further review; it does not prove general reliability or universal compatibility.
