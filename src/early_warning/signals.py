def build_early_warning(df):
    x=df.sort_values(['company_id','fiscal_year']).copy(); g=x.groupby('company_id')
    x['margin_change']=g['ebitda_margin'].diff(); x['coverage_change']=g['interest_coverage'].diff(); x['leverage_change']=g['debt_to_ebitda'].diff()
    x['flag_revenue_decline']=(x.revenue_growth_yoy<0).astype(int)
    x['flag_margin_compression']=(x.margin_change<-.02).astype(int)
    x['flag_rising_leverage']=(x.leverage_change>.5).astype(int)
    x['flag_falling_coverage']=(x.coverage_change<-.5).astype(int)
    x['flag_negative_fcf']=(x.free_cash_flow<0).astype(int)
    x['flag_earnings_quality']=((x.cfo_to_net_income<.8)&(x.net_income>0)).astype(int)
    x['flag_ccc']=(g.cash_conversion_cycle.diff()>10).astype(int)
    flags=[c for c in x if c.startswith('flag_')]; x['ew_risk_score']=x[flags].sum(axis=1)/len(flags)*100
    x['ew_state']=x.ew_risk_score.apply(lambda v:'Healthy' if v<=15 else 'Watchlist' if v<=35 else 'Elevated Risk' if v<=55 else 'High Risk' if v<=75 else 'Distressed')
    return x
