# TRUTH ENGINE v4.1 — Development Candidate

**Status:** Working draft. Not released, not merged into `main`, and not performance-validated.

This branch starts the v4.1 modular development track while preserving v4.0 as the public baseline. The purpose is to turn partially specified v4.0 principles and material from the project's development memo into testable operating procedures—not to add terminology or claim proven gains.

## Language governance

- English is the normative authoring source for shared protocol requirements and module maintenance.
- Arabic is an official translation intended to preserve the same obligations, permissions, status definitions, thresholds, and stop conditions.
- Arabic is not a separate policy fork. Translation changes must be reviewed against the English source.
- User-facing language remains the user's language. English-first source maintenance does not require English-only operation.
- No language is presumed superior across all models and tasks. Paired English/Arabic evaluation is required, including native Arabic tasks.

## v4.1 workstreams

1. **Core protocol:** task triage, claim-based analysis, evidence requirements, falsifiability, and stopping rules.
2. **Claim and evidence ledger:** atomic claims, source provenance, source classification, contradiction tracking, and six-question source checks.
3. **Agent independence and security:** blind first-pass assessment, role separation, persuasion resistance, prompt-injection boundaries, and least privilege.
4. **Uncertainty and decision analysis:** confidence, evidence strength, verification coverage, residual uncertainty, and the firewall between factual findings and recommendations.
5. **Evaluation:** pilot cases, reproducible runs, metric definitions, failure severity, bilingual parity, and release gates.

## Source material reviewed

The development track compares the current v4.0 repository with the supplied v4.0 Arabic copies, both v3.1 variants, and the Arabic development memo containing the proposed Master Prompt 2.0. The two v3.1 files are not interchangeable: one variant weakens tool-permission and action-approval safeguards. That variant is quarantined pending provenance review and is not a source for v4.1.

## Release gate

Do not describe this candidate as stable until:
- module content and internal consistency are reviewed;
- Arabic/English semantic parity has been checked by bilingual reviewers;
- pilot cases are run against a baseline and v4.0 under recorded conditions;
- critical security tests pass;
- accuracy, abstention, cost, latency, and regressions are reported;
- the change log and source citations are reviewed.

No benchmark result or performance improvement is claimed. This README records the branch's development intent; it is not evidence that the complete module set is already published on this branch.
