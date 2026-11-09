# Tests derived from the Arrowhead GSoSD 5.3.0

This package contains **796 specification-derived test cases** for the supplied 39-page architectural draft: **293 native component tests** and **503 deployment checks**. A further **27 self-tests** validate the runner. These numbers are parameterized cases, not distinct architectural requirements.

The recorded native run has **277 passes and 16 failures**. All 16 failures are canonical-name findings in Go and Rust. The deployment checks have **503 skips**, because no running test cloud or live credentials were supplied. No primary implementation source, security policy or running system was changed.

Start with [RESULTS.md](RESULTS.md), [FINDINGS.md](FINDINGS.md) and [COVERAGE.md](COVERAGE.md). [TRACEABILITY.md](TRACEABILITY.md) and `requirements.json` map every specification-derived case to PDF sections and physical page numbers.

## What is executable now

- Java: 64 authorization-engine decisions, compiled from all 80 production source files of primary ConsumerAuthorization. The real engine and DTO converter run; a controlled database lookup boundary supplies relevant policy rows. This does not exercise SQL policy selection or persistence.
- Go: 115 cases exercise the primary ConsumerAuthorization module's private core helper, including 63 authorization decisions, ten metadata comparisons, 18 canonical-name cases, six AMQP endpoint cases and 18 advertised-core-service cases. The role-switching helper is tested; independently packaged sibling executables are not thereby certified.
- Rust: 114 cases exercise the primary core library: the shared 91 authorization/metadata/naming vectors plus 23 core service-matrix cases. Policy tests use its existing isolated fixture and actual authorization code.
- Deployment: 282 registration/interface/naming checks need only a configured inspector and selected running systems. Another 221 behavioral assertions need scenario fixtures. `config/profile.example.json` contains 16 concrete HTTP recipes for login and authorization; the remaining 205 need IDD-specific setup/request/observation fixtures. Those 205 are assertion definitions, not completed end-to-end workflows.

## Run local component tests

Use Python 3.11 or later. Java needs a suitable JDK (the recorded run used JDK 22); Go, Rust/Cargo and OpenSSL are used by their respective tests. No Python packages are needed. Native dependencies must already be cached; Go and Rust use offline dependency resolution.

From this folder:

```sh
python3 run_selftests.py
python3 run_native.py --language all
python3 summarize_results.py
```

`run_native.py` discovers the enclosing Eclipse workspace. Elsewhere, supply `--root /path/to/Eclipse`. `--language java`, `go` and `rust` run one implementation. All source changes needed for tests are injected into disposable copies under the system temporary folder. `--work-dir /private/tmp/gsosd-native-work` can reuse build caches; it must be a dedicated scratch folder.

Java's exact dependency list is resolved from the primary ConsumerAuthorization Surefire report and matching local Maven cache. The runner compiles production source freshly, not the archived test classes. If that classpath is missing, build the primary Java module with its normal Maven setup first; the runner records unavailable dependencies instead of claiming a pass. Go/Rust source closures are copied without build outputs or Git history. Rust's temporary reduced workspace may prune the copied lockfile, but the runner rejects package versions absent from the source lockfile.

The native command intentionally exits nonzero for the currently recorded conformance failures. Do not change expectations merely to make these tests green. A pass does not certify deployment or Java/Go/Rust wire equivalence.

## Configure and run deployment checks

Copy `config/profile.example.json` to a local profile, update HTTPS endpoints, trusted CA, client certificate/key paths and the selected `systems`. Paths are relative to the profile file. Use a dedicated test provider/consumer namespace and a registry inspector allowed to perform direct discovery. The mandatory base systems are ServiceRegistry, Authentication and ConsumerAuthorization; optional systems are tested only when listed. To run the complete 5.3 inventory, list all 20 names in `catalog.json`.

Supply tokens and the test consumer password using the environment-variable names in `actors.*.token_env` and `secret_variables`. The package contains no passwords, certificates, private keys or active tokens. Bootstrap/setup of those identities is outside this package. Requests always verify TLS peers and refuse redirects; an inaccessible server is not interpreted as a successful denial test.

```sh
python3 run_live.py --profile /path/to/profile.json
python3 run_live.py --profile /path/to/profile.json --filter RegistrationTests
python3 run_live.py --profile /path/to/profile.json --filter AUTHZ --allow-mutations
python3 summarize_results.py
```

