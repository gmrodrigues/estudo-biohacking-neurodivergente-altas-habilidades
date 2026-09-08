# Retomada da próxima sessão

Estado registrado em 2026-09-08. O primeiro ciclo, o artigo comparativo e o
portal foram publicados. O site confirmou a publicação do artigo após o deploy
do commit `8cd3875`:

- [portal do estudo](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/)
- [artigo do ciclo 001](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/cycles/cycle-001/article.html)
- [repositório](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades)

## O que já está concluído

- NHANES 2021–2023 foi inspecionado e o ciclo 001 foi executado em adultos.
- H1 testou cafeína e sono; H2 sono/sedentarismo e sintomas; H3 magnésio e sono.
- O Ridge prevê o escore modificado de sintomas sem diagnóstico como entrada.
- O ciclo contém código, hashes, gráficos, `results.json`, auditoria, dossiê,
  artigo e fichas de comparação.
- O artigo compara seis estudos e orienta a quantificação de cafeína e magnésio.
- A tese conceitual sobre capacidades encobertas foi registrada em
  `catalog/data-sources/FOUNDATIONAL_HYPOTHESIS.md`, com versões forte/restrita,
  alternativas e critérios que podem contrariá-la.
- O gerador do site, o registro editorial e as skills foram ampliados; dez testes
  de publicação passaram.

## Pendência científica imediata: H2

O protocolo escreveu `short_sleep` como `<7 h` e `recommended` como `7–9 h`, mas
o código atualmente usa `pd.cut(..., right=True)`. Assim, os resultados publicados
de H2 representam `≤7 h` versus `>7 a ≤9 h` e `>9 h`. A divergência está visível
no dossiê e no artigo; não ocultar ou substituir os números antigos.

Na próxima sessão:

1. Fazer um adendo explícito no ciclo 001.
2. Decidir, antes de rerodar, a convenção final (`<7`, `7–9`, `>9`) e aplicá-la
   ao código, rótulos da figura, `results.json`, `cycle.json`, dossiê e artigo.
3. Rerodar H2 e a família FDR de oito termos; registrar o impacto sobre todos os
   q-valores e atualizar os hashes apenas se algum insumo mudar.
4. Comparar a execução antiga e nova em uma tabela de auditoria, mantendo a
   execução antiga identificável no histórico Git.

## Próximo ciclo recomendado

Depois de resolver H2, executar uma rodada de robustez:

- decompor perdas por variável, peso e motivo observável;
- auditar distribuição dos pesos e a variância por estrato/PSU com método externo;
- testar sono contínuo, spline ou categorias pré-especificadas sem procurar apenas
  significância;
- analisar cafeína por faixas e, quando possível, horário/uso habitual;
- separar magnésio alimentar, suplementar e dose ausente, distinguindo magnésio
  elementar de peso do composto;
- avaliar não linearidade e sensibilidade a dados ausentes;
- repetir previsão com validação por onda/PSU ou base externa, com intervalos para
  MAE/RMSE/R² e calibração;
- manter os grupos HA, autismo e TDAH como `not_assessed` até haver medidas reais.

## Perguntas de suplementação para a próxima especificação

Priorizar cafeína e magnésio porque podem atravessar dieta, bebidas, suplementos
e medicamentos, mas não declarar que todos os regimes os contêm. Registrar por
tomada: fonte/produto, horário, cafeína total, magnésio elementar, alimento versus
suplemento/medicamento, adesão e grau de incerteza. Somar fontes sem contar duas
vezes ingredientes já incluídos no rótulo. Usar referências de segurança oficiais
como contexto, nunca como meta individual.

Não estimar interação cafeína×magnésio sem registro e modelo próprios. Coeficientes
populacionais não são previsão individual nem recomendação de dose. Não alterar
medicamentos a partir desses resultados.

## Tese orientadora e próximos dados

Não tratar “toda neurodivergência é HA prejudicada por hábitos” como fato. Manter
separadas as hipóteses: capacidades elevadas encobertas em alguns subgrupos,
contexto modificando expressão, e a versão universal que pode ser contrariada.
Antes de testar, definir medida independente de HA, critérios, normas por idade,
prejuízo/forças, tratamentos e grupo de comparação. O NHANES atual não identifica
essas dimensões. Crianças, adultos e idosos exigem normas e bases elegíveis próprias.

## Comandos de retomada

Da raiz do projeto:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/run_analysis.py
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python -m unittest discover -s tests -v
PIPENV_VENV_IN_PROJECT=1 pipenv run python scripts/build_discovery_site.py --output /tmp/science-next-site --update-readmes
```

Antes de publicar, validar YAML/JSON e executar o validador das skills. Conferir
links internos em todas as páginas e verificar o workflow do GitHub Pages; não
anunciar o deploy sem consultar a execução real.

## Estado Git a preservar

O workspace tem uma alteração local de `.obsidian/workspace.json` que não pertence
ao estudo. Não incluí-la automaticamente em commits. O próximo commit deve incluir
somente os arquivos da correção/adendo, análise e publicação efetivamente revisados.
