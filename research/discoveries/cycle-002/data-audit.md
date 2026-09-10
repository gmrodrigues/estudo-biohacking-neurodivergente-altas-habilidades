# Auditoria de seleção, pesos e variância — ciclo 002

[Protocolo local](protocol.md) · [Agregados e proveniência](results.json)

## Mapa de mensuração

SEQN: chave individual dentro da mesma onda; não publicado neste relatório. H1 usa DR1TCAFF/100 → SLD012, com energia, idade/idade², sexo registrado, raça/etnia, escolaridade e PIR. H2 usa SLEEP_CAT e PAD680/60 → soma DPQ sem DPQ030. H3 usa DR1TMAGN/100, DSQTMAGN/100 e indicador de ausência → SLD012, com os mesmos ajustes de H1. Exposições continuam transversais e com janelas diferentes. Campos originais, motivos de exclusão e pesos estão nas tabelas abaixo.

## Escopo e registro

Auditoria pós-resultados do ciclo 001 corrigido, registrada localmente em 2026-09-09 antes da execução desta rodada. Usa os mesmos seis XPT, participantes e especificações. Não é replicação, nova evidência de eficácia ou validação em outra população.

Foram reproduzidas as chaves dos participantes analíticos e todas as estimativas do ciclo anterior. Os hashes dos insumos permanecem iguais. O pacote svy 0.28.0 foi instalado como dependência de desenvolvimento pelo Pipenv; o lock registra suas dependências.

## Cobertura e seleção

DEMO contém 11.933 pessoas, sendo 8.153 com idade ≥18. As ligações necessárias a cada pergunta deixam 6.337 adultos. A tabela usa este último denominador: as retenções não representam participação no inquérito ou na população inteira.

Os 273 participantes de 18–19 anos nas junções têm DMDEDUC2 ausente por elegibilidade da variável (20+). Portanto, a amostra final 20–80 não inclui os mais jovens do protocolo 18+. Ausência estrutural não é recusa. A idade máxima também é truncada na divulgação.

A renda/PIR falta em 831 dos 6.337 adultos. H1/H3 têm 1.351 recordatórios indisponíveis e pesos dietéticos zero. Essas perdas se sobrepõem: contagens marginais não podem ser somadas. Atribuições sequenciais dependem da ordem dos filtros e não revelam causas clínicas de ausência.

| Modelo | Após junções | Analisados | Retenção | Excluídos após junções |
|---|---|---|---|---|
| H1 | 6.337 | 4.211 | 66,45% | 2.126 |
| H2 | 6.337 | 4.522 | 71,36% | 1.815 |
| H3 | 6.337 | 4.194 | 66,18% | 2.143 |

## Desigualdade dos pesos

Kish = (soma dos pesos)²/soma dos pesos² descreve apenas a desigualdade de ponderação. Não incorpora clusters, estratificação, desfecho ou covariáveis e não deve ser interpretado como tamanho efetivo completo da regressão.

Não foram truncados, recalibrados ou substituídos pesos. As somas após seleção não recuperam automaticamente a população-alvo: o ajuste original de não resposta do inquérito não elimina seleção adicional por casos completos.

| Modelo | Peso | N | Kish | CV | Fração dos pesos no 1% maior |
|---|---|---|---|---|---|
| H1 | WTDRD1 | 4.211 | 2460,2 | 0,844 | 5,45% |
| H2 | WTMEC2YR | 4.522 | 2957,1 | 0,727 | 4,39% |
| H3 | WTDRD1 | 4.194 | 2450,7 | 0,843 | 5,36% |

## Variância: comparação independente executada

A matriz de covariáveis foi compartilhada para isolar o cálculo estatístico. Em svy, o desenho foi definido com todos os registros de peso positivo, estrato e PSU antes de selecionar o domínio de casos completos com where. Foi usada aproximação com reposição, sem correção de população finita.

Todos os 15 estratos e 30 PSUs do desenho têm participantes nas três amostras analíticas. Nesse caso concreto, o cálculo Taylor anterior coincide numericamente com o cálculo que preserva o desenho completo. Isso não autoriza reutilizar a rotina anterior em domínios que esvaziem PSUs: ela ignora estratos com menos de duas PSUs observadas.

A comparação verifica cada coeficiente e seu erro-padrão, não a matriz completa de covariância ou testes conjuntos. Não valida mensuração, escolha de confundidores, seleção de casos completos, causalidade ou transporte para HA/autismo/TDAH.

