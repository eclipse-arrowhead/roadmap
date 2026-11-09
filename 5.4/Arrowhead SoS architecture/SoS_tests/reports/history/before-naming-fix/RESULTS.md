# Recorded test results — 2026-11-03

Source: GSoSD Core and Support Systems 5.3.0, draft dated 2026-11-02; 39 pages. SHA-256: `e823ecd9aa1f8e5082d756db3fa20a1e72c8eac70e11c3697c224e15f7bf91d1`.

## Implementation tests

| Target | Passed | Failed | Skipped | Scope |
|---|---:|---:|---:|---|
| java | 64 | 0 | 0 | 80 freshly compiled consumer-authorization source files; real engine/DTO conversion, controlled database lookup boundary |
| go | 107 | 8 | 0 | Private core helper inside the primary ConsumerAuthorization module, copied to a temporary directory |
| rust | 106 | 8 | 0 | Primary native core library and public contracts, copied to a temporary directory |

Total: **293 native cases: 277 passed, 16 failed**. All 16 failures concern canonical identifiers in Go and Rust: eight matching failures per implementation. These failures have not been suppressed or fixed. See `FINDINGS.md` and the raw logs.

## Deployment checks

**503 authored deployment checks, 503 skipped, zero live conformance passes.** No profile, live credentials, broker connection or running cloud was used. Of these checks, 282 inspect real service registrations when configured and 221 are behavioral assertions. The example profile supplies 16 concrete authentication/authorization recipes; the other 205 behavioral assertions still need IDD-specific setup, request and observation fixtures before they can exercise a deployment. They are not complete end-to-end automation by themselves.

## Runner checks

**27 harness self-tests passed.** These check the test runner (oracles, typed interpolation, mutation preflight, HTTPS enforcement, successful controls for negative tests and cleanup). They are not counted as Arrowhead conformance passes.

## Limits

No deployed Java/Go/Rust cloud, SQL integration, AMQP or MQTT exchange, offboarding flow, UI, failure injection, end-to-end federation, complete backwards-compatibility matrix or full security review was exercised. A component test pass is not an operational or release certification. Source fingerprints are in `reports/source-fingerprints.json`. The three implementations still report version 5.2.2 in many source artifacts; these tests target the supplied 5.3.0 architectural draft.
