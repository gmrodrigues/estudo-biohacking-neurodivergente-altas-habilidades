"""Publication tests use simulated fixtures only inside temporary directories."""

from copy import deepcopy
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import unquote, urlparse

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

from scripts.build_discovery_site import build, load_cycles


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("src", "href") and not urlparse(value).scheme:
                self.targets.append(unquote(value))


class DiscoverySiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def cycle(self, cycle_id="cycle-001"):
        directory = self.root / "research/discoveries" / cycle_id
        (directory / "figures").mkdir(parents=True)
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.errorbar([0.2, -0.1], [0, 1], xerr=[0.3, 0.2], fmt="o")
        ax.axvline(0, color="gray", linestyle="--")
        ax.set_yticks([0, 1], ["Fixture A", "Fixture B"])
        ax.set_xlabel("Efeito simulado (unidade de teste)")
        ax.set_title("DADOS SIMULADOS — teste de publicação")
        fig.tight_layout()
        fig.savefig(directory / "figures/effect.png", dpi=120)
        plt.close(fig)
        data = {
            "schema_version": 1, "id": cycle_id, "status": "completed",
            "data_kind": "empirical_aggregate",  # Exercise the production schema in an isolated test.
            "title": f"Fixture simulada {cycle_id}", "completed_at": "2026-09-07",
            "summary": "Fixture isolada; não representa resultado do estudo.",
            "population": "Amostra simulada de teste",
            "findings": [{"question": "Teste de renderização", "estimate": "0.2",
                          "uncertainty": "Intervalo simulado [-0.1, 0.5]",
                          "sample": "N simulado = 20", "interpretation": "Teste, sem inferência"}],
            "figures": [{"path": "figures/effect.png", "alt": "Intervalos simulados de teste",
                         "caption": "Fixture gerada por Matplotlib; não é evidência empírica."}],
            "limitations": ["Dados simulados exclusivos do teste."],
            "sources": [{"title": "Documentação NHANES", "url": "https://www.cdc.gov/nchs/nhanes/"}],
            "reproducibility": {"command": "pipenv run python -m unittest discover -s tests",
                                "code_revision": "test-fixture",
                                "input_sha256": {"fixture": sha256(b"simulated fixture").hexdigest()}},
        }
        path = directory / "cycle.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path, data

    def test_no_readme_before_first_completed_cycle(self):
        self.assertEqual(build(self.root, self.root / "site", True), 0)
        self.assertFalse((self.root / "README.md").exists())
        self.assertIn("Ainda não há resultados", (self.root / "site/index.html").read_text())

    def test_completed_cycles_have_plots_navigation_and_readmes(self):
        self.cycle()
        self.cycle("cycle-002")
        self.assertEqual(build(self.root, self.root / "site", True), 2)
        for page in (self.root / "site").rglob("*.html"):
            links = Links()
            links.feed(page.read_text())
            for target in links.targets:
                self.assertTrue((page.parent / target).is_file(), (page, target))
        first = (self.root / "site/cycles/cycle-001/index.html").read_text()
        self.assertIn("Próximo ciclo", first)
        self.assertIn("Incerteza", first)
        self.assertTrue((self.root / "research/discoveries/cycle-001/README.md").is_file())
        self.assertIn("cycle-002/README.md", (self.root / "README.md").read_text())
        self.assertTrue((self.root / "site/cycles/cycle-001/figures/effect.png").is_file())

    def test_readme_preserves_user_text_and_updates_without_duplicate_blocks(self):
        self.cycle()
        (self.root / "README.md").write_text("# Texto do usuário\n\nIntrodução própria.\n")
        build(self.root, self.root / "site-a", True)
        build(self.root, self.root / "site-b", True)
        readme = (self.root / "README.md").read_text()
        self.assertTrue(readme.startswith("# Texto do usuário"))
        self.assertEqual(readme.count("<!-- discovery-cycles:start -->"), 1)

    def test_incomplete_cycle_does_not_publish(self):
        path, data = self.cycle()
        data["status"] = "draft"
        path.write_text(json.dumps(data))
        self.assertEqual(load_cycles(self.root), [])

    def test_real_planning_lists_every_completed_cycle(self):
        """Keep the editorial roadmap synchronized with completed artifacts."""
        project = Path(__file__).resolve().parents[1]
        study = json.loads((project / "research/site/study.json").read_text())
        planning = next(page for page in study["pages"] if page["id"] == "planejamento")
        rendered = json.dumps(planning, ensure_ascii=False)
        for cycle, _ in load_cycles(project):
            number = int(cycle["id"].split("-")[1])
            self.assertIn(f"Ciclo {number:03d}", rendered)

    def test_invalid_publication_inputs_rejected(self):
        path, data = self.cycle()
        variants = []
        synthetic = deepcopy(data)
        synthetic["data_kind"] = "synthetic"
        variants.append(synthetic)
        missing_interval = deepcopy(data)
        del missing_interval["findings"][0]["uncertainty"]
        variants.append(missing_interval)
        missing_plot = deepcopy(data)
        missing_plot["figures"][0]["path"] = "figures/missing.png"
        variants.append(missing_plot)
        escape_path = deepcopy(data)
        escape_path["figures"][0]["path"] = "../../outside.png"
        variants.append(escape_path)
        unsafe_url = deepcopy(data)
        unsafe_url["sources"][0]["url"] = "javascript:alert(1)"
        variants.append(unsafe_url)
        for variant in variants:
            with self.subTest(variant=variant):
                path.write_text(json.dumps(variant))
                with self.assertRaises(ValueError):
                    load_cycles(self.root)

    def test_html_escapes_result_content(self):
        path, data = self.cycle()
        data["summary"] = "<script>alert('test')</script>"
        path.write_text(json.dumps(data))
        build(self.root, self.root / "site")
        body = (self.root / "site/index.html").read_text()
        self.assertNotIn("<script>", body)
        self.assertIn("&lt;script&gt;", body)

    def test_rejects_reusing_output_and_research_as_output(self):
        build(self.root, self.root / "site")
        for output in (self.root / "site", self.root, self.root / "research/site"):
            with self.subTest(output=output), self.assertRaises(ValueError):
                build(self.root, output)

    def test_public_narrative_navigation_review_and_privacy(self):
        path, _ = self.cycle()
        editorial = self.root / "research/site"
        editorial.mkdir(parents=True)
        study = {"intro": [{"title": "Visão", "paragraphs": ["Perguntas públicas"]}],
                 "pages": [{"id": "objetivos", "title": "Objetivos",
                            "sections": [{"title": "Escopo", "items": ["Planejado"]}]}]}
        (editorial / "study.json").write_text(json.dumps(study))
        (path.parent / "public-dossier.json").write_text(json.dumps({
            "review_note": "Limite em revisão <7h",
            "sections": [{"title": "Método", "paragraphs": ["<script>untrusted</script>"]}]}))
        # A neighboring private file must never be discovered or copied automatically.
        (path.parent / "personal-history.json").write_text('"PRIVATE-SENTINEL"')
        build(self.root, self.root / "site", True)
        for html in (self.root / "site").rglob("*.html"):
            body = html.read_text()
            self.assertNotIn("PRIVATE-SENTINEL", body)
            links = Links()
            links.feed(body)
            for target in links.targets:
                self.assertTrue((html.parent / target).is_file(), (html, target))
        cycle_html = (self.root / "site/cycles/cycle-001/index.html").read_text()
        self.assertLess(cycle_html.index("Limite em revisão"), cycle_html.index("<h2>Resultados"))
        self.assertNotIn("<script>", cycle_html)
        self.assertIn("&lt;script&gt;", cycle_html)
        self.assertIn("Limite em revisão", (path.parent / "README.md").read_text())
        self.assertFalse((self.root / "site/cycles/cycle-001/personal-history.json").exists())

    def test_editorial_rejects_unsafe_links_and_page_paths(self):
        editorial = self.root / "research/site"
        editorial.mkdir(parents=True)
        for entry in (
            {"id": "../escape", "title": "Invalid", "sections": []},
            {"id": "valid", "title": "Invalid", "sections": [{"title": "Source",
             "links": [{"title": "Unsafe", "url": "javascript:alert(1)"}]}]},
        ):
            with self.subTest(entry=entry):
                (editorial / "study.json").write_text(json.dumps({"intro": [], "pages": [entry]}))
                with self.assertRaises(ValueError):
                    build(self.root, self.root / "site")

    def test_article_has_same_content_in_site_markdown_and_navigation(self):
        path, _ = self.cycle()
        (path.parent / "article.json").write_text(json.dumps({
            "title": "Artigo de teste", "summary": "Resultados exploratórios",
            "sections": [{"title": "Comparação", "paragraphs": ["<b>Não executar HTML</b>"],
                          "table": {"headers": ["Medida", "Valor"], "rows": [["A", "1"]]},
                          "links": [{"title": "Fonte", "url": "https://www.cdc.gov/"}]}]}))
        build(self.root, self.root / "site", True)
        destination = self.root / "site/cycles/cycle-001"
        self.assertEqual((destination / "article.md").read_text(), (path.parent / "article.md").read_text())
        body = (destination / "article.html").read_text()
        self.assertIn("&lt;b&gt;", body)
        self.assertNotIn("<b>", body)
        self.assertIn("article.html", (destination / "index.html").read_text())
        self.assertIn("article.html", (self.root / "site/index.html").read_text())
        self.assertIn("article.md", (self.root / "README.md").read_text())
        for html in (self.root / "site").rglob("*.html"):
            parser = Links(); parser.feed(html.read_text())
            for target in parser.targets:
                self.assertTrue((html.parent / target).is_file(), (html, target))


if __name__ == "__main__":
    unittest.main()
