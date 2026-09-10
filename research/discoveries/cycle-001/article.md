# Cafeína e magnésio: o que os dados ajudam a decidir sobre suplementação

Artigo para pessoas neurodivergentes interessadas em suplementação · Ciclo 001, NHANES 2021–2023 · Comparação com estudos humanos, quantificação das associações e orientação para avaliar exposições. Análise exploratória, sem validação individual; H2 corrigida com adendo em 2026-09-09.

## Antes de personalizar, precisamos saber o que conseguimos medir

Qual combinação de sono, alimentação, suplementos e atividade favorece o funcionamento de uma pessoa? Essa pergunta orienta nosso estudo sobre altas habilidades, autismo, TDAH e suas coexistências. O primeiro ciclo começou por uma questão mais delimitada: quais relações aparecem quando examinamos medidas públicas de hábitos e sintomas em adultos?

Encontramos uma associação entre maior ingestão de cafeína e menor duração de sono; associações entre sono, sedentarismo e sintomas; e resultados inconclusivos para magnésio. Um modelo sem rótulos diagnósticos conseguiu alguma previsão dos sintomas, mas deixou a maior parte da variação individual sem explicar.

O alcance desses achados depende da população. Não identificamos HA, autismo ou TDAH neste recorte do NHANES. Os participantes também não constituem um grupo neurotípico confirmado. A rodada informa relações populacionais que poderão orientar estudos posteriores; ainda não permite escolher uma rotina específica para superdotados.


## A tese orientadora: capacidades encobertas ou condições distintas?

A motivação do projeto inclui uma hipótese forte: seria toda neurodivergência uma expressão de altas habilidades prejudicadas por hábitos ou condições desfavoráveis? Registramos essa formulação como pergunta, não como conclusão. Ela é diferente de perguntar se algumas pessoas têm capacidades elevadas cuja expressão é limitada por sono, estresse, saúde ou barreiras ambientais.

Autismo e TDAH são condições do neurodesenvolvimento, com participação de fatores genéticos e de desenvolvimento. A literatura clínica não os define como consequências de hábitos inadequados nem como sinônimos de superdotação. Melhorar sono ou funcionamento não demonstra que uma condição era apenas uma alta habilidade oculta. Apoio adequado pode beneficiar pessoas com diferentes perfis de capacidade.

Para testar a ideia, precisamos medir capacidades e dificuldades de forma independente, definir previamente o que conta como alta habilidade e acompanhar mudanças no contexto. As alternativas incluem capacidades elevadas encobertas em alguns participantes, coexistência de HA com condições distintas, e melhora funcional sem HA. Todas devem permanecer possíveis.

O primeiro ciclo não mede essas capacidades ou diagnósticos; portanto, não confirma nem refuta a tese. Ele apenas investiga algumas exposições que podem orientar perguntas posteriores. Dificuldades de rotina também podem ser consequência de sintomas, limitações materiais ou falta de suporte: a pesquisa não deve convertê-las em culpa individual.


