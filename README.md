# CreditWatch — Corporate Credit Risk Intelligence

A portfolio-grade corporate credit-risk analytics prototype: SEC financial data → cleaning → credit ratios → transparent scorecard → distress probability → early warning → stress testing → SQL analytics → Excel committee model → Streamlit dashboard.

> Distress is a constructed financial-distress proxy, not legal default.

## Implemented
- SEC Company Facts ingestion with descriptive User-Agent
- Defensive XBRL ingestion layer
- 15+ credit ratios
- 4-pillar percentile scorecard and 5 internal risk tiers
- Constructed forward distress proxy
- Logistic Regression PD model utilities with ROC-AUC, KS, precision/recall
- Early-warning signals and risk states
- Base / Downside / Severe Downside stress testing
- SQLite schema and analytical SQL
- Streamlit dashboard with clearly labelled demo mode
- Automated tests

## Run
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