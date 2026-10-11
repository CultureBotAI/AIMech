#!/usr/bin/env python3
"""Extract a local PDF with stable page locators and optional page renders.

Requires PyMuPDF in the selected environment. This is a reading aid, not OCR,
table reconstruction or scientific interpretation. It never edits the source.
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def selected_pages(specification, count):
    pages = set()
    if not specification:
        return pages
    for segment in specification.split(","):
        bounds = segment.strip().split("-")
        if len(bounds) not in {1, 2}:
            raise ValueError("render pages must be numbers or inclusive ranges, e.g. 1,3-5")
        start = int(bounds[0])
        end = int(bounds[-1])
        if not 1 <= start <= end <= count:
            raise ValueError(f"render range outside PDF pages 1–{count}: {segment}")
        pages.update(range(start, end + 1))
    return pages


def extract(source, destination, source_url=None, render_pages="", dpi=144):
    import pymupdf

    raw = source.read_bytes()
    with pymupdf.open(stream=raw, filetype="pdf") as document:
        if document.needs_pass:
            raise ValueError("encrypted PDF requires an accessible authorized copy")
        if not document.page_count:
            raise ValueError("PDF has no pages")
        renders = selected_pages(render_pages, document.page_count)
        if not 36 <= dpi <= 300:
            raise ValueError("render DPI must be between 36 and 300")
        # Validate input before creating anything, and never replace an earlier extraction.
        destination.mkdir(parents=True, exist_ok=False)
        manifest = {
            "source_file": str(source.resolve()),
            "source_url": source_url,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "extracted_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "engine": "PyMuPDF", "engine_version": pymupdf.__version__,
            "page_count": document.page_count, "pdf_metadata": document.metadata,
            "pages": [],
            "warnings": ["Reading order, equations and tables require document/visual inspection."],
            "visual_inspection": "not_performed_by_extractor",
        }
        output = ["# PDF text extraction", "",
                  "Reading aid only. Check layout, equations and tables against the PDF.", ""]
        for index, page in enumerate(document, start=1):
            text = page.get_text("text", sort=True)
            page_data = {"pdf_page": index, "printed_label": page.get_label(),
                         "text_characters": len(text.strip())}
            if len(text.strip()) < 80:
                manifest["warnings"].append(
                    f"PDF page {index}: little extractable text; inspect render for scans/figures."
                )
            if "\ufffd" in text:
                manifest["warnings"].append(f"PDF page {index}: replacement glyphs in extraction.")
            output.extend([f"## PDF page {index}", "", text.rstrip(), ""])
            if index in renders:
                filename = f"page-{index:04d}.png"
                page.get_pixmap(dpi=dpi, alpha=False).save(destination / filename)
                page_data["render"] = filename
            manifest["pages"].append(page_data)
        (destination / "paper.md").write_text("\n".join(output), encoding="utf-8")
        manifest["extraction_status"] = "complete"
        (destination / "manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--source-url")
    parser.add_argument("--render-pages", default="")
    parser.add_argument("--dpi", type=int, default=144)
    args = parser.parse_args()
    try:
        manifest = extract(args.pdf, args.output, args.source_url, args.render_pages, args.dpi)
    except ImportError:
        print("ERROR: use a Python environment with PyMuPDF installed.", file=sys.stderr)
        return 1
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"output": str(args.output), "pages": manifest["page_count"],
                      "warnings": manifest["warnings"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
