# Auditoria de magnésio por produto e antiácido — ciclo 003

[Protocolo local](protocol.md) · [Agregados e hashes](results.json)

## Pergunta e alcance

Esta auditoria pós-resultados pergunta o que DSQTMAGN ausente representa na amostra H3. Liga registros participante-produto de 2021–2023 à base de rótulos 1999–2023 por DSDPID. Não ajusta modelo de sono, não testa eficácia e não é replicação.

Os resultados públicos são agregados. Nomes de produtos associados a participantes e SEQN não são publicados.

## Cardinalidade e cobertura das ligações

DSQIDS_L tem 11.375 ocorrências relatadas por 4.017 participantes e 3.417 produtos distintos. Ocorrências repetidas foram preservadas porque podem representar recipientes, formulações ou doses distintas.

DSPI contém uma linha por DSDPID. Das ocorrências, 11.210 ligam a DSPI e DSII; 165 não têm produto/ingredientes correspondentes, coerente com registros sem correspondência ou identificação suficiente.

| Checagem | Resultado |
|---|---|
| DSPI_unique_DSDPID | True |
| DSQIDS_rows | 11375 |
| DSQIDS_participants | 4017 |
| DSQIDS_unique_products | 3417 |
| product_match_rows | 11210 |
| product_unmatched_rows | 165 |
| ingredient_match_rows | 11210 |

## Estados de magnésio na amostra H3

DSQTMAGN ausente não é um único estado. Entre 4.194 participantes, 1.348 têm magnésio quantificado; 1.522 possuem produtos liberados sem magnésio identificado; 47 têm produto sem correspondência suficiente; 1.271 não têm registro de produto liberado; apenas 6 têm rótulo com magnésio e total ausente.

O indicador legado SUPP_MAG_UNQUANT vale 1 para 1.401 usuários de algum suplemento com DSQTMAGN ausente. Ele não identifica dose de magnésio desconhecida: mistura sobretudo ausência de magnésio identificado com poucos casos de cálculo incompleto.

| Estado operacional auditado | N |
|---|---|
| Magnésio quantificado | 1348 |
| Produtos relatados, sem magnésio identificado | 1522 |
| Produto sem correspondência; magnésio não identificado | 47 |
| Rótulo com magnésio, total ausente | 6 |
| Sem produto liberado | 1271 |

## Antiácidos explicam DSD010=2 com magnésio

Os 28 participantes de H3 com DSD010=2 e DSQTMAGN presente possuem registro de antiácido. O codebook define DSD010=2 para quem não tomou suplemento, mesmo que tenha antiácido contendo cálcio ou magnésio registrado apenas na seção de antiácidos.

Portanto, esses valores não são inconsistências nem devem ser zerados. DSQTMAGN agrega suplementos e antiácidos; DSD010 descreve uso de suplemento segundo a regra editada pelo NCHS.

## Reconstrução do total

Para todos os 1.613 participantes com total e componentes presentes no arquivo completo, a soma de DSQIMAGN × dias/30 ficou a no máximo 0,05 mg de DSQTMAGN. A diferença é compatível com a resolução de uma casa decimal do total. Isso valida a ligação e a regra de frequência, mas não prova ingestão ou composição real.

| Checagem | Valor |
|---|---|
| both_present_n | 1613 |
| exact_before_rounding_n | 1249 |
| within_half_of_0_1_unit_n | 1613 |
| max_absolute_difference_before_rounding | 0.05000000000001137 |

## Quatro ocorrências de produto com magnésio sem quantidade individual

Na amostra H3 há quatro ocorrências com ingrediente de magnésio identificado e DSQIMAGN ausente, distribuídas por seis participantes cujo total fica ausente porque outros registros também entram na agregação. Todas têm dias e quantidade válidos e correspondência de produto; uma não tem razão entre porção relatada e porção do rótulo. Nas outras três, a ausência não é explicada pelos campos públicos examinados.

Não se imputou quantidade. Rótulos e nomes de ingredientes não bastam para converter compostos em magnésio elementar sem as regras e unidades específicas.

| Antiácido | Dias válidos | Quantidade válida | Razão de porção presente | Sem correspondência | N |
|---|---|---|---|---|---|
| False | True | True | False | False | 1 |
| False | True | True | True | False | 3 |

## Decisão científica

A exposição quantitativa DSQTMAGN permanece utilizável com limites para magnésio calculado de suplementos e antiácidos. O coeficiente do indicador legado continua sendo uma descrição do modelo executado, mas deve ser nomeado como qualquer suplemento relatado com total de magnésio ausente, sem interpretá-lo como magnésio de dose desconhecida.

Uma nova análise de H3 precisa registrar antes dos efeitos como separar: zero sustentado por produtos sem magnésio; quantidade calculada; produto rotulado com magnésio sem cálculo; produto não identificado; e antiácido. A pequena célula ambígua não sustenta um coeficiente próprio complexo. H3 permanece estimable_with_limits; forma química e biodisponibilidade continuam needs_data.

HA, autismo e TDAH permanecem not_assessed. Nenhuma conclusão orienta dose ou produto individual.

## Fontes

- [CDC DSQIDS_L: produtos, antiácidos, cálculo e cautelas](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQIDS_L.htm)
- [CDC DSQTOT_L: totais de suplementos e antiácidos](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm)
- [CDC NHANES-DSD: informações dos produtos (DSPI)](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSPI.htm)
- [CDC NHANES-DSD: ingredientes (DSII)](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSII.htm)
- [CDC NHANES-DSD: misturas (DSBI)](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSBI.htm)

## Reprodução

```bash
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/run_audit.py
PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-003/render_audit.py
```
