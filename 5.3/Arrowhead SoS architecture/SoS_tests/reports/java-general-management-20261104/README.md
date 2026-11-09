# Java generalManagement correction — 4 November 2026

All 18 previously failing registration/interface/naming checks now pass. The six affected systems are **AIGym, CertificateAuthority, DataManager, GateTunnel, Gatekeeper, and SysMonitor**.

| Verification | Passed | Failed | Errors | Skipped |
|---|---:|---:|---:|---:|
| Existing Java deployment suite (503 collected) | 298 | 0 | 0 | 205 |
| Additional live management access checks | 18 | 0 | 0 | 0 |
| Source tests across six Java builds | 70 | 0 | 0 | 0 |

The 205 skipped cases still lack isolated live fixtures and are not conformance passes. Native Go/Rust tests and other clouds were not rerun for this Java change.

## Implementation

The primary Java implementations now register `generalManagement` version `1.0.0`, with a `generic_https` / `CERT_AUTH` interface at their actual advertised address and port. The registered `status` operation is served at `GET /<system-path>/mgmt/general/status`. Registration happens in the system's normal startup process; no registry-only synthetic entries were inserted. Existing system-specific management and functional services are preserved.

The status response uses actual runtime health. CertificateAuthority preserves its Sysop/CertificateAuthority management allowlist; Gatekeeper, GateTunnel and SysMonitor preserve their Sysop/LocalCloudManager allowlist. AIGym requires Sysop. DataManager enforces its existing authenticated sysop-only policy even when the optional framework management filter is disabled. Mutual TLS and certificate-bound identity tokens remain required.

Only the implemented status operation is advertised here. This change does **not** implement or claim the broader `get-log` / `get-config` generalManagement contract. The current architectural deployment checks verify registration, interface properties, and naming, rather than those operation contracts.

Additional direct checks verify Sysop success (HTTP 200), ordinary isolated consumer rejection (403), and missing token rejection (401) on all six endpoints. Source regression tests cover access restrictions and identity binding. AIGym also needed a discovered Authentication URL-template correction: replacing `{token}` rather than appending a second token path segment. A regression test covers both discovered templates and legacy endpoint suffixes.

## Deployment and reproducibility

The six images were built from `Eclipse-Arrowhead-java/` using their Dockerfiles, including `mvn clean verify`, and deployed only to the existing Java cloud. Existing data volumes, credentials, and authorization policies were preserved, including the previously approved Blacklist read permission. All six affected containers passed their health checks after deployment.

[`deployment.json`](deployment.json) records primary source paths and file hashes, deployed image IDs, and health. [`source-tests.json`](source-tests.json) records the 70 source test outcomes. [`results.json`](results.json) and [`checks.log`](checks.log) record all 503 existing checks. [`endpoint-results.json`](endpoint-results.json) records the 18 extra checks.

The reusable read-only endpoint verifier is [`../../check_java_general_management.py`](../../check_java_general_management.py). Run it with `--profile <isolated-profile.json> --report <results.json>`. It needs active trusted Sysop (`inspector`) and non-sysop (`consumer`) actors; tokens come from environment variables. The local Java port defaults can be overridden with named endpoint origins in the profile. The deployment run provisioned four temporary test identities and removed all four successfully (HTTP 200); temporary private keys were deleted. See [`cleanup.json`](cleanup.json). Secrets and resolved deployment configuration are excluded from this report.
