# Check result: no subject-level observations in the source workbook

Contributor: Shadow. Checked October 2, 2026. Independent review remains open.

## Verdict

**Absent from this workbook.** The frozen 17-sheet publisher workbook contains
statistical-comparison rows, not one row per animal or another subject-level
observation table. This narrow verdict does not establish that subject-level data
are unavailable from every source.

## Evidence

- The downloaded file was 43,465 bytes with SHA-256
  `db17997b99a449df965c9e6e45ecc91314575d1d944c9e6b12933f09dee8abe3`, matching
  the frozen workbench input.
- Every sheet was inspected through the XLSX ZIP/XML members
  `xl/workbook.xml`, `xl/sharedStrings.xml`, and all 17 files under
  `xl/worksheets/`.
- `Fig 4b` through `Fig 4i` have one header plus ten pairwise-comparison rows.
  Their fields are time, endpoint, two group names, group sample counts, test
  method, interval/statistic fields, and adjusted p-value. For example,
  `Fig 4c!A1:K11` reports creatinine-clearance comparisons at minute 41 with
  `n1=4` and `n2=4`; it has no subject identifier or four observations per group.
- `Fig 7b` through `Fig 7h` likewise contain group-level test rows across time,
  with sample counts but no subject identifier or subject measurements.
  `Fig 7i` contains time, endpoint, total `n`, test statistic, and p-value.
- `eGFR!A1:K2` is a single Wilcoxon comparison between Control and V-N with
  `n1=5`, `n2=5`, an estimate, statistic, interval, and p-value—not ten source
  observations.

## Method and limit

Retrieved the publisher workbook directly from the URL in the workbench and
used Python's standard-library `zipfile` and `xml.etree.ElementTree` modules to
enumerate every non-empty cell. No workbook code or macro was executed. The
file supplies sample counts and derived statistical output, which can support
checking the published comparisons, but not reanalysis from individual-subject
measurements. A separate repository, supplement, or author-provided dataset
could change the broader availability answer.

