# Mapa de estado e desatualização do estudo

Data da revisão: 2026-09-10. Este mapa é o controle editorial entre ciclos: não
introduz resultados, não substitui protocolos e deve ser revisado antes de cada
novo commit de ciclo e depois de cada publicação.

## Caminho até as conclusões

O estudo não tem uma conclusão única pronta: há quatro tipos de conclusão, cada
um com uma evidência mínima diferente. Os ciclos 001–004 concluíram a primeira
etapa de fundação; não autorizam saltar diretamente para conclusões clínicas,
causais ou sobre HA, autismo e TDAH.

| Pergunta que pode receber conclusão | Etapa atual | Próxima evidência necessária | Quando a conclusão será permitida | Limite que continuará declarado |
|---|---|---|---|---|
| Há associações populacionais entre cafeína/sono e sono/sintomas? | H1 e H2 executadas e auditadas para erros, graus e seleção observável | Especificação não linear registrada e replicação em dados compatíveis | Após estabilidade da direção/magnitude em análise registrada e replicação; a formulação será "associação" | Transversalidade, causalidade reversa e seleção não observada |
| Magnésio se associa ao sono, e para quem? | H3 inconclusiva; mensuração por produto e antiácido foi auditada | Nova H3 com estados de exposição registrados, cobertura e multiplicidade | Somente se o estimando prévio for estimável e reproduzível; resultado nulo/inconclusivo também encerra a pergunta nesta base | Produto não identificado, dose/tempo e causalidade |
| Um modelo prevê sintomas em pessoas novas sem diagnóstico? | Ridge tem desempenho interno, aproximadamente R² 0,09 | Validação congelada por PSU/onda ou outra onda compatível, calibração e intervalo | Após desempenho fora da amostra que supere a referência na divisão reservada | Previsão não identifica causa, diagnóstico ou tratamento individual |
| HA, autismo e TDAH diferem ou compartilham dimensões? | Não mensurado nesta base; nenhuma comparação foi feita | Coorte com cognição e condições medidas independentemente, critérios e tamanho por combinação | Após auditoria de medida e análise registrada dos grupos; conclusões serão específicas à coorte | Sem inferir HA, NT, autismo ou TDAH por proxies ou ausência de registro |

Assim, a conclusão atual é limitada e verificável: esta rodada estabeleceu quais
associações e previsões são tecnicamente examináveis em adultos NHANES e quais
permanecem inconclusivas ou não mensuradas. A conclusão sobre grupos clínicos ou
HA depende de outra fonte de dados; a conclusão causal depende de desenho que
meça tempo e intervenção, não apenas de mais ajustes no mesmo corte transversal.

## Porta de entrada: fundação analítica antes de comparações

E1 documental iniciada em 2026-09-10: [triagem de adequação das fontes](../../catalog/data-sources/SOURCE_FIT_AUDIT.md).
Atualizar decisões com os dicionários e a cobertura conjunta, ainda não medida.
ABCD/NBDC e seus limites de uso/autismo substituem a suposição de acesso NDA
como caminho atual único. Nenhuma nova POC empírica foi aprovada.

O [plano da fase 1](../../catalog/data-sources/PHASE_1_PLAN.md) detalha E1–E6,
POC-01 a POC-06 e critérios de encerramento. Sua publicação é planejamento;
não representa execução ou aprovação empírica das bases.

Esta fase não começa por uma análise de efeito. Ela começa quando uma fonte
elegível tiver uma base analítica mínima viável: chaves participante-onda,
medidas documentadas, temporalidade, perdas e pequenas provas de conceito. Mais
ciclos NHANES podem aprimorar mensuração nutricional, mas não convertem a base em
coorte de capacidade, TDAH ou autismo.

1. **Fonte e governança:** ABCD é a entrada longitudinal; registrar versão,
   acesso autorizado e estruturas antes de baixar microdados.
2. **Fundação analítica:** auditar chaves, ondas, campo→construto, informantes,
   unidades, ausência, perdas e cobertura; executar POC-01 a POC-03.
3. **Prova longitudinal mínima:** registrar um hábito em t e função executiva em
   t+1; POC-04 pode terminar em `needs_data` ou resultado nulo.
4. **Perfis e comparação:** somente após fundação, testar estabilidade de perfis
   e medidas independentes de condição. Mesmo associação longitudinal não prova
   que hábito cause, explique ou elimine uma condição.

## Dados, inferências e efeito no roteiro

