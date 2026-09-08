import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,precision_score,recall_score
FEATURES=['debt_to_ebitda','net_debt_to_ebitda','interest_coverage','ebitda_margin','current_ratio','quick_ratio','cfo_to_net_income','fcf_to_debt','revenue_growth_yoy']
def ks_statistic(y,p):
    x=pd.DataFrame({'y':y,'p':p}).sort_values('p'); bad=(x.y==1).sum(); good=(x.y==0).sum()
    if not bad or not good:return np.nan
    return float(np.max(np.abs((x.y==1).cumsum()/bad-(x.y==0).cumsum()/good)))
def fit_logistic(train):
    cols=[c for c in FEATURES if c in train.columns]; d=train.dropna(subset=cols+['distress_flag'])
    m=Pipeline([('scale',StandardScaler()),('logit',LogisticRegression(class_weight='balanced',max_iter=2000))]); m.fit(d[cols],d.distress_flag); return m,cols
def evaluate(model,test,cols):
    d=test.dropna(subset=cols+['distress_flag']); p=model.predict_proba(d[cols])[:,1]; y=d.distress_flag
    return {'roc_auc':roc_auc_score(y,p) if y.nunique()>1 else np.nan,'ks':ks_statistic(y,p),'precision':precision_score(y,p>=.5,zero_division=0),'recall':recall_score(y,p>=.5,zero_division=0),'n':len(d)}
