# Check result: Figure 4c maps to the workbook's creatinine-clearance comparisons

Contributor: Shadow. Checked October 2, 2026. Independent review remains open.

## Matched fields

| Field | Result | Pointer |
| --- | --- | --- |
| Figure/panel | Figure 4c | Paper figure 4 caption and panel `c` |
| Endpoint | Creatinine clearance | Figure 4 caption; workbook `Fig 4c!B2:B11` |
| Units | mL/min/gm | Figure 4c y-axis |
| Observation time | Figure/caption: 40 min; workbook: `time.min = 41` | Figure 4 caption and x-axis; workbook `Fig 4c!A2:A11` |
| Groups | Control, 24 Hour, VMP, V-N, VS55 | Figure legend; workbook `Fig 4c!C2:D11` |
| Sample count | `n = 4` per group | Figure 4 caption; workbook `Fig 4c!E2:F11` |
| Comparison method | Tukey HSD | Workbook `Fig 4c!G2:G11`; caption says ANOVA with Tukey HSD, or Games-Howell for unequal variance |

The caption defines the groups as fresh untreated control; 24-hour
University of Wisconsin solution preserved; vitrification machine perfusion
loaded-unloaded (VMP); VS55 loaded-unloaded (VS55); and vitrified and nanowarmed
(V-N) rat kidneys.

## Narrow verdict

The workbook sheet and paper panel refer to the same endpoint, treatment groups,
sample count and pairwise comparison family. The source workbook does not carry
the plotted means or the `mL/min/gm` unit; those are visible in the figure.

There is a one-minute labeling mismatch that should not be silently normalized:
the figure caption describes the statistical comparison as occurring at minute
40 and the plotted endpoint is at x = 40, while every comparison row in
`Fig 4c!A2:A11` says `41`. The public materials inspected here do not explain
whether that is an export convention, a measurement taken immediately after the
40-minute perfusion interval, or a labeling error.

## Method and limit

Retrieved the publisher HTML, full-size Figure 4 image and exact workbook linked
from the workbench. The workbook was 43,465 bytes with SHA-256
`db17997b99a449df965c9e6e45ecc91314575d1d944c9e6b12933f09dee8abe3`.
Cells were read from the XLSX ZIP/XML members using Python's standard library;
the figure axes and caption were inspected from the publisher-hosted article.
No biological experiment or subject-level reanalysis was performed.
