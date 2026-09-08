# Methodology

## Scope
CreditWatch is a corporate-credit portfolio analytics prototype. The transparent scorecard is the primary decision-support layer; statistical models are secondary.

## Scorecard
Leverage & Coverage 40%; Profitability & Cash Conversion 25%; Liquidity & Working Capital 20%; Growth & Volatility 15%. Metrics are converted to 0–100 percentile signals rather than arbitrary universal sector thresholds. Internal tiers: Tier 1 85–100, Tier 2 70–84, Tier 3 55–69, Tier 4 40–54, Tier 5 below 40.

## Distress proxy
The project uses a constructed forward deterioration proxy. It is not legal default, bankruptcy, or an agency probability of default.

## Validation
Use time-based train/test splits. Headline metrics include ROC-AUC, KS, precision/recall and calibration; accuracy is not a headline metric for imbalanced distress outcomes.

## Stress testing
Base: no shock. Downside: revenue -10%, EBITDA margin -200 bps, interest +15%, debt +5%. Severe Downside: revenue -20%, EBITDA margin -300 bps, interest +30%, debt +10%.

## Limitations
SEC XBRL concepts vary across issuers; public-company bias is material; private-credit covenants and management information are absent; and the constructed label cannot be treated as observed default.
