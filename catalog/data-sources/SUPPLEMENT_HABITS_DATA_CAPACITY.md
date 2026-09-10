# Modelo de dados e capacidade amostral para suplementação e hábitos

Revisado em 2026-09-10. A fonte só entra em análise de suplementação quando
registra, para a mesma pessoa, exposição com janela/quantidade interpretável,
desfecho e confundidores. Um grande N de “uso sim/não” não substitui produto,
dose, adesão ou tempo.

## Inventário de fontes

| Fonte | N divulgado ou disponível | Exposição de suplementação | Hábitos e desfechos | Melhor uso | Limite que bloqueia |
|---|---:|---|---|---|---|
| **NHANES 2021–2023** | 4.775 adultos na estimativa oficial de uso de suplemento; 8.860 registros nos arquivos locais de dieta/suplementos; 11.375 relatos de produtos/antiácidos | 30 dias: produto, dias, quantidade habitual, tamanho de porção, ingredientes e totais de 34 componentes; antiácidos separados | Recordatório alimentar de 1 dia, sono habitual, sintomas, demografia e desenho complexo | Associação populacional ponderada entre dieta/suplemento e desfechos medidos; auditoria de produto/dose | Transversal; coleta de suplemento mudou para telefone; não mede adesão real, efeito causal ou HA/TDAH/autismo nesta onda |
| **All of Us** | Mais de 747.000 participantes com dados liberados; 54.509 com atividade Fitbit válida e 34.379 com sono elegível no estudo de wearables citado | Pesquisa de estilo de vida e EHR podem registrar uso/medicação, mas exposição detalhada por produto/dose precisa de auditoria no Workbench | EHR, pesquisas, medidas físicas e Fitbit com sono/atividade longitudinais | Replicação/trajectória de sono e atividade; avaliação de interação com contexto de saúde | Acesso por instituição e acordo; suplementação detalhada não pode ser presumida; usuários de Fitbit são subconjunto selecionado |
| **HBN** | Meta de 10.000; N liberado por versão precisa ser contado | Fenótipos de estilo de vida/dieta, mas produto/dose de suplemento não confirmados nesta triagem | Sono, atividade, actigrafia, cognição e fenótipo psiquiátrico potencialmente no mesmo recurso | Estudos de hábitos e funcionamento em jovens após auditoria de campos | Acesso a fenótipos por DUA; amostra encaminhada; sem campo confirmado não estimar suplemento |
| **NSCH 2024** | 51.375 crianças, pesos nacionais | Não é base de dose/produto de suplemento | Sono, atividade, saúde, tratamento, escola, família e contexto | Contexto populacional de hábitos e diagnósticos relatados | Sem exposição detalhada a suplemento; não usar para hipóteses de dose/composição |
| **UK Biobank** | Cerca de 500.000 participantes no programa; estado de acesso precisa ser confirmado antes de planejar aquisição | Questionários de estilo de vida/dieta e registros de saúde; detalhamento/ondas de suplemento exigem codebook específico | Atividade por acelerometria em subconjunto, sono, saúde e medidas físicas | Futuro estudo adulto de hábitos após acesso e auditoria | Não é fonte aberta imediata; não assumir variável de suplemento comparável a NHANES |
| **ClinicalTrials.gov** | Registros, protocolos e resultados agregados, não uma coorte individual | Intervenção e dose protocoladas quando registradas | Desfechos e eventos adversos agregados conforme estudo | Mapa de ensaios e síntese de intervenção | Não fornece microdados individuais para reanálise; registro não demonstra eficácia |
| **DSLD/DSID** | Produtos, não participantes | Rótulo e, no DSID, conteúdo analisado de categorias | Nenhum desfecho humano individual | Normalizar formulação e checar plausibilidade de exposição | Não mede ingestão, adesão, efeito ou segurança individual |

## Modelo mínimo para uma hipótese de suplemento

| Domínio | Obrigatório | Estados que impedem conclusão |
|---|---|---|
| Produto | Nome/ID, categoria, ingrediente e versão do rótulo ou composição | `product_unknown`, `unmatched_product`, `ingredient_unknown` |
| Dose e tempo | Quantidade por tomada, porção, dias/semana ou janela documentada | `dose_missing`, `days_missing`, `window_incompatible` |
| Fonte concorrente | Dieta, outros suplementos e medicamento/antiácido quando relevante | `double_count_risk`, `source_unmeasured` |
| Desfecho | Medida, unidade, instrumento e janela temporal | `outcome_missing`, `temporal_mismatch` |
| Contexto | Idade, sexo/gênero conforme instrumento, condição, medicação, energia/dieta e contexto | `confounder_missing`, `condition_not_measured` |
| Desenho | Peso/centro/onda, seleção e qualidade | `design_unimplemented`, `selected_subsample` |

## Modelo mínimo para uma hipótese de hábito

