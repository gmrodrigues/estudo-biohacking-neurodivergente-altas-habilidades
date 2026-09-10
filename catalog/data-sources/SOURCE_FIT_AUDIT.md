# Triagem de adequação das fontes — E1

Data: 2026-09-10. Status: auditoria documental inicial executada.
Nenhuma nova base individual foi ingerida; nenhuma POC empírica foi aprovada.
Critérios: [A-01 a A-05](PHASE_1_PLAN.md). N conjunto permanece desconhecido
até contar pessoas com todas as medidas requeridas na mesma janela.

## Decisões que mudam o plano

1. ABCD permanece candidata longitudinal, mas não representa todo o espectro
   autista. A documentação atual informa exclusão de autismo moderado/grave no
   recrutamento e mensuração de autismo por relato parental no KSADS.
2. A documentação atual ABCD anuncia release 7.0 e acesso pelo NBDC Data Hub.
   NDA/5.1 é referência histórica, não release atual automaticamente selecionada.
3. A FAQ ABCD proíbe inserir dados em ferramentas de IA generativa. O trabalho
   aqui usa documentação pública. Uma autorização de acesso individual não
   autoriza transferir microdados, saídas individuais ou arquivos ABCD à conversa.
   Código genérico pode ser preparado sem dados; execução com esses dados
   depende de ambiente e fluxo compatíveis com o acordo.
4. UK Biobank tem campos específicos úteis, mas seus totais marginais não
   comprovam sobreposição nem capacidade para discriminar P98/P99.
5. NHANES 2013–2014 tem cognição em pessoas de 60 anos ou mais: merece auditoria
   complementar própria; não é extensão cognitiva dos participantes 2021–2023.

Fonte ABCD: [FAQ atual](https://docs.abcdstudy.org/latest/info/faq.html).
A página latest é mutável; congelar versão documental antes da implementação.

## Fichas por fonte

| Fonte | Evidência consultada | Campo/estrutura ou instrumento | Pergunta atendida em princípio | O que falta | Decisão |
|---|---|---|---|---|---|
| ABCD | FAQ atual, visão do estudo e tabela KSADS de release 6.1 | mh_p_ksads__adhd; mh_p_ksads__asd são nomes de tabelas 6.1, não campos 7.0 confirmados | A-01/A-02/A-04; A-03 restrita à seleção e relato disponíveis | Mapear cognição, hábito, desfecho independente e covariáveis da mesma release; contar junções e pares de ondas no ambiente autorizado | Candidata condicionada; não aprovada para comparação ampla de autismo |
| HBN | Portal oficial de fenótipos e notas de release 10.0 | WISC-V e WISC-V Integrated citados nas notas; nomes de colunas ainda não verificados | A-01/A-03 e possivelmente A-02 | DUA; dicionário da versão escolhida; hábito, desfecho independente e N conjunto; diferenças entre avaliação remota/presencial | Candidata clínica; acesso e cobertura pendentes |
| UK Biobank | Showcase dos campos 20016, 6155, 1160 e 20023 | 20016: raciocínio; 6155: vitaminas/minerais; 1160: duração do sono; 20023: tempo médio para identificar correspondências | A-02/A-05 em adultos; A-04 se houver pares elegíveis | Outras medidas de capacidade; independência de desfecho, janelas, covariáveis, diagnósticos e interseção de participantes | Candidata a auditoria tabular; nenhum modelo aprovado |
| NHANES 2013–2014 | Codebook CFQ_H | CERAD, fluência animal, CFDDS (Digit Symbol Coding) | A-01/A-02/A-05 limitadas a dimensões cognitivas em idosos | Junção com dieta/suplementos e hábitos do mesmo ciclo, pesos, covariáveis e N final | Priorizar auditoria aberta complementar; não mede HA/TDAH/TEA como núcleo |
| NSCH | Página oficial de downloads | Codebook tópico da edição deve ser mapeado; nomes não inferidos | Apoio a condições × hábitos × funcionamento | Fixar edição e verificar campos exatos; sem bateria cognitiva comparável documentada nesta triagem | Não aprovada para capacidade × exposição; complemento apenas |

As notas HBN 10.0 são históricas e documentam instrumentos/mudança de protocolo,
não o número atual de participantes nem a última versão.

## UK Biobank: primeira prova documental de amplitude versus resolução

Campo 6155: 498.471 participantes com alguma informação, incluindo 497.240 na
avaliação inicial; é resposta categórica de uso regular, não dose em mg.
Campo 20016: 236.512 participantes em alguma instância; 165.284 na avaliação
inicial. É soma de acertos em 13 questões, com 14 valores possíveis, e questões
não respondidas no tempo recebem zero.

Portanto, não usar 498.471 como N de suplemento × cognição. Também não derivar
P98/P99 como identificação precisa de alta capacidade a partir de um escore curto
com empates e limitação temporal. Essa é uma limitação de resolução inferida
da documentação, a verificar com distribuição e medidas adicionais.

Fontes: [6155](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=6155),
[20016](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=20016),
[1160](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=1160),
[20023](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=20023).

## Próximas aquisições com propósito definido

1. ABCD: dicionário de uma release fixa e mapeamento de capacidade, hábito,
   desfecho e condição; preparar execução externa compatível com o acordo.
2. HBN: dicionário público/termos; avaliar se resolve a limitação de autismo do
   ABCD antes de priorizar imagem.
3. UK Biobank: completar mapa de campos e instâncias, acrescentando contexto e
   outras medidas cognitivas; N conjunto depende do acesso individual.
4. NHANES: obter CFQ_H, DEMO_H, dieta, suplementos e hábito do mesmo ciclo.
   Primeiro contar cobertura conjunta e independência entre domínios cognitivos;
   não executar uma correlação genérica como aprovação do núcleo.
5. NSCH: verificar condição, hábito e funcionamento no codebook; documentar
   explicitamente a ausência de cognição e manter como linha complementar.

## Fontes adicionais consultadas

- [ABCD visão geral](https://docs.abcdstudy.org/latest/study/)
- [ABCD KSADS, tabela de release 6.1](https://docs.abcdstudy.org/latest/assets/files/documentation/non_imaging/6_1_ksads_p.pdf)
- [HBN fenótipos e acesso](https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/Phenotypic.html)
- [HBN release 10.0](https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/release/release_notes10_0.html)
- [NHANES CFQ_H](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/CFQ_H.htm)
- [NSCH downloads](https://www.census.gov/programs-surveys/nsch/data/datasets.html)
