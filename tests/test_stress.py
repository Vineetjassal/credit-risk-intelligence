import pandas as pd
from src.stress_testing.scenarios import stress_row
def test_stress():
    out=stress_row(pd.Series({'revenue':1000,'ebitda_margin':.20,'total_debt':400,'interest_expense':40}))
    assert set(out.scenario)=={'Base','Downside','Severe Downside'}
    assert out[out.scenario=='Severe Downside'].revenue.iloc[0]<1000
