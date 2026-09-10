# Fase inicial: base analítica e provas de conceito

Plano operacional vigente: [Fase 1 — base ampla e POCs](PHASE_1_PLAN.md).
O plano define etapas, cobertura, precisão, seis POCs e critérios de encerramento.

Estado: `blocked_by_access` para microdados ABCD. O protocolo, os critérios e a
auditoria de metadados podem ser concluídos agora; esta fase não estima benefício
de hábito ou suplemento.

## Produto

Uma tabela por participante-onda, cujo dicionário preserve origem de cada medida.
Cada prova usa variáveis pré-definidas e informa perdas, sem exigir que todos os
domínios estejam completos para toda a amostra.

| Domínio | Exigência mínima | Estado |
|---|---|---|
| Identidade longitudinal | identificador pseudônimo e onda | `measured` |
| Capacidade | duas medidas cognitivas documentadas por janela | `measured` |
| Perfil neurocognitivo | diagnóstico e/ou escala dimensional, com informante | `measured` ou `explicit_proxy` |
| Hábito | sono, atividade/sedentarismo ou rotina com janela clara | `measured` |
| Desfecho | função executiva, desempenho ou funcionamento na onda seguinte | `measured` |
| Contexto | idade, sexo registrado, centro, SES e tratamento relevante | `measured` |

## Provas de conceito

| ID | Pergunta | Passa se | Restringe se |
|---|---|---|---|
| POC-01 | IDs formam trajetórias sem duplicação? | cardinalidade, ondas e perdas reproduzidas | IDs/ondas não acompanham a mesma pessoa |
| POC-02 | Há cobertura para capacidade contínua por onda? | instrumentos, escalas e ausências documentados | proxy único ou exclusão seletiva é necessária |
| POC-03 | Capacidade e sintomas podem ser descritos sem rótulo automático? | contingências e incerteza por grupo são reportáveis | diagnóstico, informante ou célula são insuficientes |
| POC-04 | Hábito em `t` pode ligar-se a função executiva em `t+1`? | janela, ordem temporal, ajuste mínimo e retenção verificados | exposição e desfecho ocupam a mesma janela |

POC-01 a POC-03 são auditorias. POC-04 pode estimar associação longitudinal
pré-registrada. Resultado não significativo pode ser inconclusivo; descartar um
efeito relevante exige precisão suficiente. Não procurar interações até obter
significância.

## Esquema mínimo

```text
participant_wave
  participant_id, wave, assessment_window, site
  cognition_*, executive_function_*, academic_function_*
  adhd_*, autism_*, informant_*, medication_*
  sleep_*, activity_*, diet_*
  age, sex_recorded, socioeconomic_context_*
  provenance: source_file, variable, instrument, unit, missing_code
```

`provenance` é obrigatório. Uma variável calculada registra fórmula, versão e
campos de origem. Ausência, recusa, salto e não uso não são fundidos sem codebook.

## Entrada ABCD

ABCD é a primeira candidata porque acompanha quase 12 mil jovens desde 9–10 anos
e mede desenvolvimento cognitivo, comportamento, sono, atividade e contexto ao
longo do tempo. O NIMH descreve 21 locais e o NDA exige conta/acesso para dados
individuais. A execução começa após autorização legítima e manifesto de versão.

Fontes: [NIMH ABCD](https://www.nimh.nih.gov/research/research-funded-by-nimh/research-initiatives/adolescent-brain-cognitive-developmentsm-study-abcd-studyr) e [NDA](https://nda.nih.gov/data_dictionary.html?source=ABCD&submission=ALL).
