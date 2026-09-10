# ABCD: seleção tabular e execução local

Estado: infraestrutura testada com dados sintéticos; microdados não baixados.
Release candidata: 7.0, conforme documentação consultada em 2026-09-10.
A confirmação do DUC e da versão disponível ao pesquisador permanece pendente.

## Fluxo

Download automatizado e análise por script não são tratados como envio de dados
ao modelo. O agente pode orquestrar ferramentas com acesso autorizado; arquivos,
linhas de exemplo e saídas com dados permanecem locais. A FAQ não é uma aprovação
genérica de qualquer integração: respeitar o acordo e impedir a exposição dos
dados ao contexto generativo.

O processo de acesso atual é NBDC/DUC, com vínculo institucional e aprovação de
responsável institucional. Antes da aprovação é possível consultar o dicionário.
Não solicitar credenciais na conversa; autenticação ocorre no mecanismo oficial.

Fonte: [acesso oficial](https://docs.abcdstudy.org/latest/usage/access.html).

## Seleção mínima documental

| Papel | Tabela/campo confirmado na documentação pública | Escolha ainda pendente |
|---|---|---|
| Raciocínio | nc_y_wisc | Campo de escore e norma da release exportada |
| Dimensões cognitivas | nc_y_nihtb | Escolher medidas independentes do desfecho |
| Administração | nc_y_nihtb_adm__rmt | Recodificação documentada e estratos de modalidade |
| Sono | ph_p_sds | Campo de exposição, janela e datas |
| Horários de sono | ph_y_mctq | Campo, onda e comparabilidade etária |

A bateria NIH Toolbox não é constante entre ondas. Aplicação remota muda a
disponibilidade de tarefas e compostos; Flanker remoto usa outra plataforma.
Não construir trajetória de índice global automaticamente. WISC Matrix Reasoning
mede um domínio, não uma identificação completa de HA. Examinar normas e
invariância antes de combinar escores.

Fonte: [neurocognição](https://docs.abcdstudy.org/latest/documentation/non_imaging/nc.html).

SDS é relato parental e tem datas ausentes em parte das primeiras ondas.
MCTQ inclui horários em dias escolares e livres. Isso ainda não demonstra
regularidade medida diariamente.
Fonte: [saúde física](https://docs.abcdstudy.org/latest/documentation/non_imaging/ph.html).

Estas são tabelas candidatas, não uma lista completa de campos pronta para
download. Faltam exportação do dicionário da release, campos de condição,
covariáveis, chaves exatas, códigos de ausência e eventos. Nenhum nome canônico
do template deve ser confundido com nome oficial de variável.

## Script entregue

scripts/audit_analytic_export.py recebe CSV harmonizado, com uma linha por
participante/evento. Ele rejeita chave duplicada/ausente, papéis sobrepostos e
valores não numéricos nos campos de medidas. Conta cobertura conjunta de
capacidade, exposição, desfecho e contexto, cobertura com condições e pares de
eventos com desfecho basal e posterior.

O relatório é local e não constitui aprovação A-01/A-02: não testa psicometria,
precisão de interação nem independência conceitual. Condições são auditadas por
presença de medida, não por prevalência. Eventos informados não comprovam datas.

O arquivo abcd-export.template.json é deliberadamente draft e o script recusa
executá-lo como configuração validada. Após revisar o dicionário, produzir
configuração local com nomes canônicos, códigos de ausência e status reviewed.

Exemplo de execução após harmonização e revisão:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python scripts/audit_analytic_export.py \
  --input data/restricted/abcd/analytic.csv \
  --config data/restricted/abcd/reviewed-config.json \
  --output data/restricted/abcd/coverage-local.json
```

A pasta data/restricted está ignorada pelo Git. O relatório é criado com
permissão 0600, sem sobrescrever arquivo anterior. stdout informa apenas conclusão;
erros não exibem valores nem traceback. Não abrir o relatório no contexto da IA
como consequência automática da execução; exportação/publicação requer revisão
conforme os termos.

## Próximo passo operacional

Confirmar acesso e release, obter o dicionário público/exportado e resolver os
campos pendentes. Com pacote autorizado, automatizar a harmonização e executar
a auditoria local. Testes sintéticos validam o software, não a base ABCD.
