from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "SKILL.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/career-to-founder-map-2026.md",
    "references/reasoning-chain.md",
    "references/framework-comparison.md",
    "references/operator-archetypes.md",
    "references/career-to-founder-transition.md",
    "references/signal-lenses.md",
    "references/youth-campus-lens.md",
    "references/scorecards.md",
    "references/evidence-confidence.md",
    "references/window-and-why-not-yet.md",
    "references/business-design.md",
    "references/output-template.md",
    "references/recommended-reading.md",
    "radar/README.md",
    "radar/2026-08.md",
    "radar/decision-ledger.md",
    "radar/opportunities.json",
]

REQUIRED_EXAMPLES = [
    "examples/b2b-sales-to-distribution.md",
    "examples/cross-border-operator.md",
    "examples/industrial-technician-to-business.md",
    "examples/procurement-supply-chain-to-business.md",
    "examples/domain-operator-plus-ai.md",
    "examples/growth-operator-to-owned-business.md",
]

SYNTHETIC_MARKER = "Fictional operator archetype. Not based on any real user or private conversation."


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES + REQUIRED_EXAMPLES:
        if not (ROOT / path).is_file():
            errors.append(f"missing required file: {path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    skill = read("SKILL.md")
    if not skill.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    for token in [
        "name: finding-mobility-opportunities",
        'version: "8.1.0"',
        "Public-Example Safety Rule",
        "Career-to-Founder Transition",
        "Evidence Coverage",
        "Why-Not-Yet",
        "START / BUY A REAL OPTION / WATCH / REJECT",
    ]:
        if token not in skill:
            errors.append(f"SKILL.md missing required token: {token}")

    for path in REQUIRED_EXAMPLES:
        content = read(path)
        if SYNTHETIC_MARKER not in content:
            errors.append(f"public example missing synthetic marker: {path}")

    readme = read("README.md")
    for token in [
        "Human Capital → Cash Flow → Owned Capital",
        "Career-to-Founder Transition Lens",
        "Public Example Policy",
        "Score ≠ Confidence",
        "Opportunity Decision Ledger",
        "Synthetic public examples only",
    ]:
        if token not in readme:
            errors.append(f"README.md missing required token: {token}")

    transition = read("references/career-to-founder-transition.md")
    for token in [
        "Payer Proximity",
        "Transaction Frequency",
        "Tacit Knowledge",
        "Portability",
        "Assetization Potential",
    ]:
        if token not in transition:
            errors.append(f"career-to-founder lens missing section: {token}")

    confidence = read("references/evidence-confidence.md")
    for token in [
        "Opportunity Score",
        "Evidence Coverage",
        "Evidence Quality",
        "Confidence",
        "Key Unknown",
    ]:
        if token not in confidence:
            errors.append(f"evidence-confidence missing token: {token}")

    window = read("references/window-and-why-not-yet.md")
    for token in [
        "Why-Not-Yet Test",
        "Opening",
        "Crowding",
        "Consolidating",
        "Opportunity Half-Life",
    ]:
        if token not in window:
            errors.append(f"window logic missing token: {token}")

    ledger = read("radar/decision-ledger.md")
    for token in ["OPEN", "UPGRADED", "DOWNGRADED", "KILLED"]:
        if token not in ledger:
            errors.append(f"decision ledger missing status: {token}")

    try:
        dataset = json.loads(read("radar/opportunities.json"))
        opportunities = dataset.get("opportunities", [])
        if len(opportunities) < 1:
            errors.append("radar/opportunities.json must contain at least one opportunity")
        ids = [item.get("id") for item in opportunities]
        if None in ids or len(ids) != len(set(ids)):
            errors.append("opportunity IDs must be present and unique")
        for item in opportunities:
            for key in ["first_seen", "stage", "current_verdict", "status", "confidence"]:
                if key not in item:
                    errors.append(f"opportunity {item.get('id')} missing key: {key}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid radar/opportunities.json: {exc}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Opportunity Radar validation passed.")
    print(f"Checked {len(REQUIRED_FILES)} required files and {len(REQUIRED_EXAMPLES)} synthetic examples.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
