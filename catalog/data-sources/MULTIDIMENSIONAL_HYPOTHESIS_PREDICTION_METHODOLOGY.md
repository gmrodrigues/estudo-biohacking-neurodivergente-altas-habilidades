# Metodologia multidimensional, confirmatória e preditiva

**Data:** 2026-09-07

## Finalidade e separação das perguntas

O estudo é centrado em altas habilidades (HA), comparável com autismo, TDAH e
neurotípicos, mas deve prever resultados mesmo sem diagnóstico conhecido.

1. **Mensuração:** quais dimensões latentes explicam os indicadores?
2. **Hipótese:** uma exposição antecede diferença num desfecho definido?
3. **Predição:** quanto se prevê em pessoas, tempos ou bases nunca vistos?

Boa previsão não prova causalidade; fator estatístico não é doença; associação
compatível com uma teoria não confirma essa teoria.

## Modelo de mensuração

Harmonizar indicadores de cognição; função executiva/atenção; sociocomunicação e
sensorialidade; humor/ansiedade; sono/circadiano; nutrição, suplementação e
metilação; atividade, corpo e desempenho; criatividade/arte; educação/trabalho;
família; autonomia financeira; substâncias; saúde, medicação e suporte.

Comparar CFA/ESEM, IRT, modelos correlacionados, bifator e hierárquico por ajuste,
estabilidade e interpretação. Testar invariância configural, métrica e escalar
por idade, sexo/gênero, idioma, base e grupo. Sem invariância, usar parâmetros
específicos ou alinhamento; não comparar médias como equivalentes. Um modelo
normativo estima desvios individuais por dimensão, formando um perfil, não rótulo.

## Núcleo preditivo sem diagnóstico

O modelo principal não recebe HA, autismo, TDAH ou outro diagnóstico como entrada.
Usa apenas medidas disponíveis antes da previsão. Os rótulos ficam separados e
são revelados depois do treino para validação, comparação de calibração/erro e
auditoria de dano diferencial. O sistema estima função, risco, resposta e
incerteza; não substitui diagnóstico clínico.

Alvos preferidos são futuros: mudança em atenção, sono, humor e desempenho,
resposta/tolerabilidade de intervenção, adesão e eventos adversos. Prever o rótulo
diagnóstico é tarefa secundária e só cabe com padrão clínico independente.

Na escassez de um grupo, estudar relações isoladas dentro de domínios e amostras
gerais, seguido de modelo hierárquico com *partial pooling* entre perfis, idades e
bases. Aprendizado multitarefa pode compartilhar representação sem pressupor qual
neurodivergência existe. Intervalos permanecem largos quando falta informação.
Dados sintéticos servem para potência e testes do software, nunca como confirmação.

## Testes de hipóteses

Antes de olhar o resultado, registrar população, exposição, comparador, desfecho,
janela, estimando, DAG, direção, confundidores, mediadores, modificadores,
contraste isolado/duplo/triplo, análise e critério de refutação.

Fluxo: congelar dicionário e plano; avaliar confiabilidade, seleção e ausência;
estimar magnitude e intervalo; controlar multiplicidade por família; aplicar
controles negativos e especificações alternativas; replicar em outra onda/base;
classificar como compatível, incompatível, inconclusiva ou exploratória.

Observacionais longitudinais usam modelos mistos; exposições variantes no tempo
podem exigir modelos estruturais marginais. Mediação exige ordem temporal.
Suplementação pessoal deve preferir N-of-1 randomizado, cego quando possível, com
washout plausível, segurança e regra de parada.

## Treino, validação e explicação preditiva

Separar treino/validação/teste por pessoa e tempo; reservar centro ou base para
validação externa. Comparar média/base-rate, elastic net e GAM antes de boosting.
Usar validação cruzada aninhada, calibração e intervalos. Impedir vazamento de
desfecho, medidas posteriores, diagnóstico revelado ou transformação ajustada no
teste.

```text
predição = nível basal
         + dimensões latentes
         + contexto e exposições
         + interações pré-especificadas
         + incerteza
```

Explicar com cargas/escores latentes, ablação por domínio, permutação e ALE/SHAP,
sempre como comportamento do algoritmo, não causalidade. Mostrar estabilidade
entre folds, calibração e erro por idade, sexo/gênero e diagnóstico revelado
posteriormente. Contrafactuais devem ser plausíveis e acionáveis.

## Registro teórico anterior aos resultados

Cada teoria deve registrar mecanismo, previsão, temporalidade, moderadores,
evidência primária, rivais e falsificador. Achados ficam apenas “consistentes com”:

| Teoria | Previsão | O que a enfraquece |
|---|---|---|
| compensação/mascaramento | capacidade reduz sinais observados, não necessariamente custo funcional | nenhuma discrepância entre teste e vida real |
| ajuste pessoa–ambiente | autonomia e adequação de demanda moderam função/humor | efeito igual em ambientes distintos |
| cascata desenvolvimental | sono, estresse e suporte antecedem mudança | ordem temporal inversa |
| carga alostática | contexto familiar/financeiro liga-se a sono, humor e recuperação | ausência longitudinal após controle basal |
| excitação em U invertido | cafeína ajuda até um ponto e depois piora ansiedade/sono | relação monotônica replicada |
| bioenergética | creatina ajuda mais sob baixa disponibilidade/alta demanda | nenhum gradiente por estado basal |
| um carbono/metilação | B12/folato/homocisteína funcionais modificam relações | sinal só genético e pós-hoc |
| usuário saudável | adesão, renda, dieta e treino confundem suplemento | efeito persiste em RCT e controles negativos |

Selecionar estudos antes da interpretação, extrair população, desenho, dose,
comparador, desfecho, risco de viés e transportabilidade. Não transportar achados
de autismo/TDAH para HA sem teste formal.

## Produtos e limite dos dados atuais

Entregar mapa de cobertura; modelo de mensuração; tabela confirmatória completa;
modelo sem diagnóstico congelado; validação externa/equidade; cartões
teoria–achado. Exploração só vira confirmação em nova amostra ou janela.

O NHANES local permite prototipar nutrição, sono, depressão e atividade em adultos;
ClinicalTrials.gov mapeia estudos, não efeitos individuais. Nenhum identifica HA
adequadamente. Portanto, sustentam pipeline e hipóteses isoladas, não validam ainda
o modelo completo HA–autismo–TDAH.
