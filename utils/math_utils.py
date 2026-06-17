import math


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value to the inclusive range [lo, hi]."""
    if lo > hi:
        raise ValueError(f"lo ({lo}) must not exceed hi ({hi})")
    return max(lo, min(value, hi))


def round_to(value: float, decimals: int) -> float:
    """Round value to the given number of decimal places."""
    if decimals < 0:
        raise ValueError(f"decimals must be >= 0, got {decimals}")
    return round(value, decimals)


def percentage(part: float, total: float, decimals: int = 2) -> float:
    """Compute part/total * 100, rounded to decimals places."""
    if total == 0:
        raise ZeroDivisionError("total must not be zero")
    return round_to(part / total * 100, decimals)
