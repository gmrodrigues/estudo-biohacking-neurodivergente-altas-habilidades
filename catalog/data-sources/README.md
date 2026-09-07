# Catálogo de fontes de dados em saúde e suplementação

Este diretório reúne fontes úteis para pesquisa exploratória sobre neurodivergência,
desempenho físico, sono, fisiologia e suplementação. O catálogo distingue dados
abertos de dados sujeitos a cadastro, treinamento, termo de uso ou aprovação.

A metodologia integrada está em
[`MULTIDIMENSIONAL_HYPOTHESIS_PREDICTION_METHODOLOGY.md`](MULTIDIMENSIONAL_HYPOTHESIS_PREDICTION_METHODOLOGY.md),
com esquema operacional em
[`multidimensional-model-schema.yaml`](multidimensional-model-schema.yaml).

O [plano de descobertas e skills](DISCOVERY_PLAN.md) define a primeira rodada de
análises, seus limites e as seis habilidades reutilizáveis para executá-la e
publicar os resultados de cada ciclo com gráficos navegáveis no GitHub Pages.

O arquivo [`sources.yaml`](sources.yaml) é a versão estruturada e deve ser tratado
como a fonte principal. As informações de acesso devem ser verificadas antes do
início de cada projeto, pois políticas e versões dos conjuntos podem mudar.

Consulte também [`ACCESS_FROM_CODEX.md`](ACCESS_FROM_CODEX.md) para saber quais
fontes podem ser consultadas ou baixadas diretamente a partir deste ambiente e
quais dependem de credenciais ou aprovação do pesquisador.

O relatório [`REPORT_DATA_MODELS_GIFTEDNESS.md`](REPORT_DATA_MODELS_GIFTEDNESS.md)
descreve modelos de dados e desenhos de pesquisa possíveis, usando como caso de
uso a personalização de dieta, suplementação, exercício e sono para pessoas com
altas habilidades/superdotação.

A [`INITIAL_FEASIBILITY_ANALYSIS.md`](INITIAL_FEASIBILITY_ANALYSIS.md) registra a
primeira inspeção efetiva dos metadados do ABCD, OpenNeuro e All of Us e o perfil
reproduzível dos microdados públicos do NHANES baixados neste workspace.

A [`TWICE_EXCEPTIONAL_MODELS.md`](TWICE_EXCEPTIONAL_MODELS.md) especifica modelos
para TDAH, autismo, depressão, ansiedade/fobia social, transtornos de aprendizagem
e outras condições que podem coexistir com altas habilidades.

As hipóteses iniciais de suplementação estão documentadas em
[`SUPPLEMENTATION_HYPOTHESES.md`](SUPPLEMENTATION_HYPOTHESES.md) e no registro
estruturado [`supplementation-hypotheses.yaml`](supplementation-hypotheses.yaml).

A priorização baseada nos interesses pessoais confirmados nesta conversa — com
uma seção específica sobre metilação — está em
[`PERSONALIZED_HYPOTHESIS_PRIORITY.md`](PERSONALIZED_HYPOTHESIS_PRIORITY.md).

O histórico informado pelo usuário está estruturado em
[`personal-supplement-history.yaml`](personal-supplement-history.yaml), e as
hipóteses específicas para esses itens estão em
[`PERSONAL_SUPPLEMENT_HYPOTHESES.md`](PERSONAL_SUPPLEMENT_HYPOTHESES.md).

O desenho central do estudo — HA, autismo, TDAH, duplas, tripla e neurotípicos —
está em [`CORE_STUDY_DESIGN.md`](CORE_STUDY_DESIGN.md).

A estratificação por ciclo de vida, sexo/gênero, profissão, escolaridade,
criatividade e inclinação artística está em
[`STRATIFICATION_MODEL.md`](STRATIFICATION_MODEL.md) e
[`stratification-schema.yaml`](stratification-schema.yaml).

## Visão rápida

| Fonte | Tema principal | Acesso | Uso sugerido |
|---|---|---|---|
| NIMH Data Archive / ABCD | Neurodesenvolvimento, TDAH, autismo, cognição | Controlado | Hipóteses sobre neurodivergência, sono e atividade física |
| OpenNeuro | MRI, EEG, MEG, PET e iEEG | Aberto | Neuroimagem e neurofisiologia reproduzível |
| PhysioNet | Sinais fisiológicos e dados clínicos | Misto | Sono, fadiga, ECG, EEG e biomarcadores digitais |
| NSRR | Sono, polissonografia e actigrafia | Cadastro/solicitação | Sono, recuperação e desempenho |
| All of Us | EHR, questionários, wearables e genômica | Misto/controlado | Estudos populacionais multimodais |
| NHANES | Exames, dieta, suplementos e atividade física | Aberto | Associações populacionais e biomarcadores |
| Open Humans | Dados pessoais e wearables voluntariamente compartilhados | Misto/opt-in | Estudos N-of-1 e ciência cidadã |
| DATASUS | Epidemiologia e serviços de saúde brasileiros | Predominantemente aberto/agregado | Contexto epidemiológico brasileiro |
| NIH ODS Fact Sheets | Sínteses de evidência sobre suplementos | Aberto | Eficácia, segurança e interações |
| DSLD | Rótulos de suplementos | Aberto/API | Ingredientes, doses e formulações comerciais |
| DSID | Conteúdo de suplementos medido analiticamente | Aberto | Diferença entre rótulo e conteúdo estimado |
| ClinicalTrials.gov | Ensaios clínicos e resultados | Aberto/API | Evidência experimental e estudos em andamento |
| PubChem | Química, bioatividade e toxicologia | Aberto/API | Mecanismos e segurança de ingredientes |
| openFDA CAERS | Eventos adversos de suplementos e alimentos | Aberto/API | Detecção de sinais de segurança |
| Anvisa / Nutrivigilância | Regulação e eventos adversos no Brasil | Aberto, sobretudo agregado | Segurança e situação regulatória brasileira |

## Cuidados de interpretação

- Notificações de eventos adversos ajudam a detectar sinais, mas não demonstram
  que um produto causou o evento.
- Informação de rótulo não comprova pureza, identidade ou conteúdo laboratorial.
- Associação observacional não demonstra eficácia de uma intervenção.
- Dados individuais de saúde podem permanecer reidentificáveis mesmo após a
  remoção de nome e documentos.
- Pesquisa envolvendo outras pessoas pode exigir consentimento, avaliação ética,
  proteção conforme a LGPD e, no Brasil, análise pelo sistema CEP/CONEP.
- Resultados de bases populacionais não substituem avaliação médica nem tornam
  segura a automodificação de medicamentos, hormônios ou doses elevadas.

## Campos do catálogo

Cada registro em `sources.yaml` contém identificador, nome, URL, organização,
temas, modalidades, nível de acesso, formatos, usos indicados, limitações e notas
de ética/privacidade. `last_verified` registra apenas a data em que a página da
fonte foi conferida, não uma auditoria completa de seus dados.
