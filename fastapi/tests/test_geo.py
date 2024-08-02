from hypothesis import settings, given, strategies as st
from helpers.geo import calculate_square


@given(
    lat=st.floats(min_value=-90, max_value=90),
    lon=st.floats(min_value=-180, max_value=180),
    distance=st.floats(min_value=1e-5)
)
@settings(max_examples=150)
def test_geo_square(lat, lon, distance):
    print(f"Testing with inputs lat={lat}, lon={lon}, distance={distance}")
    res = calculate_square(lat, lon, distance)
    assert res.min_lat <= lat
    assert res.max_lat >= lat
    assert res.min_lon <= lon
    assert res.max_lon >= lon
