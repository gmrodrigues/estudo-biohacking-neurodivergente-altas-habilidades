---
name: science-hypothesis-test
description: "Registre e teste hipóteses de sono, nutrição, suplementação, desempenho e contexto neste estudo, com estimandos, incerteza, multiplicidade e comparação entre excepcionalidades quando identificadas."
---

# Testes de hipóteses

Leia [as convenções](../science-discovery/references/project-contract.md) e o
relatório de auditoria da pergunta. Se não existir, execute a parte pertinente
de [auditoria](../science-data-audit/SKILL.md). Consulte o registro de hipóteses
existente; use os documentos pessoais apenas se a pergunta exigir personalização.

## Registrar antes dos efeitos

Copie [a ficha de hipótese](assets/hypothesis.yaml) para a rodada. Preencha exposição,
comparador, população, alvo, estimando, janela, DAG, ajustes, direção ou intervalo
previsto, menor efeito de interesse e famílias de testes. Registre quais dados já
foram vistos. Plano local datado não equivale a pré-registro externo independente;
resultado que motivou a hipótese precisa de novos dados para confirmação.

Defina o critério de transporte para HA/ASD/ADHD, inclusive isoladas, duplas e
triplas. Use `not_assessed` quando faltarem medidas de grupo. Um contraste
populacional permanece útil mesmo sem viabilizar a comparação diagnóstica.

## Escolher o estimando e executar

Em dados transversais, estime associações ajustadas ou diferenças descritivas;
especifique quando uma meta causal não é identificável. Se longitudinais, preserve
ordem temporal e dependência por participante/família/centro. Ajuste confundidores
segundo o DAG, evitando selecionar covariáveis apenas por p-valor ou condicionar
automaticamente em mediadores e colisores.

No NHANES, use o desenho auditado para estimativa e variância. Um ajuste com
`sample_weight` ou erros robustos genéricos pode não implementar o desenho.
Escolha implementação adequada, gerenciada pelo Pipenv quando Python.

Reporte magnitude, unidade, intervalo, N bruto/efetivo, dados ausentes, número de
testes e correção planejada. Use splines e interações apenas com justificativa e
informação suficiente. Interação é um contraste direto: significância em um grupo
e ausência em outro não estabelecem diferença entre eles.

## Robustez e interpretação

Analise confundimento residual, causalidade reversa, seleção, erro de exposição e
ausência informativa. Prefira análises de sensibilidade motivadas por riscos
concretos, preservando todos os resultados. Com sono e PHQ-9, avalie sobreposição
do item de sono e nomeie corretamente qualquer escore modificado.

Separe descoberta, teste reservado e replicação. Não significância não é
equivalência: um teste de equivalência exige margens previamente justificadas.
Dados sintéticos permitem verificar recuperação de um efeito conhecido e potência,
sem contar como participantes ou evidência do efeito real.

O resultado da rodada inclui ficha preenchida, código/comando Pipenv e
`hypothesis-results.md`: estimativa, compatibilidade com a previsão,
incerteza, sensibilidades e comparações pendentes. Use `inconclusive` quando o
intervalo comportar alternativas relevantes, inclusive em estratos pequenos.
Um pedido de hipótese sobre suplemento autoriza análise, não mudança de dose ou
execução de um experimento pessoal.
