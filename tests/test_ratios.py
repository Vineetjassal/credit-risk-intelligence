import pandas as pd
from src.financial_analysis.ratios import add_ratios
def test_ratio_engine():
    df=pd.DataFrame([{'company_id':1,'revenue':1000,'operating_income':150,'depreciation_amortization':50,'net_income':80,'total_debt':600,'cash':100,'equity':500,'interest_expense':50,'current_assets':300,'current_liabilities':200,'receivables':100,'inventory':80,'payables':70,'cogs':550,'cfo':120,'capex':40}])
    out=add_ratios(df); assert round(out.debt_to_ebitda.iloc[0],4)==3; assert round(out.interest_coverage.iloc[0],4)==4; assert out.free_cash_flow.iloc[0]==80
