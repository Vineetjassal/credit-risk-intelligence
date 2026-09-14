"""Generate a concise, auditable credit committee memo from model outputs."""
from __future__ import annotations

def build_credit_memo(company: str, score: float, tier: str, pd: float, exposure: float, key_risks: list[str], mitigants: list[str]) -> str:
    risks = "\n".join(f"- {x}" for x in key_risks) or "- None flagged"
    mins = "\n".join(f"- {x}" for x in mitigants) or "- None documented"
    return f"""# Credit Committee Memo — {company}\n\n## Executive view\n- Internal score: **{score:.0f}/100**\n- Risk tier: **{tier}**\n- Indicative 12-month PD: **{pd:.1%}**\n- Exposure: **₹{exposure:,.1f} Cr**\n\n## Key risks\n{risks}\n\n## Mitigants / monitoring actions\n{mins}\n\n## Decision framework\nUse the score, PD, concentration, EWS signals and stress results together. The distress proxy is analytical and should not be interpreted as legal default.\n"""
