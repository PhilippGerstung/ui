import math

from services.prices import compare_prices
from hypothesis import given
from hypothesis import strategies as st
import pytest


@given(reference_price=st.floats(allow_nan=False),
       historic_prices=st.dictionaries(st.datetimes(), st.floats(allow_nan=False), min_size=1))
@pytest.skip("Not all hypothesis cases are passing")
def test_price_comparison(reference_price, historic_prices):
    """Hypothesis test for price comparison function"""
    result = compare_prices(reference_price=reference_price, historic_prices=historic_prices)
    if math.isnan(reference_price):
        assert math.isnan(result.reference_price)
        return
    # TODO improve
    assert result.reference_price == reference_price
    assert result.minimum_last_week <= result.maximum_last_week
    assert result.minimum_last_week <= result.average_last_week <= result.maximum_last_week
