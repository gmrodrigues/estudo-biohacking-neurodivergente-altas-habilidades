"""Build a static results site from completed, aggregate discovery cycles."""

import argparse
from datetime import date
from html import escape
import json
from pathlib import Path
import re
import shutil
from urllib.parse import quote, urlparse


REPO_URL = "https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades"
PAGES_URL = "https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/"
START = "<!-- discovery-cycles:start -->"
END = "<!-- discovery-cycles:end -->"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
STYLE = """
@font-face { font-family: LeagueGothic; src: url('https://gmrodrigues.github.io/old-site/assets/font/LeagueGothic-Regular.otf') format('opentype'); font-display: swap; }
:root { color-scheme: light; font-family: system-ui, sans-serif; color: #182c38;
  background: #f4f6f7; line-height: 1.65; }
body { margin: 0; } main { max-width: 1080px; margin: auto; padding: 2rem 1.2rem 4rem; }
h1, h2 { line-height: 1.2; } h1 { font-size: clamp(1.8rem, 5vw, 2.7rem); }
h2 { margin-top: 2.4rem; } a { color: #075e75; text-underline-offset: .2em; }
a:focus-visible { outline: 3px solid #d18810; outline-offset: 4px; }
nav { display: flex; flex-wrap: wrap; gap: 1.2rem; margin: 1rem 0; }
.eyebrow { color: #42616c; text-transform: uppercase; letter-spacing: .08em; font-size: .8rem; }
article, figure { background: white; border: 1px solid #d7e1e6; border-radius: .6rem;
  padding: 1.2rem; margin: 1.2rem 0; } figure img { width: 100%; height: auto; }
figcaption { color: #384f5c; } .table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; background: white; }
th, td { padding: .7rem; text-align: left; border-bottom: 1px solid #d7e1e6; vertical-align: top; }
th { background: #e5eef1; } pre { overflow-x: auto; padding: 1rem; background: #e5eef1; }
code { overflow-wrap: anywhere; } footer { border-top: 1px solid #c8d8df; margin-top: 3rem; padding-top: 1rem; }
.notice { border-left: 5px solid #b77113; background: #fff4dd; padding: 1rem; }
.reading { max-width: 78ch; } section { scroll-margin-top: 1rem; }
.masthead { color: #edf4f4; background-color: #050505;
  background-image: linear-gradient(120deg, #050505f2, #05050599),
    url('https://gmrodrigues.github.io/old-site/assets/img/galaxy-wallpapers-22-1.jpg');
  background-size: cover; background-position: center; border-bottom: 3px solid orangered; }
.masthead-inner { max-width: 1080px; margin: auto; padding: 2rem 1.2rem; }
.masthead a { color: #edf4f4; } .masthead .identity { font-size: 1.05rem; text-decoration: none; }
.masthead .handle { color: #ff7948; font: 1.6rem LeagueGothic, Impact, sans-serif; letter-spacing: .05em; }
.masthead .brand-title { font: clamp(2rem, 6vw, 3.4rem) LeagueGothic, Impact, sans-serif; margin: .4rem 0; }
.masthead p { margin: .3rem 0; } .masthead .back-link { display: inline-block; margin-top: .8rem; }
@media(max-width:600px) { main { padding: 1rem .8rem; } article, figure { padding: .8rem; } }
"""


def render_sections(sections):
    """Render public editorial content as escaped text, never arbitrary HTML."""
    body = ""
    for section in sections:
        body += f"<section><h2>{escape(text_field(section, 'title'))}</h2>"
        for paragraph in section.get("paragraphs", []):
            body += f"<p class='reading'>{escape(paragraph)}</p>"
        if section.get("items"):
            body += "<ul>" + "".join(f"<li>{escape(x)}</li>" for x in section["items"]) + "</ul>"
        if section.get("table"):
            table = section["table"]
            body += "<div class='table-wrap'><table><thead><tr>"
            body += "".join(f"<th>{escape(x)}</th>" for x in table["headers"]) + "</tr></thead><tbody>"
            for row in table["rows"]:
                if len(row) != len(table["headers"]):
                    raise ValueError("Editorial table has inconsistent columns")
                body += "<tr>" + "".join(f"<td>{escape(x)}</td>" for x in row) + "</tr>"
            body += "</tbody></table></div>"
        if section.get("links"):
            body += "<ul>"
            for link in section["links"]:
                url = text_field(link, "url")
                if urlparse(url).scheme != "https" or not urlparse(url).netloc:
                    raise ValueError("Editorial sources must be HTTPS URLs")
                body += f"<li><a href='{escape(url, quote=True)}'>{escape(text_field(link, 'title'))}</a></li>"
            body += "</ul>"
        body += "</section>"
    return body


