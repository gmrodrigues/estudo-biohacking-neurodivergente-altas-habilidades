# Desenho central: altas habilidades, autismo, TDAH e neurotípicos

**Data:** 2026-09-07  
**Foco primário:** altas habilidades (HA)  
**Comparadores de validação:** autismo (ASD), TDAH (ADHD) e neurotípicos (NT)

## Objetivo

Estudar altas habilidades como um perfil multidimensional e usar autismo e TDAH
para testar quais achados são específicos de HA, compartilhados com outras formas
de neurodivergência ou explicados por sintomas coexistentes. No sentido inverso,
usar os perfis de força observados em HA para investigar heterogeneidade,
compensação e desempenho preservado em autismo e TDAH.

Autismo e TDAH são **grupos comparadores**, não controles saudáveis. O grupo NT é
a referência populacional operacional. “Neurotípico” significa que os instrumentos
aplicados não identificaram HA, ASD ou ADHD segundo os critérios pré-especificados;
não significa ausência de toda diferença, sintoma ou condição humana.

## Grupos centrais

| Código | HA | ASD | ADHD | Papel |
|---|---:|---:|---:|---|
| NT | 0 | 0 | 0 | referência operacional |
| HA | 1 | 0 | 0 | grupo focal isolado |
| ASD | 0 | 1 | 0 | segundo comparador; valida especificidade social/sensorial |
| ADHD | 0 | 0 | 1 | comparador de validação executiva/atencional |
| HA+ASD | 1 | 1 | 0 | dupla excepcionalidade |
| HA+ADHD | 1 | 0 | 1 | dupla excepcionalidade |
| ASD+ADHD | 0 | 1 | 1 | dupla neurodivergência sem HA identificada |
| HA+ASD+ADHD | 1 | 1 | 1 | tripla excepcionalidade principal |

Depressão, ansiedade/fobia social, transtornos de aprendizagem, coordenação, OCD
e tiques entram inicialmente como fenótipos dimensionais e modificadores. Tornam-se
novas células apenas quando identificação e amostra suportarem comparações válidas.

## Comparações obrigatórias

### Altas habilidades versus neurotípicos

Estima o perfil associado a HA em cognição, sono, atividade, saúde mental,
desempenho físico e resposta a intervenções. É a comparação focal, mas não define
sozinha especificidade.

### Altas habilidades versus autismo

É a seção de comparação solicitada. Deve avaliar:

- perfil cognitivo global e assimetria entre domínios;
- atenção, flexibilidade e velocidade de processamento;
- comunicação social, funcionamento adaptativo e sensorialidade;
- sono, ansiedade, depressão e qualidade de vida;
- interesses intensos, motivação e aprendizagem, sem patologização automática;
- resposta e tolerabilidade a dieta, suplementos, exercício e sono.

Interpretação:

- uma semelhança HA–ASD não prova mecanismo comum;
- uma diferença média não diagnostica indivíduos;
- linguagem ou QI alto não equivale a baixa necessidade de suporte;
- o grupo `HA+ASD` é indispensável: sem ele, a comparação força pessoas reais em
  categorias incompletas.

### Altas habilidades versus TDAH

Testa se diferenças em atenção, inibição, variabilidade de resposta e organização
são específicas de ADHD, de HA, ou da combinação `HA+ADHD`. Deve incluir prejuízo
funcional e informantes, não apenas teste de atenção.

### Autismo versus TDAH

Funciona como validação diferencial: verifica se um marcador supostamente ligado
a HA é, na verdade, compartilhado por neurodivergência, sono ou comorbidade. O
grupo `ASD+ADHD` evita atribuir sobreposição a somente um diagnóstico.

### Duplas e tripla

Cada dupla é comparada com NT, HA, ASD e ADHD conforme seus componentes. A tripla
`HA+ASD+ADHD` é comparada com:

- NT;
- HA, ASD e ADHD isolados;
- HA+ASD, HA+ADHD e ASD+ADHD;
- valor previsto por efeitos principais e interações duplas.

## Modelo estatístico central

Não usar uma coluna de grupo exclusiva como única representação. Preservar os
indicadores e escores contínuos:

```text
Y = HA + ASD + ADHD
    + HA×ASD + HA×ADHD + ASD×ADHD
    + HA×ASD×ADHD
    + idade + sexo/gênero + contexto + centro + tempo
    + medicação + terapia + suporte + erro
```

Para repetição temporal, incluir intercepto e inclinações individuais. Interações
recebem regularização hierárquica forte. Se células forem pequenas, reportar a
incerteza ou não estimar; não fundir grupos substantivamente diferentes para obter
significância.

## Uso recíproco dos grupos

### O que HA pode ajudar a investigar em ASD/ADHD

- forças preservadas ocultas por escores globais;
- compensação que mascara prejuízo funcional;
- discrepâncias entre capacidade e execução cotidiana;
- aprendizagem rápida em domínio específico;
- desenho de suporte baseado em forças, não somente déficits.

### O que ASD/ADHD ajudam a verificar em HA

- se variabilidade executiva atribuída a HA é explicada por ADHD;
- se traços sociais/sensoriais atribuídos a HA são explicados por ASD;
- se sono, ansiedade e depressão mediam associações aparentes;
- se um marcador cognitivo é específico, transdiagnóstico ou artefato de seleção;
- se uma intervenção melhora desempenho ou apenas reduz um prejuízo coexistente.

