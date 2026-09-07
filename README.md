# Biohacking, neurodivergência e altas habilidades

Projeto de pesquisa sobre relações entre cognição, sono, alimentação,
suplementação, atividade física e contexto de vida, com foco em altas
habilidades/superdotação e comparações com autismo, TDAH e pessoas neurotípicas
quando essas características forem efetivamente avaliadas.

O objetivo é construir modelos multidimensionais, testar hipóteses e desenvolver
preditores de desfechos que funcionem mesmo sem um diagnóstico conhecido. As
análises distinguem associação, previsão e efeito causal, considerando também
excepcionalidades isoladas, duplas e triplas.

<!-- discovery-cycles:start -->
## Resultados

O projeto está na preparação do primeiro ciclo de descobertas. Já existem um
catálogo de fontes, análises descritivas de viabilidade, hipóteses e ferramentas
de publicação; ainda não há ciclos científicos concluídos.

Cada ciclo terá gráficos, estimativas, incertezas, fontes e limitações. Seus
resultados serão ligados aqui e publicados em páginas navegáveis no GitHub Pages.
O workflow está preparado; a publicação efetiva ainda precisa ser verificada.

Consulte o [plano da primeira rodada](catalog/data-sources/DISCOVERY_PLAN.md).
<!-- discovery-cycles:end -->

## Métodos e dados

- [Catálogo e acesso às fontes](catalog/data-sources/README.md).
- [Viabilidade e dados já inspecionados](catalog/data-sources/INITIAL_FEASIBILITY_ANALYSIS.md).
- [Metodologia multidimensional e preditiva](catalog/data-sources/MULTIDIMENSIONAL_HYPOTHESIS_PREDICTION_METHODOLOGY.md).
- [Desenho dos grupos e comparações](catalog/data-sources/CORE_STUDY_DESIGN.md).
- [Estratificação demográfica e contexto de vida](catalog/data-sources/STRATIFICATION_MODEL.md).
- [Hipóteses de suplementação](catalog/data-sources/SUPPLEMENTATION_HYPOTHESES.md).

Os insumos públicos locais incluem componentes do NHANES 2021–2023 e registros
do ClinicalTrials.gov. O NHANES selecionado permite estudar relações em adultos,
mas não identifica adequadamente altas habilidades. Registros de ensaios não
equivalem, por si só, a evidência de eficácia. Esses limites orientam quais
perguntas podem ser respondidas em cada ciclo.

## Executar

Requisitos: Python 3.14 e Pipenv. Execute os comandos na raiz do repositório.
Todas as dependências e execuções Python são gerenciadas pelo Pipenv.

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev
```

Reproduzir o perfil descritivo dos dados NHANES locais:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python catalog/data-sources/analyze_nhanes.py
```

Verificar as ferramentas de publicação:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python -m unittest discover -s tests -v
```

## Ciclos e publicação

As análises de cada ciclo ficam em `research/discoveries/<cycle-id>/`, com
manifesto `cycle.json`, relatório e gráficos. O
[contrato de publicação](skills/science-cycle-publish/references/cycle-format.md)
define os campos e critérios para concluir um ciclo.

Para gerar o site e atualizar a seção de resultados deste README, use um
diretório de saída vazio:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python scripts/build_discovery_site.py --output _site --update-readmes
```

Se `_site` já contiver um build, escolha outra pasta vazia. O
[workflow de publicação](.github/workflows/discovery-pages.yml) utiliza GitHub
Actions e requer Pages habilitado no repositório. Cada página terá navegação
entre ciclos, gráficos e dados agregados. Rascunhos não são publicados.

## Skills do estudo

| Skill | Uso |
|---|---|
| [science-discovery](skills/science-discovery/SKILL.md) | conduzir uma rodada de descobertas |
| [science-data-audit](skills/science-data-audit/SKILL.md) | verificar cobertura e validade dos dados |
| [science-hypothesis-test](skills/science-hypothesis-test/SKILL.md) | registrar e testar hipóteses |
| [science-predictive-model](skills/science-predictive-model/SKILL.md) | prever desfechos sem diagnóstico conhecido |
| [science-evidence-synthesis](skills/science-evidence-synthesis/SKILL.md) | confrontar achados com estudos e teorias |
| [science-cycle-publish](skills/science-cycle-publish/SKILL.md) | gerar gráficos, documentação e páginas por ciclo |

Para iniciar a primeira rodada no Codex com as skills instaladas:
“Use `$science-discovery` para investigar cafeína e sono, começando pela auditoria.”
