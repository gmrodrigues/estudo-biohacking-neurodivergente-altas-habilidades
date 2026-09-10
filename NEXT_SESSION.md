# Retomada da próxima sessão

Estado atualizado em 2026-09-10. Os ciclos 001–004, o artigo comparativo e o
portal foram enviados ao remoto. O último marco é `fcfb14e`; a página
“Ciclos e hipóteses” deve ser conferida após cada deploy porque seu roteiro é
editorial e pode ficar defasado mesmo quando os artefatos do ciclo estão corretos:

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

## Correção H2 concluída e enviada em 2026-09-09

O [adendo](research/discoveries/cycle-001/amendments/h2-boundary-2026-09-09/protocol.md)
foi registrado antes da reexecução corrigida, após conhecimento dos resultados
originais. A convenção registrada foi aplicada: `<7 h`, `7–9 h inclusive`, `>9 h`.
Exatamente 686 pessoas com 7 h passaram à referência; n=4.522 preservado.

- Curto: +1,120 ponto, IC95% +0,718 a +1,521; q=0,00010891.
- Longo: +1,214 ponto, IC95% +0,561 a +1,868; q=0,00336216.
- Sedentarismo: +0,1178 ponto/hora, IC95% +0,0871 a +0,1485; q=0,00000520.

O alvo é o **escore de sintomas sem sono (0–24)**; o identificador interno
legado `PHQ8_NOSLEEP` não denota o PHQ-8 convencional. A
[auditoria comparativa](research/discoveries/cycle-001/amendments/h2-boundary-2026-09-09/audit.md)
preserva coeficientes, IC, p e q anteriores e corrigidos dos oito termos.
H1, sua sensibilidade, H3, previsão e hashes de insumos reproduziram exatamente
os resultados originais. Só os três q-valores de H2 mudaram. `results-original.json`
preserva o agregado anterior; código e figuras anteriores estão no commit
`3a4eec48a45e1d29ac670663ae4187cbe9a2e087` e ancestrais.

A correção, código, figura, manifesto, dossiê, artigo e planejamento foram
enviados no commit `321408f` e posteriormente complementados pelo ciclo 004.
A correção não constitui replicação nem validação externa da variância.
Validação: 12 testes passaram; seis skills válidas; JSON/YAML parseados; sete
páginas e 50 links locais verificados. PNGs conferidos visualmente. Build em
`/tmp/science-h2-reviewed-20260909`; navegador integrado indisponível, então a
conferência visual de páginas largas/estreitas permanece pendente.

## Ciclo 002 concluído e enviado em 2026-09-09

[Auditoria completa](research/discoveries/cycle-002/data-audit.md),
[protocolo](research/discoveries/cycle-002/protocol.md) e
[agregados](research/discoveries/cycle-002/results.json).

- Reproduzidos participantes e estimativas H1/H2/H3. Retenção pós-junções:
  66,45%, 71,36%, 66,18%. Os 273 adultos 18–19 não têm escolaridade 20+.
- Kish: 2.460,2 / 2.957,1 / 2.450,7; apenas desigualdade dos pesos.
- svy 0.28.0 no desenho completo reproduz coeficientes e erros-padrão
  (diferenças relativas de SE <2e-13). Todas as 30 PSUs continuam representadas.
- **Inferência exige cuidado:** o ciclo 001 usa 15 graus do desenho; svy aplica
  max(1, 15−(k−1)), resultando em 1 para k=17/17/18. Com o padrão svy nenhum
  q<0,05; com 15 graus os testes anteriores são reproduzidos. Não escolher
  convenção por significância. O piso de 1 é comportamento do pacote, não uma
  conclusão de que seja a escolha correta. R não foi executado.
- Em H3, 1.401 usuários de algum suplemento têm DSQTMAGN ausente. O ciclo 003
  auditou a composição e mostrou que o indicador não significa magnésio com
  dose desconhecida.
- Pipfile/lock acrescentam svy como dependência de desenvolvimento; pacotes
  analíticos existentes mantiveram versões. 13 testes passaram, incluindo
  fixture analítica em que um domínio esvazia uma PSU.

Relatório, gráficos, manifesto e planejamento foram enviados no commit `321408f`.
O ciclo 004 adicionou uma atualização posterior da convenção de inferência e da
seleção observável.

