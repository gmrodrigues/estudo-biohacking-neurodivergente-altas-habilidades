---
name: science-predictive-model
description: "Construa e avalie modelos dimensionais que preveem desfechos sem conhecer HA, autismo ou TDAH neste estudo. Use para representação latente, previsão fora da amostra, escassez de dimensões e explicação das contribuições preditivas."
---

# Previsão sem diagnóstico conhecido

Leia [as convenções](../science-discovery/references/project-contract.md), a
auditoria da pergunta e `MULTIDIMENSIONAL_HYPOTHESIS_PREDICTION_METHODOLOGY.md` em
`catalog/data-sources`. Use [a ficha do modelo](assets/model-card.yaml) para
registrar os alvos, dados disponíveis e estado real de validação.

## Definir o que será previsto

Declare usuário/população, momento da previsão, variáveis disponíveis nesse
momento, alvo e horizonte. NHANES transversal permite avaliar previsão em outras
pessoas do mesmo desenho; não demonstra previsão futura ou resposta a mudar dieta.
Para efeitos de intervenção individuais são necessários dados e pressupostos
causais adicionais. Um preditor de desfecho não é automaticamente um recomendador.

O modelo principal exclui rótulos HA/ASD/ADHD e proxies administrativos que os
revelem diretamente. Use lista explícita de entradas permitidas e justificativa
para sinais ligados a tratamento/serviço. Diagnósticos ficam separados para
auditorias posteriores; não escolha arquitetura, variáveis ou limiares em função
do desempenho de subgrupos no teste reservado.

## Construir as dimensões disponíveis

Diferencie fatores latentes refletidos por itens, índices formados por variáveis
e exposições de contexto. Não force família, finanças e suplementos a serem
sintomas de um mesmo fator. Comece com domínios teoricamente definidos e modelos
simples. Compare modelos fatoriais/IRT apenas se quantidade e natureza dos
indicadores permitirem identificação; trate ordinalidade e confiabilidade.

Avalie invariância antes de comparar escores por idade, idioma ou população.
Identificação e normas psicométricas não surgem da padronização z. Se houver
modelo normativo, declare quem compõe a referência e valide sua cobertura de
intervalos/percentis; referência populacional não implica neurotipicidade.

Com dados escassos, trabalhe por tarefa/domínio e compartilhe parâmetros somente
quando houver medidas-âncora compatíveis ou uma amostra de ligação. Sem indicadores
conjuntos ou ponte identificável, correlações entre dimensões de bases separadas
não são estimáveis: apresente cenários, não correlações descobertas. Imputação
não recupera validamente um domínio nunca observado sem pressupostos testáveis.

## Treinar e avaliar

Separe pessoas e unidades relacionadas, incluindo famílias, entre treino/teste.
Use centro/base e tempo quando existirem e forem relevantes. Ajuste imputação,
escala, seleção e mensuração latente somente no treino de cada fold. O próprio
desfecho e seus itens não podem integrar os preditores ou fatores explicativos.

Compare baseline simples com elastic net/GAM e só amplie complexidade se melhorar
a validação. Use seleção interna aninhada quando houver ajuste de hiperparâmetros.
Registre métrica primária, incerteza, calibração, cobertura dos intervalos, erro
por estrato e influência da amostragem. Trate o conjunto externo como indisponível
para escolhas; se reutilizado, reclassifique-o como desenvolvimento.

Avalie falta de domínios esperada no uso real e mudança de distribuição. Defina
quando abster-se por entradas insuficientes ou população fora do suporte. Sem
validação externa, identifique o modelo como validado apenas internamente.

## Explicar e entregar

Relate cargas/escores quando válidos, ablação por domínio e contribuições
aditivas quando a arquitetura permitir. Para modelos não aditivos, documente
baseline, interações e método de atribuição; não force a soma de contribuições
como uma identidade estrutural. SHAP/permutação explicam o preditor e podem ser
instáveis com variáveis correlacionadas. Verifique estabilidade entre divisões.

Um perfil incompleto deve mostrar dimensões observadas, inferidas e indisponíveis,
com incerteza. Entregue modelo/ficha, transformação reproduzível, métricas no teste
e limitações. Código novo deve verificar riscos concretos de vazamento, separação
de grupos e entradas ausentes. Use [TRIPOD](https://www.tripod-statement.org/) como
referência de relato, consultando a versão pertinente; conformidade documental
não demonstra utilidade clínica.
