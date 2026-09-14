"""Transparent advanced credit-risk calculations for CreditWatch.

These are analytical prototype utilities, not production regulatory models.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RiskComponents:
    pd: float
    lgd: float
    ead: float

    @property
    def expected_loss(self) -> float:
        return self.pd * self.lgd * self.ead

    @property
    def unexpected_loss_proxy(self) -> float:
        # Simple portfolio-style proxy; production models require validated loss data.
        return (self.pd * (1 - self.pd)) ** 0.5 * self.lgd * self.ead


def estimate_lgd(collateral_coverage: float, recovery_rate: float | None = None) -> float:
    """Estimate LGD from collateral coverage or an explicit recovery assumption."""
    if recovery_rate is not None:
        return max(0.0, min(1.0, 1.0 - recovery_rate))
    coverage = max(0.0, min(1.5, collateral_coverage))
    recovery = min(0.9, 0.25 + 0.5 * coverage)
    return max(0.05, 1.0 - recovery)


def estimate_ead(current_exposure: float, undrawn_limit: float = 0.0, ccf: float = 0.5) -> float:
    """Estimate exposure at default using a transparent credit-conversion factor."""
    if current_exposure < 0 or undrawn_limit < 0:
        raise ValueError("exposures cannot be negative")
    return current_exposure + max(0.0, min(1.0, ccf)) * undrawn_limit


def build_rating_migration(current_rating: str, direction: str) -> dict[str, str]:
    """Return a simple one-notch migration view around the current rating."""
    scale = ["AAA", "AA", "A", "BBB", "BB", "B", "CCC", "CC", "C", "D"]
    if current_rating not in scale:
        raise ValueError("unsupported rating")
    i = scale.index(current_rating)
    direction = direction.lower()
    if direction == "upgrade":
        target = scale[max(0, i - 1)]
    elif direction == "downgrade":
        target = scale[min(len(scale) - 1, i + 1)]
    else:
        target = current_rating
    return {"current": current_rating, "one_notch_upgrade": scale[max(0, i - 1)], "one_notch_downgrade": scale[min(len(scale) - 1, i + 1)], "scenario": target}
