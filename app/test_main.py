from fastapi.testclient import TestClient
from .main import app
import pytest
import time

client = TestClient(app)

@pytest.fixture
def wait_between_tests():
    time.sleep(1) # this resets the ratelimit before running test_ratelimit

def test_picture():
    response = client.get("/picture")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "image/jpg"

def test_ratelimit(wait_between_tests):
    response_list = []
    for req_count in range(0, 5):
        response_list.append(client.get("/picture"))
    assert response_list[0].status_code == 200
    assert response_list[0].headers.get("content-type") == "image/jpg"
    response_codes = map(lambda r: r.status_code, response_list[1:])
    assert list(response_codes) == [429]*4
