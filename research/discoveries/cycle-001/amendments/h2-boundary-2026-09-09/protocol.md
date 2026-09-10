# Adendo H2: fronteira de 7 horas

Registrado localmente em 2026-09-09, antes de executar o ajuste corrigido.
Os resultados originais já eram conhecidos. Este adendo corrige a execução de
uma análise exploratória; não constitui pré-registro independente ou replicação.

## Decisão e escopo

Aplicar a definição de `hypotheses.yaml`: sono curto **<7 h**, referência
**7–9 h inclusive**, sono longo **>9 h**. Ausência permanece ausente. Os valores
exatamente 7 e 9 pertencem à referência. Não escolher a fronteira por resultados.

Preservar participantes, desfecho, covariáveis, pesos, desenho e método de
variância. Reexecutar o pipeline determinístico e recalcular Benjamini–Hochberg
nos mesmos oito termos (H1: dois; H2: três; H3: três). H1, sua sensibilidade,
H3 e previsão devem reproduzir os números originais; verificar essa invariância.
Não alterar insumos brutos ou hashes para acomodar a correção.

Nome público do desfecho: **escore de sintomas sem sono (0–24)**, soma de DPQ010,
DPQ020 e DPQ040–DPQ090, exigindo oito respostas válidas 0–3. O identificador
interno legado `PHQ8_NOSLEEP` será preservado para comparação, mas não denota o
PHQ-8 convencional e não possui cortes clínicos validados neste estudo.

## Proveniência e validação planejada

A execução original está em `results-original.json`, cópia exata do resultado
versionado antes da alteração. Código, figuras e documentação originais permanecem
no commit `3a4eec4` e em seus ancestrais. O arquivo de auditoria registrará hashes
das duas execuções e do código corrigido, contagens por categoria, quantos
participantes mudaram de grupo, coeficientes/IC95%/p/q anteriores e corrigidos
dos oito termos, além das verificações de invariância.

Testar as duas fronteiras, valores ausentes e a família FDR. Atualizar figura,
resultados, manifesto, dossiê, artigo e planejamento juntos. Preservar comparação
histórica visível no dossiê público. A variância ainda exige validação externa
com análise de domínio: esta correção não resolve essa pendência.

## Fontes conferidas nesta sessão

O [codebook SLQ_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/SLQ_L.htm)
define SLD012 a partir de horários usuais, arredondados a meia hora, com extremos
codificados como 2 (<3 h) e 14 (≥14 h). Esses extremos continuam nos respectivos
grupos; não se alterou sua interpretação quantitativa em H1/H3/previsão.
O [codebook DPQ_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.htm)
documenta DPQ030 como item de sono e a divulgação pública apenas de adultos.
