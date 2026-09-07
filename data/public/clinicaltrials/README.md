# ClinicalTrials.gov — consultas iniciais

Registros públicos obtidos pela API v2 em 2026-09-07. São evidências adjacentes
sobre neurodivergência; não são estudos específicos de altas habilidades.

| Arquivo | Consulta | Estudos | Com resultados | SHA-256 |
|---|---|---:|---:|---|
| `adhd_dietary_supplement.json` | condição TDAH; intervenção “Dietary Supplement” | 83 | 11 | `911af4a1623a03bdf0ba0ca879150e8f6bab119feac00b1ca6acbea6d1856103` |
| `autism_dietary_supplement.json` | condição TEA; intervenção “Dietary Supplement” | 87 | 17 | `98a0c2ba151cd15ee8d604d52985fd26a98d67d957234aca6a13daac439e638c` |

Execução:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python catalog/data-sources/analyze_clinical_trials.py
```

As consultas retornam registros ruidosos: podem conter medicamentos, dieta,
exercício e nomes diferentes para a mesma substância. Antes do grafo, é necessário
normalizar nomes, verificar o tipo de intervenção e distinguir protocolo de
resultado efetivamente publicado.

