-- Latest borrower risk distribution
SELECT credit_tier,COUNT(*) borrowers FROM credit_scores WHERE fiscal_year=(SELECT MAX(fiscal_year) FROM credit_scores) GROUP BY credit_tier;
-- Highest leverage
SELECT c.company_name,fs.fiscal_year,fr.debt_to_ebitda FROM financial_ratios fr JOIN financial_statements fs ON fs.statement_id=fr.statement_id JOIN companies c ON c.company_id=fs.company_id ORDER BY fr.debt_to_ebitda DESC LIMIT 20;
-- Coverage deterioration
SELECT company_id,fiscal_year,interest_coverage,interest_coverage-LAG(interest_coverage) OVER(PARTITION BY company_id ORDER BY fiscal_year) yoy_change FROM financial_ratios fr JOIN financial_statements fs ON fs.statement_id=fr.statement_id;
-- Early warning distressed borrowers
SELECT c.company_name,e.fiscal_year FROM early_warning_signals e JOIN companies c ON c.company_id=e.company_id WHERE e.ew_state='Distressed';
-- Prediction calibration by outcome
SELECT model_name,actual_distress_flag,AVG(predicted_probability) avg_predicted_probability,COUNT(*) observations FROM risk_predictions GROUP BY model_name,actual_distress_flag;
