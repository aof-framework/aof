import json
from pathlib import Path
import pytest
from runtime.safety_kernel.kernel import SafetyKernel

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/safety_kernel").glob("SK-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_fixture(path):
    case=json.loads(path.read_text())
    d=SafetyKernel().evaluate(case["facts"])
    assert d.status==case["expected_decision"]

def test_allow_only_when_all_gates_pass():
    facts={
        "capability_present":True,
        "authority_granted":True,
        "scope_match":True,
        "policy_permits":True,
        "state_valid":True,
        "state_transition_authorized":True,
        "risk_permits":True,
        "risk_acceptance_required":False,
        "verification_required":True,
        "verification_status":"Verified"
    }
    d=SafetyKernel().evaluate(facts)
    assert d.status=="Allow"
    assert d.execute_allowed is True
    assert all(g.status=="Pass" for g in d.gate_results.values())

def test_pending_is_not_allow():
    facts={
        "capability_present":True,
        "authority_granted":True,
        "scope_match":True,
        "policy_permits":True,
        "state_valid":True,
        "state_transition_authorized":True,
        "risk_permits":True,
        "risk_acceptance_required":False,
        "verification_required":True,
        "verification_status":"Pending"
    }
    d=SafetyKernel().evaluate(facts)
    assert d.status=="Pending"
    assert d.execute_allowed is False

def test_fail_dominates_pending():
    facts={
        "capability_present":True,
        "authority_granted":False,
        "policy_determined":False,
        "state_valid":True,
        "risk_permits":True,
        "verification_required":True,
        "verification_status":"Verified"
    }
    d=SafetyKernel().evaluate(facts)
    assert d.status=="Deny"
    assert d.execute_allowed is False

def test_capability_does_not_create_authority():
    facts={
        "capability_present":True,
        "authority_granted":False,
        "policy_permits":True,
        "state_valid":True,
        "risk_permits":True,
        "verification_required":False,
    }
    assert SafetyKernel().evaluate(facts).status=="Deny"

def test_approval_like_signal_not_used_for_authority():
    facts={
        "capability_present":True,
        "approval_present":True,
        "authority_granted":False,
        "policy_permits":True,
        "state_valid":True,
        "risk_permits":True,
        "verification_required":False,
    }
    assert SafetyKernel().evaluate(facts).status=="Deny"

def test_unknown_mandatory_policy_not_implicit_allow():
    facts={
        "capability_present":True,
        "authority_granted":True,
        "mandatory_policy_unknown":True,
        "state_valid":True,
        "risk_permits":True,
        "verification_required":False,
    }
    assert SafetyKernel().evaluate(facts).status=="Pending"

def test_verification_inconclusive_not_pass():
    facts={
        "capability_present":True,
        "authority_granted":True,
        "policy_permits":True,
        "state_valid":True,
        "risk_permits":True,
        "verification_required":True,
        "verification_status":"Inconclusive",
    }
    assert SafetyKernel().evaluate(facts).status=="Pending"
