# Auditoria inicial de bases abertas para HA, TDAH e autismo

Revisado em 2026-09-10. Esta triagem separa bases **desidentificadas e abertas**
de bases que exigem conta, aceite ou aprovação. A disponibilidade de um arquivo
não valida automaticamente cada fenótipo nem permite concluir sobre HA.

## Decisão operacional

Há dados que permitem iniciar imediatamente auditorias sobre autismo, TDAH e
capacidade cognitiva. Ainda não há uma base aberta identificada que registre HA
como identificação educacional/avaliação validada junto de TDAH e autismo.
Assim, os estudos abertos abaixo devem chamar o construto de **capacidade
cognitiva medida**, não de HA, até uma definição operacional e sua validade serem
auditadas. Essa distinção mantém a prioridade no tema sem fabricar grupos.

| Base | Acesso e desidentificação | Medidas úteis | Uso publicado | Melhor uso imediato | Limite decisivo |
|---|---|---|---|---|---|
| **ABIDE I/II** | Fenótipos e imagens anonimizados; CSVs públicos e acesso a imagens por repositório/conta | Autismo, controles, idade, sexo, QI total/verbal/desempenho e escalas conforme centro | Estudos multissítio de conectividade e estrutura em autismo; o primeiro intercâmbio publicou 1.112 participantes | Auditoria ASD × capacidade cognitiva e replicação por centro | Não é coorte de HA; TDAH, sono, dieta e medicação têm cobertura heterogênea; QI vem de instrumentos diferentes |
| **ADHD-200** | Fenótipos e versões pré-processadas distribuídos abertamente | TDAH/controles, subtipo, idade, sexo, lateralidade, QI e imagem estrutural/repouso | Competição ADHD-200 e estudos posteriores testaram classificação em quase mil jovens | Auditoria TDAH × capacidade cognitiva e transporte para outro conjunto | Legado multissítio; sem autismo/HA e sem núcleo amplo de sono/nutrição |
| **Healthy Brain Network (HBN)** | Biobanco desidentificado de acesso aberto, sujeito às regras de uso/publicação | Fenótipos psiquiátricos, comportamentais, cognitivos e de estilo de vida; imagem, EEG e actigrafia | Estudos transdiagnósticos já combinaram HBN e ABIDE e analisaram heterogeneidade de coorte | **Primeiro candidato para o núcleo comum** ASD/TDAH/cognição/sono/atividade em jovens | Amostra comunitária encaminhada, não referência populacional; exigir auditoria da versão, termos e cobertura real |
| **OpenNeuro — Transdiagnostic Connectome Project** | Publicado em OpenNeuro; dados desidentificados sob os termos da plataforma | 241 adultos, entrevista clínica e mais de 50 questionários cognitivos/psicológicos, além de RM | Publicado como recurso transdiagnóstico para relações cérebro–comportamento | Piloto adulto para estrutura de dados e análises dimensionais | Pequeno e amplo em diagnósticos; não é coorte dirigida a HA/TDAH/autismo e não substitui replicação |
| **NKI-Rockland Sample** | Recurso longitudinal desidentificado; fenótipos completos exigem acordo de uso assinado, sem IRB como requisito do repositório | Cognição, comportamento, estado psiquiátrico, imagem e fatores de saúde modificáveis ao longo da vida | Estudos do próprio recurso descrevem mais de 300 variáveis em 26 domínios e trajetória infância–adulto | Replicação dimensional de cognição/psicopatologia e comparação de generalização | Não é download aberto sem DUA; não oferece identificação de HA e diagnóstico/cobertura precisam ser auditados |
| **PING** | Dados compartilháveis, mas portal exige conta, acordo de uso e aprovação breve | Neurocognição padronizada, história do desenvolvimento, comportamento, imagem e genótipos em 3–20 anos | Repositório de 1.493 crianças/adolescentes já descrito em estudos de desenvolvimento cerebral e cognição | Referência normativa de capacidade por idade e validação de definição cognitiva | Predominantemente desenvolvimento típico; não é coorte TDAH/autismo/HA e algumas camadas têm restrições |
| **MIPDB** | EEG bruto e pré-processado público sob CC BY-NC-SA | Paradigmas de função cognitiva e fenótipos do desenvolvimento | Recurso aberto para medidas dimensionais de processamento de informação no desenvolvimento | Piloto técnico para tarefas/EEG e normas dimensionais | Não é base diagnóstica de HA/TDAH/autismo; não sustenta contrastes clínicos centrais |
| **ABCD/NDA** | Metadados públicos; dados individuais requerem acesso legítimo/qualificado | Longitudinal, cognição, saúde mental, sono, ambiente e desenvolvimento | Recurso longitudinal usado em muitos estudos; liberação 5.1 indicada pelo NDA | Melhor candidato de longo alcance após acesso para trajetória e validação temporal | Não é download aberto imediato e HA deve ser operacionalizada, não presumida |

## Sequência priorizada

1. **Agora, sem credencial adicional:** baixar somente os fenótipos públicos de
   ABIDE II e ADHD-200, registrar versões/hashes e produzir auditorias separadas.
   O resultado esperado é `estimable_with_limits` para ASD×capacidade e
   TDAH×capacidade, não uma comparação HA×TDAH×autismo.
2. **Em paralelo:** revisar os termos e o manifesto de variáveis do HBN. Se o
   conjunto liberado contiver as medidas prometidas e puder ser usado sob seus
   termos, ele será o primeiro candidato a integrar TDAH, autismo, cognição,
   sono e atividade no mesmo protocolo.
3. **Para a conclusão central sobre HA:** obter coorte com identificação de HA ou
   registrar e validar uma definição de capacidade elevada baseada em instrumentos
   comparáveis e normas por idade. Sem isso, o rótulo de saída permanece
   “capacidade cognitiva”, não “altas habilidades”.
