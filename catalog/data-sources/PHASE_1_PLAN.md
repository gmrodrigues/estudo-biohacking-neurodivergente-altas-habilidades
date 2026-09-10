# Fase 1 — base ampla, auditada e validada por POCs

Estado: planejamento; POCs ainda não executadas. Data: 2026-09-10.
Este plano é a referência operacional da fase inicial do [programa](../PROGRAM.md).

## Objetivo e definição de sucesso

Construir um acervo analítico reproduzível que permita testar relações simples
entre capacidade cognitiva contínua, condições/sintomas, hábitos e funcionamento,
com uma linha complementar de nutrição e suplementação.

“Ampla” significa cobertura conjunta útil, diversidade de medidas e tamanho
analítico suficiente por pergunta. A soma dos participantes anunciados pelas
fontes não mede essa amplitude. Não será criada uma tabela única de pessoas de
coortes independentes: cada fonte terá tabelas próprias e um dicionário comum.

A fase termina com uma versão congelada das bases, relatório de cobertura,
POCs reproduzíveis e decisões por hipótese. Uma base pode ser aprovada mesmo
quando a hipótese substantiva não encontra associação.

## Escopo inicial e ordem das fontes

| Prioridade | Frente | Entrega inicial |
|---|---|---|
| 1 | ABCD: candidata longitudinal principal | Verificar acesso, release, medidas cognitivas, hábitos, condições e ondas realmente disponíveis |
| 2 | HBN: candidata complementar de cognição e condições | Auditar acesso e medidas; avaliar compatibilidade, sem assumir seguimento longitudinal |
| 3 | NHANES: nutrição e suplementos | Reaproveitar ingestão, produtos, ausência e desenho amostral já auditados |
| 4 | NSCH e demais fontes abertas já catalogadas | Avaliar alternativas para perguntas de hábitos e funcionamento quando a fonte principal não estiver acessível |
| Posterior | UK Biobank, Terman, SMPY e neuroimagem | Preparar acesso/metadados; ingestão depende de contribuição concreta às lacunas iniciais |

Acesso pendente em ABCD bloqueia sua ingestão, não toda a fase. Prosseguir com
auditorias e POCs independentes nas fontes acessíveis. Uma alternativa sem
cognição não substitui a frente cognitiva: registrar a lacuna.

## Etapas e entregas

| Etapa | Trabalho | Entrega verificável | Critério de passagem |
|---|---|---|---|
| E1 — requisitos | Selecionar perguntas simples e definir população, exposição, desfecho e tempo | Matriz pergunta × campo × fonte × onda | Cada pergunta tem requisitos explícitos e decisão preliminar de viabilidade |
| E2 — acesso e aquisição | Conferir termos, release, arquivos e integridade; baixar somente o necessário | Manifesto com origem, versão, hash, data e acesso observado | Arquivos legíveis e acesso legítimo; metadados separados de microdados |
| E3 — estrutura analítica | Normalizar códigos/unidades; juntar apenas dentro da mesma fonte | Tabelas por fonte e participante/onda, dicionário e código reproduzível | Chaves únicas na granularidade declarada; nenhuma perda ou expansão de junção inexplicada |
| E4 — amplitude real | Contar elegíveis, completos, pares longitudinais e subgrupos | Relatório de cobertura e precisão por pergunta | Sobreposição suficiente para o estimando; déficits e restrições registrados |
| E5 — POCs | Executar auditorias e testes substantivos pequenos | Protocolos, código, agregados, gráficos e resultados nulos/inconclusivos | Decisão reproduzível por POC, sem selecionar por significância |
| E6 — congelamento | Revisar achados e lacunas; versionar base e contratos | Manifesto da versão analítica e backlog priorizado | Outro processamento reproduz contagens e resultados dentro da tolerância registrada |

E1 antecede aquisição extensa. E2–E4 podem ocorrer em fontes independentes.
E5 só usa tabelas aprovadas em E3; E6 consolida inclusive decisões de insuficiência.
Prazos de acesso externo não serão tratados como prazo garantido de entrega.

