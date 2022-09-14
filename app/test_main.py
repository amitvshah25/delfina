from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_picture():
    response = client.get("/picture")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "image/jpg"
