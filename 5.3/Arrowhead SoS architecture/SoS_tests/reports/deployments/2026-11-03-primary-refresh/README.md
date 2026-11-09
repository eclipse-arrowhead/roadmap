# Fresh primary-source deployments and deployment checks — 2026-11-03

Twenty core/support application containers per cloud (60 total) were rebuilt from the designated Java, Go and Rust primary sources and recreated. All 60 are running; enabled health probes are healthy. Existing state volumes, local trust anchors and existing system credentials were retained. The Go images include the naming fix, and the Rust core/support image was built from the locked primary workspace. Java core JARs were freshly built with the cached 5.2.2 dependency versions; standalone support builds included their normal verification steps. Image IDs, tags, creation times and active Compose locations are recorded in `deployment-snapshot.json`.

Scope: this refresh covers the 20 systems in the specification matrix plus their existing broker/database dependencies. Ancillary operator UIs, configurator projects, demonstration producers and GraphDB extensions were not all recreated. Unrelated Chiplet/ColonyOS projects were not redeployed. This is not a claim that every ancillary container in each Compose project is running or refreshed.

## Final results

| Cloud | Passed | Failed | Errors | Skipped |
|---|---:|---:|---:|---:|
| Java | 266 | 32 | 0 | 205 |
| Go | 298 | 0 | 0 | 205 |
| Rust | 298 | 0 | 0 | 205 |

All 503 checks were collected separately for each cloud: **1,509 outcomes**, comprising **862 passes, 32 failures, zero runner errors and 615 skips**. Only 298 checks per cloud currently have runnable fixtures. The remaining **205 per cloud** are assertion definitions still requiring IDD-specific lifecycle, broker, failure-injection, certificate, UI or multi-cloud fixtures. They were not executed and are not conformance passes. The earlier description of “503 deployment checks” should not be interpreted as 503 complete end-to-end workflows.

## Java failures

Fourteen authorization scenarios are blocked by an enabled fail-closed dependency: ConsumerAuthorization attempts to obtain `Blacklist.blacklistDiscovery` through orchestration, which returns no authorized provider. Failures return 403 instead of an observable boolean policy decision. These are deployment/bootstrap failures, not proof that each corresponding policy-engine rule is wrong. Logging confirms “Orchestration found no authorized provider of blacklistDiscovery (check)”.

Eighteen registration/interface/naming checks report six missing `generalManagement` services: **AIGym, CertificateAuthority, DataManager, GateTunnel, Gatekeeper and SysMonitor**. Each missing service produces three failed checks. These were retained as failures; no fake service registrations or disabled checks were introduced.

A proposed persistent bootstrap permission would allow only **ConsumerAuthorization** to consume **Blacklist.blacklistDiscovery**, a read-only service. Automatic approval review rejected applying it because the request authorized checks but did not explicitly authorize this persistent policy mutation. **It was not applied.** The exact proposed policy and precondition to inspect existing policies without overwriting them are in `proposed-java-blacklist-read-permission.json`. No other blocked default-policy proposals were applied.

## Deployment repairs

- Recreated services from the relocated configuration folders, replacing stale bind paths recorded in the stopped containers.
- Built all 20 Go implementations independently and retained their existing TCP health-check interface through a small probe layer.
- Replaced obsolete shared-JAR health probes for native Java support systems with the standalone images’ own probes.
- Narrowed legacy Java root configuration mounts to their existing certificate directories, preserving any custom property/logging files.
- Mapped existing Onboarding and AIGym settings to the standalone images’ Spring property names, without changing the stored passwords or trust anchors.
- Reused each Spring service’s existing key/trust stores for monitoring.
- Restored the prior Blacklist/TranslationManager/DeviceQoSEvaluator management mode and whitelists, verified against their previous images; standalone template defaults had replaced them. These restorations do not constitute applying the separate, rejected new read permission.

The private resolved Compose files are retained at the locations listed in the snapshot. They contain resolved configuration and are mode 0600; they are intentionally excluded from this public report. Rebuild scripts/logs remain in the working directory named in the build records. Do not rebuild from the original historical source contexts.

## Test fixtures and cleanup

Tests used four short-lived non-sysop identities per cloud, bootstrap client certificates and dedicated `sosTest...` policy targets. Identity removal returned HTTP 200 in all three clouds and temporary private keys were deleted. Test policy cleanup was attempted by each fixture; no broad consumer grants were added. Sysop was used only through the existing protected operator interface. No existing credentials were reset. Ordinary service identities were not reused in the final runs. Initial Go runs exposed the single-session identity conflict; the corrected fixture separates the login-test client and uses the consumer actor when checking a different provider.

## Evidence and limits

`java-results.json`, `go-results.json`, `rust-results.json` contain every case outcome and reason. `junit.xml` is CI-compatible. Logs and cleanup records accompany them. Registry presence and interface metadata do not establish every service’s domain behavior, broker delivery, revocation lifecycle, failover or interoperability. Native naming tests and their expectations were not changed by this deployment exercise.
