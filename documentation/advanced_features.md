# Advanced CreditWatch Features

The project is designed to evolve from a portfolio prototype into an analyst-style credit intelligence platform.

## Current enhancement set
- Watchlist flagging based on transparent score, PD and covenant rules
- Population Stability Index utility for model monitoring
- Risk-tier portfolio counts
- Covenant breach monitoring
- Data-quality monitoring
- Portfolio concentration and exposure share
- Scenario-adjusted PD and expected loss
- Automated recommended actions

## Next production-grade modules
1. **Financial spreading:** standardized 5-year P&L, balance sheet and cash-flow views.
2. **Trend intelligence:** YoY growth, margin compression, leverage trajectory and liquidity trend charts.
3. **Peer benchmarking:** compare borrowers against industry percentile distributions.
4. **PD/LGD/EAD:** separate probability of default, loss-given-default and exposure-at-default assumptions to calculate EL.
5. **Rating engine:** internal rating grades with transition matrix and rating-watch states.
6. **Covenant engine:** configurable thresholds, headroom, breach dates and remediation status.
7. **Early-warning engine:** multi-factor alert severity, alert history and alert closure workflow.
8. **Watchlist:** analyst-owned queue with priority, reason and next-review date.
9. **Portfolio heatmap:** sector, geography, rating and borrower concentration views.
10. **Model governance:** calibration, PSI, drift, feature coverage and model-version tracking.
11. **Credit memo:** one-click analyst summary covering strengths, weaknesses, risks, mitigants and recommendation.
12. **Audit trail:** record data vintage, model version, scenario, score and decision rationale.
13. **Data refresh:** scheduled SEC ingestion with validation and failure logging.
14. **API layer:** serve validated analytics to the dashboard without exposing credentials in browser code.
15. **Role-based workflow:** analyst, reviewer and committee stages for future deployment.

All demo values should remain clearly labelled synthetic until validated production data is connected.