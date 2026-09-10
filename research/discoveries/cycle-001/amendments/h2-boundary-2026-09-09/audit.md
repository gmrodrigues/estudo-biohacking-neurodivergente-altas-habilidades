# Auditoria da correção H2 — 2026-09-09

[Decisão anterior à reexecução](protocol.md) · [Execução original](results-original.json) · [Comparação completa e hashes](comparison.json)

Amostra preservada: 4,522 participantes. Exatamente 686 pessoas com 7 h passaram do grupo curto à referência.

| Grupo | Original: ≤7 / >7–≤9 / >9 | Corrigido: <7 / 7–9 / >9 |
|---|---:|---:|
| short | 1629 | 943 |
| recommended | 2422 | 3108 |
| long | 471 | 471 |

| Termo | Estimativa original [IC95%] | Corrigida [IC95%] | p original → corrigido | q original → corrigido |
|---|---|---|---|---|
| H1_caffeine | -0.053705 [-0.086949, -0.020461] | -0.053705 [-0.086949, -0.020461] | 0.0036214293 → 0.0036214293 | 0.0072428587 → 0.0072428587 |
| H1_caffeine_x_age | +0.023364 [+0.001842, +0.044887] | +0.023364 [+0.001842, +0.044887] | 0.035267573 → 0.035267573 | 0.056428117 → 0.056428117 |
| H2_short_sleep | +0.838028 [+0.581790, +1.094266] | +1.119597 [+0.717702, +1.521493] | 4.493259e-06 → 2.7227695e-05 | 1.7973036e-05 → 0.00010891078 |
| H2_long_sleep | +1.276397 [+0.619048, +1.933746] | +1.214484 [+0.560590, +1.868378] | 0.00087488669 → 0.0012608114 | 0.0023330312 → 0.0033621637 |
| H2_sedentary | +0.116509 [+0.085372, +0.147647] | +0.117836 [+0.087146, +0.148525] | 8.9435373e-07 → 6.5006723e-07 | 7.1548299e-06 → 5.2005378e-06 |
| H3_diet_magnesium | +0.017272 [-0.031654, +0.066199] | +0.017272 [-0.031654, +0.066199] | 0.46341455 → 0.46341455 | 0.46341455 → 0.46341455 |
| H3_supplement_magnesium | +0.029987 [-0.042913, +0.102887] | +0.029987 [-0.042913, +0.102887] | 0.39444546 → 0.39444546 | 0.46341455 → 0.46341455 |
| H3_supplement_unquantified | +0.051818 [-0.083428, +0.187064] | +0.051818 [-0.083428, +0.187064] | 0.42691519 → 0.42691519 | 0.46341455 → 0.46341455 |

H1/H3: horas de sono; H2: pontos no escore de sintomas sem sono (0–24), sedentarismo por hora/dia.

Os três termos de H2 permanecem positivos e com IC95% acima de zero. O contraste curto aumentou, o longo diminuiu; o estimando mudou porque 7 h passou à referência registrada. Isso não é replicação ou evidência causal.

Todos os oito q-valores foram recalculados; apenas os três de H2 mudaram. H1, sua sensibilidade, H3, previsão, campos originais da auditoria e hashes de insumos reproduziram exatamente a execução original. A checagem independente de FDR com statsmodels passou. A variância de desenho ainda requer validação externa.

Comandos, a partir da raiz:

```bash
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/run_analysis.py
MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/audit_h2_amendment.py
```
