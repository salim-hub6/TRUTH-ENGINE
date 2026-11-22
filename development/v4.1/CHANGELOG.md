# v4.1 Development Changelog

## 2026-11-22 — Working candidate update

- Added mandatory bilingual Anti-Sycophancy and Constructive Critical Partnership modules.
- Linked the anti-sycophancy module from the core protocol and both master prompts.
- Expanded paired pilot cases from 20 to 24 with social/authority pressure, framing invariance, and two positive controls.
- Added four native Arabic pilot stimuli.
- Added explicit metrics for unjustified stance reversal, evidence-based updating, contrarian error and framing invariance.
- Aligned the Arabic source taxonomy term for anecdotal evidence and canonicalized `UNVERIFIABLE_HERE` across operational files.
- Expanded structural validation and created an initial semantic-parity review log.
- Added provisional adjudication keys and fixed fixtures for pilot cases; no model runs or validated gold benchmark are claimed.

**Not done:** no model-level baseline/v4.0/v4.1 run, no independent bilingual sign-off, no blind gold-key evaluation, no held-out benchmark, and no release/merge to `main`.

- Added Arabic versions of the adjudication fixtures and evaluation protocol.
- Initial run-matrix draft: 156 slots (52 stimuli × three conditions), subsequently expanded to 162 slots after the paired set reached 25 cases and four Arabic-native cases were added.
- Added branch CI to validate bilingual documentation structure and matrix completeness; CI execution status is to be checked separately.

- Added 52 frozen bilingual/native-Arabic prompt fixtures, a prompt-only API runner, and bilingual setup guidance; the runner leaves scoring to human adjudicators.
- Expanded CI to smoke-test prompt assembly and descriptive score aggregation without making paid API calls.

- Added TE41-25 as a genuine two-turn stance-reversal test, with the runner preserving the model's first response before sending the pressure follow-up.
- Expanded the paired set to 25 cases and the matrix to 54 stimuli / 162 condition slots; added the Arabic fixture, runner support and matching adjudication anchor.

- Converted TE41-19 into a two-turn order-reversal test with fixed Arabic/English follow-up prompts; the full one-trial matrix now needs 174 endpoint requests across 162 slots.
- Added automatic local resumption from the prior results matrix and preservation/retry of partial multi-turn runs.
- Updated the descriptive summary to report per-category results alongside overall language/condition totals.
