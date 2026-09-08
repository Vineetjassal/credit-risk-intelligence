import numpy as np
import pandas as pd

def safe_div(a, b):
    a = pd.to_numeric(a, errors='coerce')
    b = pd.to_numeric(b, errors='coerce')
    return a / b.replace(0, np.nan)

def add_ratios(df):
    out = df.copy()
    out['ebitda'] = out['operating_income'] + out['depreciation_amortization']
    out['free_cash_flow'] = out['cfo'] - out['capex']
    out['revenue_growth_yoy'] = out.groupby('company_id')['revenue'].pct_change()
    out['ebitda_margin'] = safe_div(out['ebitda'], out['revenue'])
    out['net_margin'] = safe_div(out['net_income'], out['revenue'])
    out['debt_to_ebitda'] = safe_div(out['total_debt'], out['ebitda'])
    out['net_debt_to_ebitda'] = safe_div(out['total_debt'] - out['cash'], out['ebitda'])
    out['debt_to_equity'] = safe_div(out['total_debt'], out['equity'])
    out['interest_coverage'] = safe_div(out['ebitda'], out['interest_expense'])
    out['current_ratio'] = safe_div(out['current_assets'], out['current_liabilities'])
    out['quick_ratio'] = safe_div(out['cash'] + out['receivables'], out['current_liabilities'])
    out['cfo_to_net_income'] = safe_div(out['cfo'], out['net_income'])
    out['fcf_to_debt'] = safe_div(out['free_cash_flow'], out['total_debt'])
    out['dso'] = safe_div(out['receivables'], out['revenue']) * 365
    out['dio'] = safe_div(out['inventory'], out['cogs']) * 365
    out['dpo'] = safe_div(out['payables'], out['cogs']) * 365
    out['cash_conversion_cycle'] = out['dso'] + out['dio'] - out['dpo']
    return out
