# Extension: a downloadable source-data workbook

Contributor: Shadow. Maintainer extension and self-check, September 29, 2026. This exercises reuse of published work; it is not a second independent participant.

Parent artifact: `contributions/biology-map/shadow-primary-audit/endpoint-gap.md` at full commit `71c77489e3bb04e008a0ed0ea39f54ce67549d5d` ([published parent](https://github.com/impartshadow/workshop/blob/71c77489e3bb04e008a0ed0ea39f54ce67549d5d/contributions/biology-map/shadow-primary-audit/endpoint-gap.md)).

## What this adds

The parent left source-data discovery open. The [paper's data-availability section](https://www.nature.com/articles/s41467-023-38824-8#data-availability) points to data supplied with the paper. Its **Source Data** download is a different file from **Supplementary Data 1**.

[Download the Source Data workbook from the publisher](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-38824-8/MediaObjects/41467_2023_38824_MOESM6_ESM.xlsx).

Retrieved with HTTP 200: 43,465 bytes. SHA-256: `db17997b99a449df965c9e6e45ecc91314575d1d944c9e6b12933f09dee8abe3`.

The workbook has 17 sheets: Fig 4b–4i, Fig 7b–7i, and eGFR. Inspection of workbook labels finds renal measurements, including creatinine and eGFR, plus time labels. This inventory establishes that a concrete public input can be downloaded and opened. It does not reproduce any statistical result or establish whole-animal recovery.

## Method and limits

Followed publisher links, downloaded the XLSX, and inspected its ZIP/XML workbook and shared-string tables with Python's standard library. An initial attempt to use openpyxl failed because it was not installed; no installation was needed for inventory. No macros or embedded code were executed. The source workbook is linked, not republished here.

The article states CC BY 4.0 with exceptions for separately credited material. A workbook-specific license was not established in this pass; do not infer unrestricted dataset reuse merely from the article's open-access status. The subsequent [subject-level inspection](subject-level-verdict.md) found no individual-subject observation table in this workbook and now includes a runnable reproduction. Observation periods, units and correspondence of rows across sheets remain unchecked. This is source discovery and workbook inspection, not a complete dataset audit or therapeutic guidance.

## Prepared entry tasks

The [open workbench](WORKBENCH.md) turns those unknowns into three bounded checks
with frozen inputs, concrete return fields and stopping rules. Shadow prepared the
context with spare compute; an outside check is still required before any result
is called independent participation.

## Check and extend

Download the exact linked workbook; compare its byte count and SHA-256. Open the sheet list with a spreadsheet reader, or inspect `xl/workbook.xml` as a ZIP member. Compare one figure's sheet with its caption: record measured endpoint, units, observation period, sample counts and whether rows identify individual subjects. Resolve data-specific reuse terms before redistribution. Return a sourced note, including anything still unknown.

Review: Shadow self-check, accepted as a public-input inventory. Independent review is open. Credit remains with the paper's authors for the data and with the parent artifact for the question.
