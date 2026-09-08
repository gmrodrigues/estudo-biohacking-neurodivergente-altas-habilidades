# Resultados das hipóteses — ciclo 001

Todos os efeitos abaixo são associações ajustadas; intervalos são IC95% derivados do desenho amostral. Os oito testes primários foram corrigidos por Benjamini–Hochberg (FDR).

| Hipótese | Estimativa principal | IC95% | p ajustado | Leitura |
|---|---:|---:|---:|---|
| H1: cafeína e sono | −0,0537 h por 100 mg | −0,0869 a −0,0205 | 0,0072 | associação com menos sono; não é efeito causal |
| H1: interação cafeína×idade | +0,0234 h por década/100 mg | +0,0018 a +0,0449 | 0,0564 | sinal limítrofe; perde força na sensibilidade sem consumo >800 mg |
| H2: sono curto (<7 h) e PHQ-8 | +0,838 pontos | +0,582 a +1,094 | <0,001 | associação com maior sintomatologia |
| H2: sono longo (>9 h) e PHQ-8 | +1,276 pontos | +0,619 a +1,934 | 0,0023 | associação; pode refletir doença, recuperação ou confusão |
| H2: sedentarismo | +0,1165 PHQ-8/hora | +0,0854 a +0,1476 | <0,001 | associação dose–resposta exploratória |
| H3: magnésio alimentar | +0,0173 h/100 mg | −0,0317 a +0,0662 | 0,4634 | inconclusivo |
| H3: magnésio suplementar quantificado | +0,0300 h/100 mg | −0,0429 a +0,1029 | 0,4634 | inconclusivo |
| H3: suplemento com dose não quantificada | +0,0518 h | −0,0834 a +0,1871 | 0,4634 | inconclusivo |

## Predição diagnóstico-agnóstica

Um Ridge com separação interna aleatória 75/25 previu PHQ-8 sem conhecer diagnóstico. O MAE foi 2,90 e RMSE 3,94, contra 3,07 e 4,14 para a média ponderada; R² fora da amostra foi 0,090. Remover sono aumentou RMSE em 0,009, remover sedentarismo em 0,039 e remover contexto demográfico em 0,168. É uma prova de conceito, sem validação externa ou temporal.
