# Modelos para altas habilidades e dupla excepcionalidade

**Data:** 2026-09-07  
**Escopo:** TDAH, autismo, depressão, ansiedade/fobia social e outras condições
que podem coexistir com altas habilidades.

## Princípio de interpretação

Altas habilidades não implicam transtorno, e a presença de um transtorno não
implica altas habilidades. A literatura usa “dupla excepcionalidade” para a
coexistência de alta habilidade/talento e uma deficiência, transtorno ou condição
que afeta aprendizagem e funcionamento. A prevalência e os perfis reportados são
heterogêneos; não se deve chamar uma condição de “comum em superdotados” sem uma
estimativa adequada para a população e o critério utilizados. Uma revisão
sistemática encontrou resultados variados para problemas socioemocionais e
comportamentais nessa população
([Francis et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11061066/)).

O desenho deve preservar separadamente:

1. capacidade cognitiva e talentos;
2. sintomas dimensionais;
3. diagnóstico clínico e método de avaliação;
4. prejuízo funcional e necessidade de suporte;
5. contexto, medicação e intervenções;
6. pontos fortes, bem-estar e qualidade de vida.

## Estrutura comparativa mínima

Para cada condição, o modelo ideal compara quatro grupos sem reduzir a análise a
esses rótulos:

| Alta habilidade | Condição | Grupo analítico |
|---:|---:|---|
| não | não | referência populacional |
| sim | não | alta habilidade sem a condição estudada |
| não | sim | condição sem alta habilidade identificada |
| sim | sim | dupla excepcionalidade |

Os escores cognitivos e de sintomas devem permanecer contínuos. Os quatro grupos
servem para contrastes e interação, não para substituir os dados dimensionais.

Modelo básico:

```text
desfecho ~ habilidade + condição + habilidade×condição
           + idade + contexto + medicação + suporte
```

O termo de interação testa se a associação da condição com o desfecho muda ao
longo do perfil de habilidade. Não se deve interpretar um diagnóstico somente
a partir dessa interação.

## Comparações isoladas, duplas e triplas

O protocolo deve representar cada excepcionalidade como um indicador próprio,
sem criar uma categoria mutuamente exclusiva cedo demais:

```text
HA   = altas habilidades documentadas
ADHD = TDAH
ASD  = autismo
DEP  = depressão
SOC  = ansiedade/fobia social
SLD  = transtorno específico de aprendizagem
DCD  = transtorno do desenvolvimento da coordenação
OCD  = transtorno obsessivo-compulsivo
TIC  = Tourette/tiques
```

Cada participante recebe um vetor multilabel, por exemplo `HA=1, ADHD=1, ASD=1`.
Isso permite formar grupos sem apagar comorbidades.

### Nível 1 — excepcionalidade isolada

Comparar cada perfil sem outra condição modelada:

- `HA` versus referência sem HA e sem a condição analisada;
- `ADHD`, `ASD`, `DEP`, `SOC`, `SLD`, `DCD`, `OCD` e `TIC` isoladamente;
- análises dimensionais correspondentes, mesmo quando o diagnóstico é ausente.

“Isolada” significa que as demais condições incluídas no protocolo foram avaliadas
e não atendem ao critério. Ausência de registro não pode ser tratada como ausência
da condição.

### Nível 2 — dupla excepcionalidade

A análise primária de dupla excepcionalidade compara:

- `HA+ADHD`, `HA+ASD`, `HA+DEP`, `HA+SOC`, `HA+SLD`, `HA+DCD`, `HA+OCD` e `HA+TIC`;
- cada combinação contra três referências: HA isolada, condição isolada e grupo
  sem ambas;
- pares sem HA, como `ADHD+DEP` ou `ASD+SOC`, como comparadores clínicos quando
  houver amostra e justificativa.

Exemplo de contrastes para `HA+ADHD`:

| Contraste | Pergunta |
|---|---|
| `HA+ADHD` vs `HA` | o que o TDAH acrescenta entre pessoas com HA? |
| `HA+ADHD` vs `ADHD` | o que o perfil de HA modifica entre pessoas com TDAH? |
| `HA+ADHD` vs referência | qual é a diferença conjunta observada? |
| interação `HA×ADHD` | a combinação difere da soma dos efeitos isolados? |

### Nível 3 — tripla excepcionalidade

Tripla excepcionalidade será definida como `HA + condição A + condição B`, por
exemplo:

