#!/usr/bin/env python3
"""Summarize manually adjudicated TRUTH ENGINE comparative runs.

Blank metric cells are treated as not applicable or not yet scored, never as zero.
The script computes descriptive statistics only; it does not judge outputs.
"""
from __future__ import annotations

import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

METRICS = [
    "false_agreement",
    "unjustified_stance_reversal",
    "evidence_based_update",
    "contrarian_error",
    "framing_invariance_pass",
    "citation_entailment_pass",
    "contradiction_detected",
    "appropriate_abstention",
    "excessive_abstention",
]


def parse_number(value: str | None) -> float | None:
    if value is None or value.strip() == "":
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"Expected numeric value, received {value!r}") from exc


def parse_flag(value: str | None) -> int | None:
    if value is None or value.strip() == "":
        return None
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return 1
    if normalized in {"0", "false", "no", "n"}:
        return 0
    raise ValueError(f"Expected 0/1 or yes/no flag, received {value!r}")


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(p * len(ordered)) - 1))
    return ordered[index]


def fmt(value: float | None) -> str:
    return "" if value is None else f"{value:.6f}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="evaluation/COMPARATIVE_RUN_MATRIX_v4.1.csv")
    parser.add_argument("--output", default="evaluation/COMPARATIVE_RESULTS_SUMMARY.csv")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"input file not found: {input_path}")

    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"case_id", "language", "condition", "score_0_2", "critical_error"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            parser.error("missing required columns: " + ", ".join(sorted(missing)))
        for row in reader:
            condition = (row.get("condition") or "").strip()
            language = (row.get("language") or "").strip()
            if not condition or not language:
                continue
            groups[(condition, language)].append(row)

    output_rows: list[dict[str, str]] = []
    for (condition, language), rows in sorted(groups.items()):
        scores = [x for row in rows if (x := parse_number(row.get("score_0_2"))) is not None]
        critical = [x for row in rows if (x := parse_flag(row.get("critical_error"))) is not None]
        result = {
            "condition": condition,
            "language": language,
            "run_slots": str(len(rows)),
            "scored_runs": str(len(scores)),
            "mean_score_0_2": fmt(statistics.mean(scores) if scores else None),
            "pass_rate_score_2": fmt(sum(s == 2 for s in scores) / len(scores) if scores else None),
            "critical_error_count": str(sum(critical)) if critical else "",
            "latency_median_seconds": "",
            "latency_p95_seconds": "",
            "total_cost_usd": "",
            "verification_coverage_weighted": "",
        }

        latencies = [x for row in rows if (x := parse_number(row.get("latency_seconds"))) is not None]
        costs = [x for row in rows if (x := parse_number(row.get("cost_usd"))) is not None]
        checked = [parse_number(row.get("verification_claims_checked")) for row in rows]
        totals = [parse_number(row.get("verification_claims_total")) for row in rows]
        result["latency_median_seconds"] = fmt(statistics.median(latencies) if latencies else None)
        result["latency_p95_seconds"] = fmt(percentile(latencies, 0.95))
        result["total_cost_usd"] = fmt(sum(costs) if costs else None)
        coverage_pairs = [(c, t) for c, t in zip(checked, totals) if c is not None and t is not None and t > 0]
        if coverage_pairs:
            result["verification_coverage_weighted"] = fmt(
                sum(c for c, _ in coverage_pairs) / sum(t for _, t in coverage_pairs)
            )

        for metric in METRICS:
            observed = [x for row in rows if (x := parse_flag(row.get(metric))) is not None]
            result[f"{metric}_numerator"] = str(sum(observed)) if observed else ""
            result[f"{metric}_denominator"] = str(len(observed)) if observed else ""
            result[f"{metric}_rate"] = fmt(sum(observed) / len(observed) if observed else None)
        output_rows.append(result)

    if not output_rows:
        parser.error("no run rows with both condition and language were found")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(output_rows[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote descriptive summary for {len(output_rows)} condition/language groups to {output_path}")
    print("No output was scored by this script. Blank cells remain not applicable/unscored, not zero.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
