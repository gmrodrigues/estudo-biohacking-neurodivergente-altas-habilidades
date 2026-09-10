"""Render the public cycle 003 measurement audit from aggregate results."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
RESULTS = json.loads((OUT / "results.json").read_text())


def write_json(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def table(headers: list[str], rows: list[list[object]]) -> dict:
    return {"headers": headers, "rows": [[str(cell) for cell in row] for row in rows]}


h3 = RESULTS["h3"]
states = h3["state_counts"]
state_rows = [
    ["Magnésio quantificado", states["quantified_magnesium"]],
    ["Produtos relatados, sem magnésio identificado", states["reported_products_no_magnesium_identified"]],
    ["Produto sem correspondência; magnésio não identificado", states["no_magnesium_identified_with_unmatched_product"]],
    ["Rótulo com magnésio, total ausente", states["magnesium_label_but_total_missing"]],
    ["Sem produto liberado", states["no_released_product_record"]],
]
sources = [
    {"title": "CDC DSQIDS_L: produtos, antiácidos, cálculo e cautelas",
     "url": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQIDS_L.htm"},
    {"title": "CDC DSQTOT_L: totais de suplementos e antiácidos",
     "url": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm"},
    {"title": "CDC NHANES-DSD: informações dos produtos (DSPI)",
     "url": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSPI.htm"},
    {"title": "CDC NHANES-DSD: ingredientes (DSII)",
     "url": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSII.htm"},
    {"title": "CDC NHANES-DSD: misturas (DSBI)",
     "url": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSBI.htm"},
]
sections = [
    {
        "title": "Pergunta e alcance",
        "paragraphs": [
            "Esta auditoria pós-resultados pergunta o que DSQTMAGN ausente representa na amostra H3. Liga registros participante-produto de 2021–2023 à base de rótulos 1999–2023 por DSDPID. Não ajusta modelo de sono, não testa eficácia e não é replicação.",
            "Os resultados públicos são agregados. Nomes de produtos associados a participantes e SEQN não são publicados.",
        ],
    },
    {
        "title": "Cardinalidade e cobertura das ligações",
        "paragraphs": [
            "DSQIDS_L tem 11.375 ocorrências relatadas por 4.017 participantes e 3.417 produtos distintos. Ocorrências repetidas foram preservadas porque podem representar recipientes, formulações ou doses distintas.",
            "DSPI contém uma linha por DSDPID. Das ocorrências, 11.210 ligam a DSPI e DSII; 165 não têm produto/ingredientes correspondentes, coerente com registros sem correspondência ou identificação suficiente.",
        ],
        "table": table(
            ["Checagem", "Resultado"],
            [[key, value] for key, value in RESULTS["joins"].items()],
        ),
    },
    {
        "title": "Estados de magnésio na amostra H3",
        "paragraphs": [
            "DSQTMAGN ausente não é um único estado. Entre 4.194 participantes, 1.348 têm magnésio quantificado; 1.522 possuem produtos liberados sem magnésio identificado; 47 têm produto sem correspondência suficiente; 1.271 não têm registro de produto liberado; apenas 6 têm rótulo com magnésio e total ausente.",
            "O indicador legado SUPP_MAG_UNQUANT vale 1 para 1.401 usuários de algum suplemento com DSQTMAGN ausente. Ele não identifica dose de magnésio desconhecida: mistura sobretudo ausência de magnésio identificado com poucos casos de cálculo incompleto.",
        ],
        "table": table(["Estado operacional auditado", "N"], state_rows),
    },
    {
        "title": "Antiácidos explicam DSD010=2 com magnésio",
        "paragraphs": [
            "Os 28 participantes de H3 com DSD010=2 e DSQTMAGN presente possuem registro de antiácido. O codebook define DSD010=2 para quem não tomou suplemento, mesmo que tenha antiácido contendo cálcio ou magnésio registrado apenas na seção de antiácidos.",
            "Portanto, esses valores não são inconsistências nem devem ser zerados. DSQTMAGN agrega suplementos e antiácidos; DSD010 descreve uso de suplemento segundo a regra editada pelo NCHS.",
        ],
    },
    {
        "title": "Reconstrução do total",
        "paragraphs": [
            "Para todos os 1.613 participantes com total e componentes presentes no arquivo completo, a soma de DSQIMAGN × dias/30 ficou a no máximo 0,05 mg de DSQTMAGN. A diferença é compatível com a resolução de uma casa decimal do total. Isso valida a ligação e a regra de frequência, mas não prova ingestão ou composição real.",
        ],
        "table": table(["Checagem", "Valor"], [[key, value] for key, value in RESULTS["reconstruction"].items()]),
    },
    {
        "title": "Quatro ocorrências de produto com magnésio sem quantidade individual",
        "paragraphs": [
            "Na amostra H3 há quatro ocorrências com ingrediente de magnésio identificado e DSQIMAGN ausente, distribuídas por seis participantes cujo total fica ausente porque outros registros também entram na agregação. Todas têm dias e quantidade válidos e correspondência de produto; uma não tem razão entre porção relatada e porção do rótulo. Nas outras três, a ausência não é explicada pelos campos públicos examinados.",
            "Não se imputou quantidade. Rótulos e nomes de ingredientes não bastam para converter compostos em magnésio elementar sem as regras e unidades específicas.",
        ],
        "table": table(
            ["Antiácido", "Dias válidos", "Quantidade válida", "Razão de porção presente", "Sem correspondência", "N"],
            [[row["antacid"], row["valid_days"], row["valid_quantity"], row["serving_ratio_present"],
              row["no_or_unknown_match"], row["n"]] for row in h3["record_level_ambiguity"]],
        ),
    },
    {
        "title": "Decisão científica",
        "paragraphs": [
            "A exposição quantitativa DSQTMAGN permanece utilizável com limites para magnésio calculado de suplementos e antiácidos. O coeficiente do indicador legado continua sendo uma descrição do modelo executado, mas deve ser nomeado como qualquer suplemento relatado com total de magnésio ausente, sem interpretá-lo como magnésio de dose desconhecida.",
            "Uma nova análise de H3 precisa registrar antes dos efeitos como separar: zero sustentado por produtos sem magnésio; quantidade calculada; produto rotulado com magnésio sem cálculo; produto não identificado; e antiácido. A pequena célula ambígua não sustenta um coeficiente próprio complexo. H3 permanece estimable_with_limits; forma química e biodisponibilidade continuam needs_data.",
            "HA, autismo e TDAH permanecem not_assessed. Nenhuma conclusão orienta dose ou produto individual.",
        ],
    },
]

review_note = (
    "Auditoria de mensuração posterior ao ciclo 001: o indicador legado de 1.401 pessoas não representa "
    "magnésio não quantificado. Somente 6 participantes têm produto rotulado com magnésio e total ausente. "
    "Os coeficientes anteriores são preservados, com interpretação corrigida."
)
write_json("public-dossier.json", {"schema_version": 1, "review_note": review_note, "sections": sections})

cycle = {
    "schema_version": 1,
    "id": "cycle-003",
    "status": "completed",
    "data_kind": "empirical_aggregate",
    "title": "Magnésio por produto: o que a ausência em DSQTMAGN realmente significa",
    "summary": "Auditoria de DSQIDS/DSPI/DSII mostra que o indicador legado de 1.401 usuários mistura produtos sem magnésio identificado com somente 6 casos de rótulo com magnésio e total ausente.",
    "population": "Amostra H3 do NHANES 2021–2023, n=4.194 adultos de 20–80 anos; auditoria de produtos e antiácidos, sem novo modelo de desfecho.",
    "completed_at": "2026-09-09",
    "findings": [
        {
            "question": "Quantos participantes marcados pelo indicador legado têm evidência de produto com magnésio?",
            "estimate": "6 de 1.401 têm produto rotulado com magnésio e DSQTMAGN ausente",
            "uncertainty": "Contagens exatas nos arquivos locais; classificação depende da correspondência pública de rótulos e não requer IC.",
            "sample": "H3 n=4.194; DSQIDS_L ligado a DSPI/DSII por DSDPID.",
            "interpretation": "O indicador legado não mede magnésio de dose desconhecida e precisa de nome descritivo.",
        },
        {
            "question": "Por que participantes sem suplemento podem ter magnésio quantificado?",
            "estimate": "28 participantes com DSD010=2 e DSQTMAGN presente; todos possuem antiácido",
            "uncertainty": "Contagem não ponderada; não estima prevalência de uso de antiácidos.",
            "sample": "H3 n=4.194; DSDANTA no nível produto.",
            "interpretation": "DSQTMAGN soma suplementos e antiácidos, enquanto DSD010=2 pode significar ausência de suplemento com antiácido registrado separadamente.",
        },
        {
            "question": "Os componentes individuais reproduzem o total?",
            "estimate": "1.613 de 1.613 totais ficam a ≤0,05 mg da soma DSQIMAGN × dias/30",
            "uncertainty": "Concordância aritmética na resolução divulgada; não é incerteza de ingestão.",
            "sample": "Arquivo completo DSQIDS_L/DSQTOT_L, participantes com ambos os valores presentes.",
            "interpretation": "A ligação e a frequência foram reproduzidas; autorrelato, rótulo e adesão permanecem fontes de erro.",
        },
    ],
    "figures": [{
        "path": "figures/magnesium-states.png",
        "alt": "Contagens dos cinco estados de mensuração de magnésio na amostra H3",
        "caption": "H3, n=4.194, contagens não ponderadas. Estados derivados de DSQTOT_L, DSQIDS_L e rótulos DSPI/DSII; não representam prevalência populacional ou efeito no sono.",
    }],
    "limitations": RESULTS["limitations"] + [
        "DSQTMAGN ausente não foi imputado; quatro ocorrências rotuladas com magnésio permanecem sem quantidade individual.",
        "A auditoria não ajusta novo modelo e não altera resultados numéricos de H3.",
    ],
    "sources": sources,
    "reproducibility": {
        "command": "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/run_audit.py",
        "code_revision": "working tree; run_audit.py sha256=" + hashlib.sha256((OUT / "run_audit.py").read_bytes()).hexdigest(),
        "input_sha256": {name + ".xpt": item["sha256"] for name, item in RESULTS["file_inventory"].items()},
    },
}
write_json("cycle.json", cycle)

lines = ["# Auditoria de magnésio por produto e antiácido — ciclo 003", "",
         "[Protocolo local](protocol.md) · [Agregados e hashes](results.json)", ""]
for section in sections:
    lines += ["## " + section["title"], ""]
    for paragraph in section.get("paragraphs", []):
        lines += [paragraph, ""]
    if "table" in section:
        data = section["table"]
        lines += ["| " + " | ".join(data["headers"]) + " |",
                  "|" + "|".join(["---"] * len(data["headers"])) + "|"]
        lines += ["| " + " | ".join(row) + " |" for row in data["rows"]]
        lines += [""]
lines += ["## Fontes", ""] + [f"- [{item['title']}]({item['url']})" for item in sources]
lines += ["", "## Reprodução", "", "```bash",
          "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/run_audit.py",
          "PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/render_audit.py",
          "```", ""]
(OUT / "data-audit.md").write_text("\n".join(lines))
print("Rendered cycle 003 audit")
