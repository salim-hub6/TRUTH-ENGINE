#!/usr/bin/env python3
"""Structural checks for the TRUTH ENGINE v4.1 development candidate.
These checks do not certify semantic translation parity or model performance.
"""
from __future__ import annotations
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
    "evaluation/PILOT_ADJUDICATION_KEYS_v4.1.md",
    "translations/ar/TRANSLATION_POLICY_AR.md",
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

    if errors:
        for e in errors: print(f"FAIL: {e}")
        print(f"Structural checks failed: {len(errors)}")
        return 1
    print("PASS: required files, fences, placeholders, local links, paired heading counts, 24 paired case IDs and four native Arabic cases.")
    print("LIMIT: structural checks do not certify semantic translation parity, security, or protocol performance.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
