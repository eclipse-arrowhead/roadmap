# Recorded test results — naming fix verified, 2026-11-03

Latest deployment run: [three-cloud results](reports/deployments/2026-11-03-primary-refresh/README.md). All 60 selected core/support containers are running. Java: 266 passed, 32 failed, 205 skipped; Go and Rust: 298 passed, zero failed, 205 skipped each. The 205 unimplemented fixtures per cloud remain a qualification limit; a proposed Java bootstrap read grant was rejected by automatic approval review and was not applied.

Source: GSoSD Core and Support Systems 5.3.0, draft dated 2026-11-02; 39 pages. SHA-256: `e823ecd9aa1f8e5082d756db3fa20a1e72c8eac70e11c3697c224e15f7bf91d1`.

## Implementation tests

| Target | Passed | Failed | Skipped | Scope |
|---|---:|---:|---:|---|
| java | 64 | 0 | 0 | 80 freshly compiled consumer-authorization source files; real engine/DTO conversion, controlled database lookup boundary |
| go | 115 | 0 | 0 | Private core helper inside the primary ConsumerAuthorization module, copied to a temporary directory |
| rust | 114 | 0 | 0 | Primary native core library and public contracts, copied to a temporary directory |

Total: **293 native cases: 293 passed, zero failed**. All 16 original Go/Rust canonical-name failures are fixed, with original expectations unchanged. Full Go regressions and all 157 Rust core tests also pass. See `NAMING_FIX_VERIFICATION.md`. Original failure evidence is retained in `reports/history/before-naming-fix/`.

## Deployment checks

**503 authored deployment checks, 503 skipped, zero live conformance passes.** No profile, live credentials, broker connection or running cloud was used. Of these checks, 282 inspect real service registrations when configured and 221 are behavioral assertions. The example profile supplies 16 concrete authentication/authorization recipes; the other 205 behavioral assertions still need IDD-specific setup, request and observation fixtures before they can exercise a deployment. They are not complete end-to-end automation by themselves.

## Runner checks

**27 harness self-tests passed.** These check the test runner (oracles, typed interpolation, mutation preflight, HTTPS enforcement, successful controls for negative tests and cleanup). They are not counted as Arrowhead conformance passes.

## Limits

No deployed cloud was changed or qualified. The subsequent regression run did exercise the existing isolated Go/Rust core TLS, process and federation fixtures; it does not establish deployed-cloud, AMQP/MQTT broker, SQL, offboarding, UI or full backward-compatibility qualification. A component test pass is not an operational or release certification. Source fingerprints are in `reports/source-fingerprints.json`. The three implementations still report version 5.2.2 in many source artifacts; these tests target the supplied 5.3.0 architectural draft.
