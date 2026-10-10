# AIO reference downloads

- [aio-full.owl](aio-full.owl): AIO release `2026-07-22`, in RDF/XML, with 442
  named AIO classes. BioPortal advertises the same version IRI. Direct BioPortal
  access returned HTTP 403 and its API required authentication, so this file was
  downloaded unchanged from the authoritative upstream Git revision
  `397851c547d1c4d8f06ef184f63c1d40bc86937a`. A BioPortal download checksum was
  unavailable; byte identity with its hosted copy has not been verified.
- [aio-applied-ontology.pdf](aio-applied-ontology.pdf): Complete 11-page journal
  article, copied unchanged from the PDF supplied by the user.
- [aio-applied-ontology.md](aio-applied-ontology.md): Markdown conversion of the
  **published Applied Ontology article**, DOI
  [10.1177/15705838241304103](https://doi.org/10.1177/15705838241304103), including
  the full article text, both tables, both original figures and their captions,
  and references. Figure images in `aio-applied-ontology-assets/` were extracted
  directly from the supplied PDF at their original resolution.
- [reference-sources.json](reference-sources.json): Exact source URLs, retrieval
  timestamps, checksums, licenses, and access/conversion limitations.

The user supplied the published journal PDF after website anti-bot challenges
prevented automated downloads. Its text was compared with the earlier web
extraction across all 11 pages. The only text-extraction difference was a
misplaced accent in the Simančík reference, now restored from the PDF. The
original figures are embedded in the Markdown, which is usable offline.
The earlier arXiv preprint has materially different content and was not used.
The Markdown preserves the article's claims; this conversion is not a
scientific review or correction of them.

AIO is CC BY 4.0. The publisher lists the article as CC BY-NC 4.0, while the
eScholarship cover metadata lists CC BY 4.0; both notices and their sources are
recorded in the manifest. These reference downloads do not replace the pinned
import source in `sources/aio/` or regenerate the concept records in `data/aio/`.
