# Auditoria de dados — ciclo 001

## Escopo

O ciclo usa adultos da coorte NHANES 2021–2023 com ligação individual por `SEQN` entre DEMO, SLQ, PAQ, DPQ, DR1TOT e DSQTOT. A análise não identifica superdotação, autismo ou TDAH: esses grupos ficam como **não avaliados** neste ciclo.

## Cobertura e filtros

- 6.337 adultos após cada junção específica por hipótese; não foi exigida interseção dos seis módulos em todos os modelos.
- H1: 4.211 observações completas.
- H2: 4.522 observações completas.
- H3: 4.194 observações completas.
- Modelo preditivo: 4.522 observações completas; idade observada de 20 a 80 anos.
- Filtros: idade ≥18, sexo, raça/etnia, escolaridade, PIR e pesos válidos; desfechos e covariáveis também precisam estar observados.

## Mensuração

`SLD012` é horas usuais de sono em dias úteis; `PAD680` é minutos de atividade sedentária no dia de referência; `DR1TCAFF` e `DR1TMAGN` vêm do recordatório alimentar de 24 horas; `DSQTMAGN` é magnésio de suplementos informado na janela do questionário. O alvo é o escore de sintomas sem sono (0–24): os itens do PHQ-9 são somados excluindo `DPQ030` (sono), para não reciclar o desfecho de sono como preditor.

### Auditoria posterior de DSQTMAGN

O [ciclo 003](../cycle-003/data-audit.md) ligou DSQIDS_L a DSPI/DSII e mostrou
que `SUPP_MAG_UNQUANT` é um nome interno legado: ele marca qualquer suplemento
relatado com total de magnésio ausente e não comprova magnésio de dose
desconhecida. Somente 6 dos 1.401 participantes marcados tinham produto rotulado
com magnésio e total ausente. Os coeficientes históricos foram preservados, com
nome e interpretação públicos corrigidos.

## Desenho amostral

Os modelos usam pesos da entrevista/exame conforme o estimando e variância linearizada por estratos (`SDMVSTRA`) e unidades primárias (`SDMVPSU`). Cada ajuste tem 15 graus de liberdade de desenho (15 estratos e 30 PSUs). Isso melhora a incerteza para a amostra complexa, mas não transforma o estudo transversal em experimento.

## Riscos restantes

Não há validação de diagnóstico clínico, longitudinalidade, medida de altas habilidades, dose confiável para todos os suplementos, nem controle completo de medicação, cronotipo, comorbidades ou causalidade reversa. Resultados são associações exploratórias agregadas, não recomendações clínicas.

## Adendo de 2026-09-09

Sono curto <7 h (n=943), referência 7–9 h inclusive (n=3.108), longo >9 h (n=471). Exatamente 686 pessoas com 7 h mudaram do grupo curto para a referência; n=4.522 preservado. A soma derivada de oito itens não é o PHQ-8 convencional e não herda cortes clínicos. [Auditoria comparativa e hashes](amendments/h2-boundary-2026-09-09/audit.md). A revisão da variância com implementação externa permanece pendente.

## Auditoria posterior do ciclo 002

Auditoria posterior (ciclo 002): coeficientes e erros-padrão foram reproduzidos com svy no desenho completo. Os p/q e IC deste ciclo usam 15 graus de liberdade; com o padrão residual de svy (piso de 1), nenhum dos oito testes tem q<0,05. A concordância da variância não resolve essa sensibilidade ou a seleção por casos completos.

[Relatório completo](../cycle-002/data-audit.md).
