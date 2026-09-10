import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["application"] == "student-ml-api"


def test_predict_success():
    response = client.post("/predict", json={"value": 10})
    data = response.json()
    assert response.status_code == 200
    assert data["input"] == 10
    assert data["prediction"] == 20


def test_predict_missing_input():
    # FastAPI/Pydantic returns 422 Unprocessable Entity for a body
    # that fails schema validation (missing required field).
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "not-a-number"})
    assert response.status_code == 422