O objetivo é compreensão recíproca, não usar HA como modelo de autismo/TDAH nem
usar autismo/TDAH como explicação geral de altas habilidades.

## Validação de toda hipótese

Cada hipótese ou achado deve passar pela matriz abaixo:

| Etapa | Teste obrigatório |
|---|---|
| descoberta | estimar em amostra/onda previamente designada |
| HA vs NT | verificar efeito focal |
| HA vs ASD | testar especificidade frente ao segundo comparador |
| HA vs ADHD | testar especificidade executiva/atencional |
| duplas | verificar modificação por coexistência |
| tripla | estimar com partial pooling ou declarar dados insuficientes |
| sintomas | repetir com escores dimensionais, não só diagnósticos |
| tratamento | ajustar/estratificar medicação, terapia e suporte |
| replicação | nova onda, centro ou base externa |
| robustez | controles negativos, ausências, seleção e múltiplos testes |

Um achado será classificado como:

- **específico de HA:** replica em HA e difere dos comparadores;
- **transdiagnóstico:** aparece em HA, ASD e/ou ADHD associado a uma dimensão;
- **condicionado:** aparece apenas em dupla/tripla ou sob tratamento/contexto;
- **não replicado:** falha no conjunto de validação;
- **indeterminado:** precisão, medição ou sobreposição insuficientes.

## Hipóteses de suplementação neste desenho

Todas as hipóteses de [`SUPPLEMENTATION_HYPOTHESES.md`](SUPPLEMENTATION_HYPOTHESES.md)
devem incluir `suplemento×HA`, `suplemento×ASD`, `suplemento×ADHD` e apenas as
interações duplas/tripla pré-especificadas.

Exemplos:

- cafeína/L-teanina: benefício agudo versus sono/ansiedade em todos os grupos;
- creatina: desempenho absoluto e relativo, sem pressupor efeito neurodivergente;
- ômega-3: hipótese adjunta em ADHD, validada em HA+ADHD e HA+ASD+ADHD;
- melatonina: efeito sobre sono, não sobre identidade diagnóstica;
- B12/folato/metilação: estado basal e biomarcadores antes de genótipo/grupo;
- ashwagandha/GABA/magnésio: tolerabilidade e sedação comparadas entre grupos;
- micronutrientes: benefício condicionado à inadequação/deficiência.

A hipótese nula primária é que HA, ASD ou ADHD **não modificam** a resposta quando
estado nutricional, sintomas, medicação, sono e contexto são controlados. Qualquer
personalização por rótulo exige replicação.

## Bases e divisão de trabalho

| Base | Papel |
|---|---|
| ABCD/NDA | descoberta longitudinal principal em jovens; cognição, ADHD, ASD, sono e atividade |
| OpenNeuro | replicação neurofisiológica em conjuntos com fenótipos válidos |
| NHANES | referência geral para dieta, suplementos, sono, depressão e biomarcadores; sem HA/ASD/ADHD completos |
| ClinicalTrials.gov | mapa de intervenções em ASD/ADHD e resultados disponíveis |
| All of Us | validação adulta geral quando variáveis autorizadas forem adequadas |
| coorte própria | oito grupos centrais e intervenções N-of-1 |

ABCD não deve ser dividido em grupos com base em um único campo. HA requer compósito
cognitivo e critério documentado; ASD/ADHD requerem estrutura diagnóstica e sintomas;
NT requer avaliação explícita dos três e das exclusões definidas.

## Desfechos compartilhados

Para comparação legítima, todos os grupos devem receber o mesmo núcleo:

- compósitos e subtestes cognitivos;
- função executiva cotidiana;
- sintomas ASD/ADHD dimensionais;
- depressão, ansiedade social e funcionamento;
- sono e cronotipo;
- dieta, suplementos e medicamentos;
- atividade, aptidão e desempenho físico;
- funcionamento adaptativo, acadêmico/laboral e qualidade de vida;
- efeitos adversos e adesão.

Instrumentos adicionais específicos podem existir, mas não substituem esse núcleo.

## Estratificação transversal

Todas as células centrais serão descritas e, quando houver dados suficientes,
comparadas por ciclo de vida, sexo/gênero, profissão, escolaridade, criatividade e
inclinação artística. A especificação completa está em
[`STRATIFICATION_MODEL.md`](STRATIFICATION_MODEL.md) e
[`stratification-schema.yaml`](stratification-schema.yaml).

Essas dimensões são moderadores e contextos, não critérios substitutos de HA,
autismo ou TDAH. Idade permanece contínua no modelo; faixas são usadas para
descrição. Correlações agregadas sempre serão confrontadas com correlações dentro
dos estratos para reduzir interpretações decorrentes do paradoxo de Simpson.

## Critérios de parada

- baixa amostra ou ausência de sobreposição entre grupos;
- definição circular, como usar atenção para formar ADHD e depois “predizer” ADHD
  com o mesmo escore;
- risco de reidentificação em combinações raras;
- evento adverso grave ou piora clínica;
- achado dependente de uma única decisão analítica não pré-especificada;
- ausência de replicação após múltiplas tentativas independentes.
