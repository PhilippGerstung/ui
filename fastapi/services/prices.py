import math
from datetime import datetime
from typing import Dict

from models.prices import PriceComparisonResult


def compare_prices(reference_price: float, historic_prices: Dict[datetime, float]) -> PriceComparisonResult:
    """
    Compares the reference price to the historic prices from duckdb
    Args:
        reference_price: current price
        historic_prices: historic prices

    Returns:
        PriceComparisonResult
    """
    historic_prices_values = historic_prices.values()
    # Check that we have at least one price except NaN
    if len(historic_prices_values) == 0 or all([math.isnan(price) for price in historic_prices_values]):
        return PriceComparisonResult(
            reference_price=reference_price,
            minimum_last_week=float("nan"),
            maximum_last_week=float("nan"),
            average_last_week=float("nan")
        )

    minimum_last_week = min(historic_prices_values)
    maximum_last_week = max(historic_prices_values)
    average_last_week = sum(historic_prices_values) / len(historic_prices_values)
    return PriceComparisonResult(
        reference_price=reference_price,
        minimum_last_week=minimum_last_week,
        maximum_last_week=maximum_last_week,
        average_last_week=average_last_week
    )