# Convenções compartilhadas do estudo

Estas instruções aplicam-se ao projeto `science`, identificado por `Pipfile` e
`catalog/data-sources`. Resolva caminhos a partir da raiz do checkout, inclusive
quando as skills estiverem instaladas por links. Mantenha o pacote de seis skills
junto para preservar suas referências. Não altere outro projeto por ter uma
skill instalada no perfil do usuário.

## Execução e proveniência

- Execute Python, ferramentas Python e validadores com
  `PIPENV_VENV_IN_PROJECT=1 pipenv run ...`. Gerencie dependências pelo Pipenv,
  preservando `Pipfile.lock`; instalação reprodutível: `pipenv sync --dev`.
- Reutilize os scripts de `catalog/data-sources`, verificando suas premissas.
  Perfis descritivos existentes não equivalem a pipelines inferenciais validados.
- Preserve `data/public` como insumo bruto; grave derivados em `data/derived` e
  relatórios em `research/discoveries/<run-id>`. Registre consultas, versão, data,
  hash, critérios de amostra, comando e semente quando aplicável.
- A skill não autoriza publicação de novos dados pessoais, pedidos de acesso,
  recrutamento, intervenção, commit ou push. Siga o escopo autorizado na conversa.

## Construtos, pessoas e comparações

Ao discutir a tese do projeto, leia
[`FOUNDATIONAL_HYPOTHESIS.md`](../../../catalog/data-sources/FOUNDATIONAL_HYPOTHESIS.md).
Distinga a proposta universal (toda neurodivergência seria HA encoberta) de
hipóteses sobre alguns subgrupos e efeitos do contexto. Não a trate como fato nem
reinterprete o ciclo 001 como seu teste. Mantenha critérios independentes de HA,
alternativas e resultados que poderiam contrariar a tese. Melhora funcional não
prova etiologia; dificuldades de rotina podem ser consequência de sintomas ou
barreiras. Não atribua culpa ou condicione necessidades de suporte à presença de HA.

O foco é HA com validação em ASD, ADHD, referência operacional NT e combinações
isoladas, duplas e triplas. Leia `CORE_STUDY_DESIGN.md` quando houver comparação
de grupos. `unknown`, `not_assessed`, `not_applicable` e ausência confirmada são
estados diferentes. Capacidade cognitiva elevada, escolaridade e identificação de
HA não são intercambiáveis. Dados sem avaliações não definem NT.

O núcleo de previsão funciona sem diagnóstico. Diagnósticos podem entrar em
comparações inferenciais separadas e auditorias de desempenho, com procedência
clínica/psicométrica explícita. Um agrupamento descoberto não recebe um diagnóstico
retroativamente. Uma única queixa de concentração não identifica TDAH.

Leia `STRATIFICATION_MODEL.md` para idade, sexo/gênero, profissão, educação,
criatividade/arte, família, finanças e substâncias. Preserve idade contínua e
normas próprias por fase de vida. Campos não coletados permanecem ausentes;
suporte financeiro não é falha pessoal e uso de substâncias não é proxy moral
ou diagnóstico. Sexo registrado não fornece identidade de gênero.

## Regras de interpretação

Mantenha distintas associação transversal, mensuração latente, previsão em
novas pessoas, previsão futura e efeito de intervenção. Ajuste estatístico não
estabelece sozinho causalidade. Um modelo pode prever bem sem revelar mecanismo.
Ingestão de vitaminas não mede diretamente metilação; atividade autorreferida
não mede desempenho em calistenia ou artes marciais.

Dados sintéticos são adequados para potência, validação de código e cenários
explicitamente hipotéticos. Não ampliam N empírico nem confirmam relações.
Proteja o teste reservado de toda escolha de variável, transformação e hipótese.

## Atenção ao NHANES deste projeto

A interseção de tabelas descrita anteriormente é um inventário, não uma amostra
obrigatória para toda pergunta. Construa cada coorte com os componentes necessários.
Consulte novamente os codebooks do ciclo para recodificação e ponderação. Pesos
alimentares e de flebotomia têm propósitos diferentes; sua combinação requer a
orientação específica dos componentes. O CDC introduziu pesos de flebotomia no
ciclo 2021–2023. Preserve estratos/PSU e não trate pesos de regressão comuns como
correção completa do desenho. Fonte: [CDC, ponderação NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx).

O arquivo público `DPQ_L` contém adultos; suas respostas medem sintomas nas duas
semanas anteriores. O item `DPQ030` trata de sono. Ao relacionar sono e PHQ-9,
avalie sobreposição de conteúdo. Um escore derivado sem um item deve receber nome
próprio e não herda cortes clínicos do PHQ-9. Fonte: [codebook DPQ_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.htm).

`DSQTOT_L` resume nutrientes de suplementos e antiácidos em 30 dias. Para produtos
específicos, consulte `DSQIDS_L` e a base de produtos quando disponíveis. Não
deduza forma química, marca ou ingrediente botânico apenas dos totais. Fonte:
[codebook DSQTOT_L](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.htm).

Essas fontes foram consultadas em 2026-09-07; os valores e acessos devem ser
verificados no momento de uma análise futura.
