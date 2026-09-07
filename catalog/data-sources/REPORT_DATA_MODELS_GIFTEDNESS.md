# Relatório: modelos de dados para saúde, desempenho e altas habilidades

**Data:** 2026-09-07  
**Escopo:** fontes públicas de [`sources.yaml`](sources.yaml)  
**Caso de uso:** investigar quais padrões de dieta, suplementação, exercício e
sono beneficiam pessoas com altas habilidades/superdotação.

## Resumo executivo

As fontes públicas permitem construir modelos de descoberta de hipóteses,
harmonização, previsão e segurança. Elas não permitem, isoladamente, identificar
uma combinação universalmente ótima para pessoas superdotadas.

O obstáculo principal não é algorítmico. Quase nenhuma base mede, na mesma pessoa
e longitudinalmente, uma definição válida de superdotação, dieta, suplementos,
treino, sono, cognição, bem-estar e eventos adversos. “Superdotação” também não
possui uma única operacionalização: estudos usam testes de inteligência,
desempenho acadêmico, criatividade ou modelos multidimensionais. Uma revisão
sistemática encontrou heterogeneidade de critérios e falta de padronização que
dificultam comparações entre estudos
([Gilar-Corbi et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11615676/)).

A arquitetura recomendada possui três camadas:

1. **Evidência pública:** gera hipóteses, referências e sinais de segurança.
2. **Coorte prospectiva específica:** identifica altas habilidades explicitamente
   e mede exposições, confundidores e desfechos de forma harmonizada.
3. **Ensaios N-of-1:** estimam a resposta de cada pessoa; um modelo hierárquico
   aprende quais perfis respondem a quais intervenções.

O resultado legítimo não seria “a dieta dos superdotados”, mas: **para uma pessoa
com este perfil, histórico e objetivo, qual intervenção apresenta a melhor relação
esperada entre benefício, risco, custo e carga de adesão?**

## 1. Definição do problema

### 1.1 O que significa benefício

Maximizar somente um teste cognitivo pode piorar sono, ansiedade ou lesões. O
benefício deve ser multiobjetivo:

- cognição: atenção, memória de trabalho, velocidade e flexibilidade;
- funcionamento: trabalho profundo, tarefas concluídas e taxa de erro;
- bem-estar: humor, ansiedade, irritabilidade, energia e qualidade de vida;
- sono: duração, regularidade, latência, despertares e sonolência;
- físico: força relativa, potência, rounds e recuperação;
- segurança: pressão, frequência cardíaca, sintomas, dor e lesão;
- viabilidade: custo, tolerabilidade, complexidade e adesão.

Uma intervenção somente é “melhor” segundo preferências declaradas e restrições
mínimas de segurança.

### 1.2 Fenótipo de altas habilidades

Não se deve inferir superdotação por profissão, escolaridade, diagnóstico,
rendimento ou autoclassificação isolada. O modelo deve registrar:

- instrumento, versão, idioma, normas e data da avaliação;
- escores compostos e subescalas, preservados como variáveis contínuas;
- critério usado no estudo, inclusive percentil ou modelo multidimensional;
- domínio intelectual, acadêmico, criativo ou talento específico;
- avaliação profissional versus triagem/autorrelato;
- TDAH, autismo, transtornos de aprendizagem e medicamentos;
- idade e contexto educacional, social e cultural.

