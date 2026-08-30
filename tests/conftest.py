import pytest
from fastapi.testclient import TestClient
import subprocess
from app.main import app


@pytest.fixture
def client():
    subprocess.run(
        ["dvc", "pull", "models/model.joblib"],
        check=True
    )
    return TestClient(app)
