from hypothesis import given, strategies as st
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


@given(lat = st.floats(), lon = st.floats(), distance = st.floats())
def test_geo_square(lat):
    res = client.get(f"/recommendations/weekdays")

    assert res.status_code == 200
    assert res.json() == {"message": s * s}