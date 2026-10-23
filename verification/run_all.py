"""Run each scientific check in a fresh process and collect its JSON output."""
import argparse
import json
from pathlib import Path
import platform
import subprocess
import sys
import numpy
import scipy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON results path")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    report = {"python": platform.python_version(), "numpy": numpy.__version__,
              "scipy": scipy.__version__, "checks": {}}
    for script in sorted(here.glob("check_*.py")):
        result = subprocess.run([sys.executable, str(script)], cwd=here.parent,
                                capture_output=True, text=True, timeout=60)
        if result.returncode:
            print(result.stdout, end="")
            print(result.stderr, file=sys.stderr, end="")
            raise SystemExit(f"FAILED: {script.name} ({result.returncode})")
        try:
            report["checks"][script.name] = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Non-JSON output from {script.name}: {exc}")
        print(f"PASS {script.name}")
    report["status"] = "PASS"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
        print(f"Saved {args.output}")
    print(f"PASS: {len(report['checks'])} scientific check programs")


if __name__ == "__main__":
    main()
