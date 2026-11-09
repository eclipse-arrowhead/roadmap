# Naming-conformance fix verification — 2026-11-03

All 16 original failures are resolved without changing the specification tests or their expectations.

## Implementation

Go and Rust now validate policy identifiers before a new or updated grant is persisted:

- Provider and whitelist/blacklist identities: PascalCase, ASCII letters/digits, at most 63 characters.
- Service definitions and event types: camelCase, ASCII letters/digits, at most 63 characters.
- Operation scopes: lowercase kebab-case, beginning with a lowercase letter, at most 63 characters.

Malformed names are rejected. Existing identifiers are not silently rewritten. The generic name helper is unchanged because other identifier kinds use it. The four identical Go core helper copies were updated together; Rust's shared core covers its core executables.

New regression tests cover both SERVICE_DEF and EVENT_TYPE, single-character and length-boundary names, invalid case/separators/Unicode/newlines, whitelist/blacklist identities, no policy write on invalid input, and transaction rollback of a mixed valid/invalid grant batch.

This changes source validation only. It does not migrate existing policy records, add/remove grants, rebuild deployed images or change running clouds. Previously stored noncanonical records remain untouched; a future update containing those names must use canonical identifiers. Revoke/read behavior has not been changed by this fix.

## Verified results

| Test group | Result |
|---|---|
| Original Java specification tests | 64 passed |
| Original Go specification tests | 115 passed |
| Original Rust specification tests | 114 passed |
| Previously failing naming cases | All 16 passed; expectations unchanged |
| Full Go ConsumerAuthorization regression suite | Passed, including isolated local TLS integration tests |
| Full Rust core suite | 157 passed, zero failed/ignored, including specification cases, new regressions and local TLS/process tests |
| New Go naming/rollback regressions in Authentication, ConsumerAuthorization, SimpleStore and Dynamic modules | Passed in all four primary modules |

The 503 deployment checks still require a live profile and/or additional IDD fixtures; they have not been reclassified as passes. Historical failure reports are retained under `reports/history/before-naming-fix/`. Current source fingerprints and raw outputs are in `reports/`.
