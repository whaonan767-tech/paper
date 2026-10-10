## Software Quality Journal manuscript and public artifact

This release contains the corrected manuscript and its regenerated public
sanitized companion artifact.

### Included

- `manuscript/main.pdf` and the corresponding LaTeX source and bibliography
- `artifact/public-sanitized.zip`
- `artifact/public-sanitized-report.json`
- `artifact/SHA256SUMS`

### Changes

- Corrected manuscript citation commands and rebuilt the PDF.
- Increased the in-figure label size for improved readability.
- Regenerated the public artifact from the final manuscript and verified its
  file manifest and checksums.
- Excluded row-level annotation data, annotation workflow scripts, raw prompts,
  and raw model responses from the public artifact.

### Validation

- Manuscript: 42 pages; abstract: 192 words.
- Bibliography: 30 entries; no undefined citation/reference warnings.
- Public artifact: 40/40 core assertions and 40/40 new-experiment checks passed.
- Public artifact: 0 row-level data files, 0 raw-prompt files, 0 raw-response
  files, 0 credential findings, and 0 undeclared files.
- Public artifact SHA-256:
  `25194f53a66ad78f638fb29713884139d7398236e4f74612856eb764272f6ede`
- Manuscript PDF SHA-256:
  `3448d523242c34e7caa7fe582b8eee809cace9510f461e7f37d37a07e6788da6`

### Data restrictions

Row-level annotations, raw prompts and responses, row-level candidate lists,
compiler logs, third-party project trees, local model weights, package caches,
and credentials are not included in this public release.

The Zenodo DOI for the archived artifact is recorded in the manuscript's Data
Availability statement. If this GitHub repository is connected to Zenodo
automatic archiving, verify the DOI Zenodo assigns to this release before
publishing and ensure the manuscript cites the stable concept DOI where
appropriate.
