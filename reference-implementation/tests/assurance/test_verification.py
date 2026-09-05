import json
from pathlib import Path
import pytest
from runtime.assurance.verification import VerificationEngine

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/assurance").glob("ASR-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_assurance_fixture(path):
    c=json.loads(path.read_text())
    r=VerificationEngine().verify(
        subject_ref=c["subject_ref"],
        subject_version=c["subject_version"],
        criteria_ref=c["criteria_ref"],
        evidence_items=c["evidence"],
        verifier_ref=c["verifier_ref"],
        subject_actor_ref=c["subject_actor_ref"],
        independence_required=c["independence_required"]
    )
    assert r.status==c["expected"]

def test_execution_success_is_not_verification():
    r=VerificationEngine().verify(
        subject_ref="subject:1",
        subject_version="1",
        criteria_ref="criteria:1",
        evidence_items=[],
        verifier_ref="verifier:1",
        subject_actor_ref="agent:1",
        independence_required=False
    )
    assert r.status=="Inconclusive"

def test_verification_bound_to_version():
    ev=[{"id":"ev:1","subject_ref":"subject:1","subject_version":"1","provenance":{"source":"trace:1"},"supports_criteria":True}]
    r=VerificationEngine().verify(
        subject_ref="subject:1",
        subject_version="2",
        criteria_ref="criteria:1",
        evidence_items=ev,
        verifier_ref="verifier:1",
        subject_actor_ref="agent:1",
        independence_required=False
    )
    assert r.status=="Inconclusive"

def test_missing_criteria_is_inconclusive():
    ev=[{"id":"ev:1","subject_ref":"subject:1","subject_version":"1","provenance":{"source":"trace:1"},"supports_criteria":True}]
    r=VerificationEngine().verify(
        subject_ref="subject:1",
        subject_version="1",
        criteria_ref="",
        evidence_items=ev,
        verifier_ref="verifier:1"
    )
    assert r.status=="Inconclusive"

def test_verification_does_not_create_authority():
    ev=[{"id":"ev:1","subject_ref":"subject:1","subject_version":"1","provenance":{"source":"trace:1"},"supports_criteria":True}]
    r=VerificationEngine().verify(
        subject_ref="subject:1",
        subject_version="1",
        criteria_ref="criteria:1",
        evidence_items=ev,
        verifier_ref="verifier:1"
    )
    assert r.status=="Verified"
    assert not hasattr(r,"authority_granted")