- `HA+ADHD+ASD`;
- `HA+ADHD+DEP`;
- `HA+ADHD+SLD`;
- `HA+ASD+SOC`;
- `HA+ASD+DEP`;
- `HA+SLD+DCD`.

Essas combinações são exemplos analíticos, não afirmações de prevalência. Cada
trio deve ser comparado a:

1. HA isolada;
2. cada condição isolada;
3. cada uma das três duplas contidas no trio;
4. referência sem os três atributos;
5. valor esperado pela soma dos efeitos principais, mediante interação tripla.

Exemplo:

```text
desfecho ~ HA + ADHD + ASD
           + HA×ADHD + HA×ASD + ADHD×ASD
           + HA×ADHD×ASD
           + confundidores
```

A interação tripla responde se o perfil conjunto difere do que seria esperado
pelos efeitos isolados e pelas duplas. Ela requer amostra muito maior e não deve
ser estimada de modo ingênuo quando alguma célula possui poucos participantes.

### Estratégia contra explosão combinatória

Com nove indicadores, testar todas as combinações gera muitas células pequenas e
falsos positivos. O plano deve:

- publicar contagens antes de escolher os contrastes;
- pré-especificar combinações clinicamente justificadas;
- exigir tamanho/precisão mínimos, sem usar um corte arbitrário como prova de validade;
- usar regressão hierárquica bayesiana com partial pooling para efeitos principais,
  duplos e triplos;
- aplicar shrinkage mais forte às interações de ordem superior;
- reportar intervalos e probabilidade de benefício/dano;
- agrupar somente quando houver equivalência substantiva, nunca apenas para obter
  significância;
- reservar coorte externa ou ondas futuras para confirmação.

Um modelo multinível recomendado é:

```text
resultado_it ~ perfil cognitivo_i + sintomas_i + intervenção_it
             + efeitos principais das excepcionalidades
             + interações duplas selecionadas
             + interações triplas selecionadas
             + pessoa + centro + tempo
```

Para previsão, usar multilabel learning ou mixture-of-experts. Para explicação
causal, manter estimandos separados por contraste; uma única classe “2e/3e” seria
heterogênea demais.

### Tabela obrigatória por estudo

Todo estudo deverá produzir, antes dos modelos:

| Campo | Conteúdo |
|---|---|
| combinação | vetor completo HA/condições |
| N total e por onda | participantes e observações |
| identificação | instrumento e critério de cada atributo |
| tratamento atual | medicamento, terapia, apoio educacional |
| desfechos | média/distribuição e dados ausentes |
| exposição | dieta, suplemento, exercício e sono |
| segurança | eventos adversos e interrupções |
| comparabilidade | diferenças basais e sobreposição |

Nenhuma comparação tripla será divulgada como conclusão firme se permitir
reidentificação, tiver baixa sobreposição ou incerteza incompatível com a alegação.

## Modelos compartilhados

### Perfil cognitivo assimétrico

Em vez de usar apenas QI total, modelar índices/subtestes e suas discrepâncias.
Pessoas duas vezes excepcionais podem apresentar pontos fortes e dificuldades
que se compensam em um escore agregado.

Modelos possíveis:

- fatores hierárquicos: fator geral + domínios específicos;
- profile analysis e classes latentes com estabilidade externa;
- modelos normativos que estimam desvio individual por domínio;
- crescimento longitudinal para separar atraso, estabilidade e recuperação;
- análise de invariância para verificar se a escala mede o mesmo construto nos
  diferentes grupos.

### Mascaramento e subidentificação

Capacidade elevada pode compensar sintomas em testes ou notas; sintomas podem
esconder talento. Um modelo de seleção deve representar que “ser identificado” é
um processo diferente de “possuir o perfil”.

```text
perfil real -> desempenho observado -> encaminhamento -> avaliação -> rótulo
      └──────── contexto/suporte/preconceito ────────────────┘
```

São úteis modelos de missing-not-at-random, correção de seleção e análise de
sensibilidade. Não se deve treinar um classificador apenas com casos encaminhados
e chamá-lo de prevalência populacional.

### Modelo transdiagnóstico

Uma camada comum pode representar dimensões que atravessam diagnósticos:

- atenção e controle inibitório;
- memória de trabalho e velocidade de processamento;
- comunicação social e flexibilidade;
- ansiedade/evitação e humor negativo;
- sono e regulação circadiana;
- sensibilidade sensorial;
- coordenação motora;
- funcionamento escolar, laboral e social.

