#!/usr/bin/env python3
"""Merge one locally collected signal snapshot with the latest checked-out main snapshot."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path, fallback: dict) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def parse_time(value: str | None) -> float:
    if not value:
        return 0.0
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()
    except (ValueError, TypeError):
        return 0.0


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: merge_signal_snapshots.py LOCAL_SIGNALS_JSON LOCAL_REPORT_JSON", file=sys.stderr)
        return 2
    local_signals = read_json(Path(sys.argv[1]), {"signals": []})
    local_report = read_json(Path(sys.argv[2]), {})
    current_signals_path = ROOT / "radar" / "signals.json"
    current_report_path = ROOT / "radar" / "collection-report.json"
    current_signals = read_json(current_signals_path, {"schema_version": "1.0", "signals": []})
    current_report = read_json(current_report_path, {})

    merged: dict[str, dict] = {}
    for item in current_signals.get("signals", []) + local_signals.get("signals", []):
        if not isinstance(item, dict) or not item.get("id"):
            continue
        old = merged.get(item["id"])
        if old is None or parse_time(item.get("collected_at")) >= parse_time(old.get("collected_at")):
            merged[item["id"]] = item

    signals = sorted(
        merged.values(),
        key=lambda item: (item.get("published_at") or item.get("collected_at") or ""),
        reverse=True,
    )[:1200]
    as_of = max(
        [v for v in (current_signals.get("as_of"), local_signals.get("as_of")) if v],
        key=parse_time,
        default=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    )
    current_signals_path.write_text(
        json.dumps({
            "schema_version": "1.0",
            "as_of": as_of,
            "purpose": "Collected public signals for later research. These are unverified leads, not validated opportunities.",
            "signal_count": len(signals),
            "signals": signals,
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Preserve the report belonging to the newest completed collection run.
    report_to_keep = local_report if parse_time(local_report.get("finished_at")) >= parse_time(current_report.get("finished_at")) else current_report
    current_report_path.write_text(
        json.dumps(report_to_keep, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Merged signal snapshots: {len(signals)} unique signals; report finished_at={report_to_keep.get('finished_at', 'unknown')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
