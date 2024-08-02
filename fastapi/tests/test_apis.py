from hypothesis import given, strategies as st
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_geo_square():
    res = client.get(f"/recommendations/weekdays")

    assert res.status_code == 200
