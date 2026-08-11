from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "SKILL.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "references/reasoning-chain.md",
    "references/framework-comparison.md",
    "references/operator-archetypes.md",
    "references/career-to-founder-transition.md",
    "references/signal-lenses.md",
    "references/youth-campus-lens.md",
    "references/scorecards.md",
    "references/business-design.md",
    "references/output-template.md",
    "references/recommended-reading.md",
    "radar/README.md",
    "radar/2026-08.md",
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
        'version: "8.0.0"',
        "Public-Example Safety Rule",
        "Career-to-Founder Transition",
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

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Opportunity Radar validation passed.")
    print(f"Checked {len(REQUIRED_FILES)} required files and {len(REQUIRED_EXAMPLES)} synthetic examples.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
