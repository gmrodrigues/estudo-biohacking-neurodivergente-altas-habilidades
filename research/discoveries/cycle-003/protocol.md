# Ciclo 003 — auditoria de magnésio por produto e antiácido

Registro local de 2026-09-09, anterior à execução desta auditoria. Os resultados
de H3 e a descoberta da ambiguidade em `DSQTMAGN` já são conhecidos. Esta rodada
avalia mensuração; não testa novamente a associação com sono e não constitui
pré-registro externo ou replicação.

## Pergunta e decisão prévia

Entre os participantes de H3, o que significa `DSQTMAGN` ausente: ausência de
produto com magnésio, produto contendo magnésio sem ingestão calculável, antiácido,
produto não identificado ou combinação desses estados?

Usar `DSQIDS_L` no nível participante-produto, ligado por `SEQN`, e `DSPI`/`DSII`
no nível de produto, ligados exclusivamente por `DSDPID`. Preservar ocorrências
repetidas de produtos porque podem representar recipientes, doses ou formulações
distintas. Verificar cardinalidade e cobertura antes de agregar.

Classificar separadamente:

- magnésio individual calculado em `DSQIMAGN`;
- produto cujo rótulo em `DSII` contém ingrediente elementar `MAGNESIUM`;
- ingrediente composto cujo nome contém `MAGNESIUM`, sem assumir conversão para
  magnésio elementar;
- antiácido (`DSDANTA=1` ou `2`), mantendo a seção de origem;
- ausência de correspondência ou baixa certeza (`DSDMTCH`);
- dias, quantidade ou razão de porção ausentes/inválidos.

Comparar a soma de `DSQIMAGN × DSD103 / 30` com `DSQTMAGN`, permitindo apenas
diferença numérica de arredondamento. Não publicar nomes de produtos associados
a participantes nem `SEQN`; resultados públicos serão agregados.

## Limites

Nome contendo “magnesium” não prova quantidade elementar, biodisponibilidade,
forma ingerida ou indicação clínica. Ausência de `DSQIMAGN` não será convertida
automaticamente em zero ou em dose desconhecida. A base de rótulos reúne produtos
desde 1999 e só será usada após restringir aos `DSDPID` observados em 2021–2023.
Botânicos e misturas podem exigir `DSBI`; esta auditoria verificará cobertura, mas
não inferirá magnésio oculto sem identificação explícita e unidade harmonizada.

H3 permanece numericamente preservada até que um adendo separado registre um
novo estimando e tratamento de exposição. HA, autismo e TDAH permanecem
`not_assessed`.

## Fontes oficiais

- [DSQIDS_L: documentação e códigos](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQIDS_L.htm)
- [DSQTOT_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm)
- [NHANES-DSD: DSPI](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSPI.htm)
- [NHANES-DSD: DSII](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSII.htm)
- [NHANES-DSD: DSBI](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSBI.htm)
