"""Capture the real GitHub Markdown renderer at one pinned public revision.

Screenshots require a visual review; renderer counts are not a correctness proof.
This script is read-only and opens only this repository's selected pages.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

from playwright.sync_api import sync_playwright

REPOSITORY = "GoGoKo699/Atomtronic-Isolation-Quantum-Limits"
PAGES = (
    "README.md",
    "learning/README.md",
    "learning/WEEDBROOK_BRIDGE.md",
    "learning/MILESTONES.md",
    "science/model.md",
    "science/collection_boundary.md",
    "science/communication_rates.md",
    "science/scattering_noise.md",
    "science/stable_atomic_model.md",
    "science/finite_bandwidth.md",
    "science/interpretation.md",
)
ERROR_TEXT = (
    "the following macros are not allowed",
    "unable to render rich display",
    "math rendering error",
    "parseerror:",
    "undefined control sequence",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.revision):
        parser.error("revision must be a full lowercase 40-character commit SHA")
    args.output.mkdir(parents=True, exist_ok=True)
    report = {
        "repository": REPOSITORY, "revision": args.revision,
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "manual_visual_review_required": True, "pages": [],
    }
    failures = 0
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1100},
                                      device_scale_factor=1, color_scheme="light",
                                      reduced_motion="reduce")
        for index, path in enumerate(PAGES):
            page = context.new_page()
            page.set_default_timeout(45000)
            name = f"{index:02d}-" + path.replace("/", "-").removesuffix(".md")
            url = f"https://github.com/{REPOSITORY}/blob/{args.revision}/{path}"
            item = {"path": path, "url": url, "status": "FAILED"}
            try:
                response = page.goto(url, wait_until="domcontentloaded", timeout=60000)
                item["http_status"] = response.status if response else None
                if response is None or response.status != 200:
                    raise RuntimeError(f"GitHub returned HTTP {item['http_status']}")
                body = page.locator(".markdown-body").first
                body.wait_for(state="visible")
                height = page.evaluate("document.documentElement.scrollHeight")
                # Trigger lazy formula and image rendering throughout long pages.
                for y in range(0, min(int(height), 100000), 900):
                    page.evaluate("y => window.scrollTo(0, y)", y)
                    page.wait_for_timeout(80)
                page.wait_for_function("document.fonts.status === 'loaded'", timeout=15000)
                page.wait_for_timeout(1000)
                # Reset both document and nested scroll containers. Capture the
                # full page before locator screenshots can scroll its first
                # heading behind GitHub's sticky file header.
                page.evaluate("""() => {
                    for (const element of document.querySelectorAll('*')) {
                        if (element.scrollTop) element.scrollTop = 0;
                        if (element.scrollLeft) element.scrollLeft = 0;
                    }
                    window.scrollTo(0, 0);
                }""")
                page.wait_for_timeout(250)
                item["heading"] = body.locator("h1").first.inner_text()
                item["math_renderer_count"] = body.locator("math-renderer").count()
                item["katex_count"] = body.locator(".katex").count()
                item["mathml_count"] = body.locator("math").count()
                markers = body.locator(".katex-error, mjx-merror, [data-mjx-error]")
                item["math_error_markers"] = markers.all_text_contents()
                text = body.inner_text().lower()
                item["github_error_messages"] = [message for message in ERROR_TEXT if message in text]
                # GitHub's macro-rejection component is not a KaTeX/mjx error;
                # inspect visible alert text as well as renderer-specific nodes.
                item["visible_alerts"] = [alert.inner_text() for alert in body.locator("[role=alert]").all() if alert.is_visible()]
                item["screenshot"] = name + ".png"
                page.screenshot(path=str(args.output / item["screenshot"]), full_page=True, animations="disabled")
                page.screenshot(path=str(args.output / (name + "-page-top.png")), animations="disabled")
                formulas = body.locator("math-renderer")
                count = formulas.count()
                samples = []
                for number in sorted({0, count // 2, count - 1}) if count else []:
                    filename = f"{name}-math-{number:03d}.png"
                    try:
                        formulas.nth(number).screenshot(path=str(args.output / filename), animations="disabled", timeout=10000)
                        samples.append(filename)
                    except Exception as exc:
                        samples.append({"index": number, "capture_error": str(exc)})
                item["formula_samples"] = samples
                if item["math_error_markers"] or item["github_error_messages"] or item["visible_alerts"]:
                    raise RuntimeError("GitHub-rendered Markdown contains an error or alert")
                item["status"] = "CAPTURED"
                print(f"CAPTURED {path}: {count} math containers", flush=True)
            except Exception as exc:
                failures += 1
                item["error"] = str(exc)
                try:
                    page.screenshot(path=str(args.output / (name + "-failure.png")))
                except Exception:
                    pass
                print(f"FAILED {path}: {exc}", file=sys.stderr, flush=True)
            finally:
                report["pages"].append(item)
                page.close()
        context.close()
        browser.close()
    report["status"] = "FAILED" if failures else "CAPTURED"
    (args.output / "capture.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
