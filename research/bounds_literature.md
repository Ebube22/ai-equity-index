Research-Backed Bounds

Great question — the **Bounds Literature** doc is where you show reviewers (and future collaborators) that you didn’t just pick numbers arbitrarily. Even though your refined dataset already contains normalized 0–1 values, you should still record **theoretical or policy-backed ranges** for transparency.

Here’s a professional draft for `research/bounds_literature.md`:

Bounds Literature — Educational Equity Index

This document summarizes the rationale for bounding and normalizing indicators included in the **Educational Equity Index**.
Although the refined dataset is already normalized to \[0,1], it is important to document the theoretical bounds and sources for reproducibility and transparency.

Indicators and Bounds

| Indicator                                                       | Bound Applied | Justification / Literature                                                                                                                                                                  |
| --------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fairness Combined (`fairness_combined`)**                     | 0.0 – 1.0     | Constructed as a composite normalized score. By definition, a fairness index is constrained to the unit interval. Comparable to fairness measures used in educational studies (OECD, 2018). |
| **Inspection Quality (`inspection_norm`)**                      | 0.0 – 1.0     | Derived from `positive_proportion` of Ofsted outcomes, which are proportions bounded between 0 and 1. Scaled version is therefore naturally in \[0,1].                                      |
| **Gender Equity Index Refined (`gender_equity_index_refined`)** | 0.0 – 1.0     | Represents gender balance/equity. As with gender parity indices in UNESCO/World Bank reports, values are normalized to the unit interval.                                                   |
| **Equity Index (computed)**                                     | 0 – 100       | Rescaled version of the three normalized components. This is a design choice to make the score more interpretable by policymakers and non-technical audiences.                              |

Key Assumptions

* Indicators are **already normalized** in the refined dataset, meaning no additional clamping/scaling was required at the dashboard stage.
* Normalization ensures comparability across heterogeneous metrics (e.g., fairness vs inspection).
* The **0–100 rescale** was chosen because it aligns with policy communication standards (e.g., performance indexes, inspection scores).

References

* OECD (2018). *Equity in Education: Breaking Down Barriers to Social Mobility*.
* UNESCO Institute for Statistics (UIS) — *Gender Parity Index methodology*.
* Ofsted (UK) — *Inspection outcomes framework*.

