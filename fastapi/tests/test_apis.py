from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_geo_square():
    res = client.get("/recommendations/weekdays")

    assert res.status_code == 200
