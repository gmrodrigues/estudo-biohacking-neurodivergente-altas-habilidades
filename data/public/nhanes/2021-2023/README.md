# NHANES August 2021–August 2023

Arquivos públicos usados na análise inicial. Eles são derivados do ciclo que o
CDC denomina NHANES August 2021–August 2023.

| Arquivo | Conteúdo | URL oficial | SHA-256 |
|---|---|---|---|
| `DEMO_L.xpt` | Demografia e desenho amostral | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt | `ca4374a158b493b8b0163e1388da21d57a18d1b9cecff2aa4e2fa2bec494fe23` |
| `DSQTOT_L.xpt` | Totais diários provenientes de suplementos | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQTOT_L.xpt | `8ee3e55578f56918a190100bb321a0b580f824ca3cc439901f2fd707dbe695f8` |
| `PAQ_L.xpt` | Questionário de atividade física | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/PAQ_L.xpt | `de34acfed4523f10f52bea06e64ed33c8db973cb38d3539eeceb2b68039248c8` |
| `SLQ_L.xpt` | Questionário de sono | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/SLQ_L.xpt | `918c3258b2f466ac1cae55ea45330c736dbdc573ee4dc72306e3d2b222764741` |
| `DR1TOT_L.xpt` | Nutrientes provenientes de alimentos no primeiro dia | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR1TOT_L.xpt | `73a3097aab64000f9c1d138367363ca605968b691e349981132bd6032ca6c9ef` |
| `BMX_L.xpt` | Medidas corporais | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.xpt | `44440c416d9ad709e8b1708a5975378ab4d5b18edc39eb5015c2ae7186500170` |
| `DPQ_L.xpt` | PHQ-9 e impacto funcional | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.xpt | `25605a02685035fe997477b31a0991cca2776b0f72f24a8e61ac5b018456304b` |
| `VID_L.xpt` | Vitamina D sérica | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/VID_L.xpt | `5901de08d633fa31f2199af53e49f434e89a2bf2cc26539b84d1787f85166fa7` |
| `BPXO_L.xpt` | Pressão e pulso oscilométricos | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BPXO_L.xpt | `189aa9bed689d2c69cf8d780b01de85073276fea5694dd52cdf696229f9054a6` |
| `DSQIDS_L.xpt` | Ocorrências de suplementos e antiácidos por participante | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DSQIDS_L.xpt | `807aedb121f96c5326dffd64d7930a7fce370b4c0545160fe70d08257e4a196d` |
| `DSPI.xpt` | Catálogo público de produtos NHANES-DSD 1999–2023 | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSPI.xpt | `2b8854be8d0f1d959677b8689ea992c1b594e36c68d4a54a2767c4b19473d914` |
| `DSII.xpt` | Ingredientes dos produtos NHANES-DSD 1999–2023 | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSII.xpt | `ef28499e937207533600bb082b05d50a1f0ce9abc1dd9a6ac71af886337aeaff` |
| `DSBI.xpt` | Ingredientes de misturas NHANES-DSD 1999–2023 | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSBI.xpt | `007f3eee960ae65e758fa21b9b3ca57c08edfbc871e1b3bd67e48c7815527720` |

Execute o perfilamento a partir da raiz do projeto:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python catalog/data-sources/analyze_nhanes.py
```

Os pesos, estratos e unidades primárias de amostragem devem ser usados em qualquer
inferência populacional. O script atual descreve disponibilidade e interseção; ele
não produz estimativas populacionais.
