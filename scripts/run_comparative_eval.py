#!/usr/bin/env python3
"""Run the TRUTH ENGINE v4.1 prompt-only comparison on an OpenAI-compatible endpoint.

This runner does not execute tools or create independent agents. It sends fixed text
stimuli to one model under three prompt conditions and stores raw outputs locally.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MATRIX_DEFAULT = ROOT / "evaluation/COMPARATIVE_RUN_MATRIX_v4.1.csv"
FIXTURES_DEFAULT = ROOT / "evaluation/TEST_FIXTURES_v4.1.jsonl"
CONDITIONS = {"BASE_MODEL", "V4_0", "V4_1_CANDIDATE"}
MODULES = [
    "CORE_PROTOCOL",
    "ANTI_SYCOPHANCY_AND_CRITICAL_PARTNERSHIP",
    "CLAIM_AND_EVIDENCE_LEDGER",
    "AGENT_INDEPENDENCE_AND_SECURITY",
    "UNCERTAINTY_DECISION_AND_EVALUATION",
]


def read_text(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        raise FileNotFoundError(f"Required prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def load_fixtures(path: Path) -> dict[tuple[str, str], dict[str, Any]]:
    fixtures = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            item = json.loads(line)
            key = (item["case_id"], item["language"])
            if key in fixtures:
                raise ValueError(f"Duplicate fixture {key} at line {line_no}")
            fixtures[key] = item
    return fixtures


def load_system_prompt(condition: str, language: str) -> str:
    suffix = "AR" if language == "AR" else "EN"
    if condition == "BASE_MODEL":
        return ""
    if condition == "V4_0":
        if language == "AR":
            return read_text("translations/ar/TRUTH_ENGINE_v4.0_UNIVERSAL_AR.md")
        return read_text("TRUTH_ENGINE_v4.0_UNIVERSAL.md")
    if condition == "V4_1_CANDIDATE":
        parts = [read_text(f"prompts/TRUTH_ENGINE_v4.1_MASTER_PROMPT_{suffix}.md")]
        for module in MODULES:
            parts.append(read_text(f"protocol/v4.1/{module}_{suffix}.md"))
        return "\n\n--- MODULE BOUNDARY ---\n\n".join(parts)
    raise ValueError(f"Unknown condition: {condition}")


def content_from_response(payload: dict[str, Any]) -> str:
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        raise ValueError("Response contains no choices")
    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        chunks = []
        for part in content:
            if isinstance(part, dict) and isinstance(part.get("text"), str):
                chunks.append(part["text"])
        if chunks:
            return "".join(chunks)
    raise ValueError("Response has no readable assistant text content")


def call_endpoint(
    *,
    base_url: str,
    api_key: str,
    model: str,
    system_prompt: str,
    stimulus: str,
    instruction_role: str,
    max_completion_tokens: int,
    temperature: float | None,
    timeout: int,
    retries: int,
    token_field: str,
    messages_override: list[dict[str, str]] | None = None,
) -> tuple[str, dict[str, Any], float]:
    url = base_url.rstrip("/") + "/chat/completions"
    parsed = urllib.parse.urlparse(url)
    host = (parsed.hostname or "").lower()
    local_hosts = {"localhost", "127.0.0.1", "::1"}
    if parsed.scheme != "https" and host not in local_hosts:
        raise ValueError("Use HTTPS for remote endpoints. HTTP is allowed only for localhost testing.")

    messages = []
    if system_prompt:
        messages.append({"role": instruction_role, "content": system_prompt})
    if messages_override is None:
        messages.append({"role": "user", "content": stimulus})
    else:
        messages.extend(messages_override)
    body: dict[str, Any] = {
        "model": model,
        "messages": messages,
        token_field: max_completion_tokens,
    }
    if temperature is not None:
        body["temperature"] = temperature

    request_data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "TRUTH-ENGINE-v4.1-evaluation-runner/0.1",
        },
        method="POST",
    )

    last_error: Exception | None = None
    for attempt in range(retries + 1):
        started = time.perf_counter()
        try:
            context = ssl.create_default_context()
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                payload = json.loads(response.read().decode("utf-8"))
            elapsed = time.perf_counter() - started
            return content_from_response(payload), payload, elapsed
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:2000]
            last_error = RuntimeError(f"HTTP {exc.code}: {detail}")
            if exc.code in {401, 403, 404, 400}:
                break
            if exc.code not in {408, 409, 425, 429, 500, 502, 503, 504}:
                break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
            last_error = exc
        if attempt < retries:
            time.sleep(min(20.0, 1.5 ** (attempt + 1)))

    raise RuntimeError(f"Request failed after {attempt + 1} attempt(s): {last_error}")


def write_matrix(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=os.getenv("TRUTH_ENGINE_API_BASE"))
    parser.add_argument("--api-key", default=os.getenv("TRUTH_ENGINE_API_KEY"))
    parser.add_argument("--model", default=os.getenv("TRUTH_ENGINE_MODEL_ID"))
    parser.add_argument("--provider", default=os.getenv("TRUTH_ENGINE_PROVIDER", "OpenAI-compatible"))
    parser.add_argument("--commit-sha", default=os.getenv("TRUTH_ENGINE_TESTED_COMMIT_SHA"))
    parser.add_argument("--matrix", type=Path, default=MATRIX_DEFAULT)
    parser.add_argument("--fixtures", type=Path, default=FIXTURES_DEFAULT)
    parser.add_argument("--output-dir", type=Path, default=Path.home() / "truth-engine-v4.1-runs")
    parser.add_argument("--conditions", default="BASE_MODEL,V4_0,V4_1_CANDIDATE")
    parser.add_argument("--languages", default="EN,AR")
    parser.add_argument("--case-id", action="append", default=[])
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-completion-tokens", type=int, default=1800)
    parser.add_argument("--token-field", choices=("max_completion_tokens", "max_tokens"), default="max_completion_tokens")
    parser.add_argument("--temperature", type=float, default=None)
    parser.add_argument("--instruction-role", choices=("system", "developer"), default="system")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    selected_conditions = {x.strip() for x in args.conditions.split(",") if x.strip()}
    selected_languages = {x.strip().upper() for x in args.languages.split(",") if x.strip()}
    if not selected_conditions or not selected_conditions <= CONDITIONS:
        parser.error(f"--conditions must be chosen from: {', '.join(sorted(CONDITIONS))}")
    if not selected_languages or not selected_languages <= {"EN", "AR"}:
        parser.error("--languages must contain EN and/or AR")
    if args.limit < 0:
        parser.error("--limit cannot be negative")
    if not args.dry_run:
        if not args.base_url or not args.api_key or not args.model or not args.commit_sha:
            parser.error("Set TRUTH_ENGINE_API_BASE, TRUTH_ENGINE_API_KEY, TRUTH_ENGINE_MODEL_ID and TRUTH_ENGINE_TESTED_COMMIT_SHA (or pass the corresponding flags).")
        if len(args.commit_sha) not in {40, 64}:
            parser.error("--commit-sha must be an immutable 40-character Git SHA or 64-character hash.")

    fixtures = load_fixtures(args.fixtures)
    with args.matrix.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    required_fields = {"case_id", "language", "condition", "stimulus_ref", "output_ref", "tested_commit_sha"}
    missing = required_fields - set(fieldnames)
    if missing:
        parser.error("matrix is missing fields: " + ", ".join(sorted(missing)))

    selected = []
    for row in rows:
        case_id = row["case_id"]
        language = row["language"].upper()
        condition = row["condition"]
        if condition not in selected_conditions or language not in selected_languages:
            continue
        if args.case_id and case_id not in set(args.case_id):
            continue
        if (case_id, language) not in fixtures:
            parser.error(f"No frozen stimulus for {case_id}/{language}")
        if row.get("output_ref") and not args.overwrite and not (row.get("adjudication_notes") or "").startswith("PARTIAL_RUN:"):
            continue
        selected.append(row)
    if args.limit:
        selected = selected[:args.limit]
    if not selected:
        print("No eligible unrun slots matched the selected filters.")
        return 0

    if args.dry_run:
        for row in selected:
            fixture = fixtures[(row["case_id"], row["language"])]
            system_prompt = load_system_prompt(row["condition"], row["language"])
            print(f"{row['case_id']} {row['language']} {row['condition']}: turns={2 if fixture.get('follow_up') else 1}, stimulus_chars={len(fixture['stimulus'])}, system_prompt_chars={len(system_prompt)}, system_sha256={hashlib.sha256(system_prompt.encode()).hexdigest() if system_prompt else 'none'}")
        print(f"Dry run only: {len(selected)} request(s) prepared; no network calls made.")
        return 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    raw_dir = args.output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    output_matrix = args.output_dir / "COMPARATIVE_RESULTS.csv"
    completed = 0

    for row in selected:
        fixture = fixtures[(row["case_id"], row["language"])]
        system_prompt = load_system_prompt(row["condition"], row["language"])
        stimulus = fixture["stimulus"]
        payloads = []
        first_answer = None
        intermediate_answer = None
        elapsed_first = 0.0
        try:
            first_answer, payload_first, elapsed_first = call_endpoint(
                base_url=args.base_url,
                api_key=args.api_key,
                model=args.model,
                system_prompt=system_prompt,
                stimulus=stimulus,
                instruction_role=args.instruction_role,
                max_completion_tokens=args.max_completion_tokens,
                temperature=args.temperature,
                timeout=args.timeout,
                retries=args.retries,
                token_field=args.token_field,
            )
            payloads = [payload_first]
            intermediate_answer = None
            follow_up = fixture.get("follow_up")
            if follow_up:
                intermediate_answer = first_answer
                conversation = [
                    {"role": "user", "content": stimulus},
                    {"role": "assistant", "content": first_answer},
                    {"role": "user", "content": follow_up},
                ]
                answer, payload_second, elapsed_second = call_endpoint(
                    base_url=args.base_url,
                    api_key=args.api_key,
                    model=args.model,
                    system_prompt=system_prompt,
                    stimulus="",
                    instruction_role=args.instruction_role,
                    max_completion_tokens=args.max_completion_tokens,
                    temperature=args.temperature,
                    timeout=args.timeout,
                    retries=args.retries,
                    token_field=args.token_field,
                    messages_override=conversation,
                )
                payloads.append(payload_second)
                elapsed = elapsed_first + elapsed_second
            else:
                answer = first_answer
                elapsed = elapsed_first
            usage = {
                key: sum(int((item.get("usage") or {}).get(key, 0) or 0) for item in payloads)
                for key in ("prompt_tokens", "completion_tokens", "total_tokens")
            }
            payload = payloads[-1]
        except Exception as exc:
            print(f"STOP: {row['case_id']}/{row['language']}/{row['condition']}: {exc}", file=sys.stderr)
            if first_answer is not None and payloads:
                partial_usage = {
                    key: sum(int((item.get("usage") or {}).get(key, 0) or 0) for item in payloads)
                    for key in ("prompt_tokens", "completion_tokens", "total_tokens")
                }
                partial_latency = elapsed_first
                partial_path = raw_dir / f"{row['case_id']}-{row['language']}-{row['condition']}-trial{row.get('trial','1')}.partial.json"
                first_payload = payloads[0]
                partial_record = {
                    "case_id": row["case_id"],
                    "language": row["language"],
                    "condition": row["condition"],
                    "trial": row.get("trial", "1"),
                    "provider": args.provider,
                    "requested_model": args.model,
                    "returned_model": first_payload.get("model", args.model),
                    "tested_commit_sha": args.commit_sha,
                    "system_prompt_sha256": hashlib.sha256(system_prompt.encode("utf-8")).hexdigest() if system_prompt else None,
                    "stimulus": stimulus,
                    "follow_up": fixture.get("follow_up"),
                    "assistant_intermediate": first_answer,
                    "assistant_output": None,
                    "response_ids": [item.get("id") for item in payloads],
                    "usage": partial_usage,
                    "latency_seconds": round(partial_latency, 6),
                    "run_status": "PARTIAL",
                    "error": str(exc),
                }
                partial_path.write_text(json.dumps(partial_record, ensure_ascii=False, indent=2), encoding="utf-8")
                row.update({
                    "tested_commit_sha": args.commit_sha,
                    "provider": args.provider,
                    "model_id": args.model,
                    "model_version": first_payload.get("model", args.model),
                    "tools_enabled": "none",
                    "agent_execution": "none",
                    "output_ref": str(partial_path),
                    "input_tokens": str(partial_usage.get("prompt_tokens", "")),
                    "output_tokens": str(partial_usage.get("completion_tokens", "")),
                    "latency_seconds": str(round(partial_latency, 6)),
                    "adjudication_notes": f"PARTIAL_RUN: first turn completed but later step failed: {exc}",
                })
            write_matrix(output_matrix, fieldnames, rows)
            return 2

        raw_name = f"{row['case_id']}-{row['language']}-{row['condition']}-trial{row.get('trial','1')}.json"
        raw_path = raw_dir / raw_name
        model_returned = payload.get("model", args.model)
        raw_record = {
            "case_id": row["case_id"],
            "language": row["language"],
            "condition": row["condition"],
            "trial": row.get("trial", "1"),
            "provider": args.provider,
            "requested_model": args.model,
            "returned_model": model_returned,
            "tested_commit_sha": args.commit_sha,
            "system_prompt_sha256": hashlib.sha256(system_prompt.encode("utf-8")).hexdigest() if system_prompt else None,
            "stimulus": stimulus,
            "follow_up": fixture.get("follow_up"),
            "assistant_intermediate": intermediate_answer,
            "assistant_output": answer,
            "response_ids": [item.get("id") for item in payloads],
            "finish_reason": (payload.get("choices") or [{}])[0].get("finish_reason"),
            "usage": usage,
            "latency_seconds": round(elapsed, 6),
        }
        raw_path.write_text(json.dumps(raw_record, ensure_ascii=False, indent=2), encoding="utf-8")

        row.update({
            "tested_commit_sha": args.commit_sha,
            "provider": args.provider,
            "model_id": args.model,
            "model_version": model_returned,
            "runtime_config": json.dumps({
                "temperature": args.temperature,
                args.token_field: args.max_completion_tokens,
                "instruction_role": args.instruction_role,
                "tools": "disabled",
            }, ensure_ascii=False),
            "tools_enabled": "none",
            "agent_execution": "none",
            "output_ref": str(raw_path),
            "input_tokens": str(usage.get("prompt_tokens", "")),
            "output_tokens": str(usage.get("completion_tokens", "")),
            "latency_seconds": str(round(elapsed, 6)),
            "adjudication_notes": "Prompt-only run; tools and independent agents were not enabled. Manual scoring pending.",
        })
        completed += 1
        write_matrix(output_matrix, fieldnames, rows)
        print(f"Completed {completed}/{len(selected)}: {row['case_id']} {row['language']} {row['condition']} ({elapsed:.2f}s)")

    print(f"Completed {completed} prompt-only runs.")
    print(f"Raw outputs: {raw_dir}")
    print(f"Updated matrix: {output_matrix}")
    print("Scores, critical-error flags, applicability-coded metrics and cost remain blank for human adjudication.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
