# Prioridade imediata: fase HA, TDAH e autismo

Data: 2026-09-10. Esta é a frente principal do estudo a partir deste registro.
Os ciclos restantes sobre NHANES são manutenção metodológica: podem continuar
quando não atrasarem a entrada desta fase, mas não são pré-requisito para ela.

## Decisão de escopo

O NHANES atual permanece útil somente como referência adulta para sono, dieta,
suplementos, sintomas e método. Ele não pode gerar conclusões sobre HA, TDAH,
autismo, dupla excepcionalidade ou referência neurotípica porque não os mede.

A próxima rodada prioritária é uma **auditoria de fonte para neurodesenvolvimento
e capacidade**, ainda sem estimar efeitos. Seu produto é uma decisão documentada:
`estimable`, `estimable_with_limits` ou `needs_data` para cada contraste
HA×TDAH×autismo.

## Entrada imediata: bases abertas; ABCD em paralelo

Project Talent (HA/capacidade), ABIDE II (autismo), ADHD-200 (TDAH) e NSCH
(TDAH/autismo em referência populacional) permitem começar agora por arquivos
públicos e desidentificados. A Healthy Brain Network é o primeiro candidato a
reunir, no mesmo recurso, TDAH, autismo, cognição, sono e atividade, após
conferência de seus termos e da versão de dados. A [auditoria de bases
abertas](OPEN_NEURODEVELOPMENT_DATA_AUDIT.md) registra essas fontes, estudos que
as reutilizaram e seus limites.

O ABCD/NDA segue em paralelo como candidato longitudinal: seu catálogo público
lista domínios de TDAH, autismo, cognição, função executiva e sono, e a liberação
5.1 é a referência atual indicada pelo próprio NDA. Dados individuais e notas de
liberação para usuários qualificados exigem acesso legítimo ao NDA.

Ele não deve ser chamado de base de HA por padrão: capacidade/HA precisa de uma
definição operacional prévia a partir de medidas cognitivas documentadas, com
normas adequadas à idade. Se a cobertura não permitir essa definição, o resultado
correto é `needs_data` para HA, mesmo que TDAH/autismo sejam mensuráveis.

## Roteiro de execução

| Ordem | Entrega verificável | Critério de passagem | Resultado se falhar |
|---|---|---|---|
| 1 | Inventário aberto Project Talent, ABIDE II, ADHD-200 e NSCH: versão, licença, arquivos e hashes | Arquivos públicos baixados sem dados identificáveis | Registrar falha de acesso; não contornar credenciais |
| 2 | Auditoria campo→construto por base | Cognição, medidas TDAH/autismo, chaves, centro e ausências documentados | Marcar cada construto indisponível ou aproximação explícita |
| 3 | Dossiê HBN e acesso ABCD: termos, versão, responsável e variáveis | Termos aceitos legitimamente ou metadados suficientes para inventário | `blocked_by_access`; manter bases abertas separadas |
| 4 | Definições e fluxo de elegibilidade | Critério de HA/capacidade, TDAH, autismo e referência, com informante, idade e tamanho das células | Não formar grupos por um único escore, profissão ou ausência de diagnóstico |
| 5 | Protocolo do primeiro ciclo comparativo | Estimandos, covariáveis, interações, temporalidade e multiplicidade antes dos efeitos | Não estimar até o protocolo existir |

## Primeiro conjunto mínimo de perguntas

1. Como perfis contínuos de capacidade cognitiva, atenção/função executiva e
   funcionamento se distribuem entre medidas independentes de TDAH/autismo?
2. Há diferenças ou interações pré-especificadas entre capacidade e condição para
   sono e funcionamento, sem atribuir causalidade a hábitos?
3. Em ondas posteriores, mudanças de sono e funcionamento antecedem umas às
   outras de modo compatível com o modelo registrado?

Essas perguntas priorizam descrição e trajetória. Uma hipótese de suplemento ou
rotina só entra depois que exposição, medicação, tempo e segurança estiverem
medidos para a coorte escolhida.

## Atualizações obrigatórias desta frente

Ao concluir cada passo, atualizar este arquivo, `sources.yaml`,
`ACCESS_FROM_CODEX.md`, `STATUS_AND_STALENESS_MAP.md`, `NEXT_SESSION.md`,
`research/site/study.json` e o README. O primeiro ciclo com dados autorizados
também exigirá protocolo, auditoria, manifesto, código reproduzível e publicação
agregada.

## Fontes oficiais consultadas em 2026-09-10

- [NIMH Data Archive: ABCD e liberação 5.1](https://nda.nih.gov/general-query.html?q=query%3Dfeatured-datasets%3AAdolescent+Brain+Cognitive+Development+Study+%28ABCD%29)
- [NDA Data Dictionary](https://nda.nih.gov/data_dictionary.html?source=ABCD&submission=ALL)
- [Instruções de solicitação de acesso](https://nda.nih.gov/ndarpublicweb/Documents/Data_Access_Documents_Completion_Instructions.pdf)
