"""Build a conservative tabular evidence graph from ClinicalTrials.gov records."""

import csv
import json
import re
import unicodedata
from pathlib import Path


INPUT_DIR = Path("data/public/clinicaltrials")
OUTPUT_DIR = Path("data/derived/evidence-graph")


def normalized_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def canonical_intervention(name: str, declared_type: str) -> tuple[str, str]:
    text = normalized_text(name)
    rules = (
        (("placebo", "control", "canola oil"), "placebo/control", "placebo"),
        (("omega 3", "epa dha", "eicosapentaenoic", "docosahexaenoic", "lcpufa"), "omega-3/EPA-DHA", "supplement"),
        (("phosphatidylserine",), "phosphatidylserine", "supplement"),
        (("probiotic", "synbiotic", "postbiotic", "lactococcus", "inulin"), "microbiome intervention", "supplement"),
        (("melatonin",), "melatonin", "supplement"),
        (("sulforaphane",), "sulforaphane", "supplement"),
        (("n acetyl cysteine", "nac"), "N-acetylcysteine", "supplement"),
        (("methylphenidate",), "methylphenidate", "drug"),
        (("diet", "carbohydrate", "nutrition"), "dietary intervention", "diet"),
        (("training", "exercise", "physical activity"), "exercise intervention", "exercise"),
    )
    for terms, canonical, kind in rules:
        if any(term in text for term in terms):
            return canonical, kind
    type_map = {
        "DIETARY_SUPPLEMENT": "supplement",
        "DRUG": "drug",
        "BEHAVIORAL": "behavioral",
        "DEVICE": "device",
        "PROCEDURE": "procedure",
        "DIAGNOSTIC_TEST": "diagnostic",
        "BIOLOGICAL": "biological",
        "COMBINATION_PRODUCT": "combination_product",
        "OTHER": "other",
    }
    return name.strip(), type_map.get(declared_type, "unclassified")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    studies: dict[str, dict] = {}
    interventions: dict[str, dict] = {}
    edges: set[tuple[str, str, str, str]] = set()

    for path in sorted(INPUT_DIR.glob("*.json")):
        condition_query = "ADHD" if path.name.startswith("adhd") else "autism"
        payload = json.loads(path.read_text())
        for record in payload.get("studies", []):
            protocol = record.get("protocolSection", {})
            identity = protocol.get("identificationModule", {})
            status = protocol.get("statusModule", {})
            design = protocol.get("designModule", {})
            nct_id = identity.get("nctId")
            if not nct_id:
                continue
            studies[nct_id] = {
                "id": nct_id,
                "title": identity.get("briefTitle", ""),
                "status": status.get("overallStatus", ""),
                "study_type": design.get("studyType", ""),
                "phases": "|".join(design.get("phases") or []),
                "has_results": str("resultsSection" in record).lower(),
                "source": "ClinicalTrials.gov",
            }
            edges.add((nct_id, "STUDIES_CONDITION", f"condition:{condition_query}", path.name))

            module = protocol.get("armsInterventionsModule", {})
            for intervention in module.get("interventions", []):
                original = intervention.get("name", "").strip()
                if not original:
                    continue
                canonical, kind = canonical_intervention(original, intervention.get("type", ""))
                intervention_id = "intervention:" + normalized_text(canonical).replace(" ", "-")
                interventions.setdefault(
                    intervention_id,
                    {"id": intervention_id, "canonical_name": canonical, "kind": kind},
                )
                edges.add((nct_id, "TESTS", intervention_id, original))

    node_rows = list(studies.values()) + [
        {
            "id": row["id"],
            "title": row["canonical_name"],
            "status": "",
            "study_type": row["kind"],
            "phases": "",
            "has_results": "",
            "source": "normalized intervention",
        }
        for row in interventions.values()
    ] + [
        {"id": "condition:ADHD", "title": "ADHD", "status": "", "study_type": "condition", "phases": "", "has_results": "", "source": "query"},
        {"id": "condition:autism", "title": "Autism Spectrum Disorder", "status": "", "study_type": "condition", "phases": "", "has_results": "", "source": "query"},
    ]
    edge_rows = [
        {"source": source, "relation": relation, "target": target, "original_label": label}
        for source, relation, target, label in sorted(edges)
    ]
    write_csv(
        OUTPUT_DIR / "nodes.csv",
        ["id", "title", "status", "study_type", "phases", "has_results", "source"],
        node_rows,
    )
    write_csv(
        OUTPUT_DIR / "edges.csv",
        ["source", "relation", "target", "original_label"],
        edge_rows,
    )

    kinds: dict[str, int] = {}
    for intervention in interventions.values():
        kinds[intervention["kind"]] = kinds.get(intervention["kind"], 0) + 1
    print(f"study_nodes={len(studies)}")
    print(f"intervention_nodes={len(interventions)}")
    print(f"edges={len(edges)}")
    print(f"intervention_kinds={kinds}")


if __name__ == "__main__":
    main()
