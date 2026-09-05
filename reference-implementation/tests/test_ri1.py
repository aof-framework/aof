import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def test_adapter_contract_transport_neutral():
    c=json.loads((ROOT/"contracts/adapter-contract.json").read_text())
    assert c["transport_neutral"] is True

def test_required_operations_complete():
    c=json.loads((ROOT/"contracts/adapter-contract.json").read_text())
    expected={"load_context","invoke_reasoning","resolve_governance_inputs","observe_state","execute_effect","collect_evidence","cleanup_or_reconcile"}
    assert expected.issubset(set(c["required_operations"]))

def test_no_authority_minting():
    c=json.loads((ROOT/"contracts/adapter-contract.json").read_text())
    assert "adapter_must_not_mint_authority" in c["hard_prohibitions"]

def test_no_deny_suppression():
    c=json.loads((ROOT/"contracts/adapter-contract.json").read_text())
    assert "adapter_must_not_suppress_deny" in c["hard_prohibitions"]

def test_native_and_brownfield_modes_supported():
    a=json.loads((ROOT/"architecture/runtime-architecture.json").read_text())
    assert "AOFNative" in a["implementation_modes"]
    assert "AdapterBasedBrownfield" in a["implementation_modes"]

def test_pending_not_allow():
    r=json.loads((ROOT/"contracts/runtime-result-contract.json").read_text())
    assert "Pending != Allow" in r["rules"]

def test_untrusted_proposal():
    from adapters.reference_adapter import ReferenceAdapter
    obs=ReferenceAdapter().invoke_reasoning("agent:1","task:1",{})
    assert obs.payload["proposal"]["status"]=="UntrustedProposal"

def test_ri1_has_no_consequential_effect_execution():
    from adapters.reference_adapter import ReferenceAdapter
    try:
        ReferenceAdapter().execute_effect({}, {})
    except NotImplementedError:
        return
    raise AssertionError("RI-1 must not execute effects.")

def test_no_openapi_dependency():
    names=[p.name.lower() for p in ROOT.rglob("*") if p.is_file()]
    assert not any("openapi" in n for n in names)

def test_valid_at_check_boundary_documented():
    t=(ROOT/"architecture/RI1-RUNTIME-ARCHITECTURE.md").read_text()
    assert "ValidAtCheck != ValidAtEffect" in t

def test_claim_evidence_verification_boundary_documented():
    t=(ROOT/"architecture/RI1-RUNTIME-ARCHITECTURE.md").read_text()
    assert "Claim != Evidence != Verification" in t

def test_brownfield_output_is_untrusted():
    from adapters.brownfield_adapter import BrownfieldAdapter
    class Legacy:
        def reason(self, task_ref, context_snapshot):
            return {"answer":"legacy"}
    obs=BrownfieldAdapter(Legacy()).invoke_reasoning("agent:1","task:1",{})
    assert obs.payload["proposal"]["status"]=="UntrustedProposal"
