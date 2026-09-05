# AOF v1.0 Reference Implementation
## RI-2 — Safety Kernel Reference Implementation

**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

RI-2 implements the reference Safety Kernel as a fail-controlled decision boundary.

Canonical predicate:

`ExecuteAllowed = C ∧ H ∧ P ∧ S ∧ R ∧ V`

where:
- C = Capability
- H = Authority
- P = Policy
- S = State
- R = Risk
- V = Verification

Decision aggregation:
- any gate `Fail` -> `Deny`;
- no `Fail` and at least one `Pending` -> `Pending`;
- all gates `Pass` -> `Allow`.

`Pending` MUST NOT be treated as `Allow`.

The kernel remains non-effecting in RI-2. Consequential execution is deferred to RI-3.

Reference components:
- CapabilityGate
- AuthorityEvaluator
- PolicyEvaluator
- StateValidator
- RiskGate
- VerificationGate

Hard semantic boundaries:
- Capability != Authority
- Approval != AuthorityGrant
- PolicyPrompt != PolicyEnforcement
- RiskAssessment != RiskAcceptance
- Pending != Pass
- ValidAtCheck != ValidAtEffect
