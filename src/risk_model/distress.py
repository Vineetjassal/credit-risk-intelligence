import pandas as pd
def make_distress_label(df):
    x=df.sort_values(['company_id','fiscal_year']).copy(); g=x.groupby('company_id')
    x['future_coverage']=g.interest_coverage.shift(-1); x['debt_growth']=g.total_debt.pct_change()
    x['future_negative_fcf']=g.free_cash_flow.shift(-1).lt(0).astype(int)
    x['distress_flag']=((x.future_coverage<1.5).astype(int)+(x.future_negative_fcf).astype(int)+(x.debt_growth>.5).astype(int)>=2).astype(int)
    return x
