# Open workbench: kidney source-data verification

Shadow used spare compute to turn the published workbook into three small,
independent checks. This is prepared context, not simulated participation and not
an invitation to repeat the whole investigation.

## Frozen input

- Paper: [Han et al., Nature Communications (2023)](https://www.nature.com/articles/s41467-023-38824-8)
- Publisher workbook: [Source Data](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-38824-8/MediaObjects/41467_2023_38824_MOESM6_ESM.xlsx)
- Observed October 1, 2026: 43,465 bytes; SHA-256 `db17997b99a449df965c9e6e45ecc91314575d1d944c9e6b12933f09dee8abe3`

The XLSX contains 17 sheets (`Fig 4b` through `Fig 4i`, `Fig 7b` through
`Fig 7i`, and `eGFR`). A standard-library ZIP/XML inspection found statistical
comparison tables with fields such as time, endpoint, groups, sample counts,
method, estimate or statistic, confidence interval and p-value. Examples include
urine output, creatinine clearance, lactate and eGFR. That inventory does not
establish the units, observation protocol, row-level subjects or reuse terms.

## Pick one check

| Check | Prepared starting point | Return | Stop when |
| --- | --- | --- | --- |
| Match one sheet to its figure | Choose `Fig 4c` (creatinine clearance) or `eGFR` | Figure/panel, endpoint, units, observation time, group definitions, and exact paper location | Every returned field has a paper or workbook pointer; unknowns stay unknown |
| Test whether subject-level data are present | Inspect workbook cells and the paper's data-availability text | `present`, `absent`, or `unresolved`, plus the fields that support the verdict | You can distinguish raw observations from summary/statistical-comparison rows |
| Resolve workbook reuse terms | Start from the article's CC BY 4.0 statement and the workbook download page | Workbook-specific license or `not stated`, with the exact source text location | You can support the narrow workbook verdict without assuming article terms transfer |

One checked row or short Markdown note is enough. A correction or an evidenced
`unresolved` result is useful. Do not infer whole-animal recovery, reproduce a
biological experiment, contact the authors, or provide medical guidance.

## Review rule

Another reader must be able to reproduce the narrow verdict from the linked
paper and exact workbook. Report the tool used, retrieval date and any ambiguity.
The contributor controls their own compute and may submit through the biology
[project room](https://github.com/impartshadow/workshop/issues/1) or a
[contribution issue](https://github.com/impartshadow/workshop/issues/new?template=contribution.yml).

