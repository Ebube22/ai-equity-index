# Dashboard Guide (Power BI)



Title: Educational Equity Index Dashboard

Subtitle: AI-powered insights into fairness, inspection quality, and local authority performance across the UK



This dashboard provides a simple but powerful view of how fairness, inspection quality, and gender equity vary across Local Authorities (LAs). It combines normalized scores (0–1) into a single Equity Index (0–100) for interpretability.



###### **📊 Dashboard Elements**

###### **KPI Cards (Top Row)**



* Avg. Gender Equity Score → Average of gender\_equity\_index\_refined across all LAs.
* Avg. Fairness Score → Average of fairness\_combined.
* Avg. Inspection Quality Score → Average of inspection\_norm.
* Equity Index (0–100) → Combined index summarizing fairness, inspection, and gender equity. A higher value indicates stronger overall equity.



###### **Line Chart — Fairness vs Inspection Quality by Local Authority**



* X-axis: la\_name (Local Authority)
* Y-axis: Average of fairness\_combined (light blue) and inspection\_norm (dark blue)
* Insight: Compare fairness and inspection quality trends across LAs. Divergences highlight where strong inspection outcomes may not translate into fairness, or vice versa.



###### **Histogram — Equity Index Distribution Across Local Authorities**



* X-axis: Equity Index (0–100), binned
* Y-axis: Number of Local Authorities in each band
* Insight: Shows how equity is distributed nationally. Clusters indicate systemic patterns; long tails highlight outliers.



###### **Scatter Plot — Fairness vs Inspection Quality**



* X-axis: fairness\_combined
* Y-axis: inspection\_norm
* Points: Each Local Authority (colored uniquely for visibility)
* Insight: Highlights the relationship between fairness and inspection. Dense clusters near the diagonal show alignment; off-diagonal points suggest mismatch between fairness and inspection outcomes.



###### **Bar Chart — Top 10 Local Authorities by Equity Index**

* Axis (X): Equity Index (0–100)
* Axis (Y): la\_name (Top 10 LAs)
* Insight: Identifies the leading LAs by combined equity index. Useful for benchmarking and sharing best practices.



#### **How to Use**



* Policymakers: Identify high-performing LAs and areas needing support.
* Researchers: Explore patterns between fairness, gender equity, and inspection outcomes.
* Stakeholders: Use the Equity Index to track progress over time and evaluate the impact of interventions.
