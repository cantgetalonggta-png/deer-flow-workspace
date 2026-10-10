"""Unit tests for skill-engine state integrity — Cycle 2."""
import json
from pathlib import Path

STATE = Path(__file__).resolve().parents[1] / "skill-engine" / "state.json"

def test_state_exists():
    assert STATE.exists(), f"missing {STATE}"

def test_state_has_atoms():
    data = json.loads(STATE.read_text())
    assert "atoms" in data
    assert len(data["atoms"]) >= 20
    assert data["engine"]["cycle"] >= 1

def test_master_tree_root():
    data = json.loads(STATE.read_text())
    tree = data["masterSkillsTree"]
    assert tree["id"] == "root"
    assert len(tree.get("children") or []) >= 1

def test_insights_nonempty():
    data = json.loads(STATE.read_text())
    assert len(data.get("insights") or []) >= 1

def test_counts_manifest():
    counts = Path(__file__).resolve().parents[1] / "manifests" / "counts.json"
    c = json.loads(counts.read_text())
    assert c["prod_skills"] >= 20
    assert c["catalog"] >= 1000