4. **Para trajetória e causalidade temporal:** solicitar acesso legítimo ao ABCD
   em paralelo, sem bloquear as auditorias abertas.
5. **Para validação de definição cognitiva:** considerar PING e MIPDB como
   recursos de norma/tarefa, e NKI-Rockland após DUA para replicação dimensional;
   eles não substituem a coorte de grupos.

## Protocolo mínimo antes de qualquer efeito

Para cada base: registrar versão e licença; mapear arquivo→construto→instrumento;
verificar participante/onda/chave e duplicações; listar idade, sexo, centro,
diagnóstico, informante, medicação e valores ausentes; calcular tamanho de cada
grupo e a sobreposição TDAH+autismo; testar heterogeneidade por centro e não
misturar coortes diferentes por semelhança de perfil.

O primeiro resultado publicável dessa frente será a **decisão de estimabilidade**
por base, não uma classificação clínica, biomarcador ou recomendação.

## Publicações que reutilizaram as fontes: verificação

| Base | Publicação de reutilização verificada | O que ela declara ter usado | Consequência para este estudo |
|---|---|---|---|
| ABIDE | [Periventricular white matter abnormalities and restricted repetitive behavior](https://pmc.ncbi.nlm.nih.gov/articles/PMC4660377/) | Selecionou dados ABIDE; descreve-o como banco aberto, anonimizado e multissítio, com diagnóstico variando por centro | Repetir controle de centro e qualidade; não presumir protocolo único nem generalizar de imagem para perfil completo |
| ADHD-200 | [Towards interpretable machine learning models for diagnosis aid](https://pmc.ncbi.nlm.nih.gov/articles/PMC6483231/) | Usou subconjunto aberto ADHD-200 e documentou diagnóstico, QI, idade, sexo, informante e separação treino/teste | Preservar centros e divisão externa; previsão não deve virar ferramenta diagnóstica nem critério de grupo |
| HBN | [Functional Connectivity Patterns Predict Naturalistic Viewing versus Rest](https://pmc.ncbi.nlm.nih.gov/articles/PMC12021493/) | Declara uso do HBN aberto via FCP/INDI, com versão de release, dois centros e filtros de qualidade | Fixar versão, centros e filtros antes da análise; a seleção do artigo não define nossa população |
| HBN + ABIDE | [Population heterogeneity in clinical cohorts affects predictive accuracy](https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3001627) | Combinou as duas fontes para demonstrar que heterogeneidade de coorte afeta previsão | Planejar replicação entre bases, não mesclar participantes como se fossem uma coorte única |
| NKI-Rockland | [Resting-state networks associated with cognitive processing](https://pmc.ncbi.nlm.nih.gov/articles/PMC5799084/) | Obteve imagem e repouso do NKI-Rockland e descreveu bateria cognitiva/comportamental/psiquiátrica | É útil para replicação dimensional, mas o acordo de uso e os fenótipos atuais precisam ser conferidos antes do download |
| PING | [Neuroanatomical correlates of genetic risk for obesity in children](https://pmc.ncbi.nlm.nih.gov/articles/PMC9810659/) | Usou PING para medidas estruturais e compósito de atenção, memória, velocidade e função executiva | Pode apoiar uma definição/norma cognitiva por idade; não fornece grupo autista e excluiu ASD da coorte original |
| OpenNeuro TCP | [The Transdiagnostic Connectome Project](https://pmc.ncbi.nlm.nih.gov/articles/PMC11213088/) | Publicou dados brutos anonimizados e medidas comportamentais/cognitivas no OpenNeuro | Serve como piloto adulto e teste de reprodutibilidade, não como confirmação de grupos específicos |

Essa verificação não valida os achados desses artigos como conclusões do projeto.
Ela confirma que as fontes foram reutilizadas e torna explícitas as restrições que
devem ser preservadas ao auditá-las aqui.

## Fontes verificadas

- [ABIDE II: acesso, anonimização e downloads](https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html)
- [ABIDE II: legenda de fenótipos](https://fcon_1000.projects.nitrc.org/indi/abide/ABIDEII_Data_Legend.pdf)
- [ABIDE II: índice público de CSVs fenotípicos](https://fcon_1000.projects.nitrc.org/indi/abide2/release/phenotypic_data/)
- [ADHD-200: dados pré-processados abertos](https://neurobureau.projects.nitrc.org/ADHD200/Introduction.html)
- [ADHD-200 Consortium e a competição](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2012.00062/full)
- [Healthy Brain Network: biobanco e dados desidentificados](https://childmind.org/science/global-open-science/healthy-brain-network/)
- [INDI/HBN: modalidades e acesso ao biobanco](https://childmind.org/science/global-open-science/data-sharing-initiatives/)
- [Heterogeneidade em ABIDE e HBN](https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3001627)
- [OpenNeuro: Transdiagnostic Connectome Project](https://openneuro.org/datasets/ds005237)
- [NKI-Rockland: acesso a fenótipos e DUA](https://rocklandsample.org/phenotypic-data)
- [NKI-Rockland: recurso longitudinal e associações psiquiátricas](https://rocklandsample.org/for-researchers/step-3-accessing-the-data)
- [PING: repositório de neuroimagem, neurocognição e genética](https://pmc.ncbi.nlm.nih.gov/articles/PMC4628902/)
- [MIPDB: EEG aberto](https://fcon_1000.projects.nitrc.org/indi/cmi_eeg/eeg.html)
- [NDA: ABCD e liberação atual](https://nda.nih.gov/general-query.html?q=query%3Dfeatured-datasets%3AAdolescent+Brain+Cognitive+Development+Study+%28ABCD%29)
