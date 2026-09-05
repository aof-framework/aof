# AOF v1.0 Reference Implementation
## RI-3 — Execution / State / Trace Runtime

**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

RI-3 introduces the first controlled consequential effect path in the reference implementation.

### Runtime components
- `InMemoryStateStore`
- `ExecutionContractRegistry`
- `InMemoryTraceRecorder`
- `EffectBoundary`
- `ExecutionRuntime`

### Effect Boundary sequence
1. Resolve ExecutionContract.
2. Reject missing/replayed contract.
3. Re-read current State.
4. Compare current State version with contract-bound version.
5. Require Decision status `Allow`.
6. Require contract authorization marker.
7. Re-evaluate Safety Kernel immediately before effect.
8. Dispatch through the adapter only when revalidation returns `Allow`.
9. Record Trace before and after dispatch.
10. Preserve `UnknownEffect` as non-success.

This makes the invariant executable:

`ValidAtCheck != ValidAtEffect`

A prior valid Decision does not guarantee a valid Effect. Revocation, Policy change,
State change, Risk change, or Verification change MAY block execution at the Effect Boundary.

`ExecutionContract` is an execution authorization artifact but does not itself create Authority.
