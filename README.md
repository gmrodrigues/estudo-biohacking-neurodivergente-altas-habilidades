# Saúde cognitiva de precisão

Este repositório investiga como capacidade cognitiva, perfis neurocognitivos,
sono, atividade, alimentação, biomarcadores e suplementação se relacionam ao
funcionamento ao longo do tempo. Capacidade é modelada como contínuo: um percentil
cognitivo elevado não é diagnóstico, e um diagnóstico não descreve sozinho a
arquitetura cognitiva de uma pessoa.

A primeira fase é montar e testar uma base analítica mínima viável. Antes de
modelos de efeito, ela precisa demonstrar que as medidas, a elegibilidade, a
temporalidade e as perdas permitem pequenas provas de conceito reprodutíveis.

## Comece aqui

- [Planejamento da fase 1: base ampla e validada por POCs](catalog/data-sources/PHASE_1_PLAN.md)
- [Programa científico e regras de inferência](catalog/PROGRAM.md)
- [Fase inicial: base analítica e provas de conceito](catalog/data-sources/ANALYTIC_FOUNDATION.md)
- [Primeiro ciclo ABCD](catalog/data-sources/ABCD_FIRST_CYCLE.md)
- [Dicionário de construtos](catalog/data-sources/CONSTRUCT_DICTIONARY.md)
- [Mapa de fontes, amplitude e acesso](catalog/data-sources/DATA_MODEL_AND_SAMPLE_CAPACITY.md)
- [Estado e mapa de desatualização](research/discoveries/STATUS_AND_STALENESS_MAP.md)

## Linhas do programa

| Linha | Papel | Estado atual |
|---|---|---|
| ABCD | Base longitudinal inicial: cognição, sintomas, sono, atividade e contexto | Acesso individual pendente; auditoria de metadados e especificação pronta |
| Healthy Brain Network | Replicação transdiagnóstica e perfis 2e | Avaliar versão, termos e cobertura real |
| UK Biobank | Adultos: dieta, suplementos, biomarcadores e cognição | Dossiê de acesso antes de qualquer estimativa |
| NHANES | Linha de apoio para mensuração nutricional e biomarcadores | Quatro ciclos legados, sem HA/TDAH/autismo medidos |
| Terman e SMPY | Validação conceitual de capacidade e realização | Fontes históricas; não estimam suplementação contemporânea |

<!-- discovery-cycles:start -->
## Linha empírica legada: NHANES

[Explorar gráficos e ciclos no site](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/)

[Programa e fase inicial](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/programa.html) · [Caminho até conclusões](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/conclusoes.html) · [Métodos e salvaguardas](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/objetivos.html) · [Ciclos e hipóteses](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/planejamento.html) · [Fontes e linhas de apoio](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/fontes.html) · [Progresso e decisões](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/progresso.html)

- [Inferência e seleção: estabilidade dos resultados sob reponderação](research/discoveries/cycle-004/README.md) — 2026-09-10
- [Magnésio por produto: o que a ausência em DSQTMAGN realmente significa](research/discoveries/cycle-003/README.md) — 2026-09-09
- [Auditoria de perdas, pesos e variância do ciclo 001](research/discoveries/cycle-002/README.md) — 2026-09-09
- [Artigo: Cafeína e magnésio: o que os dados ajudam a decidir sobre suplementação](research/discoveries/cycle-001/article.md)
- [Cafeína, sono, sedentarismo, magnésio e predição diagnóstico-agnóstica](research/discoveries/cycle-001/README.md) — 2026-09-09

[Métodos e fontes](catalog/data-sources/README.md)

Instale as dependências com `PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev`.
<!-- discovery-cycles:end -->

## Regras científicas

1. Associação de nutriente ou hábito não recomenda suplementação. Uma hipótese de
   consolidação de hábito requer acompanhamento ou intervenção registrados.
2. Clusters e perfis latentes são descrições que exigem estabilidade e validação;
   eles não criam diagnósticos.
3. Bases independentes não são unidas por semelhança. A comparação é uma síntese
   de construtos, estimandos, incerteza e limites.
4. Resultados sobre dupla excepcionalidade exigem medidas independentes de
   capacidade, TDAH e autismo na mesma coorte.

## Executar

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev
PIPENV_VENV_IN_PROJECT=1 pipenv run python -m unittest discover -s tests -v
PIPENV_VENV_IN_PROJECT=1 pipenv run python scripts/build_discovery_site.py --output /tmp/science-site --update-readmes
```

Dados individuais ABCD, HBN e UK Biobank só são acessados pelos canais legítimos
de cada fonte. O repositório não contorna credenciais nem publica microdados.
