# Modelo de dados e capacidade amostral das fontes candidatas

Revisado em 2026-09-10. Este é o portão de entrada das fontes: **N de catálogo
não é N analítico**. Uma fonte só pode receber protocolo de efeitos depois da
auditoria de campos, elegibilidade, grupos, ondas, ausências e qualidade.

## Inventário de amplitude

| Fonte | N divulgado/disponível | População e tempo | HA/capacidade | TDAH/autismo | Núcleo adicional | Decisão de capacidade atual |
|---|---:|---|---|---|---|---|
| Project Talent (PT60 público) | **377.016** estudantes do ensino médio em 1960 | Histórico; acompanhamentos em idade adulta | Bateria ampla de capacidade, aptidão e contexto; não rótulo contemporâneo de HA | Não é painel clínico de TDAH/autismo | Educação, trabalho, personalidade, ambiente e saúde | Forte para trajetória de capacidade; **não elegível** para contraste clínico individual HA×TDAH×autismo |
| NSCH 2024 público | **51.375** crianças 0–17 | Transversal anual, EUA, pesos complexos | Sem medida individual válida de HA | Diagnóstico relatado por cuidador de TDAH e autismo; coexistência possível | Saúde, tratamento, sono, escola, família e contexto | Forte para prevalência/contexto de TDAH/autismo; **não elegível** para HA/capacidade |
| ECLS-K:2011 público | **18.174** crianças com participação em alguma onda | Nove coletas, jardim de infância ao 5º ano | Avaliações de aprendizagem e dados escolares; identificação gifted precisa ser conferida campo a campo | Há informações de desenvolvimento/serviços, mas detalhes podem estar suprimidos ou restritos | Família, escola, professor e desenvolvimento | Triagem promissora para educação/2e; `needs_data` até confirmar campos públicos de identificação e diagnóstico |
| ABCD/NDA | **11.878** participantes divulgados na página de release consultada | Longitudinal, infância/adolescência | Neurocognição; HA requer definição operacional | Estruturas de TDAH/autismo e sintomas em metadados | Sono, ambiente, saúde mental, atividade e imagem | Maior potencial para trajetória comum; dados individuais exigem acesso legítimo |
| HBN | Meta de **10.000**; número liberado por versão deve ser auditado | 5–21 anos, coorte comunitária encaminhada | Cognição profunda; HA requer definição | Fenótipos psiquiátricos/clinicos transdiagnósticos | Sono/estilo de vida, actigrafia, EEG e imagem | Melhor candidato de núcleo comum; não usar a meta como N disponível e requer DUA para fenótipos |
| ABIDE I | **1.112**: 539 autismo, 573 controles | 17 centros, 7–64 anos | QI e subescores, instrumentos variam | Autismo versus controles | Imagem e fenótipo selecionado | Suficiente para auditoria ASD×capacidade e síntese multissítio; não TDAH/HA |
| ABIDE II | **1.114**: 521 autismo, 593 controles | 19 centros, 5–64 anos; parte longitudinal | QI total/verbal/desempenho, instrumentos variam | Autismo versus controles | Fenótipo mais amplo e imagem | Replicação ASD separada; qualidade e centro reduzem N efetivo |
| ADHD-200 | **776** participantes rotulados na competição: 285 TDAH, 491 controles | 8 centros, 7–21 anos | QI/medida cognitiva parcial | TDAH combinado/desatento e controles | Imagem estrutural e repouso; idade/sexo/lateralidade | Suficiente para auditoria TDAH×capacidade; centro e faltas definem N final |
| PING | **1.493** participantes, 3–20 anos | Transversal, 10 centros | NIH Toolbox e cognição padronizada | ASD foi exclusão; TDAH não é eixo clínico principal | Desenvolvimento, comportamento, imagem e genótipo | Referência de capacidade por idade; não contraste ASD e não coorte HA |
| NKI-Rockland | Mais de **1.500** residentes; acesso atual por DUA | Comunidade, ciclo de vida; recursos longitudinais | Bateria cognitiva | Estado psiquiátrico amplo; cobertura de TDAH/autismo requer auditoria | Saúde, comportamento e imagem | Replicação dimensional após DUA; não assumir células clínicas antes de contar |
| OpenNeuro TCP | **241** adultos: 148 clínicos, 93 comparação | Transversal, 18–70 anos | Mais de 50 questionários cognitivos/psicológicos | Diagnóstico amplo, não coorte focada em TDAH/autismo | Entrevista clínica e RM | Piloto/reprodutibilidade de modelo; insuficiente para conclusões de subgrupos pequenos |

## O que os números permitem — e não permitem

- **Amplitude sem medida do grupo não resolve a pergunta.** Project Talent e
  ECLS-K são grandes para capacidade/educação, mas não viram uma coorte clínica
  só por conterem desempenho escolar ou serviços.
