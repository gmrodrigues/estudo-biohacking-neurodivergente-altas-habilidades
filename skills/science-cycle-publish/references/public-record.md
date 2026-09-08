# Registro público contínuo

## Entradas e navegação

O gerador usa `research/site/study.json` para a apresentação e páginas de objetivos,
planejamento, fontes e progresso. Cada página tem `id`, `title` e `sections`.
Uma seção tem `title` e campos opcionais `paragraphs`, `items`, `table`
(`headers`/`rows`) e `links` (`title`/`url` HTTPS). Texto é escapado como HTML.

Em cada ciclo mantenha `public-dossier.json` com `sections` e, quando necessária,
`review_note`. A nota aparece antes dos resultados e também no README. O dossiê
é documentação editorial posterior quando não houver registro anterior verificável.
Os manifestos antigos continuam válidos, mas novos ciclos devem incluir o dossiê.

## Artigos por ciclo

Use `article.json` no diretório do ciclo, com `title`, `summary` e `sections`
no mesmo formato editorial. O gerador cria `article.html` e `article.md` no site,
inclui acesso no índice e na página do ciclo e, com `--update-readmes`, gera o
Markdown no repositório e links nos READMEs. Edite o JSON como fonte única.

O artigo interpreta resultados existentes: não o conte como novo ciclo empírico.
Inclua público-alvo, comparação com estudos, particularidades/limites,
quantificação e implicações para decisões. Notas de revisão do ciclo também devem
aparecer no artigo antes dos resultados afetados. Mantenha fichas de comparação
em `article-evidence.yaml` e marque seleção posterior aos resultados.
Para suplementação, siga a referência de comparação e decisão da skill de síntese.

## Conteúdo que permite acompanhar a pesquisa

- Objetivos: perguntas, construtos, comparadores, estratos pretendidos e limites
  de cobertura; não transformar pessoas sem diagnóstico informado em NT.
- Plano: separar executado, proposto, não estimável e dependente de acesso.
  Próximos ciclos têm critérios de avanço; não inventar datas de execução.
- Hipóteses: motivação, estimando, expectativa, registro/data, covariáveis,
  multiplicidade, resultado e limitações. Distinguir registro local de pré-registro externo.
- Métodos: módulos/ondas/variáveis, junções por pergunta, perdas observadas,
  recodificações, pesos, intervalos, seleção de modelo, teste reservado e baseline.
- Decisões: justificativa resumida baseada em artefatos, alternativas plausíveis,
  desvios, impacto conhecido e testes que distinguiriam explicações rivais.
  Não reconstruir retrospectivamente um histórico de decisões não documentado.
- Fontes: distinguir catálogo, metadados consultados, dados baixados, dados
  analisados e literatura selecionada. Contagens de ensaios precisam de data,
  consulta e ressalva sobre resultados/eficácia.
- Progresso: incluir inventários, códigos, grafos e nulos, com links para
  evidência verificável. Pendências de revisão também são progresso publicável.

Se o texto não corresponder ao código, sinalize a divergência antes dos números.
Não trocar estimativas ou apagar a versão original durante uma edição editorial.
Uma correção analítica deve registrar adendo, execução e atualização conjunta
de resultados, intervalos, multiplicidade e gráficos.

## Publicabilidade e identidade visual

Use seleção explícita de conteúdo científico agregado. Não copie automaticamente
o catálogo inteiro: ele também contém históricos pessoais de suplementos.
Links de auditoria devem apontar para documentos adequados ao público, não para
arquivos pessoais só porque já estão versionados.

A testeira remete ao site principal por fundo escuro, acento laranja e tipografia
LeagueGothic; preserve leitura clara dos relatórios e PNGs. Links relativos entre
páginas funcionam no subdiretório Pages. Alterações no site principal exigem escopo
autorizado específico; sua vinculação não autoriza outros projetos.

## Conferência

Construa em saída vazia com Pipenv e atualize READMEs. Verifique navegação entre
índice, páginas, ciclo e fontes; nota de revisão visível; distinção entre resultado
e proposta; nenhum histórico individual no HTML. Execute os testes do gerador
quando ele mudar e confira o layout em tela larga/estreita quando houver navegador.
O workflow inclui `research/site/**`, para mudanças editoriais também publicarem.
