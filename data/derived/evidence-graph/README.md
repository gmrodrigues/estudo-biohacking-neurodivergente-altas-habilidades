# Grafo inicial de evidências

Artefato derivado dos registros em `data/public/clinicaltrials`. Ele contém:

- `nodes.csv`: estudos, intervenções normalizadas e condições;
- `edges.csv`: relações `STUDIES_CONDITION` e `TESTS`;
- nome original da intervenção em cada aresta para auditoria.

Reconstrução:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv run python catalog/data-sources/build_trial_evidence_graph.py
```

A classificação é intencionalmente conservadora. `unclassified` significa que a
intervenção ainda precisa de revisão; não significa que ela não seja suplemento.
O grafo representa registros de ensaios, não comprovação de eficácia.