## Contrato mínimo dos dados

Manter tabelas de participantes, avaliações/ondas, medidas cognitivas,
condições/sintomas, hábitos, nutrição/suplementos, tratamentos e contexto.
Cada tabela declara sua granularidade e chave; produtos e medidas repetidas
não viram participantes adicionais.

Para cada campo: fonte, arquivo, versão, instrumento, informante, unidade,
janela, códigos de ausência, transformação e estado de mensuração.
Diagnóstico, rastreio e sintoma dimensional permanecem distintos.

Para cada pergunta, publicar:
- N total da fonte, elegível, com exposição, com desfecho e com ambos;
- N após ajustes e exclusões, com perdas por motivo;
- N de participantes únicos e pares de ondas, separados de número de registros;
- cobertura por idade, centro, condição e faixa cognitiva quando mensuradas;
- distribuição dos pesos e tamanho efetivo quando aplicável.

## POCs de aprovação técnica

| ID | Teste | Aprovação | Consequência da falha |
|---|---|---|---|
| POC-01 | Chaves, junções e trajetórias | Zero duplicações não explicadas; reconciliação de contagens; datas/ondas consistentes | Corrigir ingestão ou suspender a análise afetada |
| POC-02 | Mensuração cognitiva contínua | Instrumentos e normas documentados; cobertura e distribuição auditadas; comparação entre ondas justificada | Usar domínios separados ou declarar capacidade geral indisponível |
| POC-03 | Capacidade e condições coexistem nos mesmos indivíduos? | Instrumento/informante identificados e células com precisão avaliada | Não estimar contraste sem cobertura; não criar diagnóstico por cluster |
| POC-04 | Há um caminho temporal hábito → desfecho? | Exposição em t, desfecho em t+1, nível basal e dependências familiares/centro auditados | Limitar a pergunta transversal ou registrar needs_data |
| POC-05 | Exposição nutricional é reconstruível? | Separar alimento, suplemento e medicamento; conferir unidades, frequência e estados de ausência contra documentação | Excluir dose não identificável ou restringir a uso relatado |
| POC-06 | Reprodutibilidade e ausência de vazamento | Mesmo insumo reproduz resultados; pessoa/família não cruza treino e teste; transformações ajustadas no treino | Corrigir pipeline antes de divulgar desempenho |

Duas medidas cognitivas são um ponto de triagem, não prova de validade de um
índice geral. Para prever função executiva, excluir o próprio desfecho e seus
componentes futuros da construção do perfil. Desempenho acadêmico deve permanecer
separado quando for o desfecho; evitar circularidade.

## POCs de adequação ao objetivo científico

Todas são propostas, sem resultados. Estes testes substituem as hipóteses
genéricas de sono e atividade da versão anterior. O objetivo é demonstrar que
a base permite estudar fatores modificáveis em função do perfil cognitivo e
das condições medidas. Auditoria técnica é necessária, mas não aprova esse uso.

| ID | Pergunta de adequação | Desenho mínimo | Evidência exigida para aprovação |
|---|---|---|---|
| A-01 | A base distingue capacidade cognitiva, dificuldades e funcionamento sem circularidade? | Medidas cognitivas documentadas, sintomas/condições independentes e desfecho separado | Matriz conjunta de cobertura, distribuição e validade das medidas; não basta haver colunas isoladas |
| A-02 | Podemos estimar se a associação de um fator modificável com funcionamento varia ao longo da capacidade cognitiva? | Uma exposição, capacidade contínua, desfecho independente e ajustes na mesma amostra; uma interação exposição × capacidade | Suporte de exposição ao longo da capacidade, identificação do modelo e precisão pré-definida da interação; resultado pode ser nulo |
| A-03 | Podemos investigar essa relação em participantes com TDAH/autismo e capacidade elevada? | Capacidade e condição medidas independentemente; contar elegíveis com exposição e desfecho por condição e faixa cognitiva | Cobertura e precisão por contraste; cada condição/coexistência recebe aprovação ou insuficiência própria, sem exigir interação tripla nesta fase |
| A-04 | A base permite estudar trajetórias de funcionamento conforme perfil e hábito basal? | Requisitos de A-02 mais desfecho posterior e basal, pares de ondas e perdas auditadas | Estimando longitudinal viável e precisão após retenção; associação transversal não aprova trajetória |
| A-05 | A nutrição/suplementação contribui diretamente ou por uma comparação indireta identificável? | Exposição documentada e perfil/desfecho conjuntos, ou pares de estudos com construto intermediário, população e janela comparáveis | Mapa de cada ligação exposição → hábito/biomarcador → funcionamento, sua fonte e limites; ligação ausente permanece lacuna |

