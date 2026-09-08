# Auditoria de dados — ciclo 001

## Escopo

O ciclo usa adultos da coorte NHANES 2021–2023 com ligação individual por `SEQN` entre DEMO, SLQ, PAQ, DPQ, DR1TOT e DSQTOT. A análise não identifica superdotação, autismo ou TDAH: esses grupos ficam como **não avaliados** neste ciclo.

## Cobertura e filtros

- 6.337 participantes após a junção das seis tabelas.
- H1: 4.211 observações completas.
- H2: 4.522 observações completas.
- H3: 4.194 observações completas.
- Modelo preditivo: 4.522 observações completas; idade observada de 20 a 80 anos.
- Filtros: idade ≥18, sexo, raça/etnia, escolaridade, PIR e pesos válidos; desfechos e covariáveis também precisam estar observados.

## Mensuração

`SLD012` é horas usuais de sono em dias úteis; `PAD680` é minutos de atividade sedentária no dia de referência; `DR1TCAFF` e `DR1TMAGN` vêm do recordatório alimentar de 24 horas; `DSQTMAGN` é magnésio de suplementos informado na janela do questionário. O alvo depressivo é PHQ-8: os itens do PHQ-9 são somados excluindo `DPQ030` (sono), para não reciclar o desfecho de sono como preditor.

## Desenho amostral

Os modelos usam pesos da entrevista/exame conforme o estimando e variância linearizada por estratos (`SDMVSTRA`) e unidades primárias (`SDMVPSU`). Cada ajuste tem 15 graus de liberdade de desenho (15 estratos e 30 PSUs). Isso melhora a incerteza para a amostra complexa, mas não transforma o estudo transversal em experimento.

## Riscos restantes

Não há validação de diagnóstico clínico, longitudinalidade, medida de altas habilidades, dose confiável para todos os suplementos, nem controle completo de medicação, cronotipo, comorbidades ou causalidade reversa. Resultados são associações exploratórias agregadas, não recomendações clínicas.