The first two commands are suitable for registration inspection. Policy grants, revocation, login and other non-read-only requests need `--allow-mutations` and an explicitly isolated profile. The shipped example sets `test_environment` and `isolated` to true but uses placeholder certificate paths and hostnames; it cannot silently run against a real environment. `AUTHZ-no-policy` also requires a fresh test target without a prior policy.

`run_live.py` without a profile collects all 503 tests and reports them as skipped. A missing individual fixture also produces a skip. A configured request with an invalid response or failed assertion produces an error/failure. Skips are never counted as conformance passes. Native and live results are separate in JSON and JUnit output.

`python3 run_all.py` runs runner checks, native tests and deployment collection. Add `--profile` and `--allow-mutations` only for an explicitly configured isolated test environment. It exits nonzero when any layer fails.

## Add an IDD-specific scenario fixture

Each ID in `scenarios.json` has an assertion, source reference and prerequisites. Add its fixture under `profile.scenarios[case-id]`. A fixture contains:

- `variables`: local fixture identifiers and expected non-secret values;
- `control`: a known-successful request required for a negative access/TLS test;
- `setup`: ordered HTTP operations with expected statuses and optional `capture` JSON pointers;
- `request`: the operation being tested or its observation request;
- `select`: a JSON pointer into `{status, body, tls_rejected}` (default `/body`);
- `project`: optional field-to-pointer mapping for an IDD-specific observation shape;
- `cleanup`: requests run in reverse order even after an assertion fails.

Requests have `endpoint`, `actor`, `method`, `path`, optional `query`, `body`, `headers`, `capture` and `expected_statuses`. A full `${variable}` retains its JSON type; `${url:variable}` URL-encodes a path value. A setup capture such as `{"instanceId":"/body/entries/0/instanceId"}` makes that value available to later steps. Variables are preflighted before mutations. Successful setup defaults are 200/201/204; customize per IDD.

For telemetry, `project` maps actual fields to `provider`, `observationType`, `sourceTime`, `sequence`, `value`, `unit` and `quality`. Map existing IDD fields without manufacturing a missing value: for example a random observation UUID is not a numeric sequence number. No wire-field spelling or response-code detail absent from the PDF is made mandatory by implication.

The high-level PDF does not specify complete broker drivers, failure-injection controls, certificate-extension decoders, provisioning flows, UI selectors, retention periods or timing bounds. Those fixtures must be supplied from the matching IDDs/test deployment. A timeout, an HTTP error or an empty result alone is insufficient evidence of a lifecycle property unless its setup/control and observation window establish that property. For state-changing negative tests, also inspect resulting state; a failure status alone does not prove absence of side effects.

Do not populate a fixture with an already-computed boolean just to satisfy its assertion: acquire the observation from the system operation/state actually under test. Broker, certificate, topology and lifecycle assertions are not represented as executed end-to-end tests until those adapters/fixtures exist.

## Files and evidence

| File | Purpose |
|---|---|
| `catalog.json` | Five core and fifteen active support systems, services and source PDF fingerprint |
| `scenarios.json` | 221 behavioral assertions, prerequisites and source pages |
| `requirements.json`, `TRACEABILITY.md` | All 796 specification-derived cases |
| `native/` | Newly authored native source tests and shared vectors |
| `sos_tests/` | HTTPS execution, assertions and dynamic live checks |
| `config/` | Example core HTTP profile and a clearly marked lifecycle fixture template |
| `reports/native-results.json` | Native execution outcomes and scope |
| `reports/*-native.log` | Raw compiler and native test output |
| `reports/live-results.json` | Deployment outcomes, including explicit skips |
| `reports/harness-results.json` | Runner self-test outcomes |
| `reports/source-fingerprints.json` | Source snapshot hashes of tested modules |
| `reports/junit.xml` | CI-compatible combined report |
| `RESULTS.md`, `FINDINGS.md`, `COVERAGE.md` | Recorded results, reproduced failures and qualifications |

The source is `../BlackBox_5.3.0/GSoSD-Core-and-Support-Systems-5.3.0.pdf`, draft dated 2026-11-02. Its SHA-256 is recorded in `catalog.json`; no PDF instructions or embedded examples were executed. The PDF mixes 5.3 expectations, 5.2.2 behavior and unresolved proposals; those distinctions are retained in the coverage notes.
