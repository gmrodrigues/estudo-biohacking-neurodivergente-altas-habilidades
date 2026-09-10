# Resultados das hipóteses — ciclo 001

Correção H2 executada em 2026-09-09. [Adendo e comparação histórica](amendments/h2-boundary-2026-09-09/audit.md).

Associações ajustadas transversais; IC95% por estratos/PSUs e q por Benjamini–Hochberg nos mesmos oito termos. H2 compara <7 h e >9 h com 7–9 h inclusive; o escore de sintomas sem sono (0–24) não é o PHQ-8 convencional. A variância ainda aguarda confronto externo.

| Hipótese | Estimativa | IC95% | q |
|---|---:|---:|---:|
| H1: cafeína (h/100 mg, aos 45 anos) | -0,0537 | -0,0869 a -0,0205 | 0,00724286 |
| H1: cafeína×idade (h/década/100 mg) | +0,0234 | +0,0018 a +0,0449 | 0,05642812 |
| H2: sono curto <7 h (pontos) | +1,1196 | +0,7177 a +1,5215 | 0,00010891 |
| H2: sono longo >9 h (pontos) | +1,2145 | +0,5606 a +1,8684 | 0,00336216 |
| H2: sedentarismo (ponto/hora) | +0,1178 | +0,0871 a +0,1485 | 0,00000520 |
| H3: magnésio alimentar (h/100 mg) | +0,0173 | -0,0317 a +0,0662 | 0,46341455 |
| H3: magnésio suplementar (h/100 mg) | +0,0300 | -0,0429 a +0,1029 | 0,46341455 |
| H3: qualquer suplemento; total de magnésio ausente (h, indicador legado) | +0,0518 | -0,0834 a +0,1871 | 0,46341455 |

Auditoria posterior do ciclo 003 mostrou que esse indicador legado não comprova
uso de magnésio com dose desconhecida: somente 6 dos 1.401 participantes marcados
tinham produto rotulado com magnésio e total ausente.

H2 mantém associações positivas; H1 mantém associação com menos sono e interação limítrofe após FDR. H3 permanece inconclusiva. Ajuste estatístico não estabelece causalidade.

## Predição diagnóstico-agnóstica

Um Ridge com separação interna aleatória 75/25 previu o escore de sintomas sem sono (0–24) sem conhecer diagnóstico. O MAE foi 2,90 e RMSE 3,94, contra 3,07 e 4,14 para a média ponderada; R² fora da amostra foi 0,090. Remover sono aumentou RMSE em 0,009, remover sedentarismo em 0,039 e remover contexto demográfico em 0,168. É uma prova de conceito, sem validação externa ou temporal.
