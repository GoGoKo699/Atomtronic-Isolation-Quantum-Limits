"""Audit internal navigation and the shared learning map; not a proof checker."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def without_fences(text: str) -> str:
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is None:
            lines.append(line)
    if fence is not None:
        raise ValueError("unclosed Markdown fence")
    return "\n".join(lines)


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', text))
    counts: dict[str, int] = {}
    for line in without_fences(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"<[^>]*>", "", match.group(1)).lower()
        title = re.sub(r"[*`~]", "", title)
        slug = re.sub(r"[^\w\s-]", "", title).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


def audit() -> dict:
    errors: list[str] = []
    documents = sorted(ROOT.rglob("*.md")) + [ROOT / "llms.txt"]
    link_count = 0
    texts: dict[Path, str] = {}
    for path in documents:
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        texts[path] = text
        try:
            without_fences(text)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
        if text.count("$`") != text.count("`$"):
            errors.append(f"{path.relative_to(ROOT)}: unbalanced inline math delimiters")

    for path, text in texts.items():
        try:
            plain = without_fences(text)
        except ValueError:
            continue
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", plain):
            raw = match.group(1).strip()
            if raw.startswith("<") and raw.endswith(">"):
                raw = raw[1:-1]
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            link_count += 1
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing or external local target {raw}")
                continue
            if parsed.fragment and target.suffix == ".md":
                try:
                    target_text = target.read_text(encoding="utf-8")
                    if unquote(parsed.fragment) not in anchors(target_text):
                        errors.append(f"{path.relative_to(ROOT)}: missing heading {raw}")
                except ValueError as exc:
                    errors.append(f"{target.relative_to(ROOT)}: {exc}")

    milestone_path = ROOT / "learning/MILESTONES.md"
    text = milestone_path.read_text(encoding="utf-8")
    records = list(re.finditer(r"(?m)^### M(\d{2}) — (.+)$", text))
    ids = [int(record.group(1)) for record in records]
    if ids != list(range(1, 31)):
        errors.append("Milestones must be exactly M01 through M30 in order")
    fields = ("Phase", "Central question", "Understanding target", "Dependencies",
              "Story role", "Conceptual connection", "Sources")
    questions: set[str] = set()
    targets: set[str] = set()
    dependency_edges = 0
    phase_counts = {"background": 0, "narrative": 0}
    for index, record in enumerate(records):
        number = int(record.group(1))
        end = records[index + 1].start() if index + 1 < len(records) else len(text)
        body = text[record.end():end]
        values: dict[str, str] = {}
        for field in fields:
            found = re.search(r"\*\*" + re.escape(field) + r":\*\*\s*(.+?)(?=\n\s*\n|\Z)", body, re.S)
            if found is None or not found.group(1).strip():
                errors.append(f"M{number:02d}: missing {field}")
            else:
                values[field] = found.group(1).strip()
        expected_phase = "Background and preliminaries." if number <= 13 else "Narrative and innovation."
        if values.get("Phase") != expected_phase:
            errors.append(f"M{number:02d}: wrong phase")
        else:
            phase_counts["background" if number <= 13 else "narrative"] += 1
        for field, seen in (("Central question", questions), ("Understanding target", targets)):
            value = values.get(field, "")
            if value and value in seen:
                errors.append(f"M{number:02d}: repeated {field}")
            seen.add(value)
        deps = [int(item) for item in re.findall(r"\bM(\d{2})\b", values.get("Dependencies", ""))]
        dependency_edges += len(deps)
        if any(dep < 1 or dep >= number for dep in deps) or len(deps) != len(set(deps)):
            errors.append(f"M{number:02d}: dependency must refer once to an earlier milestone")
        if number > 1 and not deps:
            errors.append(f"M{number:02d}: missing prerequisite dependencies")
        if "Review " not in values.get("Sources", "") or "../science/" not in values.get("Sources", ""):
            # M02 is a convention conversion developed completely in the bridge.
            if number != 2:
                errors.append(f"M{number:02d}: missing precise anchor/project sources")

    for name in ("README.md", "llms.txt"):
        text = (ROOT / name).read_text(encoding="utf-8")
        for target in ("learning/MILESTONES.md", "learning/WEEDBROOK_BRIDGE.md"):
            if target not in text:
                errors.append(f"{name}: missing learning navigation to {target}")
    bridge = (ROOT / "learning/WEEDBROOK_BRIDGE.md").read_text(encoding="utf-8")
    if "1110.3234v1" not in bridge or "Single educational anchor" not in bridge:
        errors.append("Bridge must identify its single anchor and source version")
    if list(ROOT.rglob("COACHING.md")):
        errors.append("Personal coaching contracts do not belong in the research repository")

    reverse = Fraction(1, 100)
    gain = Fraction(1)
    noise = Fraction(9, 5)
    c = noise - gain
    threshold = c / (c + reverse)
    det98 = (1 - Fraction(98, 100)) * c - Fraction(98, 100) * reverse
    det99 = (1 - Fraction(99, 100)) * c - Fraction(99, 100) * reverse
    if (threshold, det98, det99) != (Fraction(80, 81), Fraction(31, 5000), Fraction(-19, 10000)):
        errors.append("Worked-example exact arithmetic failed")
    return {
        "status": "FAIL" if errors else "PASS",
        "documents": len(texts), "internal_links": link_count,
        "milestones": len(records), "phase_counts": phase_counts,
        "dependency_edges": dependency_edges,
        "worked_example": {"eta_critical": str(threshold), "det_at_098": str(det98), "det_at_099": str(det99)},
        "manual_scientific_and_visual_review_required": True,
        "errors": errors,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit()
    report = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    print(report, end="")
    if result["errors"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