Categorias como “QI ≥ 130” podem compor análises secundárias, mas desperdiçam
informação e ampliam erros perto do corte. Pessoas com altas habilidades e uma
condição neurodesenvolvimental devem formar estratos explícitos. Revisões apontam
falta de consenso e necessidade de estudos longitudinais nessa interseção
([Romano et al.](https://pubmed.ncbi.nlm.nih.gov/36040826/)).

## 2. Papel das fontes públicas

| Fonte | Papel | Variáveis úteis | Lacuna principal |
|---|---|---|---|
| NHANES | população e associações | dieta, suplementos, exames, atividade | não identifica altas habilidades |
| ClinicalTrials.gov | intervenções | dose, duração, desfecho, evento adverso | resultados podem faltar; população inespecífica |
| ODS | síntese de evidência | eficácia, segurança e interação | sem microdados |
| DSLD | ontologia de produtos | ingrediente, forma, dose e rótulo | declaração não comprova conteúdo |
| DSID | calibração | conteúdo analisado de algumas categorias | cobertura parcial de produtos |
| PubChem | grafo químico | identificadores, alvos e toxicologia | mecanismo não prova eficácia clínica |
| openFDA CAERS | vigilância | produto, reação, gravidade e desfecho | sem denominador e sem causalidade |
| OpenNeuro | neurofisiologia | EEG, MRI e tarefas | exposições comportamentais escassas |
| PhysioNet aberto | sinais | ECG, EEG, PPG e sono | população clínica; sem superdotação |
| DATASUS | contexto brasileiro | morbidade, território e serviços | baixa resolução para este objetivo |
| Anvisa | regulação e segurança | alertas e notificações agregadas | microdados/API limitados |
| Open Humans público | protótipo pessoal | wearables, diários e genômica | autoseleção e heterogeneidade |

NDA/ABCD, All of Us e NSRR seriam úteis posteriormente, mas dados individuais
dependem de credenciais ou aprovação. Ver [`ACCESS_FROM_CODEX.md`](ACCESS_FROM_CODEX.md).

## 3. Modelos que podem ser construídos

### 3.1 Modelo comum de observações

É a fundação do projeto: harmoniza nomes, unidades, janelas e proveniência.

```text
Participant ──< Observation >── MeasureDefinition
     ├──< GiftednessAssessment
     ├──< Diagnosis
     ├──< MedicationExposure
     ├──< SupplementExposure >── Product ──< Ingredient ── PubChem
     ├──< DietExposure
     ├──< ExerciseSession
     ├──< SleepEpisode
     └──< Outcome
```

O modelo deve distinguir produto, ingrediente e exposição. “Creatina” não basta:
são necessários forma química, dose, horário, duração, produto/lote e adesão. Para
treino: modalidade, volume, intensidade, duração e carga interna. Para sono:
episódio, origem da medida e resumo diário.

### 3.2 Grafo de conhecimento de evidências

Integra produto, ingrediente, nutriente, intervenção, população, mecanismo,
desfecho, estudo e evento adverso.

```text
produto CONTAINS ingrediente
ingrediente HAS_COMPOUND PubChem_ID
ensaio TESTS ingrediente
ensaio MEASURES desfecho
estudo INCLUDES população
relato SUSPECTS produto
ingrediente INTERACTS_WITH medicamento
evidência SUPPORTS/CONTRADICTS hipótese
```

Cada relação deve guardar fonte, desenho, amostra, estimativa, incerteza, data e
qualidade. O grafo responde o que já foi testado e quais riscos impedem um teste;
não prescreve sozinho.

### 3.3 Fenotipagem e estratificação

Análise fatorial pode reduzir escalas correlacionadas; classes latentes e
agrupamento estável podem descrever perfis por cognição, cronotipo, sono, dieta,
atividade, comorbidade e medicação. Clusters são exploratórios e não devem receber
rótulos clínicos automaticamente. Seu uso é descobrir modificadores de efeito.

### 3.4 Associação populacional

NHANES permite regressões ponderadas e dose–resposta, por exemplo:

```text
biomarcador ~ suplemento + dieta + idade + sexo + renda + atividade + saúde
```

Isso prioriza hipóteses e estima prevalência, mas não demonstra causalidade. Há
causalidade reversa, viés do usuário saudável, autorrelato e múltiplos testes.

### 3.5 Modelos causais

Cada pergunta deve definir população, intervenção, comparador, horizonte, desfecho
primário e estimando. Exemplo: “entre adultos com avaliação documentada de alta
habilidade e sono irregular, qual o efeito de oito semanas de horário regular,
comparado à rotina usual, sobre atenção sustentada?”

Um DAG mínimo inclui cronotipo, estresse, medicação, rotina escolhida, sono e
cognição. Propensity score, g-computation e modelos estruturais marginais podem
ajudar, mas continuam dependentes de confundidores medidos; não corrigem uma base
inadequada.

### 3.6 Séries temporais e efeitos atrasados

Modelos mistos, estado-espaço e distributed lag separam diferenças entre pessoas
da variação interna. Devem representar atrasos: treino pode reduzir desempenho no
dia seguinte e melhorá-lo semanas depois; cafeína pode ajudar hoje e prejudicar o
sono e o resultado de amanhã.

```text
resultado_it = perfil_i + efeito_pessoal_i(intervenção_it)
             + sono_it + treino_it + tendência_t + ruído_it
```

### 3.7 Ensaios N-of-1 e resposta hierárquica

Blocos randomizados alternam intervenção e controle, com washout quando aplicável,
desfecho pré-registrado e regra de interrupção. Vários N-of-1 podem ser agregados:

```text
efeito_pessoal_i ~ distribuição(grupo, perfil_i)
```

Cada participante aprende sobretudo com os próprios dados e parcialmente com
pessoas semelhantes. A saída deve mostrar probabilidade de benefício relevante e
de dano, não somente um ranking.

### 3.8 Recomendação multiobjetivo

Após evidência prospectiva, modelos de efeito heterogêneo ou contextual bandits
podem escolher apenas entre alternativas previamente consideradas seguras:

```text
utilidade = cognição + bem-estar + desempenho físico
            - evento adverso - lesão - custo - carga de adesão
```

Contraindicação, interação, idade, dose máxima e regras de interrupção são
restrições duras. Aprendizado por reforço livre não é apropriado para explorar
intervenções potencialmente perigosas.

### 3.9 Vigilância de segurança

openFDA e Anvisa permitem detectar desproporcionalidade e coocorrência de sintomas.
Isso prioriza revisão, mas não estima incidência. O próprio CAERS adverte que os
relatos variam em completude e não estabelecem causalidade
([documentação FDA](https://www.fda.gov/files/food/published/Read-Me-File-For-CFSAN-Adverse-Event-Reporting-System-Quarterly-Data-Extract.pdf)).

## 4. Caso de uso proposto

### 4.1 Pergunta adequada

Em vez de buscar uma solução universal:

1. quais intervenções possuem evidência e segurança razoáveis na população
   aplicável, e quais lacunas existem para altas habilidades?
2. entre alternativas elegíveis, qual produz benefício líquido em cada pessoa e
   quais características predizem respostas semelhantes?

### 4.2 Coorte mínima

- avaliação de altas habilidades documentada, com escores contínuos;
- estratificação de TDAH/autismo, condições clínicas e medicamentos;
- baseline de quatro a oito semanas sem mudanças simultâneas;
- dieta e suplemento com produto, dose, horário e adesão;
- treino por sessão, modalidade, carga externa e interna;
- sono por diário e, opcionalmente, wearable;
- teste cognitivo curto, repetível e resistente a efeito de prática;
- bem-estar e funcionamento medidos semanalmente;
- eventos adversos e critérios clínicos de interrupção.

### 4.3 Etapas

1. **Mapa de evidência:** integrar ClinicalTrials.gov, ODS, DSLD/DSID, PubChem e
   CAERS para selecionar candidatos, doses estudadas e riscos.
2. **Baseline observacional:** modelar relações internas entre sono, alimentação,
   treino e desfechos.
3. **Intervenções comportamentais:** testar primeiro sono, distribuição de treino
   e refeições, separadamente.
4. **Suplementação:** apenas com identidade, dose, evidência e contraindicações
   revistas. Deficiências devem ser diagnosticadas e tratadas clinicamente.
5. **Personalização:** agregar N-of-1, estimar modificadores e validar a política
   prospectivamente em novos participantes.

### 4.4 Primeiro estudo sugerido

Testar **regularidade do horário de sono** antes de pacotes multicomponentes:

- população: adultos com altas habilidades documentadas;
- intervenção: janela regular de dormir/acordar;
- comparador: rotina usual;
- desenho: blocos randomizados compatíveis com segurança;
- primário: atenção sustentada ou produtividade pré-definida;
- secundários: humor, sono, força relativa e recuperação;
- covariáveis: cronotipo, cafeína, medicação, treino e estresse;
- análise: N-of-1 hierárquico com efeitos atrasados;
- decisão: benefício mínimo relevante sem piora de segurança/bem-estar.

Depois, dieta, exercício e suplementos podem ser testados individualmente. Mudar
quatro dimensões simultaneamente impede atribuir o resultado.

## 5. Limites do conhecimento atual

### Possível agora

- catálogo harmonizado de ensaios, ingredientes, produtos e eventos adversos;
- grafo de evidências para desfechos cognitivos e físicos;
- modelos NHANES de dieta, suplemento, atividade e biomarcadores;
- modelos de sinais de sono, ECG/EEG e atividade;
- mapa de lacunas e protocolo de coorte específica.

### Não demonstrável somente com essas bases

- dieta universalmente ótima para superdotados;
- causalidade a partir de associação observacional;
- conteúdo real de produto a partir do rótulo;
- segurança individual pela ausência de relatos;
- resposta específica extrapolada de qualquer amostra geral;
- efeito de quatro intervenções sem desenho que as separe;
- diagnóstico de superdotação por EEG, genômica ou wearable.

A literatura específica de exercício ilustra a lacuna: uma revisão de 2026
localizou apenas quatro estudos em estudantes com altas habilidades, pequenos e
heterogêneos, e pediu estudos longitudinais e experimentais
([Rodríguez-López et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211203/)).

## 6. Vieses e validação

| Risco | Mitigação mínima |
|---|---|
| definição variável | instrumento, escore contínuo e critério registrados |
| renda e educação | medir contexto e fazer sensibilidade |
| TDAH/autismo e medicação | estratificar e testar interação |
| efeito de prática | versões alternadas, familiarização e tendência temporal |
| wearable impreciso | registrar dispositivo/firmware e validar subamostra |
| recordatório alimentar | vários dias e erro de medição explícito |
| muitos desfechos | primário pré-definido e controle de multiplicidade |
| regressão à média | baseline longo, randomização e blocos repetidos |
| seleção | documentar recrutamento e validar externamente |
| vazamento temporal | separar treino/teste por tempo e pessoa |

Validação deve incluir calibração, incerteza, benefício líquido, controles
negativos, replicação temporal e avaliação por subgrupo. Acurácia média não basta
se o modelo falhar em pessoas duas vezes excepcionais ou medicadas.

## 7. Ética e governança

- coletar o mínimo necessário e separar identidade da base analítica;
- consentir especificamente saúde, genética, wearables e reutilização;
- permitir retirada/exportação quando aplicável;
- versionar protocolos, instrumentos e modelos;
- impedir uso para negar educação, emprego ou assistência;
- envolver a população estudada no desenho;
- observar LGPD, acordos de fonte e CEP/CONEP quando aplicável.

Com menores, exigem-se responsável, assentimento, risco mínimo e supervisão. Não
cabe experimentação de medicamento, hormônio ou suplemento de desempenho sem
justificativa clínica e aprovação formal.

## 8. Arquitetura técnica

```text
fontes públicas -> camada bruta versionada -> modelo harmonizado
                                             ├─ grafo de evidência
                                             ├─ modelos de referência
                                             └─ sinais de segurança
                                                        │
                                               coorte + N-of-1
                                                        │
                                         efeito individual/subgrupo
                                                        │
                                  recomendação explicável e restrita
```

Implementação inicial: arquivos brutos imutáveis, Parquet, DuckDB, identificadores
padronizados, testes de esquema/unidade, proveniência por estimativa, modelo
bayesiano ou misto, data sheets e model cards.

## 9. Recomendação final

O projeto é viável como plataforma de **geração e teste progressivo de hipóteses**,
mas as bases atuais não sustentam um recomendador confiável específico para
superdotados. O primeiro entregável deve ser o grafo de evidências e o modelo
comum; o segundo, um protocolo prospectivo de baseline e sono; o terceiro, N-of-1
comportamentais. Suplementos entram somente após triagem de evidência e segurança.

Essa abordagem começa com o conhecido, torna as lacunas explícitas e aprende a
resposta individual sem presumir que altas habilidades constituam uma fisiologia
nutricional homogênea.

As comparações entre altas habilidades, TDAH, autismo, depressão, fobia social e
outras condições — isoladas, duplas e triplas — são especificadas em
[`TWICE_EXCEPTIONAL_MODELS.md`](TWICE_EXCEPTIONAL_MODELS.md) e no esquema
[`exceptionality-comparison-schema.yaml`](exceptionality-comparison-schema.yaml).

O desenho central com altas habilidades como foco, autismo e TDAH como grupos
comparadores de validação e neurotípicos como referência operacional está em
[`CORE_STUDY_DESIGN.md`](CORE_STUDY_DESIGN.md).

## Referências centrais

- [Catálogo das fontes](sources.yaml)
- [Matriz de acesso](ACCESS_FROM_CODEX.md)
- [NHANES](https://www.cdc.gov/nchs/nhanes/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [NIH Office of Dietary Supplements](https://ods.od.nih.gov/)
- [OpenNeuro](https://openneuro.org/)
- [PhysioNet](https://physionet.org/)
- [openFDA CAERS](https://open.fda.gov/data/caers/)
- [Revisão sobre identificação de superdotação](https://pmc.ncbi.nlm.nih.gov/articles/PMC11615676/)
- [Revisão sobre altas habilidades e neurodesenvolvimento](https://pubmed.ncbi.nlm.nih.gov/36040826/)
- [Revisão de atividade física e altas habilidades](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211203/)
