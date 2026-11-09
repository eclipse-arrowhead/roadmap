# Reproduced component findings

## Noncanonical identifiers retained by Go and Rust

GSoSD Table 1 (PDF p.8, Section 2.1.5; reiterated p.32) specifies PascalCase ASCII alphanumeric system names, camelCase ASCII alphanumeric service definitions and lowercase kebab-case operations. Input may be rejected or normalized; an accepted persisted policy must use canonical names. The new tests check the returned stored policy, not merely whether raw input was accepted.

Both implementations reproduce these eight failures:

| Field | Input retained | Architectural issue |
|---|---|---|
| Provider | `lowercase` | Not PascalCase |
| Provider | `bad_provider` | Not PascalCase; underscore |
| Service definition | `Uppercase` | Not camelCase |
| Service definition | `bad_signal` | Underscore |
| Service definition | `bad-signal` | Hyphen |
| Operation | `Uppercase` | Uppercase |
| Operation | `bad_scope` | Underscore |
| Operation | `badScope` | Uppercase; not kebab-case |

The real Go `grantRow` and Rust `authorization::grant` functions were called in isolated source copies. This establishes the component behavior; live HTTP normalization, cross-language operation and migration of pre-existing policies were not tested. Production code remains unchanged.

## Failed test identifiers

| Implementation | Test |
|---|---|
| go | `TestGSoSDCanonicalIdentifiers/NAME-provider-04` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-provider-05` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-target-10` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-target-11` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-target-12` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-scope-16` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-scope-17` |
| go | `TestGSoSDCanonicalIdentifiers/NAME-scope-18` |
| rust | `gsosd_name_provider_04` |
| rust | `gsosd_name_provider_05` |
| rust | `gsosd_name_scope_16` |
| rust | `gsosd_name_scope_17` |
| rust | `gsosd_name_scope_18` |
| rust | `gsosd_name_target_10` |
| rust | `gsosd_name_target_11` |
| rust | `gsosd_name_target_12` |
