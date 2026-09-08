import pandas as pd
PILLARS={'leverage_coverage':(['debt_to_ebitda','net_debt_to_ebitda','interest_coverage'],.40,[0,0,1]),'profitability_cash':(['ebitda_margin','net_margin','cfo_to_net_income','fcf_to_debt'],.25,[1,1,1,1]),'liquidity_working_capital':(['current_ratio','quick_ratio','cash_conversion_cycle'],.20,[1,1,0]),'growth_volatility':(['revenue_growth_yoy','ebitda_margin'],.15,[1,1])}
def _score(s,higher):
    r=s.rank(pct=True); return 100*r if higher else 100*(1-r)
def score_company(df):
    out=df.copy()
    for name,(features,w,directions) in PILLARS.items():
        parts=[_score(out[f],bool(d)) for f,d in zip(features,directions) if f in out]
        out[name]=pd.concat(parts,axis=1).mean(axis=1,skipna=True)
    out['composite_score']=sum(out[p]*w for p,(_,w,_) in PILLARS.items())
    out['credit_tier']=pd.cut(out['composite_score'],[-1,40,55,70,85,101],labels=['Tier 5','Tier 4','Tier 3','Tier 2','Tier 1'])
    return out
