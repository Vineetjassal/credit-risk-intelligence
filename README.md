# CreditWatch — Corporate Credit Risk Intelligence

A portfolio-grade corporate credit-risk intelligence prototype: SEC financial data → normalization → credit ratios → transparent scorecard → distress probability → early warning → stress testing → portfolio analytics → SQL → credit committee memo → Streamlit dashboard → GitHub Pages static dashboard.

> Distress is a constructed financial-distress proxy, not legal default.

## Implemented
- SEC Company Facts ingestion with descriptive User-Agent
- Defensive XBRL ingestion layer
- 15+ credit ratios
- 4-pillar percentile scorecard and 5 internal risk tiers
- Constructed forward distress proxy
- Logistic Regression PD model utilities with ROC-AUC, KS, precision/recall
- PD calibration diagnostics and Brier score
- Early-warning signals and risk states
- Base / Downside / Severe Downside stress testing
- Portfolio concentration and exposure-weighted PD analytics
- SQLite schema and analytical SQL
- Credit committee memo generator
- Streamlit dashboard with clearly labelled demo mode
- Responsive static CreditWatch dashboard for GitHub Pages
- GitHub Actions CI and Pages deployment workflow
- Automated tests

## Live static dashboard
The Pages deployment is configured through `.github/workflows/deploy-pages.yml` and publishes `site/` on pushes to `main`. If Pages is enabled for the repository, the expected URL is:

`https://vineetjassal.github.io/credit-risk-intelligence/`

GitHub Pages cannot execute Streamlit/Python. The static site therefore uses synthetic demo data and is designed as a portfolio-facing monitoring UI; production data should be precomputed and validated by the Python pipeline.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
streamlit run dashboard/app.py
```

For SEC ingestion, set `SEC_USER_AGENT` to a real descriptive contact string and run:
```bash
python -m src.data_ingestion.sec_ingest --ciks 320193,1652044
```

See `documentation/methodology.md` for methodology and limitations.