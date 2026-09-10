"""Render cycle 004 public artifacts from aggregate results."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
RESULTS = json.loads((OUT / "results.json").read_text())


def write_json(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def pt_number(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def table(headers: list[str], rows: list[list[object]]) -> dict:
    return {"headers": headers, "rows": [[str(cell) for cell in row] for row in rows]}


models = RESULTS["models"]
terms = RESULTS["primary_terms"]
selection_rows = []
for name in ["H1", "H2", "H3"]:
    selection = models[name]["selection"]
    balance = models[name]["balance"]
    selection_rows.append([
        name,
        selection["eligible_n"],
        selection["complete_n"],
        f"{selection['unweighted_completion_rate']:.1%}".replace(".", ","),
        pt_number(selection["propensity_min"]),
        pt_number(selection["inverse_probability_max"]),
        pt_number(balance["max_abs_smd_before"]),
        pt_number(balance["max_abs_smd_after"]),
    ])

term_labels = {
    ("H1", "CAFF100"): "Cafeína / 100 mg aos 45 anos",
    ("H1", "CAFF_X_AGE"): "Cafeína × idade por década",
    ("H2", "C(SLEEP_CAT)[T.short]"): "Sono curto <7 h",
    ("H2", "C(SLEEP_CAT)[T.long]"): "Sono longo >9 h",
    ("H2", "SED_HOURS"): "Sedentarismo por hora/dia",
    ("H3", "DIET_MAG100"): "Magnésio alimentar / 100 mg",
    ("H3", "SUPP_MAG100"): "Magnésio suplementar / 100 mg",
    ("H3", "SUPP_MAG_UNQUANT"): "Qualquer suplemento; total de magnésio ausente",
}
coefficient_rows = [[
    row["model"],
    term_labels[(row["model"], row["term"])],
    pt_number(row["reference_estimate"], 4),
    pt_number(row["ipw_estimate"], 4),
    pt_number(row["absolute_change"], 4),
    pt_number(row["ipw_ci_low"], 4) + " a " + pt_number(row["ipw_ci_high"], 4),
    f"{row['ipw_q_value']:.8f}".replace(".", ","),
] for row in terms]

sources = [
    {"title": "CDC/NCHS: variância, subpopulações e graus de liberdade",
     "url": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx"},
    {"title": "CDC/NCHS: dicas de software para o desenho NHANES",
     "url": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/softwaretips.aspx"},
    {"title": "R survey: graus residuais em svyglm",
     "url": "https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svyglm.html"},
]
sections = [
    {
        "title": "Decisão sobre inferência",
        "paragraphs": [
            "A inferência principal passa a declarar explicitamente 15 graus do desenho: 30 PSUs representados menos 15 estratos representados. Essa é a definição do NCHS para o NHANES contínuo e coincide com a implementação do ciclo 001.",
            "O grau residual igual a 1 produzido pelo padrão de svy permanece como sensibilidade conservadora. A documentação do pacote survey informa que subtrair os parâmetros é apropriado para covariáveis no nível da PSU, mas pode ser muito conservador para covariáveis individuais. Nenhum modelo foi simplificado e nenhuma covariável foi escolhida por significância.",
        ],
    },
    {
        "title": "População elegível e casos completos",
        "paragraphs": [
            "O ciclo 002 usou como denominador 6.337 adultos após junções. Para a sensibilidade de seleção, o denominador foi refinado antes dos efeitos: pessoas de 20–80 anos, com peso positivo do componente e desenho observado. Isso separa inelegibilidade estrutural e ausência coberta pelos pesos de dieta da incompletude restante.",
            "A completude é 87,8% em H1, 74,6% em H2 e 87,4% em H3. As propensões mínimas estimadas ficaram entre 0,392 e 0,599; o maior inverso foi 2,263. Não apareceu uma violação forte de positividade nas variáveis observadas usadas.",
        ],
        "table": table(
            ["Modelo", "Elegíveis", "Completos", "Retenção", "Propensão mín.", "1/p máx.", "SMD máx. antes", "SMD máx. depois"],
            selection_rows,
        ),
    },
    {
        "title": "Estabilidade dos oito contrastes",
        "paragraphs": [
            "A reponderação pela probabilidade observável de caso completo alterou os coeficientes de H1 e H2 entre 0,7% e 3,3%. Cafeína continua associada a menos sono; sono curto, sono longo e sedentarismo continuam associados a mais sintomas sob 15 graus do desenho.",
            "Os três coeficientes de H3 tiveram mudanças relativas maiores, entre 11,9% e 19,5%, porque suas estimativas de referência são pequenas. As mudanças absolutas foram de 0,0026 a 0,0101 hora, e todos os intervalos continuam incluindo zero. H3 permanece inconclusiva.",
            "A interação cafeína × idade fica em q=0,05088 após reponderação, próxima do limiar e sem mudança substantiva de magnitude. O valor não deve ser transformado em decisão binária de descoberta.",
        ],
        "table": table(
            ["Modelo", "Contraste", "Referência", "IPW", "Mudança", "IC95% IPW", "q IPW"],
            coefficient_rows,
        ),
    },
    {
        "title": "O que esta sensibilidade não resolve",
        "paragraphs": [
            "A ponderação equilibra somente idade, sexo registrado, raça/etnia e estrato. Ela não corrige seleção por sintomas, renda ou exposições não observadas, não recupera valores ausentes e não incorpora a incerteza de estimar as propensões nos intervalos.",
            "Os dados continuam transversais e com janelas diferentes. Estabilidade sob seleção observável não estabelece causalidade, validade externa ou efeito individual. HA, autismo e TDAH continuam não avaliados.",
        ],
    },
]

review_note = (
    "Ciclo pós-resultados: fixa 15 graus do desenho como convenção principal segundo o NCHS "
    "e testa seleção observável sem alterar os oito contrastes. Não é replicação."
)
write_json("public-dossier.json", {
    "schema_version": 1,
    "review_note": review_note,
    "sections": sections,
})

cycle = {
    "schema_version": 1,
    "id": "cycle-004",
    "status": "completed",
    "data_kind": "empirical_aggregate",
    "title": "Inferência e seleção: estabilidade dos resultados sob reponderação",
    "summary": "O NCHS sustenta 15 graus do desenho como convenção principal. Reponderar casos completos pela inclusão observável muda H1/H2 em no máximo 3,3%; H3 continua inconclusiva.",
    "population": "NHANES 2021–2023, adultos de 20–80 anos elegíveis por hipótese; 4.194–4.522 casos completos, sem identificação de HA/autismo/TDAH.",
    "completed_at": "2026-09-10",
    "findings": [
        {
            "question": "Qual convenção de graus usar nos contrastes principais?",
            "estimate": "15 graus = 30 PSUs − 15 estratos; 1 grau residual preservado como sensibilidade",
            "uncertainty": "Decisão metodológica baseada no desenho e documentação; não é estimativa de efeito.",
            "sample": "Todos os 30 PSUs e 15 estratos estão representados em H1/H2/H3.",
            "interpretation": "Contrastes individuais usam t com graus do desenho; não se executou busca de termos ou teste conjunto do modelo completo.",
        },
        {
            "question": "Qual a retenção dentro da população realmente elegível?",
            "estimate": "H1 87,8%; H2 74,6%; H3 87,4%",
            "uncertainty": "Contagens e proporções amostrais; não são taxas populacionais de resposta.",
            "sample": "20–80 anos, junções da hipótese, peso positivo e desenho observado.",
            "interpretation": "O denominador de 6.337 do ciclo 002 misturava elegibilidade do componente com incompletude analítica.",
        },
        {
            "question": "A seleção observável altera os contrastes principais?",
            "estimate": "H1/H2 mudam no máximo 3,3%; H3 muda até 0,0101 h em valor absoluto e segue inconclusiva",
            "uncertainty": "Taylor com propensões tratadas como fixas; seleção não observada não é corrigida.",
            "sample": "4.211 em H1, 4.522 em H2 e 4.194 em H3, reponderados pela inclusão observável.",
            "interpretation": "Há estabilidade a esta sensibilidade específica, sem eliminar viés de seleção ou causalidade reversa.",
        },
    ],
    "figures": [
        {
            "path": "figures/eligible-complete.png",
            "alt": "Elegíveis e casos completos nas três hipóteses",
            "caption": "Contagens não ponderadas após restringir a 20–80 anos, peso positivo e desenho observado.",
        },
        {
            "path": "figures/ipw-coefficients.png",
            "alt": "Coeficientes de referência e após reponderação por seleção",
            "caption": "Oito contrastes congelados; linhas conectam a estimativa de casos completos à sensibilidade IPW.",
        },
    ],
    "limitations": [
        "Propensões usam somente idade, sexo registrado, raça/etnia e estrato.",
        "A variância trata pesos de resposta estimados como fixos.",
        "Não recupera exposições/desfechos ausentes nem corrige seleção não observada.",
        "Mesma onda e participantes dos ciclos anteriores; sem replicação externa.",
        "Dados transversais não identificam efeitos causais ou individuais.",
        "HA, autismo e TDAH permanecem not_assessed.",
    ],
    "sources": sources,
    "reproducibility": {
        "command": "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/run_analysis.py",
        "code_revision": "working tree; run_analysis.py sha256=" + hashlib.sha256((OUT / "run_analysis.py").read_bytes()).hexdigest(),
        "input_sha256": RESULTS["input_sha256"],
    },
}
write_json("cycle.json", cycle)

lines = ["# Inferência e seleção por casos completos — ciclo 004", "",
         "[Protocolo](protocol.md) · [Hipótese registrada localmente](hypothesis.yaml) · [Resultados](hypothesis-results.md) · [Agregados](results.json)", ""]
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
          "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/run_analysis.py",
          "PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/render_analysis.py",
          "```", ""]
(OUT / "data-audit.md").write_text("\n".join(lines))

result_lines = [
    "# Resultados da sensibilidade à seleção — ciclo 004",
    "",
    "Oito contrastes congelados após os resultados do ciclo 001. IPW combina o peso NHANES com o inverso da probabilidade observável de caso completo; IC95% usa 15 graus do desenho.",
    "",
    "| Modelo | Contraste | Referência | IPW | Mudança | IC95% IPW | q IPW |",
    "|---|---|---:|---:|---:|---:|---:|",
]
result_lines += ["| " + " | ".join(row) + " |" for row in coefficient_rows]
result_lines += [
    "",
    "H1 e H2 permanecem próximos das estimativas de referência. H3 continua inconclusiva. A interação cafeína × idade fica limítrofe após FDR, sem mudança substantiva da magnitude.",
    "",
    "A análise corrige apenas diferenças observáveis por idade, sexo registrado, raça/etnia e estrato. Não corrige seleção não observada, não incorpora a estimação das propensões na variância e não constitui replicação.",
    "",
]
(OUT / "hypothesis-results.md").write_text("\n".join(result_lines))

print("Rendered cycle 004")
