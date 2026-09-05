import json
from pathlib import Path
import pytest
from runtime.conformance.runner import ConformanceRunner
from runtime.conformance.engine import aggregate_requirement, aggregate_conformance

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/conformance").glob("CONF-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_conformance_fixture(path):
    c=json.loads(path.read_text())
    report=ConformanceRunner().run(c["manifest"])
    assert report["final_result"]==c["expected"]

def test_blocked_never_satisfied():
    assert aggregate_requirement({"id":"REQ","test_results":["Blocked"]})=="Inconclusive"

def test_inconclusive_never_satisfied():
    assert aggregate_requirement({"id":"REQ","test_results":["Inconclusive"]})=="Inconclusive"

def test_fail_dominates_pass():
    assert aggregate_requirement({"id":"REQ","test_results":["Pass","Fail"]})=="Violated"

def test_not_applicable_requires_rationale():
    r={"id":"REQ","applicability":"NotApplicable"}
    assert aggregate_requirement(r)=="Inconclusive"

def test_scope_required_cannot_be_not_applicable():
    r={
        "id":"REQ","applicability":"NotApplicable",
        "applicability_rationale":"claimed out",
        "required_by_claimed_scope":True
    }
    assert aggregate_requirement(r)=="Inconclusive"

def test_missing_subject_binding_is_inconclusive():
    claim={
        "subject_version":"1","profile":"AOF-Core","scope":{"components":["runtime"]},
        "requirements":[]
    }
    assert aggregate_conformance(claim)=="Inconclusive"
