# TRUTH ENGINE v4.1 — Comparative Runner Guide

**Scope:** Prompt-only evaluation through an OpenAI-compatible Chat Completions endpoint. The runner does not execute tools, send external actions or create independent agents.

## 1. What the runner does

For each fixed JSONL stimulus, the runner sends three conditions to the **same configured model**:

- `BASE_MODEL`: no TRUTH ENGINE system message.
- `V4_0`: the full v4.0 protocol in English or its Arabic companion according to the stimulus language.
- `V4_1_CANDIDATE`: the v4.1 master prompt plus the five relevant protocol modules in English or Arabic.

It writes raw response records to a local directory and a completed copy of the run matrix. It leaves all scores and evaluator judgments blank.

## 2. Requirements

- Python 3.10 or later; the runner uses only the Python standard library.
- An OpenAI-compatible endpoint supporting `POST /chat/completions`.
- Permission and budget to run the requested model.
- An immutable Git commit SHA for the exact protocol files being tested.

The OpenAI Chat Completions reference documents the `/chat/completions` endpoint and recommends `max_completion_tokens` over the deprecated `max_tokens`; parameter support varies by model. See: https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create

## 3. Configure secrets outside the repository

Set environment variables in the shell used for the test:

```bash
export TRUTH_ENGINE_API_BASE="https://YOUR-ENDPOINT/v1"
export TRUTH_ENGINE_API_KEY="YOUR_SECRET_KEY"
export TRUTH_ENGINE_MODEL_ID="YOUR_PINNED_MODEL_ID"
export TRUTH_ENGINE_PROVIDER="Provider or deployment name"
export TRUTH_ENGINE_TESTED_COMMIT_SHA="40-character-git-commit-sha"
```

Never commit the API key, put it in the CSV, or paste it into public issues/logs. The runner sends only synthetic test stimuli and protocol prompts. Keep raw outputs local and access-controlled.

## 4. Dry-run first

From the repository root:

```bash
python scripts/validate_v4_1_docs.py
python scripts/run_comparative_eval.py --dry-run --limit 6
```

The dry run assembles the first six requests (three conditions for one English/Arabic paired case) and prints stimulus/system-prompt sizes and system-prompt hashes. It makes no network calls and needs no API key.

## 5. Run a small paired smoke comparison

Run one case in both languages under all three conditions:

```bash
python scripts/run_comparative_eval.py \
  --case-id TE41-01 \
  --languages EN,AR \
  --output-dir "$HOME/truth-engine-v4.1-smoke"
```

This sends six requests. Check endpoint acceptance, context limits, returned model ID, usage, latency and raw outputs before any larger run.

## 6. Run the full 162-slot matrix

After the smoke comparison is reviewed:

```bash
python scripts/run_comparative_eval.py \
  --output-dir "$HOME/truth-engine-v4.1-full-run"
```

This schedules 162 comparison slots: 25 paired cases × two languages × three conditions, plus four native-Arabic cases × three conditions. TE41-25 makes each of its six slots a two-request exchange, so the full one-trial run sends 168 endpoint requests. The run can incur provider costs. The script does not estimate or fill cost where the provider does not report it.

Use the same model snapshot and runtime settings for all three conditions. The runner uses `max_completion_tokens` by default. For a compatible endpoint that requires the older field, use `--token-field max_tokens`. If the model does not support temperature, leave it omitted; if supported and pre-registered, pass the same `--temperature` for all conditions. Do not mix settings silently.

## 7. Manual scoring and summaries

The output directory contains:
- `raw/`: one JSON record per completed response, including prompt, answer, returned model, usage, latency, commit SHA and system-prompt hash.
- `COMPARATIVE_RESULTS.csv`: a copy of the 162-slot matrix updated with execution metadata and local raw-output references.

Two evaluators should score the results using the adjudication keys and data dictionary. Populate `score_0_2`, critical flags and only the metrics applicable to that case. Empty fields mean not applicable/not evaluated, never zero.

Then summarize:

```bash
python scripts/summarize_comparative_runs.py \
  --input "$HOME/truth-engine-v4.1-full-run/COMPARATIVE_RESULTS.csv" \
  --output "$HOME/truth-engine-v4.1-full-run/COMPARATIVE_SUMMARY.csv"
```

The summary is descriptive. It does not judge responses or validate statistical significance.

## 8. Important limitations

- This runner tests prompt-level behavior using one model endpoint. It does not demonstrate real multi-agent independence, tool authorization enforcement, safe external actions or prompt-injection security at the application layer.
- TE41-10's blind independent assessment can only be claimed if separate contexts and first-pass outputs are actually implemented by the evaluation environment; this runner does not provide them.
- Live sources are not fetched by this runner. Use the frozen facts and excerpts in the JSONL fixtures.
- It makes one run per matrix slot. Repeated trials require copying rows with unique trial numbers and preserving the same stimulus/configuration; do not overwrite prior runs.
- Model aliases may move. Use a pinned model snapshot where available and retain the exact returned model identifier and commit SHA.
- A successful API run is not a passed test. Human adjudication and held-out evaluation are still required.
