# Coverage and architectural qualifications

The executable inventory covers the five Core and fifteen active Support systems in Tables 2, 3, 7 and 8. Extra workspace implementations are not made mandatory by inference.

| System | Named services including common services | Behavioral assertions |
|---|---:|---:|
| ServiceRegistry | 6 | 12 |
| Authentication | 4 | 12 |
| ConsumerAuthorization | 6 | 28 |
| DynamicServiceOrchestration | 6 | 16 |
| SimpleStoreServiceOrchestration | 6 | 8 |
| Blacklist | 4 | 8 |
| TranslationManager | 5 | 7 |
| DeviceQoSEvaluator | 4 | 5 |
| PlantDescriptionEngine | 4 | 16 |
| Choreographer | 5 | 9 |
| Configuration | 5 | 7 |
| CertificateAuthority | 5 | 12 |
| Onboarding | 4 | 16 |
| EventHandler | 5 | 9 |
| DataManager | 4 | 8 |
| TimeManager | 3 | 6 |
| SysMonitor | 5 | 10 |
| AIGym | 3 | 6 |
| Gatekeeper | 5 | 6 |
| GateTunnel | 5 | 7 |

Additional cases address the relay and cross-cutting baseline. The JSON manifest and TRACEABILITY.md contain all 796 specification-derived case identifiers. Native and deployment cases overlap in requirements; case counts are not counts of distinct normative requirements.

## Not specified enough for an automatic architectural verdict

- Exact endpoint paths, wire DTOs, token encodings, error codes, data-model translation semantics and detailed scope fallback require the per-system IDDs. The native operation fallback tests use the current implementation contract as a labeled interpretation. The live example uses paths observed in the restored Java and current Go/Rust core APIs.
- No latency, jitter, throughput, clock-deviation threshold, retention duration, cache TTL, reconciliation interval or delivery timeout is invented. Lifecycle and failure-injection fixtures must supply these from the deployment/IDD.
- Naming requirements apply to Arrowhead names, not URL paths, database names or container names.
- Port uniqueness, retired-port reservation, allocation history and all 24 cloud indices require an authoritative deployment/allocation manifest; only the documented secure AMQP default is exercised locally.
- HTTP failure status alone does not prove an operation had no side effects. The fault-injection and lifecycle fixtures must also inspect resulting state; the runner cannot infer that state from a failure response.
- The PDF is a draft mixing 5.3.0 architectural statements with 5.2.2 implementations and project proposals. In particular p.5 makes generalManagement/sysMonitor a 5.3 expectation, while pp.18 and 33 qualify sysMonitor release status. Tests target the stated draft behavior; they do not claim an upstream release obligation was already accepted.

## Unresolved issues retained as qualifications (Section 9, pp.33–34)

| Issue | Treatment |
|---|---|
| DSO/PDE backend convergence and wider contract equivalence | Managed snapshot assertions included; full equivalence not claimed |
| Engineering/operations role separation | Unauthorized management assertions included; future role split not invented |
| Standardization of sysMonitor | Draft/project-proposal classification retained |
| Arbitrary translation chains | No universal translator-chain claim |
| User authentication, OIDC, OAuth | No mandatory unstandardized authentication tests |
| Federation release/security and relay credential lifecycle | Session/peer/trust assertions authored; end-to-end qualification pending fixtures |
| AMQP versus MQTT future transport choice | Tests use current documented split; no assumed future migration |
| Intermediary event-type authorization | No invented publisher/subscriber delegation policy |
| Secure default versus development exceptions | HTTPS, identity and permission checks authored; no production deployment changed |
| Hardware attestation and announcement-based onboarding | Neither treated as a current requirement |
| Existing-session revocation, renewal, root rollover | New-handshake rejection authored; instant established-session termination not assumed |
| Stateful support replication | No unsupported multi-active replication assumptions |
| Upstream scope of project support systems | Project status retained |
