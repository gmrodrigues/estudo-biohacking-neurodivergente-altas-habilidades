"""Profile ClinicalTrials.gov records used to seed the evidence graph."""

import json
from collections import Counter
from pathlib import Path


DATA_DIR = Path("data/public/clinicaltrials")


def main() -> None:
    for path in sorted(DATA_DIR.glob("*.json")):
        payload = json.loads(path.read_text())
        studies = payload.get("studies", [])
        statuses: Counter[str] = Counter()
        phases: Counter[str] = Counter()
        interventions: Counter[str] = Counter()
        with_results = 0

        for study in studies:
            protocol = study.get("protocolSection", {})
            statuses[protocol.get("statusModule", {}).get("overallStatus", "UNKNOWN")] += 1
            phases.update(protocol.get("designModule", {}).get("phases") or ["NA"])
            for intervention in protocol.get("armsInterventionsModule", {}).get("interventions", []):
                interventions[intervention.get("name", "UNKNOWN").strip()] += 1
            with_results += int("resultsSection" in study)

        print(f"{path.name}: studies={len(studies)}, with_results={with_results}")
        print(f"statuses={dict(statuses.most_common())}")
        print(f"phases={dict(phases.most_common())}")
        print(f"top_interventions={interventions.most_common(15)}")


if __name__ == "__main__":
    main()

