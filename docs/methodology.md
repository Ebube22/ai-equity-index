
Methodology — Educational Equity Index

Objective

The Educational Equity Index provides a **0–100 score** that summarizes fairness, inspection quality, and gender equity across Local Authorities (LAs). The aim is to make equity measurable, comparable, and actionable for policy and research stakeholders.

Data Sources

This project uses two key datasets:

1. Refined Gender Equity Index (`refined_gender_equity_index.csv`)

   * Processed dataset produced by our modelling pipeline.
   * Contains fairness, inspection, and gender equity indicators already normalized to \[0,1].
   * Grain: one row per Local Authority.

2. Local Authority Lookup (`2223_la_data_revised.csv`)

   * Metadata for Local Authorities.
   * Ensures consistent **LA codes (`new_la_code`)**, names (`la_name`), and region assignments (`region_name`).
   * Used for joining and validation.

 Indicators

The refined dataset contains three core indicators:

* Fairness Combined (`fairness_combined`) — Composite fairness score, normalized \[0,1].
* Inspection Quality (`inspection_norm`) — Normalized inspection outcome, scaled from `positive_proportion`.
* Gender Equity Refined (`gender_equity_index_refined`) — Refined gender balance measure, normalized \[0,1].

Normalization & Bounds

* All indicators are constrained to \[0,1].
* Out-of-range values are clamped (min = 0, max = 1).
* Since the refined dataset is already normalized, no additional scaling is required in Power BI.

Equity Index Computation

The Equity Index (0–100) is computed in Power BI as:

EquityIndex = 100 \times \frac{\text{fairness\_combined} + \text{inspection\_norm} + \text{gender\_equity\_index\_refined}}{\text{count of non-blank indicators}}

* Each LA’s index is the average of available indicators × 100.
* Missing values are ignored (only present indicators are averaged).
* Result: integer values in the range **0–100**.


Validation

* Distribution check:** Histogram shows spread of the Equity Index across LAs.
* Relationship check:** Scatter of `fairness_combined` vs `inspection_norm` highlights where fairness and inspection diverge.
* Ranking check:** Top 10 LA chart confirms the Equity Index produces interpretable leaders.

Interpretation Bands

* 0–39:  Low equity
* 40–59: Moderate equity
* 60–79: Good equity
* 80–100:High equity

Limitations

* Restricted to three indicators in this version. Additional access and socioeconomic metrics are not yet included.
* Equal weighting is applied; alternative weightings (expert- or data-driven) may change rankings.
* Dependent on quality of input data from DfE and Ofsted.

Future Enhancements

* Incorporate longitudinal data to track progress across years.
* Extend indicators (e.g., digital access, household income, infrastructure).
* Add fairness audits for subgroups (urban vs rural, public vs private).
* Automate data refreshes into Power BI.

