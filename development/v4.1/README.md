# TRUTH ENGINE v4.1 — Development Candidate

**Status:** Working draft on `development/v4.1-modular-preview`; not a released version, not merged into `main`, and not performance-validated.

## Purpose

This work converts the supplied development memo and v4.0 requirements into modular, testable operating requirements. It does not replace v4.0. The v4.0 files remain the baseline for controlled comparison.

## Normative language and parity

- English is the normative source for shared protocol requirements and module maintenance.
- Arabic is the official companion translation, not a separate policy fork; its internal parity review is in progress and final bilingual sign-off remains a release gate.
- The user's interaction language remains the user's choice.
- Translation parity concerns obligations, permissions, evidence statuses, verification thresholds, stop/abstention conditions, metric definitions and release gates—not literal word matching.
- No universal English-over-Arabic performance advantage is assumed. Paired and native-language testing is required.

## Module inventory

### Protocol

- `protocol/v4.1/CORE_PROTOCOL_EN.md` / `_AR.md` — normative core.
- `protocol/v4.1/ANTI_SYCOPHANCY_AND_CRITICAL_PARTNERSHIP_EN.md` / `_AR.md` — **mandatory cross-cutting module**; preserves anti-sycophancy as the project's primary purpose.
- `protocol/v4.1/CLAIM_AND_EVIDENCE_LEDGER_EN.md` / `_AR.md` — atomic claims, evidence provenance, source checks and contradiction handling.
- `protocol/v4.1/AGENT_INDEPENDENCE_AND_SECURITY_EN.md` / `_AR.md` — role separation, blinded assessment, persuasion resistance and tool boundaries.
- `protocol/v4.1/UNCERTAINTY_DECISION_AND_EVALUATION_EN.md` / `_AR.md` — confidence, verification coverage, residual uncertainty, decision separation, metric definitions and evaluation governance.

### Prompts and evaluation

- `prompts/TRUTH_ENGINE_v4.1_MASTER_PROMPT_EN.md` / `_AR.md` — compact activation prompts; neither replaces the modules.
- `evaluation/TRUTH_ENGINE_v4.1_PILOT_TESTS_EN.md` / `_AR.md` — 25 paired pilot cases, including positive controls against performative contrarianism; four native Arabic cases are separately listed in `evaluation/NATIVE_ARABIC_PILOT_CASES.md`.
- `evaluation/EVALUATION_PROTOCOL_v4.1.md` / `_AR.md` — execution, scoring, statistical caution and reporting rules.
- `evaluation/COMPARATIVE_RUN_MATRIX_DATA_DICTIONARY.md` — field definitions, metric coding and the empty-cell rule.
- `evaluation/TEST_FIXTURES_v4.1.jsonl` — 54 frozen stimuli (25 paired in English/Arabic plus four Arabic-native cases).
- `evaluation/COMPARATIVE_RUNNER_GUIDE_EN.md` / `_AR.md` — setup and use of the prompt-only comparison runner.
- `scripts/run_comparative_eval.py` — optional runner for an OpenAI-compatible Chat Completions endpoint; API secrets stay outside the repository. It resumes from a prior local result matrix and retries partial multi-turn rows.
- `evaluation/PILOT_ADJUDICATION_KEYS_v4.1.md` — provisional fixed fixtures and evaluator anchors for 25 paired and four native-Arabic cases; not a validated gold benchmark.
- `evaluation/PILOT_ADJUDICATION_KEYS_v4.1_AR.md` — Arabic fixtures for the 25 paired cases; independent bilingual review is still required.
- `evaluation/COMPARATIVE_RUN_MATRIX_v4.1.csv` — 162 planned run slots: 54 stimuli × three conditions (base model, v4.0, v4.1); a full one-trial run sends 174 API requests because TE41-19 and TE41-25 use two turns.
- `scripts/summarize_comparative_runs.py` — descriptive metric aggregation for manually scored outputs; blank values remain unscored/not applicable.
- `.github/workflows/v4.1-validation.yml` — structural and matrix checks on branch updates.

### Design and governance

- `development/v4.1/DESIGN_PROPOSAL_AR.md` — Arabic design rationale and change proposal.
- `development/v4.1/SOURCE_GAP_MATRIX_AR.md` and `SOURCE_GAP_MATRIX_EN.md` — comparison of source material, v4.0 coverage and v4.1 operationalization.
- `development/v4.1/REFERENCES.md` — background sources; they do not establish v4.1 effectiveness.
- `development/v4.1/SEMANTIC_PARITY_REVIEW_LOG.md` — internal review record; independent bilingual sign-off remains outstanding.
- `development/v4.1/CHANGELOG.md` — working change record.
- `translations/ar/TRANSLATION_POLICY_AR.md` — language governance and semantic parity requirements.
- `scripts/validate_v4_1_docs.py` — structural documentation checks only.

## Evaluation status

The documentation validator checks required files, code fences, placeholders, internal links, paired heading structures and pilot-case IDs. The semantic review log records corrections and unresolved sign-off requirements. These checks do not establish semantic equivalence by themselves.

No model-level comparison has yet been run. A valid comparison must run the same cases against the base model, v4.0 and v4.1 under recorded, matched conditions, with independent scoring, raw outputs, tool traces, latency and cost. Do not claim improvement from structural checks or pilot-set design.

## Release gate

Do not label this candidate stable until: (1) all normative modules are reviewed, (2) Arabic/English semantic parity is signed off, (3) the 25 paired pilot cases and four native-Arabic cases are run against baseline and v4.0 with recorded conditions, (4) critical security tests pass, (5) a held-out test and regression review are completed, (6) cost and latency are reported, and (7) a reviewer approves the change log. No performance improvement is claimed here.
