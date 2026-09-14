"""Portfolio-level credit analytics utilities."""
from __future__ import annotations
import pandas as pd

def concentration_table(df: pd.DataFrame, exposure_col: str = "exposure") -> pd.DataFrame:
    """Return exposure share and cumulative concentration by obligor."""
    out = df[[c for c in df.columns if c != exposure_col] + [exposure_col]].copy()
    out = out.sort_values(exposure_col, ascending=False).reset_index(drop=True)
    total = out[exposure_col].sum()
    out["exposure_share"] = out[exposure_col] / total if total else 0.0
    out["cumulative_share"] = out["exposure_share"].cumsum()
    return out

def top_n_share(df: pd.DataFrame, n: int = 10, exposure_col: str = "exposure") -> float:
    """Exposure share represented by the largest n obligors."""
    if df.empty or df[exposure_col].sum() == 0:
        return 0.0
    return float(df.nlargest(n, exposure_col)[exposure_col].sum() / df[exposure_col].sum())

def weighted_pd(df: pd.DataFrame, pd_col: str = "pd", exposure_col: str = "exposure") -> float:
    """Exposure-weighted PD across a portfolio."""
    total = df[exposure_col].sum()
    return float((df[pd_col] * df[exposure_col]).sum() / total) if total else 0.0