Executar primeiro A-01 e a auditoria de suporte/precisão de A-02 e A-03. Somente
depois ajustar uma POC de A-02, escolhendo um hábito pelo alinhamento e cobertura,
antes de examinar associações. A-04 depende de seguimento; A-05 qualifica a linha
nutricional. Não começar por clusters ou interações de alta ordem.

A-05 não encadeia coeficientes de pessoas distintas para calcular benefício de
suplemento. Estudos de exposição → hábito e hábito → funcionamento podem apoiar
uma hipótese indireta; sua combinação não prova o efeito da intervenção.

## Suficiência e decisões sobre hipóteses

Antes dos testes, definir o menor efeito de interesse e a precisão necessária
na escala do desfecho. Estimar a precisão esperada com o desenho, retenção,
correlação entre ondas e dependência por família/centro; simular quando necessário.
Não escolher um N mínimo universal nem presumir suficiência por uma coorte ser grande.

Resultados têm duas decisões independentes:
1. **Base:** aprovada para a pergunta, aprovada com restrições, corrigir ou insuficiente.
2. **Hipótese:** compatível com associação relevante, compatível com efeito pequeno,
   inconclusiva ou não testável.

p > 0,05 não descarta hipótese. Um intervalo estreito que exclui o efeito mínimo
de interesse pode justificar abandonar aquela hipótese operacional; intervalo
largo pede mais informação. Falha de mensuração descarta o teste naquela base,
não uma teoria geral. Nenhuma POC observacional demonstra causalidade.

## Critério de encerramento da fase

- Ao menos uma base real aprovada em A-01 e A-02, com capacidade, fator modificável
  e funcionamento conjuntamente medidos e precisão suficiente para o estimando.
- A-03 documentada por condição e faixa cognitiva; sem cobertura adequada, a
  frente correspondente de TDAH/autismo/alta capacidade permanece insuficiente.
- Frente nutricional com produto/ingrediente ou uso distinguido e POC de mensuração.
- Auditorias técnicas executadas e ao menos uma POC A-02 reproduzível. Resultado
  nulo com precisão adequada pode aprovar a base; imprecisão excessiva não aprova
  a pergunta, mesmo que o código rode. A-04/A-05 recebem decisões próprias.
- Matriz de precisão e limites por pergunta, com plano para déficits.
- Versão congelada e recomendação fundamentada de avançar, ampliar ou restringir.

A aprovação é por uso: uma base pode sustentar sono e funcionamento e continuar
insuficiente para suplementação, alta capacidade ou coexistência de condições.
Uma associação genérica de sono ou atividade com desempenho não encerra a fase.
Se nenhum núcleo atende A-01/A-02, o produto é um diagnóstico de insuficiência e
um plano de aquisição, e a fundação científica permanece não aprovada.

## Documentação e retomada

Guardar cada execução em research/discoveries/<identificador>/ com protocolo,
manifesto, auditoria, código, resultados agregados e figuras. Microdados sujeitos
a termos permanecem no ambiente autorizado.

Após cada marco, sincronizar este plano, ANALYTIC_FOUNDATION.md, o dicionário,
sources.yaml quando o acesso mudar, NEXT_SESSION.md, o mapa de desatualização e
research/site/study.json. Registrar estado planejado, executado e validado
separadamente. Planejamento e testes com dados simulados não contam como POCs
empíricas concluídas.