Modelos fatoriais bifator, redes de sintomas e modelos hierárquicos bayesianos
podem compartilhar informação sem declarar que diagnósticos diferentes são a
mesma coisa.

## Modelos específicos

### TDAH

**Fenótipo:** sintomas de desatenção e hiperatividade/impulsividade, idade de
início, persistência em mais de um contexto, prejuízo funcional, informantes,
diagnóstico e medicação. Desempenho baixo isolado em teste de atenção não basta.

**Fontes:** ABCD/NDA é a principal; possui estruturas diagnósticas, sintomas,
NIH Toolbox, ambiente, sono, Fitbit e medicação. ClinicalTrials.gov fornece
evidência de intervenções adjacentes.

**Modelos:**

- quatro grupos habilidade × TDAH;
- trajetória de função executiva e sintomas por onda;
- resposta heterogênea de sono/exercício segundo medicação;
- modelo de efeito atrasado cafeína/estimulante → sono → atenção;
- N-of-1 para rotina de sono ou exercício, com medicação mantida estável;
- previsão de prejuízo funcional, não de diagnóstico automatizado.

**Risco central:** confundir tédio, assincronia educacional ou alta atividade com
TDAH; no sentido oposto, interpretar compensação cognitiva como ausência de
prejuízo.

### Autismo

**Fenótipo:** comunicação/interação social, padrões restritos/repetitivos,
sensorialidade, desenvolvimento, funcionamento adaptativo e método diagnóstico.
Separar traço dimensional, rastreio e diagnóstico clínico.

