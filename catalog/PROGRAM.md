# Programa: saúde cognitiva de precisão

## Pergunta orientadora

Quais fatores modificáveis se associam a trajetórias de funcionamento cognitivo,
e essas associações diferem por **capacidade cognitiva contínua** e por perfil
neurocognitivo? O programa não parte de uma alegação de que suplementos produzam
capacidade ou tratem TDAH/autismo.

## Modelo conceitual

```text
capacidade e perfil cognitivo basal ─┐
condições e sintomas dimensionais ──┼─> funcionamento e trajetória
hábito, contexto e ambiente ────────┤
nutrição, biomarcadores e exposição ┘
```

Capacidade será estimada por um conjunto documentado de medidas de raciocínio,
memória, vocabulário, função executiva e desempenho. Percentis (P95, P98, P99)
são análises de sensibilidade de um contínuo; não são rótulos clínicos de HA.

## Fase inicial: base analítica mínima viável

A primeira entrega é uma base que permita responder perguntas simples sem
fabricar comparabilidade. O padrão de passagem é a [fundação analítica](data-sources/ANALYTIC_FOUNDATION.md): versão e acesso legítimos, mapa
campo→construto, chaves/ondas, perdas, janelas temporais e contagens por perfil.

As provas de conceito são deliberadamente pequenas:

1. reproduzir regras de elegibilidade e cobertura das medidas por onda;
2. calcular índice contínuo de capacidade somente após verificar estrutura e
   invariância mínima das medidas;
3. descrever sobreposição observada entre capacidade, sintomas/diagnósticos e
   função executiva, sem diagnosticar por algoritmo;
4. testar se hábito medido em `t` antecede função executiva em `t+1`, com
   especificação mínima e resultado nulo publicável.

Falhar em uma prova descarta ou reduz o escopo da hipótese simples antes de
modelos latentes, interações ou suplementação.

## Arquitetura de fontes

| Fonte | Questão própria | Papel no programa |
|---|---|---|
| ABCD | Desenvolvimento de capacidade, sintomas, sono, atividade e contexto | Base longitudinal inicial |
| HBN | Perfis transdiagnósticos com fenotipagem profunda | Replicação e heterogeneidade 2e |
| UK Biobank | Exposições adultas, biomarcadores e cognição | Interações e replicação de hábitos/suplementos |
| NHANES | Nutrientes, produtos e biomarcadores populacionais | Medição de exposição; não identifica os perfis-alvo |
| Terman/SMPY | Capacidade e realização através da vida | Validação conceitual, não causalidade nutricional |

## Escada de inferência

1. **Descrição:** medida e perfil existem e são estáveis o suficiente?
2. **Associação longitudinal:** mudança de hábito antecede desfecho compatível?
3. **Replicação:** direção, escala e limites sobrevivem em fonte compatível?
4. **Intervenção:** protocolo definido altera hábito e desfecho, com segurança?

Suplementação só entra no quarto degrau como teste de exposição definida. A
associação entre regularidade do sono e funcionamento pode priorizar o sono como
alvo; não demonstra que qualquer suplemento o consolide.

## Produtos obrigatórios por fase

| Fase | Produto | Regra de conclusão |
|---|---|---|
| Fundação | auditoria, dicionário, manifesto de dados e provas de conceito | `estimable`, `estimable_with_limits` ou `needs_data` por pergunta |
| Descoberta | protocolo, código, resultados agregados e sensibilidades | associação delimitada, sem causalidade |
| Replicação | protocolo harmonizado e comparação de estimandos | heterogeneidade relatada, não apagada |
| Intervenção | protocolo prospectivo, segurança e análise temporal | efeito limitado à população, produto e janela testados |
