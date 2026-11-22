#!/usr/bin/env python3
"""Structural checks for the TRUTH ENGINE v4.1 development candidate.
These checks do not certify semantic translation parity or model performance.
"""
from __future__ import annotations
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ("protocol/v4.1/CORE_PROTOCOL_EN.md", "protocol/v4.1/CORE_PROTOCOL_AR.md"),
    ("protocol/v4.1/ANTI_SYCOPHANCY_AND_CRITICAL_PARTNERSHIP_EN.md", "protocol/v4.1/ANTI_SYCOPHANCY_AND_CRITICAL_PARTNERSHIP_AR.md"),
    ("protocol/v4.1/CLAIM_AND_EVIDENCE_LEDGER_EN.md", "protocol/v4.1/CLAIM_AND_EVIDENCE_LEDGER_AR.md"),
    ("protocol/v4.1/AGENT_INDEPENDENCE_AND_SECURITY_EN.md", "protocol/v4.1/AGENT_INDEPENDENCE_AND_SECURITY_AR.md"),
    ("protocol/v4.1/UNCERTAINTY_DECISION_AND_EVALUATION_EN.md", "protocol/v4.1/UNCERTAINTY_DECISION_AND_EVALUATION_AR.md"),
    ("prompts/TRUTH_ENGINE_v4.1_MASTER_PROMPT_EN.md", "prompts/TRUTH_ENGINE_v4.1_MASTER_PROMPT_AR.md"),
    ("evaluation/TRUTH_ENGINE_v4.1_PILOT_TESTS_EN.md", "evaluation/TRUTH_ENGINE_v4.1_PILOT_TESTS_AR.md"),
    ("evaluation/EVALUATION_PROTOCOL_v4.1.md", "evaluation/EVALUATION_PROTOCOL_v4.1_AR.md"),
    ("evaluation/EVALUATION_PROTOCOL_v4.1.md", "evaluation/EVALUATION_PROTOCOL_v4.1_AR.md"),
]
REQUIRED = [p for pair in PAIRS for p in pair] + [
    "development/v4.1/README.md",
    "development/v4.1/SOURCE_GAP_MATRIX_AR.md",
    "development/v4.1/SOURCE_GAP_MATRIX_EN.md",
    "development/v4.1/DESIGN_PROPOSAL_AR.md",
    "development/v4.1/REFERENCES.md",
    "development/v4.1/SEMANTIC_PARITY_REVIEW_LOG.md",
    "development/v4.1/CHANGELOG.md",
    "evaluation/NATIVE_ARABIC_PILOT_CASES.md",
    "evaluation/EVALUATION_PROTOCOL_v4.1.md",
    "evaluation/EVALUATION_PROTOCOL_v4.1_AR.md",
    "evaluation/COMPARATIVE_RUN_MATRIX_DATA_DICTIONARY.md",
    "evaluation/PILOT_ADJUDICATION_KEYS_v4.1.md",
    "evaluation/PILOT_ADJUDICATION_KEYS_v4.1_AR.md",
    "evaluation/COMPARATIVE_RUN_MATRIX_v4.1.csv",
    "evaluation/COMPARATIVE_RUN_MATRIX_DATA_DICTIONARY.md",
    "evaluation/TEST_FIXTURES_v4.1.jsonl",
    "scripts/summarize_comparative_runs.py",
    "scripts/run_comparative_eval.py",
    "translations/ar/TRANSLATION_POLICY_AR.md",
    ".github/workflows/v4.1-validation.yml",
]
def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    if errors:
        for e in errors: print(f"FAIL: {e}")
        return 1

    for rel in REQUIRED:
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        for fence in ("````", "```"):
            if sum(1 for ln in text.splitlines() if ln.strip().startswith(fence)) % 2:
                errors.append(f"unbalanced {fence} fence: {rel}")
        if re.search(r"\b(?:TODO|PLACEHOLDER|TBD)\b", text, re.I):
            errors.append(f"placeholder marker: {rel}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].strip()
            if not target or re.match(r"^(?:https?://|mailto:|tel:)", target, re.I):
                continue
            if not (p.parent / target).resolve().exists():
                errors.append(f"broken local link in {rel}: {target}")

    for en, ar in PAIRS:
        a = (ROOT/en).read_text(encoding="utf-8")
        b = (ROOT/ar).read_text(encoding="utf-8")
        headings_a = re.findall(r"^#{1,3} ", a, re.M)
        headings_b = re.findall(r"^#{1,3} ", b, re.M)
        if len(headings_a) != len(headings_b):
            errors.append(f"paired heading-count mismatch: {en} ({len(headings_a)}) vs {ar} ({len(headings_b)})")

    case_sets=[]
    for rel in ("evaluation/TRUTH_ENGINE_v4.1_PILOT_TESTS_EN.md", "evaluation/TRUTH_ENGINE_v4.1_PILOT_TESTS_AR.md"):
        text=(ROOT/rel).read_text(encoding="utf-8")
        ids=re.findall(r"^### (TE41-\d{2}) —", text, re.M)
        if len(ids) != 24 or len(set(ids)) != 24:
            errors.append(f"expected 24 unique pilot cases in {rel}; found {len(ids)}")
        case_sets.append(ids)
    if len(case_sets)==2 and case_sets[0] != case_sets[1]:
        errors.append("English/Arabic pilot case IDs or ordering differ")
    native_text=(ROOT/"evaluation/NATIVE_ARABIC_PILOT_CASES.md").read_text(encoding="utf-8")
    native_ids=re.findall(r"^## (ATE41-\d{2}) —", native_text, re.M)
    if native_ids != ["ATE41-01", "ATE41-02", "ATE41-03", "ATE41-04"]:
        errors.append(f"native Arabic case IDs incomplete or misordered: {native_ids}")

    for rel in ("evaluation/PILOT_ADJUDICATION_KEYS_v4.1.md", "evaluation/PILOT_ADJUDICATION_KEYS_v4.1_AR.md"):
        key_text = (ROOT / rel).read_text(encoding="utf-8")
        key_ids = re.findall(r"^### (TE41-\d{2}) —", key_text, re.M)
        if key_ids != [f"TE41-{i:02d}" for i in range(1, 25)]:
            errors.append(f"adjudication keys missing, duplicated or misordered in {rel}")

    # Validate immutable prompt fixtures for every language/case combination.
    fixture_path = ROOT / "evaluation/TEST_FIXTURES_v4.1.jsonl"
    fixture_keys = set()
    with fixture_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                fixture = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid JSONL fixture at line {line_no}: {exc}")
                continue
            key = (fixture.get("case_id"), fixture.get("language"))
            if key in fixture_keys:
                errors.append(f"duplicate JSONL fixture key: {key}")
            fixture_keys.add(key)
            if not isinstance(fixture.get("stimulus"), str) or not fixture["stimulus"].strip():
                errors.append(f"empty stimulus in JSONL fixture at line {line_no}")
    expected_fixture_keys = {(f"TE41-{i:02d}", lang) for i in range(1, 25) for lang in ("EN", "AR")}
    expected_fixture_keys |= {(f"ATE41-{i:02d}", "AR") for i in range(1, 5)}
    if fixture_keys != expected_fixture_keys:
        errors.append(f"fixture coverage mismatch: found {len(fixture_keys)}, expected {len(expected_fixture_keys)}")

    # Validate that the comparison matrix covers all 52 stimuli under all 3 conditions.
    matrix_path = ROOT / "evaluation/COMPARATIVE_RUN_MATRIX_v4.1.csv"
    with matrix_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    expected_conditions = {"BASE_MODEL", "V4_0", "V4_1_CANDIDATE"}
    expected_stimuli = {f"TE41-{i:02d}" for i in range(1, 25)}
    expected_stimuli |= {f"ATE41-{i:02d}" for i in range(1, 5)}
    seen = set()
    for row in rows:
        key = (row.get("case_id"), row.get("language"), row.get("condition"), row.get("trial"))
        if key in seen:
            errors.append(f"duplicate run-matrix key: {key}")
        seen.add(key)
    if len(rows) != 156:
        errors.append(f"expected 156 comparison slots, found {len(rows)}")
    found_stimuli = {row.get("case_id") for row in rows}
    if found_stimuli != expected_stimuli:
        errors.append("run matrix stimulus IDs do not match the 24 paired plus four native-Arabic cases")
    for case_id in expected_stimuli:
        case_rows = [row for row in rows if row.get("case_id") == case_id]
        expected_languages = {"EN", "AR"} if case_id.startswith("TE41-") else {"AR"}
        observed_languages = {row.get("language") for row in case_rows}
        if observed_languages != expected_languages:
            errors.append(f"unexpected language coverage for {case_id}: {observed_languages}")
        for lang in expected_languages:
            observed_conditions = {row.get("condition") for row in case_rows if row.get("language") == lang}
            if observed_conditions != expected_conditions:
                errors.append(f"missing comparison condition for {case_id}/{lang}: {observed_conditions}")

    if errors:
        for e in errors: print(f"FAIL: {e}")
        print(f"Structural checks failed: {len(errors)}")
        return 1
    print("PASS: required files, paired docs, adjudication keys, 52 fixed stimuli, four native Arabic cases and 156 comparison slots.")
    print("LIMIT: structural checks do not certify semantic translation parity, security, or protocol performance.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