| Dados efetivamente usados | Inferência que eles permitem | Inferência que eles não permitem | Como isso mudou a evolução |
|---|---|---|---|
| NHANES 2021–2023 de adultos: recordatório alimentar de um dia, cafeína, sono, tempo sedentário, sintomas, demografia, energia, pesos, estratos e PSUs | Descrever a população ponderada e estimar associações ajustadas entre as variáveis medidas | Ordem temporal, efeito causal de mudar cafeína/sono, resposta individual ou recomendação de dose | O ciclo 001 foi delimitado como associativo; H1 e H2 precisam de replicação/forma registrada antes de uma conclusão estável |
| Módulo de suplementos, produtos, ingredientes e antiácidos | Distinguir quantidade calculada, produto sem magnésio identificado, produto sem vínculo, total ausente e antiácido | Assumir que total ausente significa dose desconhecida de magnésio, consumo real ou adesão | O ciclo 003 invalidou a interpretação do indicador legado; H3 foi mantida inconclusiva e ganhou uma especificação nova obrigatória |
| Pesos, 15 estratos e 30 PSUs representados; elegíveis e casos completos por hipótese | Reproduzir erros-padrão e testar sensibilidade a graus do desenho e à seleção observável | Provar ausência de seleção não observada ou obter IC que incorpore toda a incerteza das propensões estimadas | O ciclo 002 expôs a dependência da inferência; o 004 fixou 15 graus como convenção principal e mostrou que H1/H2 mudam até 3,3% sob a sensibilidade observável |
| Mesma onda, com H1 n=4.211, H2 n=4.522 e H3 n=4.194 após dados completos | Verificar retenção e estabilidade interna das análises | Replicação independente ou generalização para outra época/população | Auditorias posteriores refinam a leitura do ciclo 001, mas não contam como confirmação independente |
| NHANES sem medida de HA, autismo, TDAH ou referência neurotípica avaliada | Declarar que esses grupos estão `not_assessed` nesta rodada | Comparar grupos, estimar prevalência ou usar escolaridade/ocupação/ausência de diagnóstico como proxy | A linha de conclusões sobre neurodivergência foi bloqueada por mensuração; mais análise desta base não resolve essa lacuna |

## Estado dos ciclos concluídos

| Ciclo | Estado científico atual | Fonte de verdade | Atualização necessária quando houver novo ciclo relacionado |
|---|---|---|---|
| 001 | Executado e corrigido para a fronteira de sono de H2; H1/H2 são associações transversais, H3 inconclusiva, Ridge somente interno | `cycle-001/results.json`, adendo H2 e artigo | Atualizar leitura editorial, não substituir os resultados históricos sem adendo |
| 002 | Auditoria de perdas, pesos e variância reproduzida; sua recomendação metodológica foi sucedida pelo ciclo 004 | `cycle-002/results.json` e `cycle-004/data-audit.md` | Preservar dados históricos e acrescentar nota posterior ao alterar inferência/seleção |
| 003 | Estados de ausência de magnésio e antiácidos auditados; indicador legado não representa dose desconhecida | `cycle-003/results.json` e `data-audit.md` | Toda nova análise H3 deve apontar para esta taxonomia |
| 004 | 15 graus do desenho registrados como convenção principal; H1/H2 estáveis à seleção observável; H3 segue inconclusiva | `cycle-004/results.json`, protocolo e hipótese | Nova análise deve declarar se muda seleção, graus ou família de testes |

## Itens que exigem novo ciclo

| Prioridade | Estado | Dependência mínima | Produto antes de estimar | Critério para atualizar documentos anteriores |
|---|---|---|---|---|
| **Fundação analítica ABCD** | **Prioridade principal; microdados exigem acesso legítimo** | Release, termos, chaves participante-onda, cognição, sintomas, sono/atividade e desfecho posterior | POC-01 a POC-04, dicionário de construtos e decisão `estimable`/`needs_data` | Atualizar plano, fontes, acesso, portal e README; não avançar a clusters, interações ou suplementação sem base aprovada |
| H3 com estados de magnésio | Proposto | DSQIDS/DSPI/DSII já auditados | Adendo datado, população, regra de classificação, estimando, contraste e multiplicidade | Atualizar ciclo 001, 003, 004, plano, portal e README se houver novo resultado |
| Formas não lineares de H1/H2 | Proposto | Dados atuais e decisão prévia de nós/forma | Protocolo com forma funcional, efeitos de interesse, família FDR e diagnóstico | Atualizar apenas após execução; não tratar gráfico exploratório como confirmação |
| Seleção não observada | Needs data/método | Premissas externas ou modelo que incorpore incerteza dos pesos | Protocolo de análise de sensibilidade e parâmetros justificados | Acrescentar limite ou resultado ao ciclo 004; não reescrever seus achados |
| Validação da previsão | Proposto | Separação por PSU/onda ou nova onda compatível | Split congelado, métrica, calibração e regra de escolha sem reutilizar holdout | Atualizar P1 e cartão do modelo somente com avaliação reservada |
| HA, autismo e TDAH | Blocked by measurement/access | Coorte com cognição e condições medidas de modo independente; acesso autorizado quando necessário | Auditoria de medida, critérios de grupo e tamanho das combinações | Não atualizar conclusões NHANES como se fossem comparações desses grupos |

## Documentos sincronizados em cada novo ciclo

1. Artefatos do próprio ciclo: protocolo/hipótese, código, `results.json`,
   `cycle.json`, dossiê, relatório, figuras e README gerado.
2. Visão atual: `README.md`, `research/site/study.json`,
   `catalog/data-sources/DISCOVERY_PLAN.md` e `NEXT_SESSION.md`.
3. Artefatos afetados por revisão: relatório/artigo do ciclo 001 e o ciclo de
   auditoria que documentou a limitação resolvida ou refinada.
4. Portal: build em diretório vazio, testes, JSON/YAML, links, figuras e página
   pública depois do deploy.

## Regras de desatualização

- Um resultado novo não reescreve o resultado anterior: acrescente adendo ou
  atualização posterior com vínculo explícito.
- Um item fica `blocked` quando depende de dados/medidas indisponíveis; não use
  escolaridade, ocupação ou ausência de diagnóstico como substitutos de HA, NT,
  autismo ou TDAH.
- Uma etapa `proposta` só passa a executada após protocolo local datado, execução
  reproduzível e revisão de figuras/interpretação.
- Após alterar `study.json`, confirme que a página “Ciclos e hipóteses” lista
  todos os ciclos `completed`; o teste de publicação cobre essa condição.
