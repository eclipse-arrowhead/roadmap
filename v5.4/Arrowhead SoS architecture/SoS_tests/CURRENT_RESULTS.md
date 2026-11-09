# Latest recorded outcomes

Latest Java verification (4 November 2026): [generalManagement correction and results](reports/java-general-management-20261104/README.md): **298 passed, zero failures/errors, 205 skipped** out of 503 checks; 18 additional endpoint access checks and 70 source tests passed. The 18 missing-registration failures are resolved on all six affected systems. The previously approved Blacklist read permission remains applied. Go/Rust historical results remain [298 passed, zero failed, 205 skipped each](reports/deployments/2026-11-03-primary-refresh/README.md); those clouds were not retested in this Java run. Missing live fixtures remain a qualification limit.

These are execution outcomes, not release certification. See RESULTS.md for the original dated run and COVERAGE.md for scope.

| Group | Pass | Fail/error | Skip |
|---|---:|---:|---:|
| native-java | 64 | 0 | 0 |
| native-go | 115 | 0 | 0 |
| native-rust | 114 | 0 | 0 |
| deployment | 0 | 0 | 503 |
| harness-self-tests | 27 | 0 | 0 |