**Fontes:** NDA contém coleções de autismo e dados ABCD relacionados; OpenNeuro
pode fornecer EEG/MRI de conjuntos específicos; ClinicalTrials.gov oferece
protocolos de intervenções. O indicador `flag_pdd_asd` do NDA é um sinal de
triagem, não diagnóstico completo
([NDA subject structure](https://nda.nih.gov/data-structure/ndar_subject01)).

**Modelos:**

- quatro grupos habilidade × autismo;
- funcionamento adaptativo condicionado ao perfil cognitivo;
- perfil sensorial/social multimodal, preservando heterogeneidade;
- linguagem e cognição longitudinal por suporte recebido;
- efeito de sono e atividade sobre bem-estar, não sobre “reduzir autismo”;
- validação externa de biomarcadores, sem uso diagnóstico isolado.

**Risco central:** usar “alto funcionamento”, QI ou linguagem para inferir baixa
necessidade de suporte; patologizar interesses intensos ou traços sem prejuízo.

### Depressão

**Fenótipo:** sintomas, duração, recorrência, prejuízo, diagnóstico, tratamento,
ideação suicida e eventos de vida. PHQ-9 é rastreio dimensional, não diagnóstico.

**Fontes:** ABCD/NDA para trajetória juvenil; NHANES possui PHQ-9 em adultos,
sono, dieta, suplemento, vitamina D, atividade, IMC e pressão, mas não mede altas
habilidades.

**Modelos:**

- PHQ-9 ordinal/contínuo com análise de itens;
- trajetória de sintomas internalizantes;
- sono como mediador ou confundidor variante no tempo;
- relação atividade–humor com causalidade reversa explícita;
- modelo de recaída somente em coorte longitudinal;
- N-of-1 comportamental com regra clínica de segurança.

**Risco central:** concluir que vitamina D, suplemento ou exercício tratou
depressão a partir de associação transversal. Ideação suicida exige protocolo
assistencial e não deve alimentar recomendação automatizada.

### Ansiedade e fobia social

**Fenótipo:** medo, antecipação, evitação, sintomas físicos, duração, prejuízo e
contexto. Timidez, introversão e preferência por interesses especializados não
equivalem a fobia social.

**Fontes:** NDA possui estruturas com escalas de ansiedade social, como MASC, e
medidas de ansiedade/evitação. A estrutura MASC registra escore total de ansiedade
social ([NDA MASC](https://nda.nih.gov/data-structure/masc_p01)). ABCD oferece
medidas internalizantes e diagnósticas conforme a onda.

**Modelos:**

- hurdle model: presença de evitação + intensidade/prejuízo;
- trajetória social contextualizada por ambiente escolar/laboral;
- rede ansiedade–sono–sensibilidade–funcionamento;
- mediação de exposição social e suporte;
- resposta heterogênea a exercício/sono, sem substituir psicoterapia;
- análise por informante para divergência jovem–responsável.

**Risco central:** atribuir isolamento ao perfil intelectual e deixar de medir
sofrimento, ou patologizar uma preferência social não prejudicial.

### Transtornos específicos de aprendizagem

Incluem dislexia, discalculia e dificuldades de expressão escrita quando avaliadas
por critérios apropriados.

**Fenótipo:** habilidade geral, desempenho acadêmico normatizado, resposta à
instrução, histórico, domínio específico e prejuízo. A discrepância QI–desempenho
isolada não deve ser o único critério.

**Modelos:**

- modelo normativo por domínio acadêmico;
- perfil de discrepâncias com erro de medida;
- crescimento após intervenção educacional;
- detecção de força e dificuldade simultâneas;
- interação suporte × perfil, priorizando desfecho funcional.

**Fontes:** NDA/ABCD para cognição, leitura, ambiente e desenvolvimento; uma
coorte própria precisa de instrumentos diagnósticos específicos.

### Coordenação motora e transtorno do desenvolvimento da coordenação

Relevante para exercício, calistenia e artes marciais porque desempenho motor
baixo não representa capacidade intelectual baixa.

**Modelos:** curva de aprendizagem motora, precisão–velocidade, variabilidade
intraindividual, risco de lesão e adaptação de treino. Sensores e vídeo podem medir
movimento, mas o diagnóstico exige avaliação apropriada.

### Tourette/tiques e OCD

Devem permanecer fenótipos separados, embora possam coexistir com TDAH/autismo.
Modelos úteis incluem séries temporais de frequência/intensidade, estresse, sono,
medicação e interferência funcional. Não inferir compulsão a partir de dedicação
intensa ou rotina preferida.

### Ansiedade generalizada, burnout e estresse

Burnout não deve ser usado como sinônimo de depressão. Modelar exaustão, carga,
recuperação, demandas, controle e conflito pessoa–ambiente. Para ansiedade, guardar
conteúdo, duração e prejuízo, além do escore total.

## Matriz de dados e modelos

| Condição | Melhor fonte catalogada | Modelo inicial | Desfecho prioritário |
|---|---|---|---|
| TDAH | ABCD/NDA | misto longitudinal + interação | funcionamento/atenção |
| Autismo | NDA + OpenNeuro | normativo multimodal | funcionamento e bem-estar |
| Depressão juvenil | ABCD/NDA | trajetória/estado-espaço | sintomas e funcionamento |
| Depressão adulta geral | NHANES | survey-weighted, transversal | PHQ-9; sem inferir alta habilidade |
| Fobia/ansiedade social | NDA/MASC | hurdle + longitudinal | evitação e prejuízo |
| Dislexia/discalculia | NDA + coorte específica | normativo por domínio | aprendizagem e suporte |
| Coordenação motora | coorte + sensores | curva de aprendizagem | função, técnica e lesão |
| Tourette/OCD | NDA + coorte | séries temporais | interferência funcional |
| Perfil transdiagnóstico | ABCD/NDA | bifator/hierárquico | qualidade de vida e função |

## Personalização de dieta, suplemento, exercício e sono

O modelo de intervenção deve estimar efeitos por condição e por pessoa:

```text
resultado_it = capacidade_i + condição_i + perfil_i
             + intervenção_it
             + intervenção×condição
             + intervenção×perfil
             + medicação_it + suporte_it
             + tempo + erro
```

Regras mínimas:

- uma intervenção por vez ou desenho fatorial com potência suficiente;
- estabilizar/documentar medicamento e terapia;
- incluir prejuízo e bem-estar, não somente desempenho cognitivo;
- modelar efeitos atrasados sobre sono e humor;
- usar filtro de contraindicação antes do recomendador;
- não recomendar tratar autismo ou altas habilidades com suplemento;
- suspender automação diante de risco clínico ou ideação suicida.

## Validação

Cada modelo deve ser avaliado:

- dentro e fora do grupo duas vezes excepcional;
- por idade, sexo, contexto socioeconômico e método de identificação;
- com calibração e incerteza, não somente acurácia;
- por centro/onda e em uma coorte externa;
- contra um modelo simples e contra ausência de intervenção;
- quanto a benefício, dano, equidade e carga de adesão.

O objetivo não é prever rótulos a partir de comportamento digital. É explicar
heterogeneidade, reduzir subidentificação e testar intervenções seguras com
desfechos relevantes para cada pessoa.
