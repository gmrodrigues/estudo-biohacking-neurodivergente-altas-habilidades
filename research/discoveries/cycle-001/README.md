# Resultados do ciclo

<!-- discovery-cycles:start -->
## Cafeína, sono, sedentarismo, magnésio e predição diagnóstico-agnóstica

Primeiro ciclo exploratório em adultos da NHANES 2021–2023: três hipóteses e previsão do escore de sintomas sem sono (0–24). Inclui correção documentada da fronteira de sono de H2 em 2026-09-09.

População: Adultos de 20–80 anos com dados completos nos módulos NHANES utilizados; grupos de superdotação, autismo e TDAH não foram identificados nesta rodada.

[Ler artigo do ciclo](article.md)

> Correção analítica de 2026-09-09: H2 foi reexecutada conforme o protocolo (<7 h, referência 7–9 h inclusive, >9 h). 686 participantes com exatamente 7 h passaram à referência, mantendo n=4.522. Os oito testes FDR foram recalculados. A comparação com a execução original está no dossiê abaixo e no adendo; H1, H3 e previsão não mudaram. O alvo é o escore de sintomas sem sono (0–24), não o PHQ-8 convencional. Auditoria posterior (ciclo 002): coeficientes e erros-padrão foram reproduzidos com svy no desenho completo. Os p/q e IC deste ciclo usam 15 graus de liberdade; com o padrão residual de svy (piso de 1), nenhum dos oito testes tem q<0,05. A concordância da variância não resolve essa sensibilidade ou a seleção por casos completos.

[Métodos, decisões e fontes no site](https://gmrodrigues.github.io/estudo-biohacking-neurodivergente-altas-habilidades/cycles/cycle-001/index.html)

[Registro editorial completo](public-dossier.json)

### A cafeína do recordatório alimentar se associa a sono usual mais curto?

-0,0537 hora por 100 mg
IC95% -0,0869 a -0,0205; p-FDR=0,0072
n=4.211; WLS com pesos de dieta e variância por estratos/PSUs

Sinal compatível com menor duração de sono, mas transversal e não causal; a sensibilidade excluindo >800 mg enfraqueceu a interação com idade.

### Sono curto/longo e sedentarismo se associam a sintomas depressivos sem reutilizar o item de sono?

Sono curto (<7 h) +1,120 pontos; sono longo (>9 h) +1,214; sedentarismo +0,1178 ponto por hora/dia
IC95% curto +0,718 a +1,521; longo +0,561 a +1,868; sedentarismo +0,0871 a +0,1485; q curto=0,00010891; longo=0,00336216; sedentarismo=0,00000520
n=4.522; referência 7–9 h inclusive; escore de sintomas sem sono (0–24); WLS com pesos de exame

Associações positivas após corrigir a fronteira registrada; causalidade reversa e confusão por saúde permanecem possíveis. A correção não é uma replicação.

### Magnésio alimentar ou suplementar se associa à duração do sono?

+0,0173 hora por 100 mg dietético; +0,0300 por 100 mg suplementar
IC95% dietético -0,0317 a +0,0662; suplementar -0,0429 a +0,1029; p-FDR=0,4634
n=4.194; indicador legado de qualquer suplemento com total de magnésio ausente; WLS com peso de dieta

Evidência inconclusiva; o intervalo inclui efeitos pequenos em ambas as direções e não sustenta protocolo de suplementação.

### É possível prever o escore de sintomas sem sono (0–24) sem conhecer o diagnóstico?

Ridge: MAE 2,903; RMSE 3,945; R² 0,090
Holdout interno único: n treino=3.391, teste=1.131; sem validação externa/temporal
n=4.522; sono, sedentarismo e contexto demográfico; pesos usados no ajuste/métricas

Prova de conceito de previsão dimensional modesta; contexto demográfico contribuiu mais que os domínios isolados nas ablações.

![Coeficientes ajustados da hipótese de cafeína e sono](figures/caffeine-sleep.png)

H1: estimativas e IC95% para cafeína e interação com idade.

![Diferenças ajustadas no escore de sintomas sem sono (0–24), após correção H2](figures/sleep-sedentary-depression.png)

H2 corrigida: sono <7 h e >9 h versus 7–9 h inclusive; sedentarismo por hora/dia. Adultos NHANES 2021–2023, n=4.522, peso WTMEC2YR, IC95% por estratos/PSUs; associação transversal.

![Coeficientes ajustados de magnésio e sono](figures/magnesium-sleep.png)

H3: magnésio alimentar, suplementar e indicador legado de qualquer suplemento com total de magnésio ausente; o ciclo 003 corrigiu sua interpretação.

![Comparação de previsão Ridge e baseline](figures/prediction-calibration.png)

Predição diagnóstico-agnóstica no holdout interno e ablações por domínio.

## Limitações

- NHANES é transversal neste recorte; associações não estabelecem causalidade.
- A rodada não mede nem estratifica altas habilidades, autismo ou TDAH.
- Recordatórios, autorrelato e suplementação têm erro de mensuração.
- O preditor tem uma única separação interna e não foi calibrado externamente.
- Resultados não são recomendação individual de dieta, suplemento, exercício ou sono.

## Fontes

- [CDC NHANES 2021–2023 codebooks and weighting guidance](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx)
- [Gardiner et al. 2023 caffeine and sleep meta-analysis](https://pubmed.ncbi.nlm.nih.gov/36870101/)
- [Longitudinal sleep and depression study](https://pubmed.ncbi.nlm.nih.gov/29861378/)
- [Maastricht Study activity and depression evidence](https://pubmed.ncbi.nlm.nih.gov/36114702/)
- [Magnesium bisglycinate randomized trial](https://pubmed.ncbi.nlm.nih.gov/40918053/)

## Reprodução

```json
{
  "command": "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/run_analysis.py",
  "code_revision": "base 3a4eec48a45e1d29ac670663ae4187cbe9a2e087 + adendo H2 2026-09-09; run_analysis.py sha256=a7aff23ae817c7c0ff5745dc1ed5d2fa6e3c3e1424148c0a6d6bf017157c8492",
  "input_sha256": {
    "DEMO_L.xpt": "ca4374a158b493b8b0163e1388da21d57a18d1b9cecff2aa4e2fa2bec494fe23",
    "DPQ_L.xpt": "25605a02685035fe997477b31a0991cca2776b0f72f24a8e61ac5b018456304b",
    "DR1TOT_L.xpt": "73a3097aab64000f9c1d138367363ca605968b691e349981132bd6032ca6c9ef",
    "DSQTOT_L.xpt": "8ee3e55578f56918a190100bb321a0b580f824ca3cc439901f2fd707dbe695f8",
    "PAQ_L.xpt": "de34acfed4523f10f52bea06e64ed33c8db973cb38d3539eeceb2b68039248c8",
    "SLQ_L.xpt": "918c3258b2f466ac1cae55ea45330c736dbdc573ee4dc72306e3d2b222764741"
  }
}
```
<!-- discovery-cycles:end -->
