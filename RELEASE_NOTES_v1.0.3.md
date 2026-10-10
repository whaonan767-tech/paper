## Software Quality Journal manuscript and public artifact

This release synchronizes the manuscript and public artifact with the stable
Zenodo concept DOI, which resolves to the latest archived version.

### Included

- `manuscript/main.pdf` and the corresponding LaTeX source and bibliography
- `artifact/public-sanitized.zip`
- `artifact/public-sanitized-report.json`
- `artifact/SHA256SUMS`

### Changes

- Updated the manuscript and repository README to cite the stable Zenodo
  concept DOI: <https://doi.org/10.5281/zenodo.23273775>.
- Rebuilt the PDF and regenerated the public sanitized artifact and checksums.
- Retained the corrected citations, readable in-figure labels, and disclosure
  restrictions from v1.0.2.

### Validation

- Manuscript: 42 pages; abstract: 192 words.
- Bibliography: 30 entries; no undefined citation/reference warnings.
- Public artifact validation: 40/40 core assertions and 40/40 new-experiment
  checks passed.
- Public artifact excludes row-level annotation data, annotation workflow
  scripts, raw prompts, and raw model responses.
- Public artifact SHA-256: `5887e79d8b3c68c93047ee05aef0fa9d919af890f8967336ba1e2ff4c384fd7e`
- Manuscript PDF SHA-256: `8c26318b2a9011b23ce000e2ff7bff157b13e059caa3eeca2c3030cf03efa4ec`
- Full file hashes are listed in `artifact/SHA256SUMS` and the repository's
  `SHA256SUMS`.

### Data restrictions

Row-level annotations, raw prompts and responses, row-level candidate lists,
compiler logs, third-party project trees, local model weights, package caches,
and credentials are not included in this public release.


