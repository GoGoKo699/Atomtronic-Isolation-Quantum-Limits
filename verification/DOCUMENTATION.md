# Checking the reading routes and hosted mathematics

The [scientific suite](README.md) and the documentation checks establish different things. Passing a link checker does not establish correct mathematical rendering. Passing numerical checks does not establish a general proof or priority over all literature.

## Source and learning-map audit

From the repository root:

```bash
python verification/audit_documentation.py --output /tmp/atomtronic-documentation.json
```

The standard-library checker validates internal file links and Markdown heading fragments, balanced fences, the contiguous M01–M30 identifiers, the 13/17 phase allocation, complete nonempty milestone fields, distinct questions and targets, and backward-only dependencies. It requires navigation from both README and llms.txt to the selected bridge and milestone map. It also checks the exact rational worked-example values independently of their decimal display.

These checks do not decide whether an explanation is educationally sufficient or a proof is correct. The targets must also be read against the canonical science. The single educational anchor is Weedbrook et al.; primary research citations remain separate proof dependencies.

## Inspect the actual GitHub renderer

For a committed public revision of this repository, install the browser dependency and capture the hosted pages:

```bash
python -m pip install playwright==1.57.0
python -m playwright install chromium
python verification/capture_hosted_math.py --revision <40-character-commit-sha> --output /tmp/atomtronic-render
```

The script opens only pinned pages of this repository. It saves the README, learning overview, bridge, milestone map and all seven scientific pages as actual browser screenshots. It records HTTP status, page headings, renderer counts, GitHub macro-rejection messages, visible alerts and math-error markers, with additional close-ups of representative equations. Network failures and missing Markdown previews are failures, not successful rendering checks. Full-page captures are taken before formula close-ups to avoid hiding the first heading beneath GitHub's sticky file header.

A reviewer must inspect the captures for incorrect symbols, visible source syntax, table collisions, missing figure content and clipping. Math-error-marker detection alone is not sufficient: GitHub's macro-rejection notices need not use a KaTeX or MathJax error class. The browser script neither signs in nor changes GitHub state. Static offline rendering is not substituted for GitHub's own output.

This repository uses roman text for named operators where the inspected GitHub renderer rejects the operator-name macro. This is a presentation convention for this host, not a restriction on the mathematical operator or a universal TeX rule.

## Continuous verification and provenance

The [verification workflow](../.github/workflows/verify.yml) runs on pull requests and main updates with read-only repository permissions. It checks the exact PR head or main commit, installs the scientific pins on Python 3.12, runs all five scientific programs, reproduces the figure byte-for-byte, performs the documentation audit, and captures hosted mathematics. Results are saved as a workflow artifact containing:

- `revision.txt` and `source.zip`: the exact public checked source;
- `results.json` and `documentation.json`: newly executed checks;
- `render/`: pinned-page screenshots and their capture metadata.

Artifacts are retained for 30 days; the source and reproduction commands remain in Git. The committed `results.json` is the original scientific baseline, not a fresh-run claim. A later workflow's outcome must be read from that run rather than inferred from an earlier success.

A successful capture or workflow is evidence about the inspected revision. It is not an independent peer review, an experiment, or a guarantee about future edits. The visible review of the captures and any remaining limitation should accompany a completion statement.
