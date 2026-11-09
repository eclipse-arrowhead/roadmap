# Arrowhead 5.2 roadmap update — 30 October 2026

Updated the GSoSD and both white-box design descriptions in their existing locations, with editable LaTeX, bibliographies and vector figures. The white-box documents retain the repository’s existing GSoSDD designation and filenames (the documents requested as SSoSDD). Release identifier 5.2.2 and DRAFT status are retained; amendment revisions are GSoSD 2.1, core GSoSDD 1.1 and support GSoSDD 0.12. No approval record was added.

## Documents

- [GSoSD — core and support systems, 45 pages](Arrowhead%20SoS%20architecture/BlackBox_5.2.2/GSoSD-Core-and-Support-Systems-5.2.2.pdf)
- [Core white-box description, 36 pages](Arrowhead%20SoS%20architecture/WhiteBox_5.2.2/GSoSDD_Arrowhead_Core_Systems_5.2.2.pdf)
- [Support white-box description, 37 pages](Arrowhead%20SoS%20architecture/WhiteBox_5.2.2/GSoSDD_Arrowhead_Support_Systems_5.2.pdf)

## Changes

- Identified Java, Go and Rust primary sources, independent Java/Go packaging and Rust shared-crate dependencies. The current Go tree has 23 modules, including the later configurator; its dated packaging audit covered 22.
- Retained five core implementations while describing the four-core default of a new Java local-cloud design. SimpleStore remains optional and running instances are not implicitly stopped.
- Made every database an integrated private host asset, including external database containers, embedded SQLite and private snapshots. Added an ownership diagram and corrected database classification in the historical deployment diagrams.
- Documented Java LocalCloudConfigurator, graphical local-cloud composition, SoS/PDE composition, orchestration and security-policy editors, plan review, revision guards and operational boundaries.
- Distinguished local-cloud configuration from the SoSConfigurator inter-cloud operations tool. The SoS editor’s browser layout and PDE authority are distinct from persisted local-cloud design positions.
- Qualified dated Java/Go/Rust interoperability claims. Retained the Go native-registry integration failure and Rust compatibility/replacement gates. Packaging test counts are attributed to their reports, not presented as newly executed acceptance tests.
- Distinguished the live Java inventory (44 containers on inspection) from the 24 October historical snapshot. GraphDBManager is an existing deployment extension outside the supplied primary implementation inventories.
- Corrected stale combined-Java-runtime, support-count and CRL statements; kept deprecated SysMonitorPublisher material explicitly historical.
- Restored the missing white-box core bibliography using the retained core bibliography and added current evidence citations. Updated document dates, cross-document revision citations and amendment tables.

## Validation and evidence

All three PDFs were rebuilt with latexmk/BibTeX. Final LaTeX logs have no overfull boxes, unresolved citations/references or errors. All 118 pages were rendered and inspected using contact sheets; new content was also inspected at reading resolution. Non-fatal float-placement and underfull-line notices remain. [Verification evidence](verification/2026-10-30/results.json) includes PDF hashes/page counts, build logs, rendered review sheets, changed-file hashes, evidence-source hashes and the read-only Java runtime inventory.

This was a documentation update. No service implementation or cloud configuration was changed or redeployed; application test suites and mixed-cloud acceptance workloads were not rerun. Implementation claims rely on the cited primary sources and dated evidence.

## Rebuild

Run `latexmk -pdf -interaction=nonstopmode -halt-on-error <document>.tex` inside the corresponding BlackBox_5.2.2 or WhiteBox_5.2.2 directory. Each directory now has the bibliography and figure inputs required for its documents.
