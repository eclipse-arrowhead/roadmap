# Java deployment-check rerun

503 checks collected: **280 passed, 18 failed, zero errors, 205 skipped**.

All 14 configured authorization scenarios passed after the approved permission update. Two other authorization assertions still lack fixtures.

The 18 failures are three assertions each for missing `generalManagement` registrations on AIGym, CertificateAuthority, DataManager, GateTunnel, Gatekeeper and SysMonitor. The 205 skips remain unimplemented deployment fixtures and are not conformance passes.

All four temporary test identities were removed successfully (HTTP 200); temporary keys were deleted by the fixture runner.
