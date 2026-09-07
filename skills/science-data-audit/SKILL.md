---
name: science-data-audit
description: "Audite cobertura, códigos, junções, amostragem e mensuração das bases deste estudo antes de analisar saúde e neurodivergência. Use também para decidir se uma hipótese é estimável nos dados disponíveis."
---

# Auditoria para análise

Leia [as convenções do projeto](../science-discovery/references/project-contract.md).
Consulte `catalog/data-sources/sources.yaml`, `ACCESS_FROM_CODEX.md` e a viabilidade
atual. Verifique o acesso efetivo: metadados, agregados, registros individuais e
resultados de estudos são níveis distintos.

## Converter a pergunta em requisitos

Liste exposição, desfecho, unidade de análise, população, janela e ajustes mínimos.
Para cada indicador registre arquivo/versão, campo, unidade, instrumento,
informante, elegibilidade, códigos de ausência e granularidade temporal. Classifique
cada dimensão como medida, aproximação explícita ou indisponível.

Faça junções apenas com chaves legítimas da mesma coorte e onda; nunca una pessoas
de bases independentes por idade, diagnóstico ou semelhança de perfil. Verifique
cardinalidade, duplicação e perdas a cada junção. Rótulos e exposições repetidas
não transformam um registro transversal em acompanhamento.

## Checagens que mudam a análise

- Recalcule contagens e cobertura por hipótese, antes/depois de exclusões e por
  estrato. Evite exigir todos os nove componentes NHANES para qualquer pergunta.
- Distinga não uso, zero, recusa, desconhecido, salto de questionário e exposição
  de quantidade desconhecida. Em suplementos, só reconstrua zero quando os
  códigos de participação e o codebook sustentarem essa interpretação.
- Verifique o tratamento dos valores quase zero na leitura SAS XPORT contra
  frequências oficiais antes de reutilizar a normalização existente.
- Valide unidades, limites documentados, idade truncada para divulgação e
  códigos como 7/9/77/99 por campo; eles não são regras universais.
- Escolha peso, estratos e PSU com a documentação dos componentes e do ciclo.
  Justifique a combinação de dieta, suplementos e exames. Se não houver desenho
  implementado corretamente, restrinja a saída a exploração da amostra.
- Compare elegíveis, respondentes e amostra analítica. Considere não resposta,
  modo de entrevista e exclusão de quem precisa de informante/intérprete.
- Audite temporalidade, sobreposição entre indicadores e desfecho e limites de
  mensuração: concentração no DPQ, sono habitual, recordatório alimentar de um dia
  e exposição suplementar de 30 dias não descrevem a mesma janela.

## Entregar uma decisão útil

Grave `data-audit.md` na rodada, com mapa campo→construto, fluxos de seleção,
ausências, desenho amostral, problemas e decisão por hipótese:
`estimable`, `estimable_with_limits`, `needs_data` ou `not_identifiable`.

Inclua comandos Pipenv que reproduzem o inventário. Reexecute apenas verificações
afetadas se o insumo mudar. Declare acesso controlado pendente sem impedir as
análises independentes em dados abertos. Não preencha diagnósticos ausentes ou
atribua validade clínica a proxies para tornar uma pergunta artificialmente viável.
