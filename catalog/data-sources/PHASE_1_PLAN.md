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

## Hipóteses simples para experimentar a base

Todas são propostas, sem resultados. Selecionar no máximo duas por primeira
rodada, conforme E4; congelar instrumento e campo exato antes de estimar.

| ID | Hipótese candidata | Desenho mínimo | O que valida na base |
|---|---|---|---|
| H-P01 | Sono basal associa-se à função executiva posterior após considerar seu nível basal | Uma exposição, um desfecho, duas ondas e ajustes pré-definidos | Ligação temporal, retenção e funcionamento do modelo longitudinal |
| H-P02 | Atividade associa-se ao funcionamento escolar | Medidas conjuntas na mesma fonte; desenho transversal se não houver seguimento | Cobertura de hábito, desfecho e contexto |
| H-P03 | Uso relatado de suplemento corresponde a exposição quantificável por ingrediente | Auditoria de produtos, frequência e quantidade | Quanto da base sustenta análise de dose e quanto permite apenas análise de uso |

H-P03 é uma hipótese de mensuração, não de eficácia. Não começar por interações
de alta ordem, P99 × TDAH × TEA, agrupamentos complexos ou dezenas de suplementos.

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

- Ao menos uma base real processada e reproduzível para perguntas de hábito e
  funcionamento, com cobertura explicitada.
- Frente cognitiva auditada: capacidade contínua utilizável ou lacuna explicitamente
  aberta; sem ela, não declarar o programa neurocognitivo plenamente habilitado.
- Frente nutricional com produto/ingrediente ou uso distinguido e POC de mensuração.
- POCs aplicáveis executadas; não aplicáveis justificadas; no mínimo uma hipótese
  substantiva simples executada, ainda que inconclusiva.
- Matriz de precisão e limites por pergunta, com plano para déficits.
- Versão congelada e recomendação fundamentada de avançar, ampliar ou restringir.

A aprovação é por uso: uma base pode sustentar sono e funcionamento e continuar
insuficiente para suplementação, alta capacidade ou coexistência de condições.

## Documentação e retomada

Guardar cada execução em research/discoveries/<identificador>/ com protocolo,
manifesto, auditoria, código, resultados agregados e figuras. Microdados sujeitos
a termos permanecem no ambiente autorizado.

Após cada marco, sincronizar este plano, ANALYTIC_FOUNDATION.md, o dicionário,
sources.yaml quando o acesso mudar, NEXT_SESSION.md, o mapa de desatualização e
research/site/study.json. Registrar estado planejado, executado e validado
separadamente. Planejamento e testes com dados simulados não contam como POCs
empíricas concluídas.
