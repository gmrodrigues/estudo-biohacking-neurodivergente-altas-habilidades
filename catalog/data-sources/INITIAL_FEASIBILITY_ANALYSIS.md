# Análise inicial de viabilidade dos modelos

**Data da análise:** 2026-09-07  
**Estado:** primeira inspeção de metadados e microdados públicos.

## Resultado principal

Não existe, nas fontes avaliadas, uma tabela pública pronta para estimar o efeito
de dieta, suplementos, exercício e sono especificamente em pessoas superdotadas.
Há dois blocos complementares:

- **ABCD/NDA:** melhor bloco para construir um fenótipo cognitivo elevado e estudar
  modificadores, porém os microdados são controlados;
- **NHANES:** melhor bloco público imediato para exposição nutricional, suplementos,
  atividade, sono e saúde, porém não identifica altas habilidades.

OpenNeuro é uma camada mecanística e de replicação. All of Us é uma camada adulta
multimodal, mas não possui fenótipo público suficiente de altas habilidades.

## Evidência observada por base

### ABCD/NDA

Os metadados públicos confirmam:

- NIH Toolbox com sete testes de memória, linguagem, atenção, flexibilidade,
  velocidade de processamento e percepção;
- compósitos fluido, cristalizado e total, incluindo escores corrigidos por idade;
- dados por evento/onda, permitindo desenho longitudinal;
- Fitbit com passos, sedentarismo, atividade leve/moderada/vigorosa, MET e
  frequência cardíaca de repouso;
- resumos diários e semanais de sono;
- instrumentos de TDAH, autismo, saúde mental, ambiente e neuroimagem.

O fenótipo defensável seria “desempenho cognitivo elevado no NIH Toolbox”, mantido
como escore contínuo e percentil. Ele não deve ser chamado automaticamente de
diagnóstico de superdotação. O acesso aos registros individuais exige aprovação.

**Modelos possíveis após acesso:**

1. trajetória latente dos compósitos cognitivos;
2. modelo misto sono/atividade → mudança cognitiva;
3. efeito heterogêneo por TDAH/autismo, sexo, renda e perfil cognitivo;
4. mediação atividade → sono → cognição;
5. integração de neuroimagem, cognição e comportamento;
6. previsão de mudança futura com validação por onda e por centro.

### NHANES — inspeção executada

Foram baixados nove arquivos oficiais do ciclo 2021–2023 e lidos com Pandas via
Pipenv. Resultados reproduzíveis:

| Arquivo | Linhas | Colunas | Participantes únicos |
|---|---:|---:|---:|
| DEMO_L | 11.933 | 27 | 11.933 |
| DSQTOT_L | 8.860 | 40 | 8.860 |
| PAQ_L | 8.153 | 8 | 8.153 |
| SLQ_L | 8.501 | 7 | 8.501 |
| DR1TOT_L | 8.860 | 168 | 8.860 |
| BMX_L | 8.860 | 22 | 8.860 |
| DPQ_L | 6.337 | 11 | 6.337 |
| VID_L | 8.727 | 10 | 8.727 |
| BPXO_L | 7.801 | 12 | 7.801 |

A interseção contém **6.337 adultos**, de 18 a 80 anos, mediana de 56 anos. Não há
menores nessa interseção. `DSQTOT_L` contém ingestão média diária proveniente de
suplementos para energia, macronutrientes, vitaminas, minerais e cafeína.

A interseção ampliada continua com 6.337 adultos. Entre eles, a cobertura é de
99,0% para sono em dias úteis, 99,9% para sedentarismo, 98,4% para IMC, 91,9% para
vitamina D sérica, 86,1% para PHQ-9 completo e 96,6% para médias de pressão. Energia
e proteína do recordatório e contagem de suplementos têm aproximadamente 79%.

O zero numérico dos arquivos SAS XPORT pode ser decodificado pelo Pandas como o
menor float IBM positivo (`5.397605346934028e-79`). O script converte esse valor
de volta para zero antes das estatísticas. Códigos documentados de recusa e
desconhecimento ainda precisam ser tratados variável por variável.

**Modelos possíveis agora:**

1. uso/contagem de suplementos por perfil demográfico;
2. classes latentes de padrões de suplementação;
3. sono em função de suplemento, cafeína e atividade, com ajuste demográfico;
4. modelos de interação suplemento × atividade;
5. ligação posterior com exames e dieta total do mesmo ciclo;
6. estimativas populacionais ponderadas, após adicionar os pesos apropriados.

