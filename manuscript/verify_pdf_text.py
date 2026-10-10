#!/usr/bin/env python3
"""Report submission-critical text-layer properties of the manuscript PDF."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", nargs="?", type=Path, default=Path("main.pdf"))
    parser.add_argument("--expected-pages", type=int, default=36)
    parser.add_argument("--max-abstract-words", type=int, default=210)
    args = parser.parse_args()

    reader = PdfReader(args.pdf)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    abstract = text.split("Abstract", 1)[1].split("Keywords:", 1)[0]
    words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", abstract)
    root = reader.trailer["/Root"]
    mark_info = root.get("/MarkInfo", {})
    marked = bool(mark_info.get("/Marked", False))
    has_structure_tree = bool(root.get("/StructTreeRoot"))
    metadata = reader.metadata or {}

    print(f"pages={len(reader.pages)}")
    print(f"abstract_words={len(words)}")
    print(f"u037e={text.count(chr(0x037E))}")
    print(f"ascii_semicolon={text.count(';')}")
    print(f"marked_content={str(marked).lower()}")
    print(f"structure_tree={str(has_structure_tree).lower()}")
    print(f"tagged_pdf={str(marked and has_structure_tree).lower()}")
    print(f"pdf_title={metadata.get('/Title', '')}")
    print(f"pdf_author={metadata.get('/Author', '')}")

    failures = []
    if len(reader.pages) != args.expected_pages:
        failures.append(f"pages={len(reader.pages)} expected={args.expected_pages}")
    if len(words) > args.max_abstract_words:
        failures.append(f"abstract_words={len(words)} maximum={args.max_abstract_words}")
    if text.count(chr(0x037E)) != 0:
        failures.append("u037e must be zero")
    if text.count(";") == 0:
        failures.append("ASCII semicolon count must be nonzero")
    if failures:
        raise SystemExit("PDF CHECK FAILED: " + "; ".join(failures))
    print("status=pass")


if __name__ == "__main__":
    main()