- [NIMH: autismo, desenvolvimento, diversidade de necessidades e forças](https://www.nimh.nih.gov/health/publications/autism-spectrum-disorder)
- [NIMH: TDAH e fatores envolvidos](https://www.nimh.nih.gov/health/publications/attention-deficit-hyperactivity-disorder-what-you-need-to-know)
- [Tese, alternativas e critérios de teste do projeto](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/catalog/data-sources/FOUNDATIONAL_HYPOTHESIS.md)

## Por que começar por cafeína e magnésio

Antes de interpretar um regime complexo de suplementação, faz sentido caracterizar exposições que podem atravessar vários produtos e a própria alimentação. A cafeína pode estar no café, chá, energéticos e em suplementos. Para quem combina fontes, contar apenas as cápsulas ou apenas o café descreve mal a exposição. O magnésio, por sua vez, pode vir da dieta, de produtos nutricionais e de alguns medicamentos.

Isso torna a dupla um ponto de partida prático para este projeto, também pela disponibilidade de variáveis no NHANES. Não medimos quantos regimes de suplementação contêm ambos; não seria correto dizer que todos os incluem. Quando aparecem em vários produtos, somar por ingrediente ajuda a identificar duplicações.

A escolha não significa que este ciclo tenha testado cafeína junto com magnésio. As análises foram separadas: não estimamos interação, sinergia ou compensação entre eles. O resultado de magnésio não autoriza supor que ele neutralize alterações de sono relacionadas à cafeína.

Para o público neurodivergente, a pergunta útil é o balanço entre o objetivo pretendido — por exemplo, alerta — e sono, ansiedade e funcionamento cotidiano. Esse balanço não foi medido integralmente aqui, nem testado por diagnóstico. A contribuição imediata do artigo é ajudar a organizar a decisão e reconhecer o que falta medir.


- [FDA: fontes de cafeína e variação de sensibilidade](https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much)
- [NIH ODS: fontes alimentares, suplementos e medicamentos com magnésio](https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/)

## O que pode orientar uma decisão hoje

São decisões de avaliação, não instruções para iniciar ou alterar tratamento. Se há medicação prescrita ou condição clínica, o registro de exposições pode apoiar a conversa com quem acompanha o cuidado. Não é necessário acrescentar outro produto para começar a compreender o regime atual.

| Situação | O que vale esclarecer | O que o ciclo oferece |
| --- | --- | --- |
| Uso de vários produtos com cafeína | Quantidade total por dia, por tomada e horário da última exposição | Motivo para examinar sono junto com consumo; não uma dose individual ideal |
| Interesse em magnésio para dormir | Ingestão alimentar, quantidade elementar suplementar, formulação e objetivo | Resultado inconclusivo para horas de sono; não escolher sal ou aumentar dose a partir dele |
| Uso dos dois compostos | Somar fontes separadamente e registrar mudanças simultâneas | Nenhuma estimativa do efeito combinado; não assumir compensação |
| TDAH, autismo, HA ou coexistências | Idade, sintomas, tratamento, sono e objetivo funcional reais | Nenhuma evidência deste ciclo de dose ou resposta específica por grupo |

## Como a análise foi construída

Usamos módulos públicos do NHANES de agosto de 2021 a agosto de 2023: demografia, recordatório alimentar, sono, atividade, sintomas depressivos e totais de suplementos. As junções foram feitas por participante e separadamente para cada pergunta. Os modelos utilizaram 4.211 pessoas para cafeína, 4.522 para sono/sedentarismo e 4.194 para magnésio.

As regressões foram ponderadas e ajustadas por idade, sexo registrado, raça/etnia, escolaridade e razão renda/pobreza; as análises nutricionais incluíram energia alimentar. A incerteza foi calculada considerando estratos e unidades primárias de amostragem, com 15 graus de liberdade. Oito termos principais receberam correção Benjamini–Hochberg para múltiplos testes.

São dados transversais: exposição e desfecho não formam uma sequência experimental. O recordatório alimentar representa um dia, a suplementação resume 30 dias e o sono é habitual. Essa diferença entre janelas, as perdas por dados incompletos e o autorrelato limitam as interpretações.

O registro local declara que as hipóteses foram escritas antes dos coeficientes, após uma inspeção inicial dos dados. Não existe pré-registro externo independente. A comparação ampliada à literatura neste artigo é posterior aos resultados e não deve ser confundida com uma validação confirmatória planejada.


- [Codebooks oficiais do NHANES](https://wwwn.cdc.gov/nchs/nhanes/default.aspx)
- [Código, fórmulas e processamento do ciclo](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/run_analysis.py)
- [Registro local das hipóteses](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/hypotheses.yaml)

## O retrato numérico do ciclo

Correção analítica de 2026-09-09: H2 foi reexecutada conforme o protocolo (<7 h, referência 7–9 h inclusive, >9 h). 686 participantes com exatamente 7 h passaram à referência, mantendo n=4.522. Os oito testes FDR foram recalculados. A comparação com a execução original está no dossiê do ciclo e no adendo; H1, H3 e previsão não mudaram. O alvo é o escore de sintomas sem sono (0–24), não o PHQ-8 convencional.

O escore de sintomas é uma soma de oito itens do PHQ-9, excluindo o item de sono, de 0 a 24. Não é o PHQ-8 convencional e não herda seus cortes diagnósticos. Todos os intervalos abaixo são IC95%; q é o valor ajustado por múltiplos testes.

Auditorias posteriores: o ciclo 002 reproduziu coeficientes e erros-padrão com svy. O ciclo 004 fixou 15 graus do desenho como convenção principal segundo o NCHS e preservou 1 grau residual como sensibilidade conservadora. A reponderação pela inclusão observável alterou H1/H2 em no máximo 3,3%; isso não elimina seleção não observada.

| Relação | Estimativa ajustada | IC95% | q |
| --- | --- | --- | --- |
| Cafeína: +100 mg, aos 45 anos | −0,0537 h de sono | −0,0869 a −0,0205 | 0,0072 |
| Sono <7 h versus 7–9 h inclusive (H2 corrigida) | +1,120 ponto no escore de sintomas sem sono (0–24) | +0,718 a +1,521 | 0,00010891 |
| Sono >9 h versus 7–9 h inclusive (H2 corrigida) | +1,214 ponto no escore de sintomas sem sono (0–24) | +0,561 a +1,868 | 0,00336216 |
| Sedentarismo: +1 h/dia (H2 corrigida) | +0,1178 ponto no escore de sintomas sem sono (0–24) | +0,0871 a +0,1485 | 0,00000520 |
| Magnésio alimentar: +100 mg | +0,0173 h de sono | −0,0317 a +0,0662 | 0,4634 |
| Magnésio suplementar: +100 mg | +0,0300 h de sono | −0,0429 a +0,1029 | 0,4634 |

- [Resultados numéricos completos](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/results.json)
- [Gráficos, métodos e nota de revisão](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/cycles/cycle-001/)
- [Ciclo 002: perdas, pesos e sensibilidade da inferência](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/cycles/cycle-002/index.html)

## Cafeína: direção familiar, uma pergunta diferente da experimental

No modelo, 100 mg adicionais de cafeína alimentar se associaram a cerca de 3,22 minutos a menos de sono aos 45 anos. A referência de idade importa porque incluímos uma interação: o coeficiente não deve ser tratado como efeito igual em todas as idades. A interação teve q=0,0564 e enfraqueceu na análise que excluiu consumos acima de 800 mg. Portanto, este ciclo não sustenta uma conclusão firme sobre resposta diferenciada por idade.

A revisão de Gardiner e colaboradores, publicada em 2023, reuniu 24 estudos sobre cafeína e sono e encontrou prejuízos em medidas de sono. Isso oferece contexto para a direção observada aqui. Entretanto, contrastes experimentais entre cafeína e controle não equivalem a uma inclinação por 100 mg de ingestão cotidiana. Não podemos concluir que a cafeína seja menos prejudicial apenas porque nosso coeficiente em minutos é pequeno.

Há também um comparador observacional próximo: o estudo publicado em 2016 com 4.730 adultos do NHANES 2007–2008 usou dois recordatórios e regressão logística para sintomas de insônia. Associações brutas perderam força após ajuste e houve interação entre cafeína e duração de sono para sono não restaurador. Nosso ciclo usa um recordatório e modela duração contínua, com interação por idade. Logo, não é uma replicação direta nem uma contradição daquele resultado.

Uma explicação concorrente continua aberta: pessoas que dormem menos podem consumir mais cafeína para manter o alerta. Medir horário de consumo, rotina de trabalho e exposição repetida ajudaria a separar essa resposta comportamental de efeitos sobre o sono.


- [Gardiner et al. (2023): revisão e meta-análise](https://pubmed.ncbi.nlm.nih.gov/36870101/)
- [Caffeine consumption, insomnia, and sleep duration (2016)](https://pubmed.ncbi.nlm.nih.gov/27377580/)

## Sono e sedentarismo: convergência observacional, sem direção causal definida

Após a correção para <7 h e >9 h versus 7–9 h inclusive, os dois grupos extremos apresentaram escores de sintomas maiores que a referência. Isso é compatível com uma relação não linear, mas três categorias não identificam uma curva nem uma duração ótima de sono. A correção alinha a execução ao protocolo; não é replicação independente.

O estudo longitudinal de 2018 sobre sono e depressão em pessoas de meia-idade e idosas encontrou relações bidirecionais. Ele ajuda a compreender por que nosso retrato transversal admite explicações nos dois sentidos. Porém, categorias de sono, instrumento e desfecho longitudinal diferem: não cabe comparar suas razões de chances diretamente com nossos pontos no escore modificado.

No Maastricht Study, 5.582 participantes tiveram atividade medida por acelerômetro e sintomas acompanhados com PHQ-9. Pessoas com sintomas prevalentes apresentaram mais tempo sedentário; o acompanhamento mediano foi de 5,1 anos. Nosso sinal é qualitativamente compatível, mas usa autorrelato de sedentarismo e uma única observação. A instrumentação e o seguimento do comparador oferecem informação que nosso ciclo não tem.

Excluir o item de sono do alvo reduz a sobreposição direta entre preditor e desfecho. Essa escolha tem um custo: cria uma medida menos comparável às escalas clínicas publicadas. É uma particularidade útil para investigar a associação, não uma validação de um novo instrumento.


- [Sono e depressão: estudo longitudinal bidirecional (2018)](https://pubmed.ncbi.nlm.nih.gov/29861378/)
- [Gianfredi et al. (2022): The Maastricht Study](https://pubmed.ncbi.nlm.nih.gov/36114702/)

## Magnésio: o resultado inconclusivo também precisa ser explicado

Não encontramos uma associação estatisticamente discernível entre magnésio e duração de sono sob as especificações utilizadas. Os intervalos admitem associações pequenas em ambas as direções. Isso não comprova ausência de benefício e tampouco confirma eficácia de suplementação.

Um estudo de NHANES 2009–2018 com 21.840 participantes relatou associação entre magnésio alimentar e duração de sono; entre 3.923 participantes com dados de suplementação, não encontrou associação significativa para os grupos de magnésio suplementar. Nosso resultado suplementar é compatível com essa incerteza, enquanto o alimentar não reproduz a detecção relatada. O comparador usou categorias de ingestão e regressão logística, com outro conjunto de ajustes; aqui usamos uma relação linear em horas. Diferenças de significância, sozinhas, não demonstram que os efeitos sejam diferentes.

Já o ensaio de Schuster e colaboradores (2025) randomizou 155 adultos com sono ruim para bisglicinato de magnésio ou placebo. Em quatro semanas houve uma melhora pequena no índice de gravidade de insônia, com tamanho de efeito d=0,2. Isso responde a uma pergunta diferente: uma formulação específica, num grupo selecionado, com um desfecho de insônia.

Nosso total de nutrientes não distingue formulações, inclui informações de suplementos/antiácidos e não mede adesão ou estado basal de magnésio. A auditoria posterior do ciclo 003 mostrou que o indicador legado de total ausente não equivale a magnésio de dose desconhecida: somente 6 dos 1.401 participantes marcados tinham produto rotulado com magnésio e total ausente. Precisamos de análises por adequação nutricional e de uma especificação registrada para estados de mensuração antes de atribuir a discrepância a uma característica biológica.


- [Dietary Magnesium Intake Is Associated With Self-Reported Short Sleep Duration but Not Self-Reported Sleep Disorder (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11799047/)
- [Schuster et al. (2025): ensaio de bisglicinato de magnésio](https://pubmed.ncbi.nlm.nih.gov/40918053/)

## O que significa prever sem conhecer o diagnóstico

O modelo Ridge combinou sono, sedentarismo, idade, sexo registrado, raça/etnia, escolaridade e renda/pobreza. Foram 3.391 participantes para treino e 1.131 para teste. O erro quadrático médio em sua raiz foi 3,94 pontos, contra 4,14 para a previsão pela média ponderada do treino. O R² foi aproximadamente 0,09: isso não significa 91% de acerto.

O modelo mostra que existe informação preditiva nesses campos mesmo sem diagnóstico, mas seu desempenho é modesto. Remover o conjunto de variáveis demográficas/contextuais aumentou o erro mais do que remover sono ou sedentarismo separadamente. Essa comparação descreve a contribuição de blocos de entradas; não identifica causas nem estabelece que cada variável demográfica seja mais importante que o sono.

O teste foi interno, aleatório e da mesma onda; não separou contextos amostrais por PSU e não avaliou pessoas de outra base ou época. Não há intervalos para essas métricas nem validação de resposta a intervenções. Os estudos citados aqui não fornecem um benchmark equivalente para esse mesmo alvo e divisão, portanto não reivindicamos superioridade preditiva.


- [Cartão do modelo e métricas](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/model-card.yaml)

## As particularidades do estudo: contribuição e limites

A contribuição defensável, por enquanto, é uma análise exploratória documentada que integra perguntas relacionadas e expõe seus limites. A busca dirigida encontrou antecedentes claros para as associações investigadas. Não foi demonstrado ineditismo científico, e nenhuma particularidade deve ser confundida com superioridade metodológica.

| Particularidade | O que acrescenta | O que não permite afirmar |
| --- | --- | --- |
| Recorte NHANES 2021–2023 | Examina uma onda diferente das análises NHANES comparadas | Não prova mudança histórica nem efeito pós-pandemia |
| Sono removido do escore de sintomas | Reduz uma fonte direta de sobreposição de conteúdo | Não valida um escore clínico novo |
| Magnésio alimentar e suplementar no mesmo ajuste | Distingue fontes no modelo, incluindo indicador de quantidade ausente | Não separa formulações nem identifica deficiência |
| Cafeína com interação por idade | Testa heterogeneidade com idade contínua | Interação não conclusiva após FDR; não sustenta personalização etária |
| Inferência e previsão no mesmo ciclo | Confronta associações com utilidade preditiva fora do treino | Não fornece causalidade ou modelo latente multidimensional validado |
| Código, hashes, nulos e nota de revisão públicos | Permite examinar decisões e reproduzir a execução | Transparência não substitui correção estatística e replicação |

## Quantificar sem transformar associação em promessa

A conclusão individual não é que a cafeína custe apenas três minutos ou que magnésio renda dois. As estimativas descrevem diferenças médias condicionadas ao modelo, sujeitas a erro de medida e confundimento. Não devem ser somadas entre si para calcular um suposto saldo de sono. H1 utilizou cafeína do recordatório alimentar, não uma análise completa de toda cafeína suplementar.

| Unidade comparada no modelo | Diferença associada de sono | IC95% em minutos | Limite para decidir |
| --- | --- | --- | --- |
| Mais 100 mg de cafeína alimentar, aos 45 anos | −3,22 minutos | −5,22 a −1,23 | Não estima o efeito de reduzir 100 mg numa pessoa; horário não medido |
| Mais 100 mg de magnésio alimentar | +1,04 minuto | −1,90 a +3,97 | Não confirma benefício nem mede correção de deficiência |
| Mais 100 mg de magnésio suplementar | +1,80 minuto | −2,57 a +6,17 | Não é ganho esperado após uma cápsula; forma e adesão desconhecidas |

## Um registro simples para individualizar a pergunta

Como instrumento de organização — ainda não validado por este estudo —, um registro por tomada pode reunir data, horário, produto/fonte, porção, quantidade de cafeína em mg, magnésio elementar em mg e grau de certeza da informação. Ausência de informação é “desconhecido”, não zero. No caso de café preparado, o teor varia; o volume sozinho não fornece uma dose exata.

Some cafeína por todas as fontes uma única vez. Para magnésio, mantenha subtotais separados de alimentos e de suplementos/medicamentos. Identifique a quantidade elementar na informação nutricional; o peso do sal ou composto não é a mesma quantidade de magnésio.

Exemplo puramente aritmético, não um regime recomendado: se dois produtos informam 80 mg e 120 mg de cafeína por porção, uma porção de cada soma 200 mg, antes de outras fontes. Se dois produtos informam 60 mg e 100 mg de magnésio elementar, o subtotal é 160 mg. Ingredientes já incluídos no total informado pelo fabricante não devem ser contados novamente.

Associe o registro a horário de deitar/levantar, tempo estimado para adormecer, despertares, funcionamento no dia seguinte e sintomas relevantes. Indique dias de treino, mudanças de medicação e outras alterações de rotina. Médias e variação entre dias ajudam a formular perguntas; melhoras simultâneas não isolam o efeito de um ingrediente.

Defina o objetivo antes de comparar períodos: dormir mais, adormecer mais rápido e sentir-se mais disposto são desfechos diferentes. Um registro observacional pode justificar uma avaliação profissional ou um protocolo prospectivo; não demonstra sozinho eficácia, e não exige aumentar doses ou interromper medicamentos.


- [NIH ODS: magnésio elementar e leitura da composição](https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/)
- [FDA: quantidade de cafeína varia entre produtos e preparações](https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much)

## Referências de segurança são diferentes de metas de consumo

A FDA menciona 400 mg/dia de cafeína como quantidade geralmente não associada a efeitos negativos para a maioria dos adultos, mas ressalta variação de sensibilidade. Isso não é meta, garantia de sono preservado ou limite personalizado para neurodivergência, gravidez ou uso de medicamentos.

O NIH ODS apresenta limite superior de 350 mg/dia de magnésio de suplementos e medicamentos para adultos, excluindo o magnésio naturalmente presente nos alimentos. É uma referência de segurança norte-americana, não dose indicada para sono. Doença renal aumenta o risco de toxicidade; há interações com alguns medicamentos. Necessidade nutricional total e limite suplementar são conceitos distintos.

Os dados deste ciclo não autorizam transpor essas referências para crianças ou ajustar tratamento de TDAH, autismo, ansiedade ou depressão. Quando doses, formulações e contexto clínico estão incertos, esclarecer essas informações vem antes de interpretar qualquer previsão.


- [FDA: referência e ressalvas para cafeína](https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much)
- [NIH ODS: limites, função renal e interações](https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/)

## O próximo ciclo deve testar as explicações, não apenas repetir os números

Após a correção de H2, o ciclo 002 auditou perdas, pesos e variância; o ciclo 003 esclareceu os estados de ausência de magnésio; e o ciclo 004 registrou a convenção de 15 graus do desenho e encontrou estabilidade de H1/H2 sob reponderação pela seleção observável. As próximas especificações devem tratar formas não lineares e buscar validação independente, preservando os limites por seleção não observada.

A comparação com a literatura sugere testes concretos: harmonizar desfechos e ajustes com estudos NHANES anteriores; considerar consumo habitual e horário de cafeína; separar inadequação nutricional de dose suplementar; e validar previsão em outra onda ou com separação por unidades amostrais. Comparações de métodos harmonizados serão mais informativas do que confrontar p-valores.

Para chegar a HA, autismo e TDAH, serão necessárias medidas cognitivas e diagnósticas apropriadas, além de amostras que sustentem comparações isoladas, duplas e triplas. Para desempenho em calistenia ou artes marciais, serão necessárias medidas físicas específicas. Este ciclo estabelece perguntas e um ponto de partida reproduzível, ainda distante de uma prescrição individual.


## Nota editorial, fontes e reprodução

Este artigo incorpora a correção analítica de H2 de 2026-09-09, documentada no adendo com comparação à execução original. Não constitui um novo ciclo ou replicação independente. Os estudos comparadores foram selecionados anteriormente por proximidade temática e metodológica, incluindo resultados positivos e inconclusivos; a busca não é uma revisão sistemática nem uma avaliação formal completa de risco de viés.

As fichas de comparação identificam acesso por resumo ou trechos do artigo, desenhos e limites de transporte. O código e os resultados originais permanecem versionados. Execução e testes do projeto usam Pipenv.


- [Fichas de comparação e limites da busca](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/article-evidence.yaml)
- [Registro metodológico e ressalvas](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/public-dossier.json)
- [Manifesto com comando e hashes dos insumos](https://github.com/gmrodrigues/estudo-biohacking-neurodivergente-altas-habilidades/blob/main/research/discoveries/cycle-001/cycle.json)
