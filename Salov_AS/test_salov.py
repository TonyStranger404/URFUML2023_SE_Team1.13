from fastapi.testclient import TestClient
from Salov_HW3_FastApi import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "programm start, input your text"}


def test__translate_first():
    response = client.post("/predict/", json={"text": "Как у тебя дела?"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == 'How are you doing?'


def test_translate_second():
    response = client.post("/predict/", json={"text": "Проверка перевода"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == "Translation check"
