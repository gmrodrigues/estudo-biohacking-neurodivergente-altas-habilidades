# Contrato do ciclo público

Entrada: `research/discoveries/<cycle-id>/cycle.json`. Um rascunho pode conter
apenas `{"status": "draft"}` e será ignorado. Para publicação, preencha os campos
abaixo com resultados executados.

| Campo | Conteúdo |
|---|---|
| `schema_version` | inteiro `1` |
| `id` | nome da pasta; letras minúsculas ASCII, dígitos e hífen |
| `status` | `completed` para ciclo revisado e concluído |
| `data_kind` | `empirical_aggregate` para resultados agregados empíricos |
| `title`, `summary`, `population` | textos não vazios e autocontidos |
| `completed_at` | data ISO `YYYY-MM-DD` |
| `findings` | lista não vazia com `question`, `estimate`, `uncertainty`, `sample`, `interpretation` |
| `figures` | lista não vazia com `path`, `alt`, `caption` |
| `limitations` | lista de textos específicos desta análise |
| `sources` | lista com `title` e URL HTTPS em `url` |
| `reproducibility` | `command`, `code_revision` e mapa `input_sha256` |

Cada campo de achado é texto com unidade/escala: permite representar correlação,
contraste ajustado, cobertura e métricas preditivas sem misturá-los num eixo.
Intervalo indisponível deve ter justificativa em `uncertainty`; inventário de
registros não exige inventar IC. O gerador verifica estrutura, não validade
científica nem veracidade dos resultados.

`code_revision` identifica commit e, se houver mudanças locais, hash/versão do
código executado. `input_sha256` mapeia fontes para hashes de 64 caracteres
hexadecimais. Não inclua caminhos pessoais ou conteúdo individual no manifesto.

`figures[].path` é relativo ao ciclo e aponta para PNG existente, sem `..`,
caminho absoluto ou link que escape da pasta. Prefira `figures/caffeine-sleep.png`.
`alt` descreve o conteúdo; `caption` informa interpretação, população, peso e
incerteza. A imagem é copiada preservando seu caminho, também referenciado no JSON.

Saída por ciclo:

```text
_site/
  index.html
  cycles.json
  cycles/<cycle-id>/
    index.html
    cycle.json
    figures/...
```

O índice lista ciclos mais recentes primeiro; cada ciclo liga ao anterior e ao
seguinte, por data de conclusão e identificador. Links relativos funcionam no
subdiretório do GitHub Pages. `--update-readmes` produz o README de cada ciclo e
atualiza o bloco de resultados do principal após a primeira conclusão. O README
principal já pode apresentar o projeto antes disso; seu texto externo ao bloco
gerado é preservado.

O workflow precisa ser enviado ao GitHub e Pages configurado para `GitHub Actions`
antes do primeiro deploy. Criar as skills não significa que isso já ocorreu.
