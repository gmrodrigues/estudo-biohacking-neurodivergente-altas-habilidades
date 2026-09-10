# Inferência e seleção por casos completos — ciclo 004

[Protocolo](protocol.md) · [Hipótese registrada localmente](hypothesis.yaml) · [Resultados](hypothesis-results.md) · [Agregados](results.json)

## Decisão sobre inferência

A inferência principal passa a declarar explicitamente 15 graus do desenho: 30 PSUs representados menos 15 estratos representados. Essa é a definição do NCHS para o NHANES contínuo e coincide com a implementação do ciclo 001.

O grau residual igual a 1 produzido pelo padrão de svy permanece como sensibilidade conservadora. A documentação do pacote survey informa que subtrair os parâmetros é apropriado para covariáveis no nível da PSU, mas pode ser muito conservador para covariáveis individuais. Nenhum modelo foi simplificado e nenhuma covariável foi escolhida por significância.

## População elegível e casos completos

O ciclo 002 usou como denominador 6.337 adultos após junções. Para a sensibilidade de seleção, o denominador foi refinado antes dos efeitos: pessoas de 20–80 anos, com peso positivo do componente e desenho observado. Isso separa inelegibilidade estrutural e ausência coberta pelos pesos de dieta da incompletude restante.

A completude é 87,8% em H1, 74,6% em H2 e 87,4% em H3. As propensões mínimas estimadas ficaram entre 0,392 e 0,599; o maior inverso foi 2,263. Não apareceu uma violação forte de positividade nas variáveis observadas usadas.

| Modelo | Elegíveis | Completos | Retenção | Propensão mín. | 1/p máx. | SMD máx. antes | SMD máx. depois |
|---|---|---|---|---|---|---|---|
| H1 | 4798 | 4211 | 87,8% | 0,599 | 1,670 | 0,026 | 0,001 |
| H2 | 6064 | 4522 | 74,6% | 0,392 | 2,263 | 0,084 | 0,003 |
| H3 | 4798 | 4194 | 87,4% | 0,595 | 1,682 | 0,027 | 0,001 |

## Estabilidade dos oito contrastes

A reponderação pela probabilidade observável de caso completo alterou os coeficientes de H1 e H2 entre 0,7% e 3,3%. Cafeína continua associada a menos sono; sono curto, sono longo e sedentarismo continuam associados a mais sintomas sob 15 graus do desenho.

Os três coeficientes de H3 tiveram mudanças relativas maiores, entre 11,9% e 19,5%, porque suas estimativas de referência são pequenas. As mudanças absolutas foram de 0,0026 a 0,0101 hora, e todos os intervalos continuam incluindo zero. H3 permanece inconclusiva.

A interação cafeína × idade fica em q=0,05088 após reponderação, próxima do limiar e sem mudança substantiva de magnitude. O valor não deve ser transformado em decisão binária de descoberta.

| Modelo | Contraste | Referência | IPW | Mudança | IC95% IPW | q IPW |
|---|---|---|---|---|---|---|
| H1 | Cafeína / 100 mg aos 45 anos | -0,0537 | -0,0531 | 0,0006 | -0,0862 a -0,0200 | 0,00852008 |
| H1 | Cafeína × idade por década | 0,0234 | 0,0237 | 0,0004 | 0,0024 a 0,0451 | 0,05087538 |
| H2 | Sono curto <7 h | 1,1196 | 1,1494 | 0,0298 | 0,7674 a 1,5313 | 0,00004661 |
| H2 | Sono longo >9 h | 1,2145 | 1,2064 | -0,0081 | 0,4420 a 1,9707 | 0,00852008 |
| H2 | Sedentarismo por hora/dia | 0,1178 | 0,1217 | 0,0039 | 0,0934 a 0,1501 | 0,00000127 |
| H3 | Magnésio alimentar / 100 mg | 0,0173 | 0,0198 | 0,0026 | -0,0294 a 0,0690 | 0,40420494 |
| H3 | Magnésio suplementar / 100 mg | 0,0300 | 0,0336 | 0,0036 | -0,0381 a 0,1052 | 0,40232144 |
| H3 | Qualquer suplemento; total de magnésio ausente | 0,0518 | 0,0619 | 0,0101 | -0,0755 a 0,1993 | 0,40232144 |

## O que esta sensibilidade não resolve

A ponderação equilibra somente idade, sexo registrado, raça/etnia e estrato. Ela não corrige seleção por sintomas, renda ou exposições não observadas, não recupera valores ausentes e não incorpora a incerteza de estimar as propensões nos intervalos.

Os dados continuam transversais e com janelas diferentes. Estabilidade sob seleção observável não estabelece causalidade, validade externa ou efeito individual. HA, autismo e TDAH continuam não avaliados.

## Fontes

- [CDC/NCHS: variância, subpopulações e graus de liberdade](https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx)
- [CDC/NCHS: dicas de software para o desenho NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/softwaretips.aspx)
- [R survey: graus residuais em svyglm](https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svyglm.html)

## Reprodução

```bash
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/run_analysis.py
PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-004/render_analysis.py
```
