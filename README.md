# Software Quality Journal Manuscript and Public Artifact

This repository contains the submission source and the public companion
artifact for the manuscript prepared for *Software Quality Journal*.

## Contents

- `manuscript/`: Springer manuscript source, bibliography, class/style files,
  metadata, and the compiled PDF.
- `artifact/public-sanitized.zip`: reproducibility package generated from the
  current manuscript and validated without row-level annotation data.
- `artifact/public-sanitized-report.json`: validation summary for the package.
- `GITHUB_RELEASE_CHECKLIST.md`: repository, archive, and submission checklist.
- `LICENSE`: repository licensing terms.

The public artifact excludes raw prompts and responses, row-level experiment
data, human annotation rows, candidate lists, compiler logs, third-party
project trees, local model weights, package caches, and credentials. The
annotation data are not publicly released.

## Build the manuscript

From `manuscript/`, compile with XeLaTeX and the included bibliography and
style files. The checked-in `main.pdf` is a convenience copy corresponding to
the checked-in source.

## Authors

- Haonan Wang, first author
- Shiyong Xiong, corresponding author: `xiongsy@cqupt.edu.cn`

The public artifact is archived at Zenodo:
https://doi.org/10.5281/zenodo.23237776

Later manuscript or artifact changes should be published as a new versioned
GitHub and Zenodo release rather than replacing the existing archive record.
