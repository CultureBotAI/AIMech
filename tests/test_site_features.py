"""The X-Mech website features: evidence and term links, curation history and
notice, schema reference, licence footer, downloads, not-found page, skip link,
feedback route, text-map coverage, visual alternatives and sibling routes.

Page-level tests read the committed pages/, which test_render_pages_check_passes
keeps identical to a fresh render, and scope each assertion to the section that
owns the feature: a page-wide "link X appears" passes when the same link
exists elsewhere on the page.
"""

from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
import posixpath
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import yaml
from jinja2 import Environment
from markupsafe import escape

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
TEMPLATES = ROOT / "src" / "aimech" / "templates"
CURATED = ROOT / "data" / "curated"
AIO = ROOT / "data" / "aio"
SITE = "https://culturebotai.github.io/AIMech/pages/"
REPO = "https://github.com/CultureBotAI/AIMech"


def load_script(name):
    spec = importlib.util.spec_from_file_location(f"aimech_{name}", ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


render_pages = load_script("render_pages")
export_records = load_script("export_records")


class Links(HTMLParser):
    """Anchors (href, text) and every href/src/action in an HTML fragment."""

    def __init__(self, html: str):
        super().__init__()
        self.anchors: list[tuple[str, str]] = []
        self.references: list[str] = []
        self._open: list[list] = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src", "action"):
            if attrs.get(key) is not None:
                self.references.append(attrs[key])
        if tag == "a":
            self._open.append([attrs.get("href"), ""])

    def handle_data(self, data):
        for anchor in self._open:
            anchor[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self._open:
            href, text = self._open.pop()
            self.anchors.append((href, " ".join(text.split())))


def page(relative: str) -> str:
    return (PAGES / relative).read_text(encoding="utf-8")


def between(html: str, start: str, end: str) -> str:
    """The fragment from a template-owned start marker to the next end marker."""
    assert start in html, start
    rest = html[html.index(start):]
    return rest[: rest.index(end)] if end in rest else rest


def record(path: Path) -> dict:
    # libyaml when available: these tests read every record, and the pure-Python
    # loader would take most of a minute (export_records.load_records does the same).
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    return yaml.load(path.read_text(encoding="utf-8"), Loader=loader)


def autolink(text, *, own=None, pages=None, root="../"):
    env = Environment(autoescape=True)
    env.filters["autolink"] = render_pages.autolink
    return env.from_string("{{ v | autolink }}").render(
        v=text, c={"id": own} if own else None, page_by_id=pages or {}, root=root)


# --------------------------------------------------------------- evidence --

@pytest.mark.parametrize(("text", "token", "href"), [
    ("Kingma and Ba (arXiv:1412.6980v9).", "arXiv:1412.6980v9", "https://arxiv.org/abs/1412.6980v9"),
    ("(EMNLP 2022, arXiv:2205.11961)", "arXiv:2205.11961", "https://arxiv.org/abs/2205.11961"),
    ("arXiv math/0403022v2, p. 4", "arXiv math/0403022v2", "https://arxiv.org/abs/math/0403022v2"),
    ("the complete arXiv1603.09630v2 paper", "arXiv1603.09630v2", "https://arxiv.org/abs/1603.09630v2"),
    ("(2012, arXiv:1010.2731v1/v3, which", "arXiv:1010.2731v1", "https://arxiv.org/abs/1010.2731v1"),
    ("(8(2):2207-2241, DOI:10.1214/14-EJS950)", "DOI:10.1214/14-EJS950",
     "https://doi.org/10.1214/14-EJS950"),
    ("see doi:10.1016/S1571-0653(04)00333-6, p. 3", "doi:10.1016/S1571-0653(04)00333-6",
     "https://doi.org/10.1016/S1571-0653(04)00333-6"),
    ("audit of `DOI:10.1007/s10208-012-9135-7`): (1)", "DOI:10.1007/s10208-012-9135-7",
     "https://doi.org/10.1007/s10208-012-9135-7"),
    ("as **10.1099/ijs.0.02316-0** states", "10.1099/ijs.0.02316-0",
     "https://doi.org/10.1099/ijs.0.02316-0"),
    ("redirects to https://proceedings.neurips.cc/paper/2013/file/x-Paper.pdf.",
     "https://proceedings.neurips.cc/paper/2013/file/x-Paper.pdf",
     "https://proceedings.neurips.cc/paper/2013/file/x-Paper.pdf"),
    ("PMID:12345678 reports", "PMID:12345678", "https://pubmed.ncbi.nlm.nih.gov/12345678/"),
])
def test_autolink_links_the_reference_token_and_keeps_the_text(text, token, href):
    html = autolink(text)
    anchors = Links(html).anchors
    assert anchors == [(href, token)], html
    # Only the token became the anchor: the surrounding text is still there.
    assert re.sub(r"<[^>]+>", "", html) == str(escape(text))


def test_autolink_ends_tokens_at_markdown_syntax():
    html = autolink("[10.1038/nature14539](https://doi.org/10.1038/nature14539) and `arXiv:1012.0621v3`")
    hrefs = [href for href, _ in Links(html).anchors]
    assert hrefs == ["https://doi.org/10.1038/nature14539", "https://doi.org/10.1038/nature14539",
                     "https://arxiv.org/abs/1012.0621v3"]
    assert not any(mark in href for href in hrefs for mark in ("%5D", "]", "`", "*", ")"))


@pytest.mark.parametrize("text", [
    "arXiv abstract page", "arxiv-abs source", "arXivv1 text", "Domain-Conditional PMI (AIMech:PMIDCDomain)",
    "Section 3, PDF p. 3, discrete NL[v](i) formula", "a 10.5 percent gain", "v10.1/x",
    "arXiv:1234.567890 is not an arXiv identifier",
])
def test_autolink_leaves_non_references_as_text(text):
    assert Links(autolink(text)).anchors == []


def test_autolink_escapes_record_text():
    html = autolink("<script>alert(1)</script> & 'q' \"x\" DOI:10.1234/x <b>")
    assert Links(html).anchors == [("https://doi.org/10.1234/x", "DOI:10.1234/x")]
    assert "<script>" not in html and "<b>" not in html
    assert "&lt;script&gt;" in html and "&amp;" in html and "&lt;b&gt;" in html


@pytest.mark.parametrize("text", [
    "Given <u, v> = 0 for all u in M_bar & R^p, ||.|| is a norm.",
    "Section 3.3, Algorithm 1 (`merge_with_quantization`), p. 5; it's \"exact\".",
    "",
])
def test_text_without_tokens_renders_as_plain_escaping(text):
    assert autolink(text) == str(escape(text))


def test_autolink_opens_record_curies_on_this_site_only():
    pages = {"AIMech:Adam": "curated/Adam.html", "AIO:Layer": "aio/Layer.html", "AIMech:SGD": "curated/SGD.html"}
    html = autolink("Unlike AIMech:Adam, AIMech:AdamW, AIMech:Unknown, AIMech:SGD, AIO:Layer and AIO:Elsewhere.",
                    own="AIMech:SGD", pages=pages)
    assert Links(html).anchors == [
        ("../curated/Adam.html", "AIMech:Adam"),
        ("../aio/Layer.html", "AIO:Layer"),
        ("https://w3id.org/aio/Elsewhere", "AIO:Elsewhere"),
    ]


@pytest.mark.parametrize(("value", "url"), [
    ("arXiv:1412.6980v9", "https://arxiv.org/abs/1412.6980v9"),
    ("arxiv:1904.09237v1", "https://arxiv.org/abs/1904.09237v1"),
    ("doi:10.1016/S0004-3702(98)00086-1", "https://doi.org/10.1016/S0004-3702(98)00086-1"),
    ("DOI:10.1214/aos/1018031", "https://doi.org/10.1214/aos/1018031"),
    ("10.1145/1273496.1273556", "https://doi.org/10.1145/1273496.1273556"),
    ("https://openreview.net/forum?id=x", "https://openreview.net/forum?id=x"),
    ("PMID:30000000", "https://pubmed.ncbi.nlm.nih.gov/30000000/"),
    ("TR-2002-119", None),
    ("slowbull/largebatch@ea8880af035222de0cbebcfa4d81d100a61ffb5a", None),
    ("pmlr-v15-larochelle11a", None),
])
def test_reference_url_resolves_only_references(value, url):
    assert render_pages.reference_url(value) == url


@pytest.mark.parametrize(("curie", "url"), [
    ("BFO:0000051", "http://purl.obolibrary.org/obo/BFO_0000051"),
    ("owl:Thing", "http://www.w3.org/2002/07/owl#Thing"),
    ("AIO:Layer", "https://w3id.org/aio/Layer"),
    ("NCIT:C16205", "https://bioregistry.io/NCIT:C16205"),
    ("AIMech:Adam", None),
    ("not a curie", None),
])
def test_curie_url_uses_the_resolver_map_then_bioregistry(curie, url):
    assert render_pages.curie_url(curie) == url


def test_record_pages_link_persistent_ids_and_definition_evidence():
    html = page("curated/Adam.html")
    row = between(html, '<tr id="source-original-paper">', "</tr>")
    assert ("https://arxiv.org/abs/1412.6980v9", "arXiv:1412.6980v9") in Links(row).anchors
    evidence = between(html, '<div class="definition-evidence">', "</ul>")
    doc = record(CURATED / "Adam.yaml")
    titles = {s["source_id"]: s["title"] for s in doc["evidence_sources"]}
    for citation in doc["definition_evidence"]:
        assert (f"#source-{citation['source_id']}", titles[citation["source_id"]]) in Links(evidence).anchors
        assert str(escape(citation["locator"])) in evidence


def test_record_prose_links_references_and_sibling_records():
    html = page("curated/ATTEMPTAttentionalMixturesOfSoftPrompts.html")
    notes = between(html, '<div class="identity-box">', "</div>")
    assert ("https://arxiv.org/abs/2205.11961", "arXiv:2205.11961") in Links(notes).anchors
    html = page("curated/AcceleratedGradientAndNegativeCurvatureExploitationForNonConvexOptimization.html")
    notes = between(html, '<div class="identity-box">', "</div>")
    target = "AIMech:PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization"
    assert (CURATED / f"{target.split(':')[1]}.yaml").is_file()
    assert (f"../curated/{target.split(':')[1]}.html", target) in Links(notes).anchors


CLEAR_REFERENCE = re.compile(r"\barXiv:[0-9]{4}\.[0-9]{4,5}|\bdoi:10\.[0-9]{4,9}/|https?://", re.I)


def test_no_curated_record_content_shows_an_unlinked_reference():
    """Every arXiv:ID, doi:10.x/... and URL in curated record content is a link."""
    unlinked = {}
    for path in sorted((PAGES / "curated").glob("*.html")):
        html = path.read_text(encoding="utf-8")
        content = between(html, '<div class="detail-header">', "<!-- Ontology & Grounding Neighborhood Diagram -->")
        text = re.sub(r"<a\b[^>]*>.*?</a>", " ", content, flags=re.S)
        text = re.sub(r"<[^>]+>", " ", text)
        if found := CLEAR_REFERENCE.findall(text):
            unlinked[path.name] = found
    assert unlinked == {}


# ------------------------------------------------------------- term links --

def test_examined_aio_candidates_show_their_labels():
    names = {record(p)["id"]: record(p)["name"] for p in AIO.glob("*.yaml")}
    checked = 0
    for path in sorted(CURATED.glob("*.yaml")):
        doc = record(path)
        if not doc.get("aio_no_match"):
            continue
        table = between(page(f"curated/{path.stem}.html"), 'aria-label="Examined AIO candidates"', "</table>")
        for target in doc["aio_no_match"]["examined_targets"]:
            if target["target"] in names:
                cell = between(table, f"<code>{target['target']}</code>", "</td>")
                assert str(escape(names[target["target"]])) in cell, (path.stem, target["target"])
                checked += 1
    assert checked > 1000


def test_aio_predicates_subsets_and_owl_parents_link_resolvers():
    html = page("aio/AutoEncoderNetwork.html")
    relations = between(html, "Axiomatic Relationships", "</ul>")
    assert "has part</strong>" in relations
    assert ("http://purl.obolibrary.org/obo/BFO_0000051", "BFO:0000051") in Links(relations).anchors
    subsets = between(html, "<strong>Subsets:</strong>", "</ul>")
    for subset in record(AIO / "AutoEncoderNetwork.yaml")["subsets"]:
        assert (subset, subset) in Links(subsets).anchors
    parents = between(page("aio/Bias.html"), "Parent Classes", "</ul>")
    assert ("http://www.w3.org/2002/07/owl#Thing", "owl:Thing") in Links(parents).anchors


def test_predicate_labels_are_the_schema_definitions():
    schema = yaml.safe_load((ROOT / "src/aimech/schema/aimech.yaml").read_text(encoding="utf-8"))
    values = schema["enums"]["RelationshipPredicate"]["permissible_values"]
    assert set(render_pages.PREDICATE_LABELS) == set(values)
    for predicate, label in render_pages.PREDICATE_LABELS.items():
        assert values[predicate]["description"].startswith(label + ";")


# ------------------------------------------------------- curation history --

def test_record_pages_list_their_recorded_sessions():
    history = between(page("curated/BeamStackSearch.html"), 'id="curation-history"', "<!-- Report a problem -->")
    assert '<time datetime="2026-10-11T06:05:37Z">' in history
    assert "EDIT" in history and "Removed unsubstantiated beam-stack short alias" in history
    assert "Codex (<code>ai_agent</code>; GPT-6)" in history
    hrefs = [href for href, _ in Links(history).anchors]
    assert f"{REPO}/issues/27" in hrefs
    assert (f"{REPO}/blob/main/history/records/BeamStackSearch/2026-10-11T060537Z-codex-56dad7.yaml"
            in hrefs)
    history = between(page("curated/GridLongShortTermMemory.html"), 'id="curation-history"',
                      "<!-- Report a problem -->")
    assert "CREATE" in history and "Add Grid Long Short-Term Memory" in history
    assert (f"{REPO}/blob/main/research/discovery/20261013T113018Z-grid-long-short-term-memory.json"
            in [href for href, _ in Links(history).anchors])


def test_record_pages_list_their_saved_reviews():
    history = between(page("curated/Adam.html"), 'id="curation-history"', "<!-- Report a problem -->")
    reviews = between(history, "Saved Reviews", "</ul>")
    hrefs = [href for href, _ in Links(reviews).anchors]
    for review_id in ("20261011T031639Z-optimization-graphs-rl-explanations",
                      "20261011T034010Z-optimizer-and-symbolic-methods"):
        assert f"{REPO}/blob/main/reviews/structured/{review_id}/review.md" in hrefs
    assert reviews.count("independence <code>self_review</code>") == 2


def write_yaml(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data), encoding="utf-8")


def test_sessions_join_records_only_through_their_sidecar_targets(tmp_path, monkeypatch):
    monkeypatch.setattr(render_pages, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(render_pages, "HISTORY_DIR", tmp_path / "history")
    session = {"id": "s", "timestamp": "2026-10-11T00:00:00Z",
               "actors": [{"name": "Codex", "type": "ai_agent", "model": "m", "agent_tool": "Codex"}]}
    events = [{"type": "EDIT", "outcome": "changed", "summary": "s", "details": "d"}]
    write_yaml(tmp_path / "history/records/A/1.yaml",
               {"target": {"kind": "record", "path": "data/curated/A.yaml"}, "session": session, "events": events})
    write_yaml(tmp_path / "history/reports/r/2.yaml",
               {"target": {"kind": "report", "path": "research/discovery/r.json"},
                "session": dict(session, timestamp="2026-10-12T00:00:00Z", id="t"), "events": events})
    write_yaml(tmp_path / "history/schema/x/3.yaml",
               {"target": {"kind": "schema", "path": "data/curated/A.yaml"}, "session": session, "events": events})
    (tmp_path / "research/discovery").mkdir(parents=True)
    (tmp_path / "research/discovery/r.json").write_text(json.dumps(
        {"selected_concept": {"id": "AIMech:B"}, "entries": [{"id": "AIMech:A"}, {"id": "AIMech:Gone"}],
         "already_present": [{"id": "AIMech:C"}]}), encoding="utf-8")
    found = render_pages.load_curation_sessions(
        {"data/curated/A.yaml": "AIMech:A", "data/curated/B.yaml": "AIMech:B", "data/curated/C.yaml": "AIMech:C"})
    assert {key: [s["id"] for s in value] for key, value in found.items()} == {
        "AIMech:A": ["s", "t"], "AIMech:B": ["t"]}
    assert found["AIMech:B"][0]["report_path"] == "research/discovery/r.json"


# ------------------------------------------------------------ schema docs --

def test_schema_page_documents_every_class_slot_and_enum():
    from linkml_runtime.utils.schemaview import SchemaView

    html = page("schema.html")
    for key, path, _status in render_pages.SCHEMAS:
        view = SchemaView(str(path))
        for name in view.all_classes():
            block = between(html, f'id="{key}-class-{name}"', '<div class="callout schema-')
            for slot in view.class_induced_slots(name):
                assert f"<code>{slot.name}</code>" in block, (key, name, slot.name)
        for name, enum in view.all_enums().items():
            block = between(html, f'id="{key}-enum-{name}"', "</dl>")
            for value in enum.permissible_values or {}:
                assert f"<code>{escape(value)}</code>" in block, (key, name, value)


SAMPLE_PAGES = ["index.html", "browse.html", "kinds/architecture.html", "branches/Bias.html",
                "curated/Adam.html", "aio/AutoEncoderNetwork.html", "map.html", "graph.html",
                "schema.html", "404.html"]


def root_of(relative: str) -> str:
    if relative == "404.html":
        return render_pages.NOT_FOUND_ROOT
    return "../" * relative.count("/")


@pytest.mark.parametrize("relative", SAMPLE_PAGES)
def test_every_page_type_links_the_schema_reference(relative):
    nav = between(page(relative), "<nav>", "</nav>")
    assert (root_of(relative) + "schema.html", "Schema") in Links(nav).anchors
    footer = between(page(relative), "<footer>", "</footer>")
    assert (root_of(relative) + "schema.html", "LinkML schema") in Links(footer).anchors


# ----------------------------------------------------------------- licence --

LICENCE_TEXT = (
    "Code: BSD-3-Clause. AIO source data and derived records in data/aio: CC BY 4.0, attributed "
    "to the Artificial Intelligence Ontology authors. The repository states no licence for the "
    "curated concepts in data/curated. Third-party source material keeps its own terms."
)


def test_the_licence_files_say_what_the_footer_says():
    assert (ROOT / "LICENSE").read_text(encoding="utf-8").startswith("BSD 3-Clause License")
    data = " ".join((ROOT / "LICENSE-DATA").read_text(encoding="utf-8").split())
    assert data.startswith("AIO source data and derived records in data/aio are licensed CC-BY-4.0.")
    assert "Artificial Intelligence Ontology authors" in data
    assert "curated" not in data


@pytest.mark.parametrize("relative", SAMPLE_PAGES)
def test_every_page_type_states_the_licences_exactly(relative):
    footer = between(page(relative), '<p class="fam license">', "</p>")
    assert " ".join(re.sub(r"<[^>]+>", "", footer).split()) == LICENCE_TEXT
    assert Links(footer).anchors == [(f"{REPO}/blob/main/LICENSE", "BSD-3-Clause"),
                                     (f"{REPO}/blob/main/LICENSE-DATA", "CC BY 4.0")]


# --------------------------------------------------------------- downloads --

def test_export_is_complete_sorted_and_deterministic(tmp_path):
    first = export_records.export(tmp_path / "a", commit="abc")
    second = export_records.export(tmp_path / "b", commit="abc")
    data = (tmp_path / "a" / export_records.RECORDS_FILE).read_bytes()
    assert data == (tmp_path / "b" / export_records.RECORDS_FILE).read_bytes()
    assert data[4:8] == b"\0\0\0\0"  # gzip MTIME: no clock in the bytes
    assert first == second
    lines = gzip.decompress(data).decode("utf-8").splitlines()
    expected = {record(p)["id"]: record(p) for p in [*CURATED.glob("*.yaml"), *AIO.glob("*.yaml")]}
    assert [json.loads(line)["id"] for line in lines] == sorted(expected)
    assert all(json.loads(line) == expected[json.loads(line)["id"]] for line in lines)
    assert first["records"] == len(expected)
    assert first["counts"] == {"curated": len(list(CURATED.glob("*.yaml"))), "aio": len(list(AIO.glob("*.yaml")))}
    assert first["sha256"] == hashlib.sha256(data).hexdigest()
    manifest = json.loads((tmp_path / "a" / export_records.MANIFEST_FILE).read_text(encoding="utf-8"))
    assert manifest == first and manifest["commit"] == "abc"


def pages_workflow():
    return yaml.safe_load((ROOT / ".github/workflows/pages.yaml").read_text(encoding="utf-8"))


def test_the_pages_workflow_builds_the_export_into_the_artifact():
    workflow = pages_workflow()
    assert workflow["permissions"] == {"contents": "read", "pages": "write", "id-token": "write"}
    steps = workflow["jobs"]["deploy"]["steps"]
    names = [step.get("name") for step in steps]
    export = steps[names.index("Export complete records")]["run"]
    assert 'scripts/export_records.py --out "$RUNNER_TEMP/site/pages/downloads"' in export
    assert names.index("Stage site") < names.index("Export complete records") < names.index(
        "Upload Pages artifact")
    assert render_pages.DOWNLOAD_FILES == (f"downloads/{export_records.RECORDS_FILE}",
                                          f"downloads/{export_records.MANIFEST_FILE}")


def test_the_landing_page_links_the_export_and_says_when_it_is_built():
    card = between(page("index.html"), '<div class="card download-card">', '<a class="card" href="schema.html#curated">')
    assert [href for href, _ in Links(card).anchors] == list(render_pages.DOWNLOAD_FILES)
    assert "each time the site is deployed" in card


REFERENCE = re.compile(r'(?:href|src|action)="([^"]*)"')


def test_committed_pages_have_no_dangling_relative_reference():
    """Every relative reference resolves to a committed file, or is a deploy-time export."""
    files = {p.relative_to(PAGES).as_posix() for p in PAGES.rglob("*") if p.is_file()}
    dangling = set()
    for path in PAGES.rglob("*.html"):
        if path.name == "404.html" and path.parent == PAGES:
            continue  # site-root-absolute; checked below
        base = path.parent.relative_to(PAGES).as_posix()
        # Script bodies build markup from data at run time; they are not references.
        html = re.sub(r"<script\b[^>]*>.*?</script>", "", path.read_text(encoding="utf-8"), flags=re.S)
        for reference in REFERENCE.findall(html):
            parts = urlsplit(reference.replace("&amp;", "&"))
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = posixpath.normpath(posixpath.join(base, parts.path))
            if resolved not in files and resolved not in render_pages.DOWNLOAD_FILES:
                dangling.add((path.relative_to(PAGES).as_posix(), reference))
    assert sorted(dangling)[:10] == []


# --------------------------------------------------------- not-found page --

def test_not_found_page_uses_only_site_root_absolute_links():
    html = page("404.html")
    references = Links(html).references
    assert references
    relative = [r for r in references
                if not r.startswith(("/AIMech/", "https://", "#", "data:"))]
    assert relative == []
    assert 'action="/AIMech/pages/browse.html"' in html
    stage = next(s for s in pages_workflow()["jobs"]["deploy"]["steps"] if s.get("name") == "Stage site")
    assert 'cp pages/404.html "$RUNNER_TEMP/site/404.html"' in stage["run"]


# --------------------------------------------------------------- skip link --

FOCUSABLE = re.compile(r"<(a\s[^>]*href|input|select|button|textarea|summary)\b", re.I)


def test_every_page_starts_with_a_skip_link_to_main():
    pages = sorted(PAGES.rglob("*.html"))
    assert len(pages) > 1900
    for path in pages:
        html = path.read_text(encoding="utf-8")
        body = html[html.index("<body>"):]
        first = FOCUSABLE.search(body)
        assert body[first.start():].startswith('<a class="skip-link" href="#main-content">'), path
        assert '<main id="main-content" tabindex="-1">' in html, path
        assert not re.search(r"<[^>]*\sautofocus\b", html), path


# ---------------------------------------------------------- feedback route --

def test_every_record_page_links_a_prefilled_issue_for_that_record():
    for origin, folder in (("curated", CURATED), ("aio", AIO)):
        for path in sorted(folder.glob("*.yaml")):
            record_id = record(path)["id"]
            html = page(f"{origin}/{path.stem}.html")
            section = between(html, "<!-- Report a problem -->", "<!-- Cross-Mech Navigation -->")
            anchors = Links(section).anchors
            issue = urlsplit(anchors[0][0])
            assert f"{issue.scheme}://{issue.netloc}{issue.path}" == f"{REPO}/issues/new"
            query = parse_qs(issue.query)
            assert query["body"] == [f"{SITE}{origin}/{path.stem}.html"]
            assert query["title"] == [f"Problem with {record_id}"]
            edits = [href for href, _ in anchors if "/edit/" in href]
            if origin == "curated":
                assert edits == [f"{REPO}/edit/main/data/curated/{path.stem}.yaml"]
            else:
                assert edits == []


def test_feedback_notes_quote_the_repository_rules():
    readme = " ".join((ROOT / "README.md").read_text(encoding="utf-8").split())
    claude = " ".join((ROOT / "CLAUDE.md").read_text(encoding="utf-8").split())
    assert render_pages.README_GENERATED_AIO in readme
    assert render_pages.CLAUDE_CURATED_EDITS in claude
    assert render_pages.CLAUDE_AIO_CORRECTIONS in claude


# --------------------------------------------------------------- responsive --

def css_rule(css: str, selector: str) -> str:
    match = re.search(r"(?:^|\n)" + re.escape(selector) + r"\s*\{([^}]*)\}", css)
    assert match, selector
    return match.group(1)


def test_stylesheet_wraps_long_tokens_and_keeps_tables_scrollable():
    css = (TEMPLATES / "style.css").read_text(encoding="utf-8")
    assert "overflow-wrap: anywhere" in css_rule(css, "main")
    assert "overflow-wrap: normal" in css_rule(css, ".table-wrap")
    assert "flex-wrap: wrap" in css_rule(css, ".breadcrumbs")
    # The two dark-theme declarations of every token block stay identical.
    explicit = re.findall(r':root\[data-theme="dark"\]\s*\{([^}]*)\}', css)
    system = re.findall(r':root:not\(\[data-theme="light"\]\)\s*\{([^}]*)\}', css)
    assert explicit and [" ".join(b.split()) for b in explicit] == [" ".join(b.split()) for b in system]


def test_every_table_region_is_focusable_and_named():
    for path in [*TEMPLATES.glob("*.html"), PAGES / "curated/Adam.html", PAGES / "browse.html"]:
        for tag in re.findall(r'<div class="table-wrap"[^>]*>', path.read_text(encoding="utf-8")):
            assert 'role="region"' in tag and 'tabindex="0"' in tag and 'aria-label="' in tag, (path, tag)


# ----------------------------------------------------------------- text map --

def map_points():
    return json.loads((ROOT / "data/embeddings/corpus_map.json").read_text(encoding="utf-8"))["points"]


def test_map_page_says_how_many_records_it_plots_and_why():
    plotted = {point[3] for point in map_points()}
    records = {record(p)["id"]: record(p) for p in [*CURATED.glob("*.yaml"), *AIO.glob("*.yaml")]}
    missing = [r for i, r in records.items() if i not in plotted]
    coverage = " ".join(re.sub(r"<[^>]+>", "", between(page("map.html"), 'id="map-coverage"', "</div>")).split())
    assert f"plots {len(plotted & set(records))} of the {len(records)} concepts" in coverage
    if missing:
        assert f"The other {len(missing)}" in coverage
        assert "data/embeddings/corpus_map.json" in coverage
    created = sorted(r["curation"]["created_at"][:10] for r in missing if "curation" in r)
    if missing and len(created) == len(missing):
        assert f"created from {created[0]} to {created[-1]}" in coverage


def test_map_coverage_reason_is_derived_from_the_records():
    def rec(i, origin, created=None):
        return {"id": i, "origin": origin, "curation": {"created_at": created} if created else {}}
    points = [[0, 0, 0, "AIMech:A", "A"], [0, 0, 0, "AIO:X", "X"], [0, 0, 0, "AIMech:Old", "Old"]]
    later = render_pages.map_coverage(points, [rec("AIMech:A", "curated", "2026-10-16T00:00:00Z"),
                                               rec("AIO:X", "aio"),
                                               rec("AIMech:B", "curated", "2026-10-18T00:00:00Z")])
    assert (later["plotted"], later["missing"], later["stale"], later["predates_missing"]) == (2, 1, 1, True)
    older = render_pages.map_coverage(points, [rec("AIMech:A", "curated", "2026-10-16T00:00:00Z"),
                                               rec("AIMech:B", "curated", "2026-10-01T00:00:00Z"),
                                               rec("AIO:Y", "aio")])
    assert older["predates_missing"] is False and older["missing_aio"] == 1


def test_record_pages_link_the_map_only_when_they_are_plotted():
    plotted = {point[3] for point in map_points()}
    for origin, folder in (("curated", CURATED), ("aio", AIO)):
        for path in sorted(folder.glob("*.yaml")):
            section = between(page(f"{origin}/{path.stem}.html"), "<!-- Cross-Mech Navigation -->", "</main>")
            hrefs = [href for href, _ in Links(section).anchors]
            on_map = any(href.startswith("../map.html?q=") for href in hrefs)
            assert on_map == (record(path)["id"] in plotted), path.stem
            assert on_map or "../map.html#map-coverage" in hrefs, path.stem


# ------------------------------------------------------ visual alternative --

@pytest.mark.parametrize(("relative", "bodies"), [
    ("map.html", ["map-table-body"]),
    ("graph.html", ["graph-node-body", "graph-edge-body"]),
])
def test_canvas_views_offer_a_table_of_what_they_plot(relative, bodies):
    html = page(relative)
    disclosure = between(html, '<details class="data-table"', "</details>")
    assert "<summary>View data as table</summary>" in disclosure
    for body in bodies:
        assert f'<tbody id="{body}"></tbody>' in disclosure
    assert "addEventListener('toggle', renderTable)" in html
    assert "<noscript>" in between(html, '<div class="map-wrap">', "<details")


# ---------------------------------------------------------- curation notice --

def normalized(text: str) -> str:
    return " ".join(text.split())


def test_status_notes_are_quoted_from_the_readme_and_schemas():
    readme = normalized((ROOT / "README.md").read_text(encoding="utf-8"))
    for sentence in render_pages.README_STATUS_NOTES.values():
        assert sentence in readme
    curated = yaml.safe_load((ROOT / "src/aimech/schema/curated_concept.yaml").read_text(encoding="utf-8"))
    aio = yaml.safe_load((ROOT / "src/aimech/schema/aimech.yaml").read_text(encoding="utf-8"))
    expected = {
        "DRAFT": curated["enums"]["CuratedReviewStatus"]["permissible_values"]["DRAFT"]["description"],
        "NOT_REVIEWED": aio["enums"]["ReviewStatus"]["permissible_values"]["NOT_REVIEWED"]["description"],
    }
    notice = between(page("index.html"), 'id="curation-notice"', '<div class="section-header">')
    for status, description in expected.items():
        assert f"<code>{status}</code>: “{description}”" in notice
        sentence = render_pages.README_STATUS_NOTES[status]
        assert str(render_pages.inline_code(sentence)) in notice


def test_landing_notice_counts_come_from_the_records():
    docs = [record(p) for p in CURATED.glob("*.yaml")]
    notice = normalized(between(page("index.html"), 'id="curation-notice"', '<div class="section-header">'))
    for method, count in Counter(d["curation"]["method"] for d in docs).items():
        assert f"<code>{method}</code> on {count} of {len(docs)}" in notice
    for curator, count in Counter(d["curation"]["curator"] for d in docs).items():
        assert f"{curator} ({count})" in notice
    if all(d["curation"]["method"] != "human" for d in docs):
        assert "human" not in notice.lower()


@pytest.fixture(scope="module")
def meanings():
    return render_pages.status_meanings(
        [render_pages.schema_reference(key, path) for key, path, _ in render_pages.SCHEMAS])


@pytest.mark.parametrize("relative", ["curated/Adam.html", "aio/AutoEncoderNetwork.html"])
def test_record_pages_explain_their_status_beside_it(relative, meanings):
    html = page(relative)
    folder = CURATED if relative.startswith("curated") else AIO
    status = record(folder / (Path(relative).stem + ".yaml"))["review_status"]
    header = between(html, '<div class="detail-title-row">', '<div class="detail-desc">')
    disclosure = between(header, '<details class="status-meaning">', "</details>")
    meaning = meanings[status]
    assert f"<summary>What <code>{status}</code> means</summary>" in disclosure
    assert f"“{meaning['description']}”" in disclosure
    assert f"schema.html#{meaning['anchor']}" in disclosure


# ------------------------------------------------- listing state and access --

@pytest.mark.parametrize("relative", ["browse.html", "kinds/architecture.html", "branches/Bias.html"])
def test_listings_announce_counts_and_report_empty_results(relative):
    html = page(relative)
    assert '<div class="filter-count" role="status" aria-live="polite">' in html
    assert '<p class="empty-state" id="emptyState" hidden>' in html


def test_listing_script_restores_only_offered_values():
    script = (TEMPLATES / "record-browser.js").read_text(encoding="utf-8")
    for control in ("sortSelect", "originSelect", "kindSelect", "branchSelect"):
        assert f"restoreSelect({control}, urlParams.get(" in script
        assert f"{control}.value = urlParams.get(" not in script
    assert "if (emptyEl) emptyEl.hidden = visibleCount !== 0;" in script


# ---------------------------------------------------------- sibling routes --

# The fleet's verified sibling routes (X-Mech unified standard, 2026-10-25): each
# Mech's search route and the two specific-record routes. A link elsewhere on a
# sibling site is a guess nothing here can check.
VERIFIED_SIBLING_ROUTES = (
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/PathwayMech/pages/records/",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
)
# Site roots carry no query; each answered HTTP 200 on 2026-10-25.
SIBLING_SITE_ROOTS = {
    f"https://culturebotai.github.io/{name}/" for name in (
        "CultureMech", "MediaIngredientMech", "CommunityMech", "TraitMech", "proteintraitsmech",
        "AntibioticMech", "CellStructureMech", "NaturalProductMech", "DUFMech", "PathwayMech",
        "TaxonMech", "HabitatMech", "CMMMech", "mechs")
}
FLEET_URL = re.compile(r"https?://culturebotai\.github\.io/[^\s\"'<>)]*")


def unverified_sibling_urls(text: str) -> set[str]:
    return {url for url in FLEET_URL.findall(text)
            if not url.startswith("https://culturebotai.github.io/AIMech/")
            and url not in SIBLING_SITE_ROOTS and not url.startswith(VERIFIED_SIBLING_ROUTES)}


def test_every_sibling_url_uses_a_verified_route():
    sources = [*TEMPLATES.glob("*.html"), ROOT / "scripts/render_pages.py"]
    built = [*PAGES.rglob("*.html")]
    found = {str(p.relative_to(ROOT)): urls for p in sources + built
             if (urls := unverified_sibling_urls(p.read_text(encoding="utf-8")))}
    assert found == {}
    # Not vacuous: the pages do link sibling sites.
    assert any(FLEET_URL.findall(p.read_text(encoding="utf-8")) for p in built[:5])
