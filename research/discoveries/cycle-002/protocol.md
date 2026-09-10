# Ciclo 002 — auditoria de seleção, pesos e variância

Registro local de 2026-09-09, antes da execução desta auditoria. Os resultados
corrigidos do ciclo 001 já são conhecidos. Esta rodada audita sua implementação;
não constitui replicação, nova hipótese de eficácia ou pré-registro externo.

## Escopo congelado

1. Reconstituir H1/H2/H3 com os mesmos insumos, variáveis e regras do ciclo 001.
   Comparar chaves de participantes e N; decompor perdas sequenciais por junção,
   elegibilidade, covariáveis, exposição/desfecho e peso. Publicar também ausências
   marginais (sobrepostas), separando ausência bruta e código fora do domínio.
2. Identificar exclusões estruturais da escolaridade de adultos de 18–19 anos.
   Mostrar perdas por estrato/PSU e proporção retida; não atribuir motivos clínicos
   a ausência de dados. Suplementação com dose ausente permanece categoria própria.
3. Resumir pesos positivos: quantis, máximo, concentração no 1% maior, CV e
   tamanho de Kish ((soma w)^2/soma w²). Kish considera apenas desigualdade dos
   pesos; não é tamanho efetivo completo do desenho ou de cada coeficiente.
4. Conferir coeficientes e erros-padrão Taylor com `svy` (versão no lock),
   especificando estrato, PSU e peso antes do domínio de casos completos.
   Usar a mesma matriz de covariáveis para isolar cálculo de variância. Conferir
   cobertura das PSUs do desenho completo. Não ignorar PSUs vazias/singletons.
   Se houver diferença, registrar e investigar convenções; não escolher método
   por significância. Registrar separadamente validação numérica e inferência.
5. Relatar achados e limitações com figuras e página do ciclo. Não corrigir
   retroativamente estimativas do ciclo 001 nesta auditoria sem adendo específico.

Não estão incluídos nesta execução: novos modelos não lineares, imputação,
interações, validação externa de previsão ou recomendações individuais. Eles
exigem especificação posterior. HA, autismo e TDAH permanecem `not_assessed`.

## Fontes metodológicas consultadas

- [CDC: variância e análise de subgrupos](https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx)
- [CDC: pesos](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx)
- [DEMO_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm)
- [DSQTOT_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm)
- [svy: implementação](https://github.com/samplics-org/svy)

A validação divulgada pelos autores do pacote contra R não substitui a comparação
executada neste projeto nem valida seleção de amostra, mensuração ou causalidade.
