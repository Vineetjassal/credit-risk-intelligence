"""Portfolio-grade monitoring utilities for CreditWatch scorecards."""
from __future__ import annotations

import math
from typing import Iterable


def population_stability_index(expected: Iterable[float], actual: Iterable[float], eps: float = 1e-6) -> float:
    """Calculate PSI for two already-normalized distributions."""
    e, a = list(expected), list(actual)
    if len(e) != len(a) or not e:
        raise ValueError("expected and actual must have the same non-zero length")
    return sum((x - y) * math.log((x + eps) / (y + eps)) for x, y in zip(e, a))


def risk_tier_counts(tiers: Iterable[str]) -> dict[str, int]:
    """Return counts by internal risk tier."""
    out: dict[str, int] = {}
    for tier in tiers:
        out[tier] = out.get(tier, 0) + 1
    return out


def watchlist_flag(score: float, pd: float, covenant_breach: bool = False) -> bool:
    """Simple transparent watchlist rule for analyst review."""
    return bool(covenant_breach or score < 50 or pd >= 0.15)
