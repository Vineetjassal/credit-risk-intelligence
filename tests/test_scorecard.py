import pandas as pd
from src.risk_model.scorecard import score_company
def test_scorecard():
    df=pd.DataFrame({'company_id':[1,2,3],'debt_to_ebitda':[1,3,6],'net_debt_to_ebitda':[.5,2,5],'interest_coverage':[8,3,1],'ebitda_margin':[.30,.20,.05],'net_margin':[.15,.08,-.05],'cfo_to_net_income':[1.2,1,.4],'fcf_to_debt':[.15,.08,-.02],'current_ratio':[2,1.4,.7],'quick_ratio':[1.8,1,.4],'cash_conversion_cycle':[20,50,100],'revenue_growth_yoy':[.10,.02,-.15]})
    out=score_company(df); assert out.composite_score.between(0,100).all(); assert out.credit_tier.notna().all()
