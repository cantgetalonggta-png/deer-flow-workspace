"""Ontology schema smoke tests."""
import json
from pathlib import Path
ONT = Path(__file__).resolve().parents[1] / "ontology" / "ontology.json"

def test_ontology_classes():
    o = json.loads(ONT.read_text())
    ids = {c["id"] for c in o["classes"]}
    for required in ["Skill", "Tool", "Plugin", "Service", "Agent"]:
        assert required in ids

def test_relations_present():
    o = json.loads(ONT.read_text())
    assert len(o["relations"]) >= 3
