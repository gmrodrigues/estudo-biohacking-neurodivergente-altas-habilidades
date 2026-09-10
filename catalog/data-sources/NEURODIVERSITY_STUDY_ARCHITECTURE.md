# Arquitetura de estudos paralelos: HA, TDAH, autismo e coexistências

Decisão registrada em 2026-09-10. O programa será composto por estudos
separados, porque não há uma base identificada que meça com validade comparável
HA, TDAH, autismo, sono, contexto e acompanhamento em todas as pessoas.

## Regra central

Cada estudo estima uma pergunta dentro de sua própria população. Comparar
resultados não autoriza juntar participantes de bases diferentes, imputar
diagnósticos ou tratar uma medida de QI como rótulo automático de HA.

| Frente | Pergunta inicial | Base de início | Produto do primeiro ciclo | Limite próprio |
|---|---|---|---|---|
| **HA/capacidade elevada** | Como capacidade medida, desempenho, bem-estar e contexto se distribuem ao longo do tempo? | Project Talent público; ECLS-K para auditoria educacional; depois coorte com identificação explícita de HA | Auditoria de capacidade, medida e trajetória | Capacidade medida não equivale automaticamente a HA identificada; o Project Talent não resolve TDAH/autismo no mesmo indivíduo |
| **TDAH** | Como atenção/função executiva, capacidade e funcionamento variam em participantes com TDAH? | ADHD-200 público; NSCH público para contexto populacional; HBN conforme termos | Auditoria de diagnóstico, centro, QI/cognição e dados ausentes | Diagnóstico/fenótipo e aquisição variam por fonte; imagem não diagnostica TDAH |
| **Autismo** | Como cognição, funcionamento e contexto variam em participantes autistas? | ABIDE II público; HBN conforme termos | Auditoria de diagnóstico, centro, QI/cognição e dados ausentes | ABIDE é multissítio e não mede toda a vida cotidiana; QI não é HA |
| **TDAH+autismo** | A coexistência difere dos perfis isolados nos desfechos comuns? | NSCH público para coocorrência relatada; HBN se as medidas permitirem | Auditoria de células, informante e sobreposição | Baixa célula e diagnóstico por relato/variável exigem intervalos e não permitem inferir HA |
| **HA+TDAH, HA+autismo e tripla** | Há padrões de capacidade e funcionamento que diferem da soma dos componentes? | Coorte específica ou fonte que meça ambos validamente | Auditoria de elegibilidade e protocolo registrado | `needs_data` até haver identificação de HA e medidas clínicas independentes |

## Ponte de comparação entre estudos

1. Criar um dicionário de construtos comuns: capacidade cognitiva, atenção/função
   executiva, sono, funcionamento, bem-estar, contexto e medicação.
2. Em cada base, classificar cada campo como `measured`, `explicit_proxy` ou
   `unavailable`; não forçar a harmonização quando instrumentos/janelas forem
   incompatíveis.
3. Registrar em cada protocolo o mesmo estimando conceitual, população, ajuste,
   contraste, período e escala de efeito quando possível.
4. Comparar estimativas, intervalos, qualidade de medida e heterogeneidade entre
   estudos por síntese, jamais por junção de IDs ou pareamento entre bases.
5. Declarar uma conclusão compartilhada somente quando os estudos forem
   comparáveis e a direção/magnitude forem consistentes; divergência é resultado,
   não erro a ocultar.

## Da comparação indireta à intervenção

Cada frente pode primeiro identificar hábitos associados a funcionamento dentro
de sua própria população. A síntese entre frentes serve para priorizar alvos de
rotina compartilhados ou específicos. Suplementos entram em uma etapa posterior:
o protocolo precisa testar se um produto/dose definido muda a adesão ou a
consolidação do hábito e o desfecho ao longo do tempo. Assim, uma associação entre
sono regular e funcionamento não é convertida diretamente em alegação de que um
suplemento "reforça" sono; ela gera uma hipótese para ensaio ou N-of-1.

## Ordem prática

1. Baixar e auditar ABIDE II e ADHD-200 em ciclos distintos.
2. Auditar o arquivo público do Project Talent como frente HA/capacidade e o
   codebook do ECLS-K para decidir se identificação educacional e diagnósticos
   coexistem na camada pública.
3. Auditar NSCH como referência populacional de TDAH, autismo e coexistência;
   não usá-lo como medida de HA.
4. Avaliar HBN para o primeiro protocolo com medidas comuns mais amplas.
5. Abrir a coorte específica HA+condições somente quando houver instrumentos,
   governança e tamanho suficientes.

O mapa de fontes e acessos está em
[OPEN_NEURODEVELOPMENT_DATA_AUDIT.md](OPEN_NEURODEVELOPMENT_DATA_AUDIT.md) e
[HIGH_ABILITY_DATA_AUDIT.md](HIGH_ABILITY_DATA_AUDIT.md).
