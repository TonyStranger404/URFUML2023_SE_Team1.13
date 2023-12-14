from fastapi.testclient import TestClient

import fast_viktor


client = TestClient(fast_viktor.app)


def test_fas():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"messege": "hello world"}


def test_read_predict():
    data = {"text": "привет мир"}
    response = client.post("/predict/", json=data)

    assert response.status_code == 200
    assert "result" in response.json()
