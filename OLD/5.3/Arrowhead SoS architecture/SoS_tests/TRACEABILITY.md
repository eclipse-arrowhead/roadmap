# Requirement-to-test traceability

PDF pages use the physical 1-based page numbers (also printed in this 39-page PDF). Source content is a test specification, not an instruction to change a running cloud.

| Test ID | Source section | PDF pages | Test kind |
|---|---|---|
| `live/SR-register` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-lookup` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-metadata-match` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-metadata-miss` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-unique-instance` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-revoke` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-expiry` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-restricted-public` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-restricted-private` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/SR-direct-access` | 3.1.1; 2.1.1; 6.1 | 7, 10, 22 | live-behavior-assertion |
| `live/AUTHN-login` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-wrong-password` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-verify` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-expired` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-logout` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-changed-credentials` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-binding` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-unknown-token` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-missing-token` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHN-self-declared` | 3.1.2; 3.2; 6.2 | 10, 12, 13, 23 | live-behavior-assertion |
| `live/AUTHZ-no-policy` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-all` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-whitelist-in` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-whitelist-out` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-blacklist-in` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-blacklist-out` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-metadata-match` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-metadata-miss` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-management-deny` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-management-allow` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-operation-allow` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-operation-deny` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-wrong-provider` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-wrong-service` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-wrong-event` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/AUTHZ-revoked` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | live-behavior-assertion |
| `live/TOKEN-time-valid` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-expired` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-usage-first` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-usage-exhausted` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-wrong-consumer` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-wrong-provider` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-wrong-service` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-wrong-operation` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-tampered` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/TOKEN-local-verification` | 3.1.3; 6.5; 7 | 11, 25, 31 | live-behavior-assertion |
| `live/DSO-eligible` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-unauthorized` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-blacklisted` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-preferred` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-exclusive` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-expired-lock` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-qos-filter` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-qos-sort` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-token` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-push` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-unsubscribe` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-translation-off` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-translation-on` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/DSO-intercloud-denied` | 3.1.4; 6.4; 6.5; 6.9; 6.12 | 11, 12, 24, 25, 28, 29, 30 | live-behavior-assertion |
| `live/SSO-priority` | 3.1.4; 6.4 | 11, 12, 24 | live-behavior-assertion |
| `live/SSO-identifiers` | 3.1.4; 6.4 | 11, 12, 24 | live-behavior-assertion |
| `live/SSO-no-tokens` | 3.1.4; 6.4 | 11, 12, 24 | live-behavior-assertion |
| `live/SSO-not-grant` | 3.1.4; 6.4 | 11, 12, 24 | live-behavior-assertion |
| `live/SSO-consumer-isolation` | 3.1.4; 6.4 | 11, 12, 24 | live-behavior-assertion |
| `live/SSO-push` | 3.1.4; 6.4 | 11, 12, 24 | live-behavior-assertion |
| `live/BL-reason` | 4.3.1 | 16 | live-behavior-assertion |
| `live/BL-active` | 4.3.1 | 16 | live-behavior-assertion |
| `live/BL-expired` | 4.3.1 | 16 | live-behavior-assertion |
| `live/BL-whitelist` | 4.3.1 | 16 | live-behavior-assertion |
| `live/BL-self-lookup` | 4.3.1 | 16 | live-behavior-assertion |
| `live/BL-fail-closed` | 4.3.1 | 16 | live-behavior-assertion |
| `live/TM-bridge` | 4.3.2; 4.2; 6.9 | 15, 16, 28 | live-behavior-assertion |
| `live/TM-bridge-token` | 4.3.2; 4.2; 6.9 | 15, 16, 28 | live-behavior-assertion |
| `live/TM-usage-report` | 4.3.2; 4.2; 6.9 | 15, 16, 28 | live-behavior-assertion |
| `live/TM-wrong-translator` | 4.3.2; 4.2; 6.9 | 15, 16, 28 | live-behavior-assertion |
| `live/TM-termination` | 4.3.2; 4.2; 6.9 | 15, 16, 28 | live-behavior-assertion |
| `live/QOS-device-map` | 4.3.3 | 16 | live-behavior-assertion |
| `live/QOS-filter` | 4.3.3 | 16 | live-behavior-assertion |
| `live/QOS-sort` | 4.3.3 | 16 | live-behavior-assertion |
| `live/PDE-one-active` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-matched` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-missing` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-withdrawn` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-atomic` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-missing-alarm` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-ambiguous-alarm` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-undescribed-alarm` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-silent-alarm` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-unmonitored-alarm` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-ack` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-operator-priority` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-plant-priority` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/PDE-includes` | 4.4.1; 5.1; 6.7 | 12, 16, 20, 21, 26, 27 | live-behavior-assertion |
| `live/CHOR-start` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CHOR-executor-token` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CHOR-step-owner` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CHOR-retry` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CHOR-parallel` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CHOR-complete` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CHOR-abort-owner` | 4.4.2; 4.2; 6.8 | 15, 16, 27, 28 | live-behavior-assertion |
| `live/CFG-own` | 4.4.3 | 17 | live-behavior-assertion |
| `live/CFG-other` | 4.4.3 | 17 | live-behavior-assertion |
| `live/CFG-proxy-allowed` | 4.4.3 | 17 | live-behavior-assertion |
| `live/CFG-proxy-denied` | 4.4.3 | 17 | live-behavior-assertion |
| `live/CFG-management` | 4.4.3 | 17 | live-behavior-assertion |
| `live/CA-sign-authorized` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-sign-denied` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-end-entity` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-key-signing` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-recorded` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-valid` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-revoked` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-untrusted` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-trusted-key-expired` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/CA-new-handshake` | 4.5.1; 5.2; 9(11) | 17, 21, 34 | live-behavior-assertion |
| `live/ONB-unapproved` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-approved` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-sequence` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-system-approved` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-system-unapproved` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-superseded` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-revoked` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-no-auto-grant` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-offboard-registry` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-offboard-identities` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-offboard-certs` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-offboard-exclusion` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-no-signing-key` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/ONB-certificate-only` | 4.5.2; 5.2; 6.6 | 17, 21, 25, 26 | live-behavior-assertion |
| `live/EVENT-matching` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/EVENT-nonmatching` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/EVENT-expired` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/EVENT-not-started` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/EVENT-publisher-binding` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/EVENT-subscriber-binding` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/EVENT-all-matching` | 4.6.1; 6.10 | 17, 28, 29 | live-behavior-assertion |
| `live/DATA-latest` | 4.6.2; 2.1.1 | 7, 17 | live-behavior-assertion |
| `live/DATA-offline-producer` | 4.6.2; 2.1.1 | 7, 17 | live-behavior-assertion |
| `live/DATA-system-isolation` | 4.6.2; 2.1.1 | 7, 17 | live-behavior-assertion |
| `live/DATA-service-isolation` | 4.6.2; 2.1.1 | 7, 17 | live-behavior-assertion |
| `live/DATA-history-window` | 4.6.2; 2.1.1 | 7, 17 | live-behavior-assertion |
| `live/DATA-signal` | 4.6.2; 2.1.1 | 7, 17 | live-behavior-assertion |
| `live/TIME-startup` | 4.6.3 | 17 | live-behavior-assertion |
| `live/TIME-within-threshold` | 4.6.3 | 17 | live-behavior-assertion |
| `live/TIME-beyond-threshold` | 4.6.3 | 17 | live-behavior-assertion |
| `live/TIME-zone` | 4.6.3 | 17 | live-behavior-assertion |
| `live/MON-authorized-only` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-durable` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-deduplicate` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-invalid` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-retention` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-history` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-mqtt` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/MON-unknown-provider` | 4.7.1; 4.7.2; 6.11 | 18, 29 | live-behavior-assertion |
| `live/AI-sample` | 4.7.3 | 18 | live-behavior-assertion |
| `live/AI-predict` | 4.7.3 | 18 | live-behavior-assertion |
| `live/AI-observations` | 4.7.3 | 18 | live-behavior-assertion |
| `live/AI-denied` | 4.7.3 | 18 | live-behavior-assertion |
| `live/GK-discovery` | 4.8.1; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GK-cloud-binding` | 4.8.1; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GK-negotiation-recheck` | 4.8.1; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GK-management` | 4.8.1; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GT-consumer` | 4.8.2; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GT-peer` | 4.8.2; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GT-service` | 4.8.2; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GT-exchange` | 4.8.2; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/GT-closed` | 4.8.2; 6.12 | 18, 29, 30 | live-behavior-assertion |
| `live/RELAY-role-inbox` | 4.8.3 | 18, 19 | live-behavior-assertion |
| `live/RELAY-cloud-inbox` | 4.8.3 | 18, 19 | live-behavior-assertion |
| `live/RELAY-sender-spoof` | 4.8.3 | 18, 19 | live-behavior-assertion |
| `live/RELAY-name-constraints` | 4.8.3 | 18, 19 | live-behavior-assertion |
| `live/RELAY-dedicated-identity` | 4.8.3 | 18, 19 | live-behavior-assertion |
| `live/BASE-plaintext-bootstrap` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-missing-authz` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-missing-authn` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-discovery-not-trust` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-orchestration-not-grant` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-own-store` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-store-failure` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/BASE-secured-before-ready` | 3.2; 4.2; 7 | 12, 13, 15, 31 | live-behavior-assertion |
| `live/COMMON-ServiceRegistry-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-ServiceRegistry-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-Authentication-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-Authentication-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-ConsumerAuthorization-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-ConsumerAuthorization-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-DynamicServiceOrchestration-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-DynamicServiceOrchestration-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-SimpleStoreServiceOrchestration-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-SimpleStoreServiceOrchestration-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-Blacklist-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-Blacklist-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-TranslationManager-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-TranslationManager-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-DeviceQoSEvaluator-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-DeviceQoSEvaluator-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-PlantDescriptionEngine-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-PlantDescriptionEngine-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-Choreographer-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-Choreographer-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-Configuration-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-Configuration-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-CertificateAuthority-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-CertificateAuthority-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-Onboarding-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-Onboarding-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-EventHandler-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-EventHandler-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-DataManager-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-DataManager-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-TimeManager-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-TimeManager-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-SysMonitor-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-SysMonitor-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-AIGym-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-AIGym-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-Gatekeeper-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-Gatekeeper-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/COMMON-GateTunnel-management` | 4.2; 5.1; 5.2 | 9, 15, 20, 21 | live-behavior-assertion |
| `live/COMMON-GateTunnel-telemetry` | 2; 4.2; 4.7.1 | 5, 15, 18 | live-behavior-assertion |
| `live/MATRIX-ServiceRegistry_serviceDiscovery_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_serviceDiscovery_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_serviceDiscovery_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ServiceRegistry_systemDiscovery_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_systemDiscovery_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_systemDiscovery_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ServiceRegistry_deviceDiscovery_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_deviceDiscovery_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_deviceDiscovery_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ServiceRegistry_serviceRegistryManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_serviceRegistryManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_serviceRegistryManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ServiceRegistry_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ServiceRegistry_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ServiceRegistry_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Authentication_identity_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_identity_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_identity_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Authentication_identityManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_identityManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_identityManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Authentication_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Authentication_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Authentication_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorization_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorization_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorization_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationToken_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationToken_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationToken_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationTokenManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationTokenManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_authorizationTokenManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ConsumerAuthorization_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-ConsumerAuthorization_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-ConsumerAuthorization_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestration_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestration_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestration_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationPushManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationPushManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationPushManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationLockManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationLockManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationLockManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationHistoryManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationHistoryManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_serviceOrchestrationHistoryManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DynamicServiceOrchestration_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestration_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestration_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestration_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationSimpleStoreManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationSimpleStoreManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationSimpleStoreManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationPushManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationPushManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationPushManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationHistoryManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationHistoryManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_serviceOrchestrationHistoryManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SimpleStoreServiceOrchestration_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Blacklist_blacklistDiscovery_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_blacklistDiscovery_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_blacklistDiscovery_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Blacklist_blacklistManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_blacklistManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_blacklistManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Blacklist_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Blacklist_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Blacklist_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TranslationManager_translationBridge_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_translationBridge_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_translationBridge_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TranslationManager_translationBridgeManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_translationBridgeManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_translationBridgeManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TranslationManager_translationReport_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_translationReport_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_translationReport_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TranslationManager_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TranslationManager_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TranslationManager_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_qualityEvaluation_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_qualityEvaluation_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_qualityEvaluation_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_deviceQualityDataManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_deviceQualityDataManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_deviceQualityDataManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DeviceQoSEvaluator_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_plantDescriptionManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_plantDescriptionManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_plantDescriptionManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_plantDescriptionMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_plantDescriptionMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_plantDescriptionMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-PlantDescriptionEngine_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Choreographer_choreographerSession_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_choreographerSession_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_choreographerSession_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Choreographer_choreographerExecutor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_choreographerExecutor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_choreographerExecutor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Choreographer_choreographerManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_choreographerManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_choreographerManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Choreographer_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Choreographer_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Choreographer_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Configuration_configuration_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_configuration_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_configuration_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Configuration_configurationProxy_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_configurationProxy_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_configurationProxy_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Configuration_configurationManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_configurationManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_configurationManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Configuration_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Configuration_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Configuration_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateSigning_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateSigning_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateSigning_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateValidation_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateValidation_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateValidation_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateAuthorityManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateAuthorityManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_certificateAuthorityManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-CertificateAuthority_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-CertificateAuthority_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-CertificateAuthority_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Onboarding_onboarding_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_onboarding_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_onboarding_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Onboarding_onboardingManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_onboardingManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_onboardingManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Onboarding_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Onboarding_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Onboarding_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-EventHandler_eventPublish_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_eventPublish_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_eventPublish_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-EventHandler_eventSubscription_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_eventSubscription_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_eventSubscription_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-EventHandler_eventHandlerManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_eventHandlerManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_eventHandlerManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-EventHandler_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-EventHandler_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-EventHandler_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DataManager_dataProxy_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_dataProxy_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_dataProxy_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DataManager_dataHistorian_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_dataHistorian_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_dataHistorian_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DataManager_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-DataManager_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-DataManager_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TimeManager_time_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TimeManager_time_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TimeManager_time_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TimeManager_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TimeManager_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TimeManager_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-TimeManager_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TimeManager_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-TimeManager_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorHistory_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorHistory_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorHistory_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorData_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorData_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorData_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitorManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SysMonitor_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-SysMonitor_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-AIGym_aiGym_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-AIGym_aiGym_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-AIGym_aiGym_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-AIGym_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-AIGym_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-AIGym_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-AIGym_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-AIGym_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-AIGym_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Gatekeeper_globalServiceDiscovery_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_globalServiceDiscovery_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_globalServiceDiscovery_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Gatekeeper_interCloudNegotiation_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_interCloudNegotiation_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_interCloudNegotiation_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Gatekeeper_gatekeeperManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_gatekeeperManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_gatekeeperManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Gatekeeper_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-Gatekeeper_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-Gatekeeper_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelConnection_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelConnection_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelConnection_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelKey_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelKey_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelKey_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_gateTunnelManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-GateTunnel_generalManagement_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_generalManagement_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_generalManagement_naming` | 2.1.5 | 8, 32 | live-registration |
| `live/MATRIX-GateTunnel_sysMonitor_presence` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_sysMonitor_protected` | 2; 3; 4.2; 4.7.1; Appendix A | 5, 9, 10, 15, 18, 38, 39 | live-registration |
| `live/MATRIX-GateTunnel_sysMonitor_naming` | 2.1.5 | 8, 32 | live-registration |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-NONE-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-NONE-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-NONE-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-NONE-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-ALL-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-ALL-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-ALL-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-ALL-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-WHITELIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-WHITELIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-WHITELIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-WHITELIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-BLACKLIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-BLACKLIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-BLACKLIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-TestConsumer-BLACKLIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-NONE-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-NONE-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-NONE-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-NONE-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-ALL-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-ALL-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-ALL-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-ALL-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-WHITELIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-WHITELIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-WHITELIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-WHITELIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-BLACKLIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-BLACKLIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-BLACKLIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-SERVICE_DEF-OtherConsumer-BLACKLIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-NONE-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-NONE-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-NONE-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-NONE-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-ALL-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-ALL-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-ALL-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-ALL-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-WHITELIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-WHITELIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-WHITELIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-WHITELIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-BLACKLIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-BLACKLIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-BLACKLIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-TestConsumer-BLACKLIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-NONE-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-NONE-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-NONE-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-NONE-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-ALL-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-ALL-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-ALL-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-ALL-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-WHITELIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-WHITELIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-WHITELIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-WHITELIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-BLACKLIST-NONE` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-BLACKLIST-ALL` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-BLACKLIST-WHITELIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `java/JAVA-AUTHZ-EVENT_TYPE-OtherConsumer-BLACKLIST-BLACKLIST` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-missing-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-SERVICE_DEF-missing-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-all-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-all-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-all-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-all-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-all-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-all-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-whitelist-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-whitelist-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-whitelist-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-whitelist-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-whitelist-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-whitelist-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-blacklist-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-blacklist-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-blacklist-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-blacklist-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-blacklist-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-SERVICE_DEF-blacklist-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-missing-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-EVENT_TYPE-missing-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-all-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-all-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-all-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-all-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-all-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-all-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-whitelist-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-whitelist-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-whitelist-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-whitelist-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-whitelist-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-whitelist-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-blacklist-all-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-blacklist-all-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-blacklist-whitelist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-blacklist-whitelist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-blacklist-blacklist-TestConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-priority-EVENT_TYPE-blacklist-blacklist-OtherConsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-isolation-provider` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-isolation-consumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-isolation-cloud` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-isolation-target` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-isolation-targetType` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-operation-all-read` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-operation-all-write` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-operation-whitelist-read` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-operation-whitelist-write` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-operation-blacklist-read` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDPolicyDecisions/AUTHZ-operation-blacklist-write` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `go/TestGSoSDMetadataSelection/META-01` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-02` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-03` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-04` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-05` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-06` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-07` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-08` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-09` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDMetadataSelection/META-10` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-provider-01` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-provider-02` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-provider-03` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-provider-04` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-provider-05` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-provider-06` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-target-07` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-target-08` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-target-09` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-target-10` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-target-11` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-target-12` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-scope-13` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-scope-14` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-scope-15` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-scope-16` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-scope-17` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDCanonicalIdentifiers/NAME-scope-18` | 2.1.5 | 8, 32 | native-component |
| `go/TestGSoSDAMQPTransport/secure-default` | 4.7.1 | 18 | native-component |
| `go/TestGSoSDAMQPTransport/secure-explicit` | 4.7.1 | 18 | native-component |
| `go/TestGSoSDAMQPTransport/plaintext` | 4.7.1 | 18 | native-component |
| `go/TestGSoSDAMQPTransport/mqtt-not-monitor` | 4.7.1 | 18 | native-component |
| `go/TestGSoSDAMQPTransport/missing-host` | 4.7.1 | 18 | native-component |
| `go/TestGSoSDAMQPTransport/embedded-password` | 4.7.1 | 18 | native-component |
| `go/TestGSoSDCoreServiceMatrix/authentication/identity` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/authentication/identityManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/authentication/generalManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/consumer-authorization/authorization` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/consumer-authorization/authorizationToken` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/consumer-authorization/authorizationManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/consumer-authorization/authorizationTokenManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/consumer-authorization/generalManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-dynamic/serviceOrchestration` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-dynamic/serviceOrchestrationPushManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-dynamic/serviceOrchestrationLockManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-dynamic/serviceOrchestrationHistoryManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-dynamic/generalManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-simple/serviceOrchestration` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-simple/serviceOrchestrationSimpleStoreManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-simple/serviceOrchestrationPushManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-simple/serviceOrchestrationHistoryManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `go/TestGSoSDCoreServiceMatrix/serviceorchestration-simple/generalManagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_authz_event_type_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_missing_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_missing_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_event_type_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_isolation_cloud` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_isolation_consumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_isolation_provider` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_isolation_target` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_isolation_targettype` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_operation_all_read` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_operation_all_write` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_operation_blacklist_read` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_operation_blacklist_write` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_operation_whitelist_read` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_operation_whitelist_write` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_all_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_all_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_all_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_all_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_all_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_all_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_blacklist_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_blacklist_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_blacklist_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_blacklist_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_blacklist_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_blacklist_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_whitelist_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_whitelist_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_whitelist_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_whitelist_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_whitelist_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_event_type_whitelist_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_all_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_all_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_all_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_all_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_all_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_all_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_blacklist_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_blacklist_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_blacklist_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_blacklist_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_blacklist_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_blacklist_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_whitelist_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_whitelist_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_whitelist_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_whitelist_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_whitelist_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_priority_service_def_whitelist_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_all_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_all_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_blacklist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_blacklist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_missing_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_missing_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_whitelist_otherconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_authz_service_def_whitelist_testconsumer` | 3.1.3; 5.2; 6.3 | 11, 21, 23, 24 | native-component |
| `rust/gsosd_matrix_authentication_generalmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_authentication_identity` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_authentication_identitymanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_consumerauthorization_authorization` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_consumerauthorization_authorizationmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_consumerauthorization_authorizationtoken` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_consumerauthorization_authorizationtokenmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_consumerauthorization_generalmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_dynamicserviceorchestration_generalmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_dynamicserviceorchestration_serviceorchestration` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_dynamicserviceorchestration_serviceorchestrationhistorymanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_dynamicserviceorchestration_serviceorchestrationlockmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_dynamicserviceorchestration_serviceorchestrationpushmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_serviceregistry_devicediscovery` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_serviceregistry_generalmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_serviceregistry_servicediscovery` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_serviceregistry_serviceregistrymanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_serviceregistry_systemdiscovery` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_simplestoreserviceorchestration_generalmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_simplestoreserviceorchestration_serviceorchestration` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_simplestoreserviceorchestration_serviceorchestrationhistorymanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_simplestoreserviceorchestration_serviceorchestrationpushmanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_matrix_simplestoreserviceorchestration_serviceorchestrationsimplestoremanagement` | 3; Appendix A.1 | 9, 38 | native-component |
| `rust/gsosd_meta_01` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_02` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_03` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_04` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_05` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_06` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_07` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_08` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_09` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_meta_10` | 3.1.1; 3.1.3 | 10, 11 | native-component |
| `rust/gsosd_name_provider_01` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_provider_02` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_provider_03` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_provider_04` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_provider_05` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_provider_06` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_scope_13` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_scope_14` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_scope_15` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_scope_16` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_scope_17` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_scope_18` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_target_07` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_target_08` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_target_09` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_target_10` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_target_11` | 2.1.5 | 8, 32 | native-component |
| `rust/gsosd_name_target_12` | 2.1.5 | 8, 32 | native-component |
