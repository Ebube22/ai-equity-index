
Assumptions Register — Educational Equity Index

This register documents the key assumptions made during data preparation, modeling, and dashboard development.

Data Sources

* The refined dataset (`refined_gender_equity_index.csv`) is assumed to have been **pre-cleaned and normalized** prior to dashboard use.
* The Local Authority lookup file (`2223_la_data_revised.csv`) is assumed to provide an **accurate mapping** between LA codes, names, and regions.

Indicators

* Fairness Combined (`fairness_combined`)**: Treated as a normalized value in \[0,1]. No further transformation applied.
* Inspection Norm (`inspection_norm`)**: Treated as normalized in \[0,1]; assumed derived from `positive_proportion`.
* Gender Equity Index Refined (`gender_equity_index_refined`)**: Treated as normalized in \[0,1]; assumed to reflect balanced participation/outcomes across genders.

Equity Index Computation

* The Equity Index is calculated as the **average of available indicators × 100**.
* Equal weighting is assumed for fairness, inspection, and gender equity.
* If any indicator is missing for an LA, the index is based on the average of the remaining available indicators (no penalties for missingness).
* Index values are interpreted on a **0–100 scale** (higher = more equitable).

Data Handling

* Duplicate columns (`Local authority` vs `la_name`) are assumed to be harmless; `la_name` is preferred for reporting.
* Missing values are assumed rare; when present, they are ignored in the computation (row remains valid if at least one indicator is available).
* Outliers are assumed to have been addressed during the creation of the refined dataset; no additional outlier filtering applied in Power BI.

Limitations

* The index does not currently adjust for socio-economic or contextual factors beyond gender and inspection quality.
* Weighting all indicators equally may not reflect their true importance; this is a deliberate choice for **transparency and simplicity**.
* Regional disparities are visible, but subgroup fairness (e.g., rural vs urban, public vs private) is not explicitly modeled in this version.

Governance

* All assumptions are **documented here** to ensure transparency for reviewers and stakeholders.
* Future updates will revise this register as additional indicators or weighting schemes are introduced.