| Modelo | N no desenho completo | Colunas/rank da matriz | Maior diferença absoluta: coeficiente | Maior diferença relativa: erro-padrão |
|---|---|---|---|---|
| H1 | 6.754 | 17/17 | 5e-13 | 4.64e-14 |
| H2 | 8.860 | 17/17 | 1.13e-13 | 5.48e-14 |
| H3 | 6.754 | 18/18 | 2.16e-13 | 1.73e-13 |

## Sensibilidade aos graus de liberdade

O ciclo 001 usa t com 15 graus (30 PSUs − 15 estratos). O padrão de svy 0.28.0 subtrai k−1 e aplica piso de 1: max(1, 15−(k−1)). Com k=17 em H1/H2 e k=18 em H3, todos chegam a 1 grau. Esse piso é comportamento do pacote, não demonstração de que 1 seja a escolha correta para estes modelos.

Os coeficientes e erros-padrão são os mesmos, mas p-valores e intervalos dependem da distribuição de referência. A documentação de R survey descreve tanto a convenção residual quanto a opção de usar os graus do desenho; alerta que a primeira pode ser muito conservadora para covariáveis individuais. Não foi executado R nesta rodada.

Recalculando p a partir de svy com 15 graus, reproduzimos o ciclo 001 e a mesma família FDR de oito termos. Com o padrão de 1 grau, nenhum teste tem q<0,05. Essa comparação é sensibilidade à convenção, não oito novas descobertas. Nenhuma das duas saídas substitui silenciosamente a outra; futuras especificações devem justificar complexidade e graus antes dos resultados.

| Modelo/termo | p: 15 graus | p: svy padrão (1) | q: 15 graus | q: svy padrão (1) |
|---|---|---|---|---|
| H1 / CAFF100 | 0.00362143 | 0.179938 | 0.00724286 | 0.359875 |
| H1 / CAFF_X_AGE | 0.0352676 | 0.259702 | 0.0564281 | 0.415523 |
| H2 / C(SLEEP_CAT)[T.short] | 2.72277e-05 | 0.106218 | 0.000108911 | 0.359875 |
| H2 / C(SLEEP_CAT)[T.long] | 0.00126081 | 0.157518 | 0.00336216 | 0.359875 |
| H2 / SED_HOURS | 6.50067e-07 | 0.0774049 | 5.20054e-06 | 0.359875 |
| H3 / DIET_MAG100 | 0.463415 | 0.589329 | 0.463415 | 0.589329 |
| H3 / SUPP_MAG100 | 0.394445 | 0.541747 | 0.463415 | 0.589329 |
| H3 / SUPP_MAG_UNQUANT | 0.426915 | 0.56404 | 0.463415 | 0.589329 |

## Magnésio: limites da ausência registrada

Na amostra H3, 1.401 pessoas declaram uso de algum suplemento, mas DSQTMAGN está ausente. Isso não comprova que tomaram magnésio com dose desconhecida: pode envolver produto sem magnésio ou incompletude da composição. O nome operacional SUPP_MAG_UNQUANT do ciclo anterior não resolve essa ambiguidade.

Há 28 pessoas com DSD010=2 e magnésio quantificado; suplementos e antiácidos têm indicadores distintos. Não concluir inconsistência nem zerar automaticamente esses valores. A recodificação e a distinção entre não exposição e quantidade desconhecida exigem detalhamento de produtos/antiácidos em uma próxima auditoria.

O ciclo 001 permanece numericamente preservado. H3 é estimável com limites de mensuração; essa checagem não confirma forma química, uso de magnésio por todos os usuários de suplemento, ou indicação clínica.

| Categoria observada em H3 | N |
|---|---|
| use_yes_mag_missing | 1401 |
| use_no_mag_missing | 1445 |
| use_no_mag_reported | 28 |
| mag_reported | 1348 |

## Conferência de leitura e códigos

Foram conferidos totais do codebook DSQTOT_L: 3.762 usuários, 2.969 não usuários, 1.613 valores presentes de magnésio e 2.106 pesos WTDRD1 zero. Os 2.106 zeros de peso estavam representados como floats SAS diminutos e foram normalizados pela regra existente. Essa checagem cobre esses campos, não todos os zeros de todos os componentes.

## Decisão e próximos testes

H1, H2 e H3: estimable_with_limits para associações na amostra de casos completos, com estimadores e erros-padrão conferidos. A robustez da inferência depende da escolha de graus, da seleção e da mensuração. Os grupos HA, autismo e TDAH continuam not_assessed.

