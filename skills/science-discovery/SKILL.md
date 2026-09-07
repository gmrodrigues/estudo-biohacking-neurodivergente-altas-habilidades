---
name: science-discovery
description: "Planeje ou execute rodadas de descobertas neste estudo de altas habilidades, neurodivergência e suplementação, conectando dados, hipóteses, previsão e evidência. Use para pedidos amplos de investigar achados; uma pergunta isolada pode usar apenas a skill especializada."
---

# Rodada de descobertas

Leia [as convenções do projeto](references/project-contract.md) antes de agir.
Localize a raiz que contém `Pipfile` e `catalog/data-sources`. Se necessário,
resolva o link de instalação desta skill para localizar o checkout.

## Escolher o trabalho

Leia o [plano de descobertas](../../catalog/data-sources/DISCOVERY_PLAN.md), a
[viabilidade](../../catalog/data-sources/INITIAL_FEASIBILITY_ANALYSIS.md) e os
artefatos da rodada anterior. Verifique se há resultados executados, sem tomar
hipóteses documentadas como achados. Um pedido apenas de plano produz um plano;
um pedido de execução prossegue até os produtos possíveis com os dados disponíveis.

Priorize perguntas pela cobertura conjunta de exposição e desfecho, qualidade de
mensuração, relevância pessoal explicitamente relatada e possibilidade de
replicação. Use a lista pessoal de suplementos somente quando a pergunta envolver
personalização; compra, interesse e uso continuado têm significados distintos.

## Conduzir a rodada

Leia a skill correspondente antes de realizar cada fase necessária. As quatro
especializadas acompanham este pacote; as fases podem ser executadas pela mesma
instância, sem exigir delegação.

1. [Auditar dados](../science-data-audit/SKILL.md): determinar perguntas
   estimáveis, pesos, cobertura, confiabilidade e população real.
2. [Testar hipóteses](../science-hypothesis-test/SKILL.md): registrar contrastes
   antes dos resultados e executar estimativas com análise de sensibilidade.
3. [Modelar previsão](../science-predictive-model/SKILL.md): quando houver alvo
   válido, avaliar desempenho fora da amostra sem rótulo diagnóstico como entrada.
4. [Interpretar evidências](../science-evidence-synthesis/SKILL.md): selecionar
   estudos e previsões teóricas antes de interpretar; depois confrontar os achados
   com mecanismos e explicações rivais. Esta fase pode começar antes dos testes.

Na falta de uma dimensão, prossiga com uma hipótese isolada estimável e registre
a lacuna. Uma amostra populacional sem diagnósticos medidos não constitui um grupo
neurotípico. Compartilhar parâmetros entre bases exige indicadores comparáveis;
não cria informação sobre combinações que nunca foram observadas.

## Entregar

Use uma rodada identificável em `research/discoveries/<run-id>/`. Entregue a
pergunta, origem dos dados, resultados com intervalos, validações executadas,
limites de transporte para HA/ASD/ADHD e próximos testes discriminantes. Inclua
comandos Pipenv e versão/hash dos insumos. Preserve resultados nulos e hipóteses
não estimáveis. Declare separadamente modelos propostos, ajustados e validados.

Pare uma análise não identificável com uma conclusão de insuficiência e continue
as perguntas independentes viáveis. Não repita ajustes até obter significância.
