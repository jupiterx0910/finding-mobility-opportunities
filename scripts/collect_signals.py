#!/usr/bin/env python3
"""Collect public RSS/Atom/arXiv signals for Opportunity Radar.

This script collects leads only. It does not infer or publish business opportunities.
It uses Python's standard library so the scheduled workflow has no third-party dependencies.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "radar" / "sources.json"
OUTPUT_FILE = ROOT / "radar" / "signals.json"
REPORT_FILE = ROOT / "radar" / "collection-report.json"
MAX_SIGNALS = 1200
TIMEOUT_SECONDS = 20
USER_AGENT = "OpportunityRadarResearchBot/0.1 (+https://github.com/jupiterx0910/finding-mobility-opportunities; public feed reader)"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def clean_text(value: str | None, limit: int = 1200) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value[:limit]


def parse_date(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).replace(microsecond=0).isoformat()
    except ValueError:
        pass
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).replace(microsecond=0).isoformat()
    except (TypeError, ValueError, OverflowError):
        return None


def text_of(element: ET.Element, paths: list[str]) -> str:
    for path in paths:
        node = element.find(path)
        if node is not None:
            if node.text and node.text.strip():
                return node.text.strip()
            # Atom links commonly store href as an attribute.
            href = node.attrib.get("href")
            if href:
                return href.strip()
    return ""


def item_link(item: ET.Element, atom: bool) -> str:
    if atom:
        for link in item.findall("{http://www.w3.org/2005/Atom}link"):
            rel = link.attrib.get("rel", "alternate")
            href = link.attrib.get("href")
            if href and rel == "alternate":
                return href.strip()
        return text_of(item, ["{http://www.w3.org/2005/Atom}id"])
    return text_of(item, ["link", "{http://www.w3.org/2005/Atom}link"])


def parse_feed(payload: bytes, source: dict[str, Any]) -> list[dict[str, Any]]:
    root = ET.fromstring(payload)
    atom = root.tag.endswith("feed") or root.tag == "{http://www.w3.org/2005/Atom}feed"
    if source.get("type") == "arxiv_api":
        entries = root.findall("{http://www.w3.org/2005/Atom}entry")
    elif atom:
        entries = root.findall("{http://www.w3.org/2005/Atom}entry")
    else:
        channel = root.find("channel")
        entries = channel.findall("item") if channel is not None else root.findall(".//item")

    records = []
    for entry in entries:
        if atom:
            title = text_of(entry, ["{http://www.w3.org/2005/Atom}title"])
            link = item_link(entry, True)
            published = text_of(entry, [
                "{http://www.w3.org/2005/Atom}published",
                "{http://www.w3.org/2005/Atom}updated",
            ])
            summary = text_of(entry, [
                "{http://www.w3.org/2005/Atom}summary",
                "{http://www.w3.org/2005/Atom}content",
            ])
            authors = [
                clean_text(a.findtext("{http://www.w3.org/2005/Atom}name"), 160)
                for a in entry.findall("{http://www.w3.org/2005/Atom}author")
            ]
        else:
            title = text_of(entry, ["title"])
            link = item_link(entry, False)
            published = text_of(entry, ["pubDate", "published", "updated", "date"])
            summary = text_of(entry, ["description", "summary", "{http://purl.org/rss/1.0/modules/content/}encoded"])
            authors = []
        title = clean_text(title, 400)
        link = link.strip()
        if not title or not link or urlparse(link).scheme not in ("http", "https"):
            continue
        source_id = source["id"]
        key = hashlib.sha256((source_id + "|" + link).encode("utf-8")).hexdigest()[:20]
        records.append({
            "id": key,
            "source_id": source_id,
            "source_name": source["name"],
            "source_type": source.get("type", "rss"),
            "source_url": source["url"],
            "url": link,
            "title": title,
            "summary": clean_text(summary, 1800),
            "published_at": parse_date(published),
            "collected_at": utc_now(),
            "region": source.get("region", "unspecified"),
            "topic_tags": source.get("topic_tags", []),
            "reliability_tier": source.get("reliability_tier", "unclassified"),
            "evidence_class": "lead_unverified",
            "verification_status": "not_reviewed",
        })
    return records


def fetch_source(source: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    started = time.monotonic()
    result: dict[str, Any] = {
        "source_id": source["id"],
        "source_name": source["name"],
        "status": "failed",
        "items_seen": 0,
        "items_new": 0,
        "duration_ms": 0,
    }
    request = urllib.request.Request(
        source["url"],
        headers={"User-Agent": USER_AGENT, "Accept": "application/atom+xml, application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.5"},
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            payload = response.read(4_000_000)
            status = getattr(response, "status", 200)
            if status != 200:
                raise RuntimeError(f"HTTP status {status}")
        records = parse_feed(payload, source)
        result.update(status="success", items_seen=len(records))
        return records, result
    except (urllib.error.URLError, TimeoutError, OSError, ET.ParseError, RuntimeError, ValueError) as exc:
        result["error"] = clean_text(str(exc), 500)
        return [], result
    finally:
        result["duration_ms"] = round((time.monotonic() - started) * 1000)


def load_json(path: Path, fallback: Any) -> Any:
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def main() -> int:
    started_at = utc_now()
    config = load_json(SOURCE_FILE, {"sources": []})
    old_data = load_json(OUTPUT_FILE, {"schema_version": "1.0", "signals": []})
    old_signals = old_data.get("signals", []) if isinstance(old_data, dict) else []
    by_id = {item.get("id"): item for item in old_signals if isinstance(item, dict) and item.get("id")}
    run_results = []
    enabled_sources = [s for s in config.get("sources", []) if s.get("enabled", True)]

    for source in enabled_sources:
        records, report = fetch_source(source)
        new_count = 0
        for record in records:
            if record["id"] not in by_id:
                by_id[record["id"]] = record
                new_count += 1
        report["items_new"] = new_count
        run_results.append(report)
        # Keep the collector polite when several feeds are configured.
        time.sleep(0.4)

    signals = sorted(
        by_id.values(),
        key=lambda item: (item.get("published_at") or item.get("collected_at") or ""),
        reverse=True,
    )[:MAX_SIGNALS]
    finished_at = utc_now()
    OUTPUT_FILE.write_text(
        json.dumps({
            "schema_version": "1.0",
            "as_of": finished_at,
            "purpose": "Collected public signals for later research. These are unverified leads, not validated opportunities.",
            "signal_count": len(signals),
            "signals": signals,
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    success_count = sum(1 for result in run_results if result["status"] == "success")
    REPORT_FILE.write_text(
        json.dumps({
            "schema_version": "1.0",
            "started_at": started_at,
            "finished_at": finished_at,
            "sources_configured": len(enabled_sources),
            "sources_succeeded": success_count,
            "sources_failed": len(enabled_sources) - success_count,
            "items_new_this_run": sum(r["items_new"] for r in run_results),
            "items_retained": len(signals),
            "results": run_results,
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Signal collection complete: {success_count}/{len(enabled_sources)} sources succeeded; {sum(r['items_new'] for r in run_results)} new leads; {len(signals)} retained.")
    for result in run_results:
        state = result["status"].upper()
        detail = result.get("error", f"{result['items_seen']} seen, {result['items_new']} new")
        print(f"- {result['source_id']}: {state} — {detail}")
    # A feed outage should not erase existing data or prevent diagnostics being committed.
    # Fail only if every configured source fails, so the workflow visibly flags a total outage.
    if enabled_sources and success_count == 0:
        print("ERROR: all sources failed; preserving existing signals and marking run unsuccessful.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