Estado na data desta auditoria: definir complexidade e graus de liberdade antes de novas especificações; auditar composição de suplementos/antiácidos e códigos de ausência; avaliar seleção/dados ausentes; só então registrar formas não lineares e validação por PSU/onda. Não executar uma busca de especificações que produzam significância.

Atualização posterior: o ciclo 003 auditou produtos e antiácidos; o ciclo 004 registrou 15 graus do desenho como convenção principal segundo o NCHS e testou reponderação pela seleção observável. As pendências atuais são a nova especificação de H3, seleção não observada, formas não lineares e validação independente.

## H1 — perdas sequenciais (ordem explícita)

| Etapa | Excluídos nesta etapa | Restantes |
|---|---|---|
| DEMO todos | 0 | 11933 |
| idade ≥18 | 3780 | 8153 |
| ligação DR1TOT_L | 1816 | 6337 |
| ligação SLQ_L | 0 | 6337 |
| RIAGENDR | 0 | 6337 |
| RIDRETH3 | 0 | 6337 |
| DMDEDUC2 | 277 | 6060 |
| INDFMPIR | 791 | 5269 |
| SLD012 | 51 | 5218 |
| DR1TKCAL | 1007 | 4211 |
| DR1TCAFF | 0 | 4211 |
| WTDRD1 | 0 | 4211 |
| SDMVSTRA | 0 | 4211 |
| SDMVPSU | 0 | 4211 |

## H1 — ausência marginal sobreposta

Denominador de cada linha: 6.337 adultos após junções. Valores inválidos são códigos observados, sem inferir sua causa além do codebook.

| Campo | Ausente bruto | Código inválido/peso zero | Valores inválidos: contagem | Total não utilizável |
|---|---|---|---|---|
| RIAGENDR | 0 | 0 | {} | 0 |
| RIDRETH3 | 0 | 0 | {} | 0 |
| DMDEDUC2 | 273 | 4 | {'9.0': 4} | 277 |
| INDFMPIR | 831 | 0 | {} | 831 |
| SLD012 | 65 | 0 | {} | 65 |
| DR1TKCAL | 1351 | 0 | {} | 1351 |
| DR1TCAFF | 1351 | 0 | {} | 1351 |
| WTDRD1 | 0 | 1351 | {'0.0': 1351} | 1351 |
| SDMVSTRA | 0 | 0 | {} | 0 |
| SDMVPSU | 0 | 0 | {} | 0 |

## H1 — cobertura por estrato/PSU

| Estrato | PSU | Peso positivo (todas idades) | Adultos ligados com peso positivo | Retidos |
|---|---|---|---|---|
| 173 | 1 | 257 | 187 | 162 |
| 173 | 2 | 248 | 197 | 168 |
| 174 | 1 | 186 | 138 | 104 |
| 174 | 2 | 243 | 173 | 152 |
| 175 | 1 | 260 | 193 | 167 |
| 175 | 2 | 211 | 171 | 156 |
| 176 | 1 | 258 | 166 | 136 |
| 176 | 2 | 144 | 118 | 85 |
| 177 | 1 | 332 | 261 | 230 |
| 177 | 2 | 175 | 139 | 126 |
| 178 | 1 | 264 | 186 | 154 |
| 178 | 2 | 219 | 159 | 137 |
| 179 | 1 | 292 | 217 | 196 |
| 179 | 2 | 177 | 131 | 112 |
| 180 | 1 | 242 | 199 | 158 |
| 180 | 2 | 223 | 161 | 125 |
| 181 | 1 | 270 | 201 | 163 |
| 181 | 2 | 194 | 160 | 131 |
| 182 | 1 | 204 | 147 | 130 |
| 182 | 2 | 251 | 172 | 126 |
| 183 | 1 | 195 | 136 | 122 |
| 183 | 2 | 197 | 145 | 118 |
| 184 | 1 | 290 | 227 | 197 |
| 184 | 2 | 260 | 166 | 132 |
| 185 | 1 | 213 | 163 | 141 |
| 185 | 2 | 219 | 161 | 140 |
| 186 | 1 | 167 | 114 | 102 |
| 186 | 2 | 205 | 161 | 130 |
| 187 | 1 | 154 | 88 | 81 |
| 187 | 2 | 204 | 149 | 130 |

## H2 — perdas sequenciais (ordem explícita)