**Modelos que não são válidos:** qualquer resultado “para superdotados”, uso de
escolaridade como proxy de superdotação ou inferência causal direta.

### OpenNeuro

A plataforma oferece conjuntos BIDS versionados, DOI por snapshot e API GraphQL.
A busca pública não revelou, nesta primeira inspeção, uma coorte grande e claramente
identificada de altas habilidades. Portanto, a unidade correta é o conjunto, não
o repositório inteiro.

**Filtro obrigatório de inclusão:** instrumento cognitivo informado, escores ou
percentis, grupo comparador, idade, método de recrutamento, diagnóstico/medicação,
licença e tamanho amostral.

**Modelos possíveis quando houver conjunto elegível:** conectividade funcional,
ERP/EEG, representação multimodal e replicação de efeitos. Amostras pequenas não
sustentam recomendadores de dieta ou rotina.

### All of Us

É promissor para EHR, medidas físicas, questionários, Fitbit e genômica em adultos.
O nível público é agregado; dados individuais ficam no Workbench. Escolaridade,
ocupação ou diagnóstico registrado não constituem identificação válida de altas
habilidades.

### ClinicalTrials.gov — inspeção executada

Duas consultas da API v2 retornaram 83 estudos para TDAH e 87 para autismo sob o
filtro de intervenção “Dietary Supplement”. Apenas 11 e 17 registros,
respectivamente, continham seção de resultados na resposta. Entre os nomes mais
frequentes estavam placebo, ômega-3, probióticos, melatonina e sulforafano.

Isso já demonstra que contagem de protocolos não equivale a evidência disponível.
Os nomes estão fragmentados (`Omega-3`, `Omega 3`, ácidos EPA/DHA etc.) e a consulta
também captura intervenções não suplementares. O grafo precisa de normalização de
entidade, classificação manual/semiautomática e um campo `has_results`.

**Uso adequado:** validar relações gerais de sono/atividade/saúde e, somente se
uma medida cognitiva adequada existir no nível autorizado, testar extremos
contínuos sem denominá-los diagnóstico clínico.

## Matriz pergunta → modelo

| Pergunta | Base mínima | Modelo | Status |
|---|---|---|---|
| Atividade prediz trajetória cognitiva elevada? | ABCD | modelo misto longitudinal | viável após acesso |
| Sono medeia associação atividade–cognição? | ABCD | mediação longitudinal/g-computation | viável após acesso, causalidade condicional |
| Quais suplementos se associam a sono em adultos? | NHANES | regressão ponderada/GAM | viável agora, observacional |
| Existem perfis de suplementação? | NHANES | classes latentes/NMF | viável agora |
| Há sinal adverso para ingrediente/produto? | CAERS + DSLD/PubChem | desproporcionalidade/grafo | viável agora, sem causalidade |
| Neurofisiologia distingue desempenho cognitivo extremo? | OpenNeuro/ABCD | multimodal hierárquico | depende de conjunto/acesso |
| Qual rotina funciona para cada pessoa? | coorte própria | N-of-1 bayesiano hierárquico | exige coleta prospectiva |
| Qual política é melhor para novos participantes? | múltiplos N-of-1 | efeito heterogêneo/bandit restrito | fase posterior |

## Próximas análises de maior valor

1. Acrescentar ao NHANES exames, dieta alimentar total e variáveis de saúde mental.
2. Definir antes da análise um conjunto pequeno de hipóteses e desfechos.
3. Criar o grafo ClinicalTrials–DSLD–PubChem–CAERS para evidência e segurança.
4. Preparar uma solicitação de acesso ao ABCD com análise e variáveis pré-registradas.
5. Desenhar a coorte prospectiva e o esquema N-of-1 descritos em
   [`REPORT_DATA_MODELS_GIFTEDNESS.md`](REPORT_DATA_MODELS_GIFTEDNESS.md).

## Fontes verificadas

- [ABCD Annual Release](https://nda.nih.gov/general-query.html?q=query%3Dfeatured-datasets%3AAdolescent+Brain+Cognitive+Development+Study+%28ABCD%29)
- [ABCD NIH Toolbox Summary Scores](https://nda.nih.gov/data-structure/abcd_tbss01)
- [ABCD Fitbit Weekly Physical Activity](https://nda.nih.gov/data-structure/abcd_fbwpas01)
- [OpenNeuro API](https://docs.openneuro.org/api.html)
- [NHANES datasets](https://wwwn.cdc.gov/nchs/nhanes/default.aspx)
- [NHANES supplement totals](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm)
