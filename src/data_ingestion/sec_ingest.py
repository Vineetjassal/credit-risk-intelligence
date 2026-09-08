import argparse,os,time
from pathlib import Path
import requests
BASE='https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json'
def fetch_companyfacts(cik,user_agent,out_dir='data/raw'):
    if not user_agent or 'example.com' in user_agent.lower(): raise ValueError('Set SEC_USER_AGENT to a real descriptive contact string.')
    r=requests.get(BASE.format(cik=cik),headers={'User-Agent':user_agent},timeout=30); r.raise_for_status()
    Path(out_dir).mkdir(parents=True,exist_ok=True); path=Path(out_dir)/f'companyfacts_{cik:010d}.json'; path.write_text(r.text); time.sleep(.15); return path
def main():
    p=argparse.ArgumentParser(); p.add_argument('--ciks',required=True); p.add_argument('--user-agent',default=os.getenv('SEC_USER_AGENT')); a=p.parse_args()
    for cik in a.ciks.split(','): print(fetch_companyfacts(int(cik.strip()),a.user_agent))
if __name__=='__main__': main()
