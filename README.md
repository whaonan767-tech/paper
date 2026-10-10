# Measuring Dependency Hallucination in Generated Code

This repository contains the manuscript source and the compiled PDF for the
study of dependency-hallucination measurement in generated code.

## Manuscript

The source is in `manuscript/main.tex`. Build it with XeLaTeX from the
`manuscript/` directory:

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

The current authors are Haonan Wang and Shiyong Xiong, with Xiong as
corresponding author. The affiliation is the School of Computer Science,
Chongqing University of Posts and Telecommunications, Chongqing 400065,
China. Corresponding-author email: xiongsy@cqupt.edu.cn.

## Data and artifact scope

The public release does not include raw prompts or responses, row-level
annotations or adjudication, registry-missing candidate lists, compiler logs,
third-party project trees, local model weights, or package-manager caches.
Annotator consent was obtained; no personal or sensitive information was
collected, and row-level annotations are not authorized for public release.

The public sanitized artifact will be added only after it is regenerated from
the final manuscript and validated. The older August 2026 archive is not
included because it predates this manuscript revision.

See `GITHUB_RELEASE_CHECKLIST.md` for the public/private boundary.
