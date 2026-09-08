import streamlit as st
import pandas as pd
import numpy as np
from src.financial_analysis.ratios import add_ratios
from src.risk_model.scorecard import score_company
from src.early_warning.signals import build_early_warning
from src.stress_testing.scenarios import stress_row
st.set_page_config(page_title='CreditWatch',layout='wide')
st.title('CreditWatch — Corporate Credit Risk Intelligence')
st.caption('Portfolio prototype • constructed distress is a proxy, not legal default')
def demo_data():
    rng=np.random.default_rng(42); rows=[]
    for i,c in enumerate(['Atlas Manufacturing','Northstar Retail','Pioneer Software','Summit Energy','Harbor Logistics']):
        for y in range(2020,2025):
            revenue=1000+i*180+(y-2020)*70+rng.normal(0,25); margin=.18-i*.015+rng.normal(0,.01)
            rows.append({'company_id':i+1,'company_name':c,'fiscal_year':y,'revenue':revenue,'operating_income':revenue*margin-30,'depreciation_amortization':30,'net_income':revenue*.07,'total_debt':300+i*60,'cash':100,'equity':700+i*80,'interest_expense':30+i*7,'current_assets':350,'current_liabilities':250,'receivables':130,'inventory':100,'payables':90,'cogs':revenue*.55,'cfo':revenue*.09,'capex':revenue*.04})
    return pd.DataFrame(rows)
df=build_early_warning(score_company(add_ratios(demo_data())))
company=st.selectbox('Company',sorted(df.company_name.unique())); latest=df[df.company_name==company].sort_values('fiscal_year').iloc[-1]
a,b,c,d=st.columns(4); a.metric('Internal Tier',str(latest.credit_tier)); b.metric('Composite Score',f'{latest.composite_score:.1f}'); c.metric('Interest Coverage',f'{latest.interest_coverage:.2f}x'); d.metric('EW State',str(latest.ew_state))
st.subheader('Financial trend'); trend=df[df.company_name==company]; st.line_chart(trend.set_index('fiscal_year')[['revenue','ebitda_margin','debt_to_ebitda','interest_coverage']])
st.subheader('Stress test'); st.dataframe(stress_row(latest),use_container_width=True)
st.info('Demo mode uses generated fixtures only to validate the application. Do not use demo figures as credit conclusions.')