def study_navigation(pages, prefix=""):
    return "<nav aria-label='Estudo'><a href='" + prefix + "index.html'>Resultados</a>" + "".join(
        f"<a href='{prefix}{p['id']}.html'>{escape(p['title'])}</a>" for p in pages) + "</nav>"


def article_markdown(article):
    """Export the same editorial source used by the HTML article."""
    lines = [f"# {text_field(article, 'title')}", "", text_field(article, "summary"), ""]
    for section in article["sections"]:
        lines += [f"## {section['title']}", ""]
        for paragraph in section.get("paragraphs", []):
            lines += [paragraph, ""]
        for item in section.get("items", []):
            lines += [f"- {item}"]
        if section.get("table"):
            table = section["table"]
            def row(values):
                return "| " + " | ".join(x.replace("|", "\\|") for x in values) + " |"
            lines += [row(table["headers"]), row(["---"] * len(table["headers"]))]
            lines += [row(values) for values in table["rows"]]
        if section.get("links"):
            lines += [""]
        lines += [f"- [{link['title']}]({link['url']})" for link in section.get("links", [])]
        lines += [""]
    return "\n".join(lines)


def load_study(root):
    path = root / "research/site/study.json"
    if not path.exists():
        return {"pages": [], "intro": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    identifiers = set()
    for entry in data["pages"]:
        slug = text_field(entry, "id")
        if not re.fullmatch(r"[a-z][a-z0-9-]{0,60}", slug) or slug == "index" or slug in identifiers:
            raise ValueError("Invalid or duplicate study page id")
        identifiers.add(slug)
        text_field(entry, "title")
        render_sections(entry["sections"])
    render_sections(data["intro"])
    return data


def text_field(record, key):
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing nonempty text: {key}")
    return value


def load_cycles(root):
    cycles = []
    for manifest in sorted((root / "research/discoveries").glob("*/cycle.json")):
        if not manifest.resolve().is_relative_to((root / "research/discoveries").resolve()):
            raise ValueError("Cycle manifest must stay within the discovery directory")
        cycle = json.loads(manifest.read_text(encoding="utf-8"))
        if cycle.get("status") == "draft":
            continue
        if cycle.get("schema_version") != 1 or cycle.get("status") != "completed":
            raise ValueError(f"Unsupported or unfinished cycle: {manifest}")
        if cycle.get("data_kind") != "empirical_aggregate":
            raise ValueError(f"Public results must be empirical aggregates: {manifest}")
        cycle_id = text_field(cycle, "id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,79}", cycle_id):
            raise ValueError(f"Invalid cycle id: {cycle_id}")
        if cycle_id != manifest.parent.name:
            raise ValueError("Cycle id must equal its directory name")
        for key in ("title", "summary", "population", "completed_at"):
            text_field(cycle, key)
        date.fromisoformat(cycle["completed_at"])
        for key in ("findings", "figures", "limitations", "sources"):
            if not isinstance(cycle.get(key), list) or not cycle[key]:
                raise ValueError(f"Completed cycle needs a nonempty {key} list")
        for finding in cycle["findings"]:
            for key in ("question", "estimate", "uncertainty", "sample", "interpretation"):
                text_field(finding, key)
        for figure in cycle["figures"]:
            for key in ("path", "alt", "caption"):
                text_field(figure, key)
            path = Path(figure["path"])
            resolved = (manifest.parent / path).resolve()
            if path.is_absolute() or ".." in path.parts or not resolved.is_relative_to(manifest.parent.resolve()):
                raise ValueError("Figure must stay within its cycle directory")
            if path.suffix.lower() != ".png" or not resolved.is_file():
                raise ValueError(f"Missing PNG figure: {path}")
            with resolved.open("rb") as stream:
                if stream.read(8) != PNG_SIGNATURE:
                    raise ValueError(f"Invalid PNG signature: {path}")
        if not all(isinstance(value, str) and value.strip() for value in cycle["limitations"]):
            raise ValueError("Limitations must be nonempty text")
        for source in cycle["sources"]:
            text_field(source, "title")
            parsed = urlparse(text_field(source, "url"))
            if parsed.scheme != "https" or not parsed.netloc:
                raise ValueError("Source URLs must be absolute HTTPS links")
        provenance = cycle.get("reproducibility", {})
        text_field(provenance, "command")
        text_field(provenance, "code_revision")
        hashes = provenance.get("input_sha256", {})
        if not isinstance(hashes, dict) or not hashes or not all(
            isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value)
            for value in hashes.values()
        ):
            raise ValueError("Input SHA-256 hashes are required")
        cycles.append((cycle, manifest.parent))
    return sorted(cycles, key=lambda item: (item[0]["completed_at"], item[0]["id"]))


