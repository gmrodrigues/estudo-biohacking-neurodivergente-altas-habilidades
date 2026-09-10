# Ciclo 004 — inferência e seleção por casos completos

Registro local de 2026-09-10, antes da execução desta sensibilidade. Os resultados
dos ciclos 001–003 são conhecidos. Esta rodada não é pré-registro externo nem
replicação independente.

## Perguntas

1. Qual convenção de graus de liberdade deve reger os oito contrastes principais?
2. Quanto da perda antes dos modelos decorre da população/componente elegível e
   quanto decorre de casos incompletos dentro dela?
3. Os coeficientes principais mudam materialmente quando os casos completos são
   reponderados pela probabilidade observável de inclusão?

## Decisões anteriores aos novos resultados

- A inferência principal usa graus do desenho: número de PSUs representados menos
  número de estratos representados. Com 30 PSUs e 15 estratos, são 15 graus.
  Esta é a definição do tutorial NHANES/NCHS. Intervalos usam t com esses graus.
- O padrão residual de `svy`, que subtrai o número de parâmetros e chega ao piso
  de 1 grau, permanece sensibilidade. A documentação do pacote `survey` informa
  que essa regra pode ser muito conservadora para covariáveis individuais.
- Os oito contrastes e a correção Benjamini–Hochberg permanecem congelados. Não
  se retiram ajustes nem se acrescentam termos para procurar significância.
- A população elegível para esta sensibilidade é 20–80 anos, após as junções da
  hipótese, com peso positivo do componente e desenho observado. Pessoas de
  18–19 anos não entram porque `DMDEDUC2` é destinada a adultos de 20 anos ou mais.
- Em cada população elegível, modela-se a probabilidade de ser caso completo com
  idade linear/quadrática, sexo, raça/etnia e estrato. O ajuste logístico usa o
  peso NHANES normalizado. Essas são variáveis observadas antes da exclusão.
- O peso de sensibilidade é peso NHANES × inverso da probabilidade estimada de
  caso completo. A análise principal desta rodada usa o inverso sem truncamento;
  uma sensibilidade o limita no percentil 99 entre casos completos.
- A variância Taylor trata os pesos de resposta estimados como fixos. Portanto,
  os intervalos não incorporam incerteza da estimação da propensão.

## Critérios de interpretação

Será relatada a mudança absoluta e relativa de cada coeficiente, sem transformar
um limiar de significância em critério de robustez. Mudança relativa é apenas
descritiva e fica indefinida quando o coeficiente de referência é zero.

O diagnóstico de seleção observável inclui distribuição das propensões, Kish dos
pesos combinados e maior diferença padronizada de idade/sexo/raça antes e depois
da reponderação. Estabilidade não elimina viés por variáveis não observadas nem
recupera exposições ou desfechos ausentes.

HA, autismo e TDAH permanecem `not_assessed`. A rodada não estima causalidade,
efeito de intervenção, dose individual, não linearidade ou validação externa.

## Fontes metodológicas

- [CDC/NCHS: variância, subpopulações e graus de liberdade](https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx)
- [CDC/NCHS: dicas de software e preservação do desenho](https://wwwn.cdc.gov/nchs/nhanes/tutorials/softwaretips.aspx)
- [R survey: `svyglm` e graus residuais](https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svyglm.html)
