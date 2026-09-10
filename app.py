# student-ml-api: simple prediction service exposing /health and /predict
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="student-ml-api")

APP_NAME = "student-ml-api"


def get_version():
    """Read the version from the VERSION file so the API and the
    Docker image always report a consistent, single source of truth."""
    version_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "VERSION")
    try:
        with open(version_path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"


class PredictRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "version": get_version(),
    }


@app.post("/predict")
def predict(request: PredictRequest):
    prediction = request.value * 2  # simple placeholder "model"
    return {"input": request.value, "prediction": prediction}