def page(title, body):
    return ("<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{escape(title)}</title><style>{STYLE}</style></head><body>"
            "<header class='masthead'><div class='masthead-inner'>"
            "<a class='identity' href='https://gmrodrigues.github.io/'>Glauber Machado Rodrigues</a>"
            "<p class='handle'>gmrodrigues / pesquisa aberta</p>"
            "<p class='brand-title'>Altas habilidades, neurodivergência e saúde</p>"
            "<p>Perguntas, dados e descobertas em construção.</p>"
            "<a class='back-link' href='https://gmrodrigues.github.io/'>← Site principal · Forte e Leve</a>"
            "</div></header><main>"
            "<p class='eyebrow'>Altas habilidades · neurodivergência · saúde</p>"
            f"{body}<footer><a href='{REPO_URL}'>Repositório e métodos</a> · "
            "Resultados de pesquisa, com seus limites de população e desenho."
            "</footer></main></body></html>")


def update_readme(path, prefix, content):
    """Preserve user-authored text outside the generated cycle block."""
    original = path.read_text(encoding="utf-8") if path.exists() else prefix
    block = f"{START}\n{content.rstrip()}\n{END}"
    if START in original or END in original:
        if original.count(START) != 1 or original.count(END) != 1 or original.index(END) < original.index(START):
            raise ValueError(f"Ambiguous generated README markers: {path}")
        before, rest = original.split(START)
        _, after = rest.split(END)
        updated = before + block + after
    else:
        updated = original.rstrip() + "\n\n" + block + "\n"
    path.write_text(updated, encoding="utf-8")


