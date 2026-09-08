# Plano de descobertas e skills

Data: 2026-09-07. Estado: plano operacional; nenhum efeito novo estimado nesta etapa.

## Primeira rodada

A primeira pergunta é quais relações entre sono, nutrição, atividade e sintomas
podemos medir com credibilidade em adultos. A auditoria definirá uma amostra por
hipótese; a interseção histórica de 6.337 registros não obriga excluir pessoas
que tenham todos os campos necessários para uma pergunta mais simples.

| Ordem | Pergunta candidata | Limite que precisa ser preservado |
|---|---|---|
| 1 | Ingestão de cafeína se associa à duração de sono, e a associação varia com idade? | recordatório de um dia e suplemento de 30 dias; L-teanina/horário não estão demonstrados nos totais locais |
| 2 | Sono e sedentarismo se associam a sintomas depressivos em conjunto? | sobreposição do item de sono no PHQ-9, confundimento e causalidade reversa |
| 3 | Ingestão de magnésio e suplementação se associam ao sono após considerar dieta e contexto? | códigos de não uso, ausência e antiácidos; totais não distinguem glicinato de treonato |

Cada pergunta terá estimando, plano datado, análise principal e sensibilidades
antes dos efeitos. Elas são candidatas priorizadas por viabilidade e pelos
interesses relatados; poderão ser retiradas se a auditoria mostrar insuficiência.
Não se presume benefício nem um mecanismo específico.

Depois, construir um primeiro preditor de duração de sono ou carga de sintomas
em pessoas reservadas para teste, sem diagnóstico como entrada. Definir um alvo
primário; comparar baseline e modelo regularizado, com preparo das variáveis
restrito ao treino. Dados transversais não validam previsão futura.

Interpretação acompanha o ciclo: selecionar estudos e previsões antes de examinar
os efeitos, confrontá-los depois e listar testes que distinguem teorias rivais.
Resultados nulos, inconclusivos e perguntas não estimáveis fazem parte da entrega.

## Ampliar conforme a cobertura

Whey/proteína e creatina são relevantes para os interesses relatados, mas dados
de dieta e atividade não medem recuperação, força relativa ou performance em artes
marciais. L-teanina, formas de magnésio e metilação funcional exigem campos ou estudos
adicionais. A síntese de estudos pode avançar enquanto essas medidas são buscadas.

HA, ASD, ADHD, duplas/triplas e NT serão comparados quando efetivamente medidos.
Pessoas sem rótulo registrado não serão classificadas NT. A auditoria verificará
também quais dimensões de família, finanças, substâncias, criatividade e profissão
existem em cada base. Crianças/adolescentes precisam de conjuntos elegíveis e normas
próprias. Acesso a microdados controlados permanece uma dependência explícita.

## Skills e produtos

| Invocação | Responsabilidade | Produto esperado |
|---|---|---|
| `$science-discovery` | conduzir a rodada e resolver a ordem das fases | relatório de descobertas e limitações |
| `$science-data-audit` | verificar se os dados sustentam a pergunta | mapa de cobertura e decisão de estimabilidade |
| `$science-hypothesis-test` | registrar e executar contrastes | ficha da hipótese e resultados com intervalos |
| `$science-predictive-model` | mensurar dimensões e prever sem diagnóstico | modelo, ficha, teste e contribuições por domínio |
| `$science-evidence-synthesis` | selecionar estudos e avaliar teorias rivais | fichas de evidência e próximos testes discriminantes |
| `$science-cycle-publish` | plotar e publicar cada ciclo | gráficos, READMEs e páginas navegáveis no GitHub Pages |

O README principal apresenta o projeto desde a preparação. Sua seção de resultados
será atualizada após cada ciclo concluído. Cada ciclo terá README próprio,
gráficos, fontes, estimativas e limites.
O gerador `scripts/build_discovery_site.py` produz índice e navegação entre ciclos;
o workflow `.github/workflows/discovery-pages.yml` está preparado para deploy no
GitHub Pages quando houver resultados concluídos e Pages estiver habilitado.
Publicação efetiva exige envio ao remoto e verificação do deploy.

Fontes das skills ficam em [skills](../../skills/science-discovery/SKILL.md), no
checkout. Sua instalação usa links individuais no diretório de skills do usuário
para que alterações locais sejam refletidas na descoberta. As referências entre
skills dependem do pacote completo. A interface pode exigir uma nova sessão para
atualizar o catálogo; é possível ler diretamente o `SKILL.md` enquanto isso.

Exemplo de próxima execução: “Use `$science-discovery` para executar a primeira
rodada, começando pela auditoria de cafeína e sono”. Isso inicia a análise; criar
ou validar a skill, por si só, não treina modelos nem produz descobertas.

Toda execução Python usa Pipenv. Os templates YAML são fichas a preencher,
marcadas como `draft`/`proposed` e `not_run`; não são motores estatísticos.

## Retomada da próxima sessão

Consulte [`NEXT_SESSION.md`](../../NEXT_SESSION.md) antes de alterar o ciclo 001.
O documento registra o estado publicado, a divergência de fronteira de sono em H2,
o adendo que precisa ser decidido antes de rerodar, a auditoria de robustez e as
perguntas de suplementação cafeína–magnésio. A tese sobre capacidades encobertas
está em [`FOUNDATIONAL_HYPOTHESIS.md`](FOUNDATIONAL_HYPOTHESIS.md) e permanece
hipótese, não conclusão do ciclo 001.
