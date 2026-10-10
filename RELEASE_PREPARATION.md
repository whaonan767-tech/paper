# Preparing the next GitHub Release

Suggested tag and release title: `v1.0.3`.

## Before creating the Release

1. Commit and push the reviewed contents of this folder to the repository's
   default branch. Do not upload anything from the wider `D:\papers` folder.
2. The manuscript and README cite the stable Zenodo concept DOI
   `10.5281/zenodo.23273775`, which represents all versions. The current v1.0.2
   version-specific DOI is `10.5281/zenodo.23278694`.
3. If the GitHub repository is connected to Zenodo auto-archiving, a new GitHub
   release will create another version-specific DOI. That is expected; keep the
   stable concept DOI in the manuscript so it does not need to change again.
4. Confirm the repository commit contains the final PDF, source, sanitized ZIP,
   report, and checksums. The public sanitized artifact must remain separate
   from any confidential review package.

## Create the GitHub Release

- Choose the just-pushed commit on the default branch.
- Create tag `v1.0.3` and title the Release `v1.0.3 - SQJ manuscript and
  sanitized artifact`.
- Paste the contents of `RELEASE_NOTES_v1.0.3.md` into the description.
- Attach these assets:
  - `artifact/public-sanitized.zip`
  - `artifact/public-sanitized-report.json`
  - `artifact/SHA256SUMS`
  - optionally `manuscript/main.pdf` as a convenient direct-download copy
- Keep the Release public only if the repository and all listed materials are
  intended to be public. Never attach raw annotations or the confidential
  review ZIP.
- If Zenodo auto-archiving is enabled, wait until Zenodo finishes processing,
  then verify the DOI landing page and the archived files. Update citations only
  if needed; do not delete the previous Zenodo version.

## Checks after publishing

- Open the GitHub Release page and confirm the tag, description, and assets.
- Download `public-sanitized.zip` and verify it against the attached
  `SHA256SUMS` entry.
- Open the Zenodo record, if created, and confirm it contains the same
  `public-sanitized.zip` and report.
- Record the Release URL and the appropriate Zenodo DOI for the manuscript and
  project README.
