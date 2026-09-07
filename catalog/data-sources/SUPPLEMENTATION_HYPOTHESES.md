# Registro inicial de hipóteses sobre suplementação

**Versão:** 0.1  
**Data:** 2026-09-07  
**Natureza:** hipóteses de pesquisa, não recomendações clínicas.

## Regras gerais

- Altas habilidades não são deficiência nutricional nem indicação de suplemento.
- Corrigir deficiência documentada é uma questão clínica diferente de buscar
  efeito ergogênico ou cognitivo em pessoa com estado nutricional adequado.
- Cada hipótese será testada em excepcionalidade isolada, dupla e tripla conforme
  [`TWICE_EXCEPTIONAL_MODELS.md`](TWICE_EXCEPTIONAL_MODELS.md).
- Medicamentos, terapia, dieta, sono e carga de treino devem ser registrados.
- Misturas proprietárias e várias mudanças simultâneas não entram na primeira fase.
- O desfecho primário e o efeito mínimo relevante devem ser definidos antes de
  observar os resultados.
- Eventos adversos, piora de sono/humor e interação medicamentosa podem anular um
  ganho pequeno de desempenho.

## Priorização

| ID | Hipótese | Prioridade | Pode começar com dados atuais? |
|---|---|---:|---|
| H01 | horário da cafeína: ganho agudo versus prejuízo de sono | alta | parcialmente, NHANES + coorte |
| H02 | creatina: potência/repetição com custo de aumento de massa | alta | ensaios + coorte esportiva |
| H03 | ômega-3: possível efeito adjunto em sintomas de TDAH | média | ClinicalTrials; coorte necessária |
| H04 | melatonina: regularidade/latência do sono, não “cognição” direta | média | ClinicalTrials; coorte necessária |
| H05 | vitamina D: benefício concentrado em deficiência | alta | sim, NHANES observacional |
| H06 | magnésio: benefício concentrado em baixa ingestão/estado | média | parcialmente, NHANES |
| H07 | ferro: correção de deficiência, não suplementação universal | alta/segurança | requer biomarcadores e supervisão |
| H08 | adequação proteico-energética: recuperação física | alta | sim para referência; coorte esportiva |
| H09 | pilhas de suplementos não superam componentes isolados | alta | exige ensaio fatorial |
| H10 | excepcionalidade modifica tolerabilidade mais que eficácia média | alta | exige coorte 2e/3e |

## Hipóteses detalhadas

### H01 — cafeína, desempenho agudo e sono subsequente

**Hipótese:** cafeína próxima ao treino/tarefa pode melhorar alerta ou desempenho
agudo em alguns participantes, mas o benefício líquido cai quando o horário/dose
piora o sono e o desempenho do dia seguinte. O efeito adverso pode ser maior com
ansiedade, fobia social ou medicamento estimulante.

- exposição: cafeína total, fonte, dose, horário, hábito e meia-vida contextual;
- primário: desempenho padronizado no mesmo dia;
- coprimário: duração/regularidade do sono e desempenho no dia seguinte;
- segurança: pressão, pulso, ansiedade, agitação e insônia;
- modelo: distributed lag/N-of-1 com `cafeína×ADHD`, `cafeína×SOC` e
  `cafeína×estimulante`;
- refutação: ausência de benefício relevante ou dano líquido após incorporar o
  sono subsequente.

