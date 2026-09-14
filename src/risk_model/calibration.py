"""Probability calibration diagnostics for credit PD models."""
from __future__ import annotations
import numpy as np

def calibration_table(y_true, pd_pred, bins: int = 10):
    """Build equal-width PD bins with count, predicted PD and observed rate."""
    y = np.asarray(y_true, dtype=float)
    p = np.clip(np.asarray(pd_pred, dtype=float), 0, 1)
    edges = np.linspace(0, 1, bins + 1)
    rows = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (p >= lo) & ((p < hi) if hi < 1 else (p <= hi))
        if mask.any():
            rows.append({"pd_band": f"{lo:.0%}-{hi:.0%}", "count": int(mask.sum()), "predicted_pd": float(p[mask].mean()), "observed_rate": float(y[mask].mean())})
    return rows

def brier_score(y_true, pd_pred) -> float:
    """Mean squared error of predicted probabilities."""
    y = np.asarray(y_true, dtype=float)
    p = np.clip(np.asarray(pd_pred, dtype=float), 0, 1)
    return float(np.mean((p - y) ** 2))
