---
name: science-evidence-synthesis
description: "Selecione estudos e confronte os achados deste projeto com teorias, resultados humanos e explicações rivais, incluindo suplementação, metilação e comparações HA, autismo e TDAH. Use para síntese de evidência e interpretação, não para contar protocolos como eficácia."
---

# Estudos e explicações dos achados

Leia [as convenções](../science-discovery/references/project-contract.md). Antes de
interpretar, obtenha a hipótese/estimando e o artefato do resultado efetivamente
executado. Se ainda não houver resultados, entregue previsões teóricas e estudos
candidatos, identificando esse estado.

## Selecionar evidência rastreável

Registre pergunta, busca, data, bases, elegibilidade, população, intervenções,
comparadores, desfechos, seguimento e critérios de qualidade antes de selecionar
estudos por direção de resultado. Busque resultados negativos e divergentes.
Uma busca rápida dirigida não deve ser descrita como revisão sistemática exaustiva.

Use fontes primárias para extrair efeitos: artigo, suplemento, protocolo e
resultados do registro quando existentes. Revise registros locais em
`data/public/clinicaltrials` e rastreie publicações por NCT/DOI/PMID. O grafo em
`data/derived/evidence-graph` é uma ferramenta de busca; verifique manualmente
tipo de intervenção, comparador e significado de cada aresta utilizada.

Um ensaio pode ter várias publicações: deduplique por estudo/amostra e preserve
relatórios complementares. `has_results` não garante resultado relevante para a
pergunta; ausência de resultados no registro não prova inexistência de publicação.

Copie [a ficha de evidência](assets/evidence-card.yaml) por estudo/achado. Extraia
denominadores, perdas, estimativa, intervalo e segurança, com localização exata.
Sem texto completo, marque a extração como limitada ao resumo. Não invente valores
faltantes nem calcule efeito a partir de uma conclusão verbal.

## Avaliar validade e transporte

Escolha avaliação de risco de viés apropriada ao desenho, documentando respostas
por domínio. Separe ensaio randomizado, observacional humano, mecanismo humano,
animal/in vitro e opinião. Metanálise exige compatibilidade de estimandos,
medidas, exposição e independência; não combine suplementos, doses ou populações
distintas apenas para obter um número agregado.

Para HA, ASD, ADHD e combinações, registre como foram identificados, idade,
sexo/gênero medidos, medicação e contexto. Generalização entre eles é uma hipótese
de transporte. Falta de evidência específica não demonstra ausência de benefício
nem justifica extrapolação automática.

Em suplementos, diferencie produto, sal/forma, dose elementar, preparação,
cointervenções e estado nutricional basal. No tema metilação, separe ingestão,
biomarcadores, variantes genéticas e função clínica; mudança em homocisteína ou
plausibilidade mitocondrial não comprova benefício cognitivo/esportivo.

## Confrontar teoria e achado

Para cada relação, apresente mecanismo candidato, estudos que o sustentam,
previsão discriminante e explicações rivais plausíveis: seleção, usuário saudável,
causalidade reversa, medicação, sobreposição de medidas ou contexto. Registre se a
teoria foi proposta antes ou depois do resultado. Teoria pós-hoc exige novo teste.

Classifique evidência como direta, indireta, conflitante ou insuficiente. Um padrão
compatível não escolhe sozinho entre mecanismos que preveem o mesmo resultado.
Especifique que medição, comparação ou estudo distinguiria as alternativas.

Entregue `evidence-synthesis.md` e fichas preenchidas com links junto às afirmações,
lacunas de acesso e limites. Personalização usa apenas fatos fornecidos pelo
usuário, sem inferir diagnóstico, uso atual ou causalidade de relatos de compra.
