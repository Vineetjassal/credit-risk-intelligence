import pandas as pd
SCENARIOS={'Base':{'revenue':0,'margin':0,'interest':0,'debt':0},'Downside':{'revenue':-.10,'margin':-.02,'interest':.15,'debt':.05},'Severe Downside':{'revenue':-.20,'margin':-.03,'interest':.30,'debt':.10}}
def stress_row(row):
    records=[]
    for name,s in SCENARIOS.items():
        revenue=row.revenue*(1+s['revenue']); margin=row.ebitda_margin+s['margin']; ebitda=revenue*margin; debt=row.total_debt*(1+s['debt']); interest=row.interest_expense*(1+s['interest'])
        records.append({'scenario':name,'revenue':revenue,'ebitda':ebitda,'debt':debt,'interest_expense':interest,'interest_coverage':ebitda/interest if interest else float('nan'),'debt_to_ebitda':debt/ebitda if ebitda>0 else float('inf')})
    return pd.DataFrame(records)
