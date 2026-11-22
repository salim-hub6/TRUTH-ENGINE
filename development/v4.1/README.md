# TRUTH ENGINE v4.1 — Development Candidate

**Status:** Working draft. Not released, not merged into `main`, and not performance-validated.

This branch begins the v4.1 modular development track while preserving v4.0 as the public baseline. Its goal is to convert partially specified principles and material from the supplied development memo into testable procedures—not to add terminology for its own sake or claim unmeasured gains.

## Language governance

- English is the planned normative authoring source for shared requirements and module maintenance.
- Arabic is intended to be an official, reviewed translation—not a separate policy fork.
- Users should continue to interact in their preferred language. English-first maintenance does not imply English-only operation.
- No universal performance advantage is assumed for English. Paired Arabic/English testing, including native-language tasks, is required before making language-performance claims.
- The English normative modules and their Arabic counterparts are part of the working development package; staged publication on this branch is still in progress.

## Files currently staged on this branch

- `development/v4.1/DESIGN_PROPOSAL_AR.md` — design rationale and proposed changes.
- `development/v4.1/SOURCE_GAP_MATRIX_EN.md` — comparison of supplied source material with v4.0.
- `development/v4.1/REFERENCES.md` — research and standards references.
- `prompts/TRUTH_ENGINE_v4.1_MASTER_PROMPT_AR.md` — Arabic candidate activation prompt.
- `evaluation/TRUTH_ENGINE_v4.1_PILOT_TESTS_AR.md` — initial Arabic pilot cases.

The complete working package also contains English and Arabic module drafts, an evaluation procedure, and translation governance. Those files are not all committed to this branch yet; do not infer their presence from this README.

## Core v4.1 workstreams

1. **Claim and evidence operations:** atomic claim IDs, evidence provenance, source classification, source checks and contradiction tracking.
2. **Independent assessment:** first-pass isolation, role separation, anti-persuasion safeguards and explicit disclosure when true independence is unavailable.
3. **Falsifiability:** testable predictions, potential falsifiers, alternatives, discriminating tests and predeclared success criteria.
4. **Uncertainty and decisions:** keep confidence, evidence strength, verification coverage and residual uncertainty distinct; prevent decision preferences from rewriting factual findings.
5. **Evaluation and release governance:** reproducible pilot runs, defined metrics, failure severity, bilingual semantic parity and explicit release gates.

## Source integrity warning

The supplied v3.1 files are not all interchangeable. One variant weakens permission boundaries and approval requirements for sensitive actions. Its provenance is unknown; it is quarantined and must not be merged without provenance review.

## Release gate

Do not label this candidate stable until:
- the complete English modules are staged and reviewed;
- Arabic/English semantic parity is checked by bilingual reviewers;
- pilot cases are run against a baseline and v4.0 under recorded conditions;
- critical security tests pass;
- accuracy, abstention, cost, latency and regressions are reported;
- source references and the change log are reviewed.

No benchmark result or performance improvement is claimed.
