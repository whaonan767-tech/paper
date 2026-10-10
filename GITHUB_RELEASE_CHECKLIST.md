# GitHub and SQJ release checklist

This file separates a public project release from the confidential artifact for
the journal editors. Do not upload the entire `D:\papers` workspace or the
confidential review ZIP to a public GitHub repository.

## Public GitHub repository

Create a clean repository containing only the following reviewed materials:

```text
README.md
LICENSE                         # choose only after confirming rights
manuscript/
  main.tex
  references.bib
  submission_metadata_sqj.tex   # identified author version; check email/address first
  sn-jnl.cls
  sn-basic.bst
  cuted.sty
  threeparttable.sty
  wrapfig.sty
  main.pdf                      # optional convenience copy; rebuild from source
artifact/
  public-sanitized.zip          # regenerate from the final manuscript/source
  SHA256SUMS
```

The main manuscript uses inline TikZ for its figures, so there are no separate
figure files at present. Include any external figure sources if that changes.
Keep the full review artifact out of GitHub; provide it only through the
journal's confidential editorial system. Do not upload raw prompts/responses,
row-level annotation or adjudication, registry-missing candidate lists,
compiler logs, third-party project trees, local model weights, package caches,
or personal credentials.

## Persistent archive and citation

GitHub is suitable for versioned source and releases, but cite a persistent
archive (for example, a Zenodo release connected to the GitHub repository) in
the paper's Data Availability statement. Archive the exact public sanitized
ZIP corresponding to the final manuscript and record both its DOI and the
GitHub release URL. Do not cite the August 2026 sanitized ZIP as the final
artifact: it predates the October manuscript and must be regenerated and
validated after the final source changes.

## Before making the repository public

- Verify the author names, corresponding-author email, department, affiliation,
  postal address, city, and country in `submission_metadata_sqj.tex`; add ORCID
  if available. The supplied details are recorded there, with institutional
  affiliation and mailing address formatted separately.
- Complete and fact-check ethics, author-contribution, the corresponding
  author's biography, and photograph requirements. The two annotators have
  confirmed informed consent, received no compensation, and do not authorize
  public release of row-level annotations. Never infer the institution's ethics
  determination or any additional consent scope. No personal or sensitive
  information was collected in the annotation activity, and the manuscript
  now records that ethics approval was not required.
- Rebuild `main.pdf` from `main.tex`, inspect all pages and figures/tables, and
  verify that no author-input placeholders remain in the submission copy.
- Rebuild and validate the public sanitized artifact from the final source;
  check its manifest and hashes, then create a new versioned archive release
  if the source or artifact differs from the DOI-linked release.
- Select an appropriate license for the manuscript, code, and aggregate data;
  check third-party notices and do not relicense material whose rights are not
  yours.
- Scan the public repository and archive for secrets, local paths, private
  annotations, project names/identifiers that should remain restricted, build
  logs, generated caches, and temporary review images.
- Use the anonymized/full review package only if requested by the editor and
  only via the journal's restricted submission channel.

## Current author facts and unresolved fields

The supplied author list is **Haonan Wang (王浩楠)** and corresponding author
**Shiyong Xiong (熊仕勇)**. The supplied affiliation and email are recorded in
`submission_metadata_sqj.tex`. Annotator consent, compensation, data-release
restriction, no-personal-data status, author contribution roles, and
biographies are recorded. Photographs if required remain pending. The current
archive concept DOI is https://doi.org/10.5281/zenodo.23273775. The supplied GitHub repository is
<https://github.com/whaonan767-tech/paper>.
