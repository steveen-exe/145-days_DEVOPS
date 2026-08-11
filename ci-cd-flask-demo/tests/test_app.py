import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_greet_valid(client):
    resp = client.get("/api/greet/Steve")
    assert resp.status_code == 200
    assert "Steve" in resp.get_json()["message"]


def test_greet_invalid(client):
    resp = client.get("/api/greet/steve123")
    assert resp.status_code == 400