# Modelo de estratificação demográfica, educacional e criativa

**Data:** 2026-09-07  
**Aplica-se a:** HA, ASD, ADHD, neurotípicos, duplas e triplas.

## Objetivo

Estimar correlações e efeitos heterogêneos sem presumir que idade, sexo, gênero,
profissão, escolaridade, criatividade ou inclinação artística definam altas
habilidades. Essas dimensões descrevem contexto, desenvolvimento e possíveis
modificadores; a identificação de HA permanece baseada em avaliação explícita.

## Ciclo de vida

Faixas iniciais harmonizadas:

| Código | Faixa | Observação |
|---|---:|---|
| child | 6–11 | instrumentos e normas infantis |
| adolescent | 12–17 | puberdade, escola e cronotipo precisam ser considerados |
| young_adult | 18–29 | transição educacional/profissional |
| midlife_adult | 30–59 | trabalho, cuidado familiar e saúde acumulada |
| older_adult | 60+ | cognição, multimorbidade e polifarmácia |

Faixas servem para tabelas e interação. Idade contínua, splines e idade do teste
devem ser preservadas no modelo para evitar degraus artificiais. Crianças,
adolescentes e adultos não devem ser combinados sob a mesma norma psicométrica.

Fontes atuais:

- ABCD começa na infância e acompanha a adolescência;
- o recorte NHANES já baixado e intersectado possui apenas adultos de 18–80 anos;
- All of Us é principalmente adulto;
- OpenNeuro varia por conjunto.

Resultados entre ciclos devem ser meta-analisados ou harmonizados por escore
normativo, não concatenados cegamente.

## Sexo e gênero

Registrar separadamente quando disponível:

- sexo registrado ao nascimento/variável biológica pertinente;
- identidade de gênero;
- terapia hormonal, gravidez, menopausa e ciclo menstrual quando relevantes e
  consentidos;
- opção desconhecida/não informada, sem imputar a partir de nome ou aparência.

“Homens versus mulheres” será uma comparação planejada, mas não necessariamente
binária em toda fonte. Diferenças observadas podem refletir seleção diagnóstica,
socialização, acesso a avaliação, hormônios ou contexto; o modelo não atribuirá
automaticamente causalidade biológica.

## Profissão e trabalho

Usar uma taxonomia hierárquica, preservando o texto original:

```text
occupation_original
occupation_code (ISCO-08 ou classificação compatível)
employment_status
work_hours
shift_work
remote_or_in_person
physical_demand
cognitive_demand
creative_autonomy
social_demand
job_control
unemployment_duration
```

Profissão é exposição/contexto e possível resultado de oportunidades; não é proxy
de capacidade. Desemprego deve incluir duração, voluntariedade, saúde, discriminação,
necessidade de suporte e incompatibilidade pessoa–ambiente.

## Escolaridade

Registrar:

- anos completos e maior nível;
- área de formação;
- desempenho quando consentido;
- aceleração, repetência, evasão e educação especial;
- qualidade/oportunidade educacional;
- escolaridade dos responsáveis para menores;
- educação formal e aprendizagem autodidata separadamente.

Escolaridade é influenciada por renda, região, suporte, deficiência e acesso. Ela
não substitui teste cognitivo nem identificação multidimensional de HA.

## Criatividade

Não usar uma pergunta genérica “sou criativo?” como medida única. Separar:

- pensamento divergente: fluência, flexibilidade, originalidade e elaboração;
- produção/realização criativa em domínio;
- criatividade cotidiana;
- motivação, abertura e tolerância à ambiguidade;
- avaliação por pares/especialistas quando aplicável;
- oportunidade e treino no domínio.

Guardar instrumento, versão, idioma, normas, domínio e método de pontuação. Testes
de pensamento divergente não equivalem a produção artística ou realização criativa.

## Inclinação e prática artística

Modelar como vetor, não como sim/não:

```text
domain: visual_art | music | writing | dance | theater | audiovisual | design | other
interest_intensity
weekly_practice_hours
years_of_practice
formal_training
portfolio_or_output
public_or_peer_recognition
professional_status
self_reported_identity
barriers_and_access
```

Inclinação, prática, habilidade e reconhecimento são construtos distintos. Um
portfólio pode ser avaliado de forma cega por múltiplos avaliadores, medindo
concordância; popularidade não deve ser tratada como qualidade intrínseca.

## Família, autonomia financeira e substâncias

Registrar composição familiar sem presumir um modelo ideal: membros e relações
do domicílio, cuidadores, irmãos/ordem de nascimento, dependentes, horas de
cuidado, transições familiares, educação/profissão parental, suporte, coesão e
conflito percebidos e histórico familiar de saúde. Separar parentesco biológico,
convivência e papel de cuidado; registrar datas para preservar a ordem temporal.