| Etapa | Excluídos nesta etapa | Restantes |
|---|---|---|
| DEMO todos | 0 | 11933 |
| idade ≥18 | 3780 | 8153 |
| ligação SLQ_L | 0 | 8153 |
| ligação PAQ_L | 0 | 8153 |
| ligação DPQ_L | 1816 | 6337 |
| RIAGENDR | 0 | 6337 |
| RIDRETH3 | 0 | 6337 |
| DMDEDUC2 | 277 | 6060 |
| INDFMPIR | 791 | 5269 |
| SLD012 | 51 | 5218 |
| PAD680 | 25 | 5193 |
| DPQ010 | 642 | 4551 |
| DPQ020 | 10 | 4541 |
| DPQ040 | 6 | 4535 |
| DPQ050 | 1 | 4534 |
| DPQ060 | 4 | 4530 |
| DPQ070 | 1 | 4529 |
| DPQ080 | 6 | 4523 |
| DPQ090 | 1 | 4522 |
| WTMEC2YR | 0 | 4522 |
| SDMVSTRA | 0 | 4522 |
| SDMVPSU | 0 | 4522 |

## H2 — ausência marginal sobreposta

Denominador de cada linha: 6.337 adultos após junções. Valores inválidos são códigos observados, sem inferir sua causa além do codebook.

| Campo | Ausente bruto | Código inválido/peso zero | Valores inválidos: contagem | Total não utilizável |
|---|---|---|---|---|
| RIAGENDR | 0 | 0 | {} | 0 |
| RIDRETH3 | 0 | 0 | {} | 0 |
| DMDEDUC2 | 273 | 4 | {'9.0': 4} | 277 |
| INDFMPIR | 831 | 0 | {} | 831 |
| SLD012 | 65 | 0 | {} | 65 |
| PAD680 | 6 | 41 | {'9999.0': 39, '7777.0': 2} | 47 |
| DPQ010 | 818 | 21 | {'9.0': 16, '7.0': 5} | 839 |
| DPQ020 | 819 | 10 | {'9.0': 7, '7.0': 3} | 829 |
| DPQ040 | 823 | 8 | {'9.0': 5, '7.0': 3} | 831 |
| DPQ050 | 824 | 3 | {'9.0': 3} | 827 |
| DPQ060 | 827 | 5 | {'7.0': 3, '9.0': 2} | 832 |
| DPQ070 | 829 | 3 | {'7.0': 2, '9.0': 1} | 832 |
| DPQ080 | 829 | 12 | {'9.0': 8, '7.0': 4} | 841 |
| DPQ090 | 831 | 5 | {'9.0': 5} | 836 |
| WTMEC2YR | 0 | 0 | {} | 0 |
| SDMVSTRA | 0 | 0 | {} | 0 |
| SDMVPSU | 0 | 0 | {} | 0 |

## H2 — cobertura por estrato/PSU

| Estrato | PSU | Peso positivo (todas idades) | Adultos ligados com peso positivo | Retidos |
|---|---|---|---|---|
| 173 | 1 | 313 | 228 | 180 |
| 173 | 2 | 326 | 253 | 184 |
| 174 | 1 | 222 | 159 | 109 |
| 174 | 2 | 370 | 250 | 169 |
| 175 | 1 | 359 | 256 | 185 |
| 175 | 2 | 279 | 229 | 161 |
| 176 | 1 | 310 | 195 | 141 |
| 176 | 2 | 229 | 174 | 104 |
| 177 | 1 | 410 | 312 | 240 |
| 177 | 2 | 236 | 174 | 147 |
| 178 | 1 | 316 | 225 | 174 |
| 178 | 2 | 297 | 209 | 163 |
| 179 | 1 | 400 | 274 | 219 |
| 179 | 2 | 242 | 168 | 112 |
| 180 | 1 | 308 | 248 | 170 |
| 180 | 2 | 309 | 215 | 130 |
| 181 | 1 | 334 | 239 | 174 |
| 181 | 2 | 242 | 199 | 130 |
| 182 | 1 | 252 | 171 | 126 |
| 182 | 2 | 327 | 221 | 142 |
| 183 | 1 | 235 | 164 | 125 |
| 183 | 2 | 270 | 194 | 116 |
| 184 | 1 | 353 | 270 | 207 |
| 184 | 2 | 329 | 206 | 123 |
| 185 | 1 | 294 | 207 | 154 |
| 185 | 2 | 268 | 191 | 134 |
| 186 | 1 | 228 | 155 | 120 |
| 186 | 2 | 270 | 206 | 149 |
| 187 | 1 | 206 | 120 | 84 |
| 187 | 2 | 326 | 225 | 150 |