def build(root, output, write_readmes=False):
    root, output = root.resolve(), output.resolve()
    if output == root or output in root.parents or output.is_relative_to(root / "research"):
        raise ValueError("Output must be a dedicated build directory outside research inputs")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Use an empty output directory for a clean site build")
    cycles = load_cycles(root)
    study = load_study(root)
    output.mkdir(parents=True, exist_ok=True)
    for entry in study["pages"]:
        body = study_navigation(study["pages"]) + f"<h1>{escape(entry['title'])}</h1>"
        body += render_sections(entry["sections"])
        (output / f"{entry['id']}.html").write_text(page(entry["title"], body), encoding="utf-8")
    cards, root_links = [], []
    for index, (cycle, directory) in enumerate(cycles):
        cycle_id = cycle["id"]
        target = output / "cycles" / cycle_id
        target.mkdir(parents=True)
        nav = ["<a href='../../index.html'>Todos os ciclos</a>"]
        article_file = directory / "article.json"
        article_link = ""
        if article_file.exists():
            article = json.loads(article_file.read_text(encoding="utf-8"))
            article_body = study_navigation(study["pages"], "../../")
            article_body += "<p><a href='index.html'>Resultados, gráficos e métodos completos do ciclo</a></p>"
            article_body += f"<h1>{escape(text_field(article, 'title'))}</h1>"
            article_body += f"<p>{escape(text_field(article, 'summary'))}</p>"
            article_body += render_sections(article["sections"])
            article_body += "<p><a href='article.md'>Baixar artigo em Markdown</a></p>"
            (target / "article.html").write_text(page(article["title"], article_body), encoding="utf-8")
            markdown = article_markdown(article)
            (target / "article.md").write_text(markdown, encoding="utf-8")
            if write_readmes:
                (directory / "article.md").write_text(markdown, encoding="utf-8")
            nav.append("<a href='article.html'>Ler artigo do ciclo</a>")
            article_link = f"<p><a href='cycles/{cycle_id}/article.html'>Ler artigo: {escape(article['title'])}</a></p>"
        for neighbor, label in ((index - 1, "Ciclo anterior"), (index + 1, "Próximo ciclo")):
            if 0 <= neighbor < len(cycles):
                other_id = cycles[neighbor][0]["id"]
                nav.append(f"<a href='../{other_id}/index.html'>{label}</a>")
        body = (study_navigation(study["pages"], "../../") + f"<nav>{' '.join(nav)}</nav><h1>{escape(cycle['title'])}</h1>"
                f"<p>{escape(cycle['completed_at'])} · {escape(cycle['population'])}</p>"
                f"<p>{escape(cycle['summary'])}</p>")
        dossier = directory / "public-dossier.json"
        if dossier.exists():
            narrative = json.loads(dossier.read_text(encoding="utf-8"))
            if narrative.get("review_note"):
                body += f"<aside class='notice'>{escape(narrative['review_note'])}</aside>"
            body += render_sections(narrative["sections"])
        body += ("<h2>Resultados</h2>"
                "<div class='table-wrap'><table><thead><tr><th>Pergunta</th><th>Estimativa</th>"
                "<th>Incerteza</th><th>Amostra</th><th>Interpretação</th></tr></thead><tbody>")
        readme = [f"## {cycle['title']}", "", cycle["summary"], "", f"População: {cycle['population']}"]
        if article_file.exists():
            readme += ["", "[Ler artigo do ciclo](article.md)"]
        if dossier.exists():
            if narrative.get("review_note"):
                readme += ["", "> " + narrative["review_note"]]
            readme += ["", f"[Métodos, decisões e fontes no site]({PAGES_URL}cycles/{cycle_id}/index.html)",
                       "", "[Registro editorial completo](public-dossier.json)"]
        for finding in cycle["findings"]:
            body += "<tr>" + "".join(f"<td>{escape(finding[key])}</td>" for key in
                                   ("question", "estimate", "uncertainty", "sample", "interpretation")) + "</tr>"
            readme += ["", f"### {finding['question']}", "", finding["estimate"],
                       finding["uncertainty"], finding["sample"], "", finding["interpretation"]]
        body += "</tbody></table></div><h2>Gráficos</h2>"
        for figure in cycle["figures"]:
            filename = quote(Path(figure["path"]).as_posix(), safe="/")
            destination = target / figure["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(directory / figure["path"], destination)
            body += (f"<figure><a href='{filename}'><img src='{filename}' alt='{escape(figure['alt'], quote=True)}' "
                     f"loading='lazy'></a><figcaption>{escape(figure['caption'])}</figcaption></figure>")
            readme += ["", f"![{figure['alt']}]({figure['path']})", "", figure["caption"]]
        body += "<h2>Limitações</h2><ul>" + "".join(f"<li>{escape(x)}</li>" for x in cycle["limitations"]) + "</ul>"
        readme += ["", "## Limitações", ""] + [f"- {x}" for x in cycle["limitations"]]
        body += "<h2>Fontes</h2><ul>" + "".join(
            f"<li><a href='{escape(s['url'], quote=True)}'>{escape(s['title'])}</a></li>" for s in cycle["sources"]) + "</ul>"
        readme += ["", "## Fontes", ""] + [f"- [{s['title']}]({s['url']})" for s in cycle["sources"]]
        provenance = json.dumps(cycle["reproducibility"], indent=2, ensure_ascii=False)
        body += f"<h2>Reprodução</h2><pre>{escape(provenance)}</pre><p><a href='cycle.json'>Dados agregados do ciclo (JSON)</a></p>"
        readme += ["", "## Reprodução", "", "```json", provenance, "```", ""]
        (target / "index.html").write_text(page(cycle["title"], body), encoding="utf-8")
        (target / "cycle.json").write_text(json.dumps(cycle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        cards.append(f"<article><p>{escape(cycle['completed_at'])}</p><h2><a href='cycles/{cycle_id}/index.html'>"
                     f"{escape(cycle['title'])}</a></h2><p>{escape(cycle['summary'])}</p>{article_link}</article>")
        root_links.append(f"- [{cycle['title']}](research/discoveries/{cycle_id}/README.md) — {cycle['completed_at']}")
        if article_file.exists():
            root_links.append(f"- [Artigo: {article['title']}](research/discoveries/{cycle_id}/article.md)")
        if write_readmes:
            update_readme(directory / "README.md", "# Resultados do ciclo\n", "\n".join(readme))
    intro = "<h1>Resultados por ciclo</h1><p>Explore perguntas, estimativas, gráficos, fontes e limites de cada rodada.</p>"
    intro = study_navigation(study["pages"]) + intro + render_sections(study["intro"])
    if not cycles:
        intro += "<article><h2>Primeiro ciclo em preparação</h2><p>Ainda não há resultados de ciclos concluídos.</p></article>"
    (output / "index.html").write_text(page("Resultados por ciclo", intro + "".join(reversed(cards))), encoding="utf-8")
    (output / "cycles.json").write_text(json.dumps([{"id": c["id"], "title": c["title"],
        "completed_at": c["completed_at"]} for c, _ in cycles], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if write_readmes and cycles:
        update_readme(root / "README.md", "# Estudo de biohacking, neurodivergência e altas habilidades\n",
                      f"## Resultados\n\n[Explorar gráficos e ciclos no site]({PAGES_URL})\n\n" +
                      " · ".join(f"[{p['title']}]({PAGES_URL}{p['id']}.html)" for p in study["pages"]) + "\n\n" +
                      "\n".join(reversed(root_links)) +
                      "\n\n[Métodos e fontes](catalog/data-sources/README.md)\n\n" +
                      "Instale as dependências com `PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev`.\n")
    return len(cycles)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True, help="Empty generated-site directory")
    parser.add_argument("--update-readmes", action="store_true")
    args = parser.parse_args()
    try:
        count = build(args.root, args.output, args.update_readmes)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, f"Site build failed: {exc}\n")
    print(f"Completed cycles: {count}; site: {args.output}")


if __name__ == "__main__":
    main()