O ODS relata heterogeneidade de resposta, efeitos adversos de doses altas e risco
ao combinar cafeína com outros estimulantes
([ODS — desempenho](https://ods.od.nih.gov/factsheets/ExerciseAndAthleticPerformance-HealthProfessional/)).

### H02 — creatina, força/potência e força relativa

**Hipótese:** creatina monohidratada melhora esforços intensos repetidos e volume
de treino, mas o aumento de massa por água pode reduzir ou neutralizar ganhos em
movimentos de calistenia dependentes de força relativa.

- primário: trabalho/repetições estritas normalizados pelo peso corporal;
- secundários: potência, recuperação, massa e sintomas gastrointestinais;
- estratos: HA, HA+ADHD, HA+ASD e triplas pré-especificadas;
- modelo: crossover/N-of-1 e curva de aprendizagem do treino;
- refutação: ganho absoluto sem ganho relativo, ou benefício menor que efeitos
  adversos/carga de adesão.

O ODS considera a creatina uma das substâncias mais estudadas para esforço intenso
intermitente e registra aumento de peso como efeito esperado
([ODS — desempenho](https://ods.od.nih.gov/factsheets/ExerciseAndAthleticPerformance-HealthProfessional/)).

### H03 — ômega-3 como adjuvante em TDAH

**Hipótese:** EPA/DHA pode produzir pequeno benefício adjunto em sintomas ou
funcionamento de um subgrupo com TDAH, condicionado à exposição basal, formulação,
adesão e tratamento concomitante. Não se espera efeito específico por HA isolada.

- primário: prejuízo funcional ou escala validada de TDAH;
- secundários: atenção, humor e eventos adversos;
- grupos: ADHD; HA+ADHD; HA+ADHD+ASD; HA+ADHD+DEP;
- modelo: meta-regressão de ensaios + N-of-1/coorte hierárquica;
- refutação: efeito posterior abaixo do mínimo relevante ou sem replicação.

O grafo local encontrou várias grafias/formulações de ômega-3, reforçando a
necessidade de normalizar EPA, DHA, proporção e produto. O ODS considera a pesquisa
em TDAH ainda em investigação
([ODS — ômega-3](https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional/)).

### H04 — melatonina como intervenção circadiana

**Hipótese:** quando houver problema de latência ou fase circadiana, melatonina
pode melhorar um desfecho de sono, e qualquer melhora cognitiva seria mediada pelo
sono. Ela não é hipótese para “tratar” autismo, TDAH ou superdotação.

- primário: latência/regularidade do sono;
- secundários: sonolência, funcionamento matinal e cognição;
- grupos: isolados e combinações com ADHD, ASD, DEP e SOC;
- modelo: mediação `intervenção→sono→funcionamento`, com horário explicitado;
- refutação: sono não melhora ou sonolência/dano elimina benefício.

Essa hipótese requer revisão clínica de indicação, horário, formulação e interação;
não será testada inicialmente por automanejo irrestrito.

### H05 — vitamina D: deficiência versus suplementação indiscriminada

**Hipótese:** associações entre vitamina D baixa, humor e desempenho refletem em
parte saúde, exposição solar e comportamento. Benefício de suplementação deve se
concentrar em deficiência documentada, sem efeito antidepressivo geral esperado.

- dados imediatos: `LBXVIDMS`, `DSQTVD`, dieta, PHQ-9, sono, atividade e IMC;
- modelo inicial: survey-weighted, spline de 25(OH)D e controles negativos;
- modelo causal futuro: ensaio estratificado por estado basal;
- grupos: depressão isolada e combinações HA+DEP, HA+ADHD+DEP, HA+ASD+DEP;
- refutação: associação desaparece após ajuste/sensibilidade; ensaio não mostra
  benefício mesmo no estrato pré-especificado.

O ODS distingue associação observacional de ensaios que, em geral, não mostraram
prevenção ou tratamento de sintomas depressivos
([ODS — vitamina D](https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/)).

### H06 — magnésio condicionado ao estado basal

**Hipótese:** eventual benefício de magnésio sobre sono, função neuromuscular ou
bem-estar será maior quando ingestão/estado basal forem baixos; em participantes
adequados, o efeito será nulo ou pequeno.

- dados atuais: magnésio alimentar e de suplementos, sono, PHQ-9, pressão e dieta;
- lacuna: biomarcador isolado de magnésio tem limitações e não está neste recorte;
- modelo: interação não linear `exposição×estado basal`, sem dicotomizar cedo;
- refutação: ausência de gradiente/modificação ou eventos adversos superiores ao
  benefício.

### H07 — ferro somente diante de deficiência documentada

**Hipótese:** correção de deficiência de ferro pode melhorar fadiga e desempenho;
suplementação universal não traz benefício e adiciona risco.

- necessários: hemograma, ferritina, saturação de transferrina, inflamação,
  menstruação/dieta e avaliação clínica;
- primário: fadiga e capacidade física, não apenas ferritina;
- modelo: estratificação por deficiência/anemia e sexo/contexto fisiológico;
- refutação: biomarcador melhora sem benefício funcional relevante;
- trava: nenhuma intervenção sem diagnóstico e supervisão.

O ODS não recomenda ferro rotineiro para desempenho e ressalta risco de excesso
([ODS — desempenho](https://ods.od.nih.gov/factsheets/ExerciseAndAthleticPerformance-HealthProfessional/)).

### H08 — adequação proteico-energética e recuperação

**Hipótese:** atingir adequação de energia/proteína beneficia adaptação e
recuperação quando a ingestão era insuficiente; exceder adequação não melhora
continuamente cognição ou desempenho.

- dados atuais: energia/proteína do recordatório, suplemento, IMC e atividade;
- coorte: ingestão repetida, peso, volume de treino e força relativa;
- modelo: curva dose–resposta com plateau e erro de medição;
- refutação: ausência de benefício no estrato inicialmente inadequado.

### H09 — pilhas não superam componentes isolados

**Hipótese:** stacks apresentam benefício líquido menor do que sugerido pela soma
de alegações dos componentes devido a redundância, interação, não adesão e eventos
adversos.

- desenho: fatorial ou desmantelamento (`stack`, componentes, placebo/controle);
- primário: benefício líquido multiobjetivo;
- segurança: ingrediente/dose total e interações;
- refutação: stack demonstra ganho incremental replicável e seguro sobre cada
  componente.

### H10 — excepcionalidade como modificador de tolerabilidade

**Hipótese:** após controlar estado nutricional e tratamento, diferenças entre
perfis HA/2e/3e aparecem mais claramente em tolerabilidade, sono e adesão do que
em efeito fisiológico médio do suplemento.

- comparações: todas as isoladas, duplas e triplas pré-especificadas;
- modelo: bayesiano hierárquico, shrinkage forte para interação tripla;
- primários: interrupção, insônia, ansiedade, sintomas GI e adesão;
- secundários: eficácia cognitiva/física;
- refutação: efeitos de eficácia específicos robustos, replicados e maiores que
  diferenças de tolerabilidade.

## Hipóteses negativas e controles

- `HN1`: HA isolada não prediz deficiência ou resposta a suplemento após contexto.
- `HN2`: escolaridade/profissão não substituem avaliação de HA.
- `HN3`: produto no rótulo não equivale a exposição biologicamente confirmada.
- `HN4`: ausência de relato no CAERS não demonstra segurança.
- `HN5`: melhora de biomarcador não implica melhora funcional.
- `HN6`: nenhuma combinação 2e/3e é automaticamente mais responsiva.

## Ordem recomendada de teste

1. Auditar disponibilidade, unidades, ausências e sobreposição no NHANES.
2. Testar H05, H06 e H08 apenas como associações populacionais exploratórias.
3. Completar o grafo de ensaios e segurança para H01–H07.
4. Pré-registrar desfechos e contrastes HA/2e/3e.
5. Iniciar coorte observacional prospectiva.
6. Testar sono/dieta/treino antes de suplementação em N-of-1.
7. Somente então executar intervenções suplementares elegíveis e supervisionadas.