- **Grupo clínico sem medida válida de HA não resolve HA.** ABIDE e ADHD-200
  suportam estudos separados de autismo/TDAH e capacidade medida; não autorizam
  rotular seu extremo de QI como HA sem uma regra validada.
- **Coexistências consomem rapidamente o N.** Mesmo bases grandes precisam ter
  as células HA+TDAH, HA+autismo e tripla contadas após exigências de medida e
  dados completos; não serão inferidas de totais marginais.
- **Multissítio não é N independente automático.** Centro, protocolo, idade,
  qualidade de imagem e informante devem entrar no desenho e no fluxo de perdas.

## Modelo de dados mínimo por estudo paralelo

| Domínio | Obrigatório para estimar | Exemplos de estado de auditoria |
|---|---|---|
| Identidade de participante/tempo | ID desidentificado estável; onda/data; centro quando houver | `measured`, `no_longitudinal_key`, `site_missing` |
| HA/capacidade | Instrumento, escore, norma por idade, versão e regra registrada | `measured_capacity`, `gifted_identification`, `not_measured` |
| TDAH/autismo | Fonte do diagnóstico, informante, data, sintomas, gravidade e medicação quando disponíveis | `clinical_measure`, `parent_report`, `screen_only`, `not_measured` |
| Desfecho comum | Sono, funcionamento, bem-estar ou desempenho, com janela temporal | `measured`, `incompatible_window`, `unavailable` |
| Contexto e confundidores | Idade, sexo/gênero conforme instrumento, centro, contexto socioeconômico e tratamento | `measured`, `partial`, `unavailable` |
| Desenho e qualidade | Peso/estrato/PSU ou origem da amostra; qualidade de dados/imagem | `complex_survey`, `multisite`, `convenience`, `quality_filtered` |

## Portões que evitam bases insuficientes

1. **Portão de medida:** nenhum contraste é elegível se um dos grupos ou o
   desfecho central for `not_measured`.
2. **Portão de células:** publicar contagem não ponderada, perda por campo e
   mínimo por grupo/centro antes de escolher modelo. Células pequenas levam a
   `needs_data` ou a contraste previamente reduzido, nunca a agregação ad hoc.
3. **Portão de tempo:** perguntas de trajetória só usam chaves/ondas reais;
   corte transversal não recebe linguagem temporal.
4. **Portão de transporte:** resultado de uma fonte é replicação externa apenas
   quando medida, população e estimando forem comparáveis; caso contrário é
   evidência complementar.
5. **Portão de HA:** só há conclusão sobre HA quando a base atende a definição
   registrada de HA; o restante é explicitamente estudo de capacidade medida.

## Primeira decisão de aquisição

A sequência abaixo foi substituída pela [triagem E1](SOURCE_FIT_AUDIT.md): ABCD,
HBN e UK Biobank como candidatas ao núcleo; NHANES cognitivo e NSCH como apoio.
Totais deste inventário são históricos e não constituem aprovação por A-01/A-05.

1. Baixar primeiro metadados/fenótipos públicos de **Project Talent,
   ABIDE II, ADHD-200 e NSCH** e gerar quatro relatórios de auditoria separados.
2. Antes de baixar arquivos grandes, listar nomes de campos, licença, tamanho,
   versão, chave e N por grupo disponível em cada manifesto/codebook.
3. Só baixar imagem, genética ou microdados sob DUA depois de a auditoria mostrar
   que ela elimina uma lacuna que os arquivos tabulares públicos não cobrem.
4. Declarar HBN, ABCD, NKI e ECLS restrito como candidatos condicionados a acesso;
   não fazer deles dependência invisível do primeiro ciclo.

## Fontes verificadas

- [Project Talent: ICPSR 33341 e N público](https://www.icpsr.umich.edu/web/NACDA/studies/33341)
- [NSCH: amostra de 2024](https://www.nschdata.org/learn-about-the-nsch/NSCH)
- [ECLS-K:2011: arquivo público e N](https://nces.ed.gov/ecls/dataproducts.asp)
- [ABCD: coleção e medidas](https://nda.nih.gov/study.html?id=1130)
- [HBN: acesso a fenótipos e meta](https://data.healthybrainnetwork.org/)
- [ABIDE II: N, grupos, centros e idade](https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html)
- [ADHD-200: competição e grupos rotulados](https://fcon_1000.projects.nitrc.org/indi/adhd200/index.html)
- [PING: repositório e N](https://pmc.ncbi.nlm.nih.gov/articles/PMC4628902/)
- [NKI-Rockland: acesso e desenho](https://rocklandsample.org/phenotypic-data)
- [OpenNeuro TCP: N e medidas](https://pmc.ncbi.nlm.nih.gov/articles/PMC11213088/)
