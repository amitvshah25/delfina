from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_ratelimit():
    response_list = []
    for req_count in range(0, 5): # make 5 requests to test 200 and 429 statuses
        response_list.append(client.get("/picture"))
    assert response_list[0].status_code == 200 # first response should be success
    assert response_list[0].headers.get("content-type") == "image/jpg" # getting a jpg
    response_codes = map(lambda r: r.status_code, response_list[1:]) # subsequent responses should be 429
    assert list(response_codes) == [429]*4