Sono, atividade, alimentação e rotina precisam ser tratados como exposições
distintas. Para cada uma, registrar instrumento (relato, actigrafia ou wearable),
janela, dias válidos, sazonalidade, turno de trabalho/escola quando disponível e
medicação. Não converter passo, tempo sedentário ou hora de deitar em “recuperação”
sem medida correspondente.

## Portões de suficiência

1. **Produto/dose:** sem produto e dose/tempo, uma pergunta de suplemento vira no
   máximo associação com uso relatado, não uma comparação de formulações.
2. **Janelas compatíveis:** recordatório de dieta de um dia, suplemento de 30 dias
   e sono habitual não descrevem o mesmo período; a incompatibilidade é limitação
   do estimando, não falha a corrigir por ajuste estatístico.
3. **N por exposição:** publicar número de usuários, não usuários, dose conhecida,
   dose ausente e dados completos antes de modelo. Não assumir que N geral sustenta
   ingrediente raro ou interação com condição.
4. **Seleção de wearable:** contagem de dias válidos, origem do dispositivo e
   características dos participantes são obrigatórias antes de interpretar hábito
   longitudinal.
5. **Causalidade:** estudo transversal ou observacional não recomenda dose nem
   mudança de rotina; ensaio/protocolo longitudinal é uma frente separada.

## Comparação indireta entre grupos e estudos

O programa pode usar uma cadeia de evidência indireta para transformar padrões
observados em hipóteses de intervenção. Ela preserva as bases separadas e evita
atribuir ao suplemento um efeito que foi observado apenas para um hábito.

| Etapa | Pergunta permitida | Dados e análise necessários | Conclusão permitida |
|---|---|---|---|
| 1. Associação dentro da frente | Em TDAH, autismo ou HA/capacidade, qual hábito acompanha sono, funcionamento ou desempenho? | Estudo próprio, medida de hábito e desfecho, ajuste e incerteza registrados | Associação específica à fonte e ao grupo medido |
| 2. Síntese indireta | A direção/magnitude da associação é consistente entre frentes comparáveis? | Mesmo construto, escala/estimando harmonizado ou transformação justificada; heterogeneidade explícita | Prioridade de hipótese compartilhada, não efeito causal comum |
| 3. Mecanismo de hábito | Uma intervenção muda o hábito-alvo de modo sustentado? | Diário, wearable ou medida repetida; adesão, tempo, medicação e eventos adversos | Mudança temporal do hábito na população estudada |
| 4. Suplemento como apoio possível | O suplemento, produto e dose definidos aumentam adesão/consolidação do hábito e melhoram desfecho? | Ensaio, experimento pragmático ou N-of-1 registrado; comparador, randomização quando viável e desfecho prévio | Efeito do protocolo específico, não recomendação geral nem tratamento de condição |

Exemplo de encadeamento: se sono regular se associa a melhor funcionamento em
mais de uma frente, isso prioriza sono como alvo. Só um estudo prospectivo pode
testar se uma rotina, intervenção comportamental ou suplemento específico ajuda
a manter essa regularidade; o estudo deve medir a própria regularidade, adesão e
o desfecho, em vez de inferir consolidação a partir de uma associação transversal.

Cada frente paralela terá o mesmo dicionário para sono, atividade, rotina,
exposição e funcionamento. A síntese compara estimativas e incertezas; nunca
combina pessoas de fontes distintas ou aplica um efeito observado em um grupo a
outro sem teste.

## Decisão de aquisição

1. Manter NHANES como referência aberta de produto/dose e associação populacional,
   com estados de mensuração já auditados para magnésio.
2. Priorizar All of Us, HBN e ABCD apenas quando a auditoria mostrar que a medida
   de hábito/exposição necessária existe na camada acessível e que o N completo
   sustenta o estimando.
3. Usar DSLD/DSID para descrição de produtos, nunca para inferir ingestão humana.
4. Usar ClinicalTrials.gov para localizar intervenções e resultados agregados,
   nunca como microdados de eficácia.

## Fontes verificadas

- [NHANES: suplemento alimentar 2021–2023](https://www.cdc.gov/nchs/products/databriefs/db561.htm)
- [NHANES: arquivos e variáveis de suplemento](https://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Dietary&Cycle=2021-2023)
- [NHANES: documentação DSQTOT](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm)
- [NHANES: notas analíticas DSQIDS](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQIDS_L.htm)
- [All of Us: fontes de dados](https://www.researchallofus.org/data-tools/data-sources/)
- [All of Us: versão e amplitude](https://www.nih.gov/news-events/news-releases/nihs-all-us-research-program-now-largest-integrated-genomics-health-database-world)
- [All of Us: wearable e critérios de atividade](https://doi.org/10.1038/s41591-026-04352-3)
- [HBN: acesso e meta](https://data.healthybrainnetwork.org/)
- [NSCH: amostra e arquivos](https://www.nschdata.org/learn-about-the-nsch/NSCH)
