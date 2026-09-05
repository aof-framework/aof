import json
from pathlib import Path
import pytest
from engine.conformance_engine import aggregate_conformance, aggregate_requirement, validate_not_applicable

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/conformance").glob("ECT-CONF-[0-9][0-9][0-9].json"))
NAFILES=sorted((ROOT/"fixtures/conformance").glob("ECT-CONF-NA-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_conformance_aggregation(path):
    c=json.loads(path.read_text())
    result=aggregate_conformance(c["facts"])
    assert result.final_result==c["expected"], result.to_dict()

@pytest.mark.parametrize("path",NAFILES,ids=lambda p:p.stem)
def test_not_applicable_guard(path):
    c=json.loads(path.read_text())
    assert validate_not_applicable(c["requirement"]) is c["expected"]

def test_fail_dominates_pass_for_same_requirement():
    req={"requirement_id":"AOF-X-010","normative_level":"MUST","applicability":"Applicable",
         "tests":[{"test_id":"T1","result":"Pass"},{"test_id":"T2","result":"Fail"}],"evidence_refs":["ev"]}
    assert aggregate_requirement(req).result=="Violated"

def test_blocked_never_becomes_satisfied():
    req={"requirement_id":"AOF-X-011","normative_level":"MUST","applicability":"Applicable",
         "tests":[{"test_id":"T1","result":"Blocked"}],"evidence_refs":[]}
    assert aggregate_requirement(req).result=="Inconclusive"

def test_inconclusive_never_becomes_satisfied():
    req={"requirement_id":"AOF-X-012","normative_level":"MUST","applicability":"Applicable",
         "tests":[{"test_id":"T1","result":"Inconclusive"}],"evidence_refs":[]}
    assert aggregate_requirement(req).result=="Inconclusive"

def test_na_requires_rationale():
    req={"requirement_id":"AOF-X-013","applicability":"NotApplicable","applicability_rationale":"","required_by_claimed_scope":False}
    assert validate_not_applicable(req) is False

def test_scope_required_claim_cannot_be_na():
    req={"requirement_id":"AOF-X-014","applicability":"NotApplicable","applicability_rationale":"claimed exclusion","required_by_claimed_scope":True}
    assert validate_not_applicable(req) is False