Medir independência financeira como dimensão dependente da idade: renda pessoal
e domiciliar, parcela das despesas próprias, estabilidade de trabalho, moradia,
dívida/patrimônio, suporte recebido/fornecido, dependentes e privação material.
Para menores, usar `not_applicable` e descrever o contexto domiciliar.

Coletar histórico de substâncias por substância: uso na vida, último ano e 30
dias, idade de início, frequência, quantidade, via, contexto, policonsumo,
consequências, tratamento e tempo de abstinência. Separar uso ilícito de uso
indevido de medicamento prescrito. Nunca usar como rótulo moral, proxy diagnóstico
ou exclusão automática. Conforme o DAG, pode ser exposição, confundidor, mediador,
modificador ou desfecho. Exigir consentimento específico, minimização e proteção
contra reidentificação, com protocolo reforçado para menores.

## Estrutura analítica

### Tabelas descritivas

Produzir contagens e distribuições para:

```text
grupo_excepcionalidade
  × ciclo_de_vida
  × sexo/gênero
  × escolaridade
  × família_profissional
  × criatividade
  × domínio_artístico
```

Não publicar células pequenas que permitam reidentificação. A tabela completa é
um diagnóstico de cobertura; não significa que toda combinação terá potência para
inferência.

### Correlações

Para cada correlação, registrar:

- hipótese e direção prévia;
- N efetivo e dados ausentes;
- escala e confiabilidade das medidas;
- correlação bruta e parcial;
- intervalo de confiança/credibilidade;
- correção por multiplicidade;
- replicação em outra onda/base;
- diferença entre correlação dentro e entre grupos.

Evitar o paradoxo de Simpson: uma correlação agregada entre criatividade e sono,
por exemplo, pode inverter dentro das faixas etárias ou profissões.

### Modelo hierárquico recomendado

```text
Y_it = excepcionalidades_i
     + idade_spline_i + sexo_i + gênero_i
     + escolaridade_i + profissão_i
     + criatividade_i + prática_artística_i
     + contexto_familiar_i + autonomia_financeira_i
     + histórico_substâncias_i
     + intervenção_it
     + interações pré-especificadas
     + pessoa_i + centro_i + tempo_t + erro_it
```

Interceptos parciais por idade, sexo/gênero e família profissional reduzem
instabilidade. Interações de alta ordem só entram com hipótese e dados suficientes.

## Interações prioritárias

- `HA×idade`: manifestação e identificação mudam ao longo da vida;
- `HA×sexo/gênero`: possível viés de encaminhamento/identificação;
- `ASD×sexo/gênero` e `ADHD×sexo/gênero`: validação de seleção diagnóstica;
- `grupo×escolaridade`: oportunidade versus capacidade;
- `grupo×demanda_profissional`: funcionamento em ambientes diferentes;
- `grupo×criatividade`: força específica versus escore cognitivo geral;
- `grupo×prática_artística`: treino e expressão do talento;
- `suplemento×idade`: metabolismo, polifarmácia e tolerabilidade;
- `suplemento×sexo/contexto_fisiológico`: estado nutricional e resposta;
- `cafeína×trabalho_em_turnos`: alerta imediato versus sono;
- `creatina×sexo×modalidade`: força absoluta, relativa e composição corporal.

## Hipóteses exploratórias úteis

1. Perfis cognitivos elevados podem se expressar de maneira diferente conforme
   oportunidade educacional e autonomia profissional.
2. Criatividade e inclinação artística podem explicar heterogeneidade não captada
   pelo compósito cognitivo.
3. Sono irregular pode mediar relações entre trabalho em turnos, sintomas e
   desempenho, em vez de ser efeito direto da excepcionalidade.
4. Diferenças de sexo/gênero na identificação podem diminuir quando escores
   dimensionais e funcionamento substituem encaminhamento clínico.
5. Efeitos de suplementos podem variar mais por estado basal, idade, medicação e
   dieta que pelo rótulo HA/ASD/ADHD.

Todas são hipóteses refutáveis, não conclusões.

## Requisitos mínimos de validação

- invariância de medida por idade, idioma e sexo/gênero;
- normas apropriadas para cada ciclo de vida;
- ponderação amostral no NHANES;
- validação temporal e externa;
- análise de dados ausentes e seleção;
- partial pooling para estratos raros;
- relatório de equidade e calibração por grupo;
- supressão de células identificáveis;
- distinção entre exploração e hipótese confirmatória.