## H3 — perdas sequenciais (ordem explícita)

| Etapa | Excluídos nesta etapa | Restantes |
|---|---|---|
| DEMO todos | 0 | 11933 |
| idade ≥18 | 3780 | 8153 |
| ligação DR1TOT_L | 1816 | 6337 |
| ligação DSQTOT_L | 0 | 6337 |
| ligação SLQ_L | 0 | 6337 |
| RIAGENDR | 0 | 6337 |
| RIDRETH3 | 0 | 6337 |
| DMDEDUC2 | 277 | 6060 |
| INDFMPIR | 791 | 5269 |
| SLD012 | 51 | 5218 |
| DR1TKCAL | 1007 | 4211 |
| DR1TMAGN | 0 | 4211 |
| DSD010 | 17 | 4194 |
| WTDRD1 | 0 | 4194 |
| SDMVSTRA | 0 | 4194 |
| SDMVPSU | 0 | 4194 |

## H3 — ausência marginal sobreposta

Denominador de cada linha: 6.337 adultos após junções. Valores inválidos são códigos observados, sem inferir sua causa além do codebook.

| Campo | Ausente bruto | Código inválido/peso zero | Valores inválidos: contagem | Total não utilizável |
|---|---|---|---|---|
| RIAGENDR | 0 | 0 | {} | 0 |
| RIDRETH3 | 0 | 0 | {} | 0 |
| DMDEDUC2 | 273 | 4 | {'9.0': 4} | 277 |
| INDFMPIR | 831 | 0 | {} | 831 |
| SLD012 | 65 | 0 | {} | 65 |
| DR1TKCAL | 1351 | 0 | {} | 1351 |
| DR1TMAGN | 1351 | 0 | {} | 1351 |
| DSD010 | 1357 | 14 | {'7.0': 10, '9.0': 4} | 1371 |
| WTDRD1 | 0 | 1351 | {'0.0': 1351} | 1351 |
| SDMVSTRA | 0 | 0 | {} | 0 |
| SDMVPSU | 0 | 0 | {} | 0 |

## H3 — cobertura por estrato/PSU

| Estrato | PSU | Peso positivo (todas idades) | Adultos ligados com peso positivo | Retidos |
|---|---|---|---|---|
| 173 | 1 | 257 | 187 | 162 |
| 173 | 2 | 248 | 197 | 168 |
| 174 | 1 | 186 | 138 | 104 |
| 174 | 2 | 243 | 173 | 152 |
| 175 | 1 | 260 | 193 | 167 |
| 175 | 2 | 211 | 171 | 156 |
| 176 | 1 | 258 | 166 | 135 |
| 176 | 2 | 144 | 118 | 85 |
| 177 | 1 | 332 | 261 | 230 |
| 177 | 2 | 175 | 139 | 125 |
| 178 | 1 | 264 | 186 | 154 |
| 178 | 2 | 219 | 159 | 137 |
| 179 | 1 | 292 | 217 | 196 |
| 179 | 2 | 177 | 131 | 111 |
| 180 | 1 | 242 | 199 | 158 |
| 180 | 2 | 223 | 161 | 125 |
| 181 | 1 | 270 | 201 | 162 |
| 181 | 2 | 194 | 160 | 130 |
| 182 | 1 | 204 | 147 | 130 |
| 182 | 2 | 251 | 172 | 124 |
| 183 | 1 | 195 | 136 | 121 |
| 183 | 2 | 197 | 145 | 118 |
| 184 | 1 | 290 | 227 | 196 |
| 184 | 2 | 260 | 166 | 130 |
| 185 | 1 | 213 | 163 | 141 |
| 185 | 2 | 219 | 161 | 139 |
| 186 | 1 | 167 | 114 | 102 |
| 186 | 2 | 205 | 161 | 127 |
| 187 | 1 | 154 | 88 | 80 |
| 187 | 2 | 204 | 149 | 129 |

## Fontes

- [CDC: variância e subpopulações NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx)
- [CDC: ponderação NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx)
- [DEMO_L: escolaridade de adultos 20+](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm)
- [DSQTOT_L: suplementos e antiácidos](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm)
- [svy: regressão e análise de domínio](https://svylab.com/docs/svy/tutorials/glm.html)
- [R survey: convenções de graus de liberdade](https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svyglm.html)

## Reprodução

```bash
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-002/run_audit.py
PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-002/render_audit.py
```
