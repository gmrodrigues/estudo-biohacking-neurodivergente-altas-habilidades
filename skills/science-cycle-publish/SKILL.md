---
name: science-cycle-publish
description: "Finalize cada ciclo deste estudo com gráficos científicos, README e páginas navegáveis no GitHub Pages. Use após análises executadas ou para preparar a publicação e atualizar a seção de resultados do README principal."
---

# Gráficos e publicação por ciclo

Leia [as convenções](../science-discovery/references/project-contract.md) e os
resultados executados. O projeto exige gráficos e navegação em cada ciclo e um
README principal desde a preparação, com resultados após cada ciclo. Preparação de ferramentas,
skills e dados de teste não constitui esse ciclo.

## Produzir gráficos

Use Matplotlib no Pipenv para PNGs científicos legíveis, com SVG/PDF de exportação
quando útil. Escolha curvas para relações não lineares, pontos com intervalos
para contrastes, distribuições para perfis e calibração/erro para previsão.
Não misture unidades incompatíveis. Inclua população, N, ponderação, eixos,
unidades e natureza dos intervalos nas figuras/legendas. Preserve resultados
nulos e escalas comparáveis entre ciclos.

Quando só houver auditoria, plote cobertura, perdas ou ausência reais e declare
que não houve inferência. Em previsão, inclua desempenho fora da amostra e
calibração pertinente. Dados ilustrativos/simulados não entram nas páginas de
resultados empíricos. Estrelas de significância não substituem magnitude e IC.

## Montar e conferir

Em `research/discoveries/<cycle-id>/`, mantenha relatório, código ou sua referência,
PNGs em `figures/` e `cycle.json`. Preencha o
[contrato de publicação](references/cycle-format.md) com agregados, fontes e
proveniência. Dados pessoais, históricos individuais de suplementos e microdados
controlados não fazem parte do site público.

Use `draft` enquanto faltar entrega; `completed` somente após revisar estatística,
figuras e interpretação. Resultados inconclusivos podem compor um ciclo concluído.
Da raiz, execute em diretório de saída vazio:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python scripts/build_discovery_site.py --output _site --update-readmes
```

O gerador cria índice, páginas, PNGs, JSON e links anterior/próximo.
`--update-readmes` cria READMEs dos ciclos e atualiza o bloco de resultados do
principal após existir um ciclo concluído, preservando sua apresentação e texto
autoral fora do bloco gerado. Se o principal faltar, o gerador cria uma versão
básica; sua criação manual não depende de concluir um ciclo. Para reconstruir,
use outra pasta vazia, evitando resultados obsoletos no build.

Confira imagens e navegação no navegador, incluindo tela estreita e links das
figuras/fontes. Use a skill de navegador disponível quando necessário. Execute
os testes com Pipenv após alterar o gerador.

## Publicar

O workflow `.github/workflows/discovery-pages.yml` publica ciclos concluídos após
push para `main`, com instalação Pipenv, e não faz deploy se a lista estiver vazia.
O README deve ser atualizado localmente antes do commit; o workflow não escreve
commits automaticamente. Siga a autorização de publicação dada na conversa, sem
estendê-la a outros repositórios ou conteúdos.

Pages precisa ter a fonte `GitHub Actions` habilitada no repositório. Verifique
ou configure quando houver acesso autorizado; sem acesso, registre essa pendência
e conclua o build local. Consulte a
[documentação oficial](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
se o fluxo mudar.

Após deploy, confira workflow e URL devolvida, abrindo índice, ciclo e gráfico.
Diferencie build local validado, workflow enviado e site publicado. Não anuncie
uma URL estimada como deploy verificado.
