# TRUTH ENGINE v4.1 — Semantic Parity Review Log

**Review date:** 2026-11-22  
**Status:** Initial internal review; not independent bilingual sign-off and not a release approval.

## Scope checked

The English/Arabic pairs for the Core Protocol, Anti-Sycophancy and Constructive Critical Partnership, Claim and Evidence Ledger, Agent Independence and Security, Uncertainty/Decision/Evaluation, Master Prompt and 24 paired pilot cases were reviewed for section structure, operational terms and material obligations.

## Checks completed

- Paired files have matching section-heading counts and corresponding section sequence.
- The 24 paired pilot IDs and their order match across the English and Arabic files.
- Authority hierarchy, least privilege, external-action approval, no self-escalation, no invented tool use, claim statuses, source checks, blind-first-pass conditions, role separation, uncertainty fields and release-gate concepts were checked for alignment.
- Four Arabic-authored cases were added separately so the Arabic test set is not limited to translated English prompts.

## Divergences found and corrected in this pass

1. The Arabic Evidence Ledger had rendered **anecdotal** as `تجريبي`, which can mean experimental. It was corrected to `شخصي/شهاداتي` to preserve the intended testimonial/anecdotal source category.
2. The Arabic Master Prompt used `UNVERIFIABLE` while the normative Claim Ledger uses `UNVERIFIABLE_HERE`. The prompt was aligned to the exact canonical status code.
3. The Arabic design proposal used the shorter `UNVERIFIABLE` label. It was aligned to `UNVERIFIABLE_HERE`, with the operational meaning restricted to current tools, sources and access.
4. The pilot count and source-gap records were updated from 20 to 24 paired cases.
5. The Arabic Core Protocol's definition of verification coverage was expanded to state its denominator explicitly, matching the English operational definition.
6. The Arabic Master Prompt now names the Decision Analyst function, matching the English prompt; a minor Arabic typo in the citation-entailment definition was also corrected.
7. The bilingual pilot set is now accompanied by provisional adjudication keys and standardized fixtures. These are evaluator guidance, not results or an independently validated gold set.
8. Added an Arabic counterpart to the evaluation protocol and Arabic adjudication fixtures for all 24 paired cases; both remain subject to independent bilingual review.
9. Added a 156-slot matrix with three conditions per stimulus and a field dictionary clarifying that empty metrics are not-applicable/unscored rather than zero.

## Remaining review requirements

- A second qualified bilingual reviewer must inspect the full text, not only headings or this log.
- Review should explicitly compare permissions, prohibitions, exception clauses, thresholds, status names, denominators and stop conditions.
- Native Arabic cases require Arabic-first scoring; dialect and jurisdictional coverage must be scoped rather than assumed.
- Reference answers and adjudication keys are still needed for all pilot cases.
- The four native Arabic cases are development stimuli, not held-out tests.

## Limits

This review is a documentation-level internal pass. It does not establish behavioral equivalence across models, security effectiveness, calibrated confidence, or performance improvement. No baseline/v4.0/v4.1 model-level comparative run has been completed in this work session.

10. Added aligned Arabic and English adjudication fixtures for the 24 paired cases, plus four Arabic-native stimuli. The fixtures are fixed test inputs but still require independent bilingual approval.
11. Added a 156-slot comparison plan and a prompt-only runner. It does not provide real tool execution, separate agent contexts or enforcement tests; those remain outside this runner's scope.

12. Added TE41-25 in both languages as a two-turn stance-reversal test. The runner now sends the follow-up only after preserving the model's actual first response, and aggregates token usage and latency across both requests.
13. The pilot set now contains 25 paired cases plus four Arabic-native cases: 54 stimuli and 162 planned comparison slots. These counts supersede the earlier 24/52/156 development plan.
14. TE41-22 remains a within-prompt three-framing consistency probe, not a substitute for a separate-context identity-switch experiment. This limitation is recorded in the data dictionary.

15. TE41-19 was strengthened from a single-turn language/order note to an actual two-turn matched stimulus. The runner sends the reordered wording only after preserving the first answer, allowing direct assessment of order sensitivity.
16. There are now two multi-turn tests (TE41-19 and TE41-25): 162 comparison slots still require 174 successful endpoint responses for a full one-trial run. This supersedes the earlier 168-request estimate.
17. The runner now resumes completed local rows and preserves a completed first turn as a partial record if a later turn fails; partial rows are retryable.

18. The validator now checks the exact 36-column matrix schema, the complete case-specific stimulus and adjudication anchors, and nonempty follow-up text for both multi-turn cases.
19. A local mock-endpoint smoke test exercised the two-turn request flow: the first assistant response was carried into the follow-up context and token usage was aggregated. This was a runner-mechanics test using synthetic responses, not a model benchmark.
20. No model-level BASE_MODEL/V4_0/V4_1 comparison has been executed. The latest queried GitHub commit status exposed no check runs; CI should therefore be treated as unconfirmed, not passed.

21. Separated the metric for presentation-order invariance (TE41-19) from identity/framing invariance (TE41-22). The run matrix now includes distinct fields, and the evaluator protocol and summary script report them separately.