## Ciclo 003 concluído e enviado em 2026-09-09

[Auditoria por produto](research/discoveries/cycle-003/data-audit.md),
[protocolo](research/discoveries/cycle-003/protocol.md) e
[agregados](research/discoveries/cycle-003/results.json).

- DSQIDS_L contém 11.375 ocorrências de 4.017 participantes; 11.210 ligaram a
  DSPI/DSII e 165 ficaram sem produto correspondente.
- Na amostra H3 (n=4.194), há 1.348 pessoas com magnésio quantificado, 1.522 com
  produtos sem magnésio identificado, 47 com produto sem correspondência, 6
  com rótulo de magnésio e total ausente, e 1.271 sem registro liberado.
- O indicador legado marca 1.401 usuários de qualquer suplemento com total
  ausente; somente 6 têm evidência de produto rotulado com magnésio e cálculo
  ausente. Nome e interpretação públicos do ciclo 001 foram corrigidos.
- Os 28 casos com DSD010=2 e magnésio quantificado têm antiácido. Em 1.613 de
  1.613 participantes, DSQIMAGN × dias/30 reconstrói DSQTMAGN a até 0,05 mg.
- Não houve imputação, novo modelo de sono, conclusão causal ou recomendação.

## Ciclo 004 concluído e enviado em 2026-09-10

[Auditoria de inferência e seleção](research/discoveries/cycle-004/data-audit.md),
[protocolo](research/discoveries/cycle-004/protocol.md),
[hipótese registrada](research/discoveries/cycle-004/hypothesis.yaml) e
[agregados](research/discoveries/cycle-004/results.json).

- A convenção principal foi fixada em 15 graus do desenho, conforme o NCHS:
  30 PSUs menos 15 estratos. O padrão residual de 1 grau permanece sensibilidade
  conservadora; nenhum termo foi retirado ou selecionado por significância.
- O denominador elegível foi refinado para 20–80 anos, peso do componente
  positivo e desenho observado. Retenção: H1 87,8%, H2 74,6%, H3 87,4%.
- A reponderação por probabilidade observável de caso completo reduziu o maior
  desequilíbrio padronizado de 0,026/0,084/0,027 para menos de 0,003.
- H1/H2 mudaram no máximo 3,3% em magnitude. H3 teve mudanças absolutas pequenas
  e continuou inconclusiva. A interação cafeína×idade ficou em q=0,05088.
- A análise não corrige seleção não observada e trata as propensões estimadas
  como fixas nos intervalos.

## Próxima rodada: fundação analítica ABCD

A prioridade deixou de ser estimar mais associações em NHANES. Antes de qualquer
modelo de efeito, montar a base analítica participante-onda e executar as quatro
provas de conceito descritas em
[`catalog/data-sources/ANALYTIC_FOUNDATION.md`](catalog/data-sources/ANALYTIC_FOUNDATION.md).
O [primeiro ciclo ABCD](catalog/data-sources/ABCD_FIRST_CYCLE.md) define a
pergunta longitudinal mínima. Sem acesso legítimo aos microdados, a saída correta
é terminar o dossiê de acesso/metadados e manter `blocked_by_access`.

## Linha NHANES legada

Consulte primeiro o [mapa de estado e desatualização](research/discoveries/STATUS_AND_STALENESS_MAP.md): ele relaciona cada pendência aos documentos que precisam ser sincronizados depois de uma execução.

1. Registrar um adendo antes de modificar H3, separando zero sustentado,
   quantidade calculada, produto não identificado, cálculo ausente e antiácido.
2. Registrar formas não lineares sem reutilizar os resultados para escolher nós
   ou termos; manter a família de testes explícita.
3. Avaliar seleção não observada e incorporar incerteza dos pesos de resposta.
4. Validar previsão por PSU/onda com intervalos; não reutilizar o holdout para
   selecionar especificações. Grupos diagnósticos continuam not_assessed.

Reprodução da auditoria:

```bash
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-002/run_audit.py
PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-002/render_audit.py
```

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
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/audit_h2_amendment.py
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/run_audit.py
PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/render_audit.py
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/run_analysis.py
PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/render_analysis.py
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
