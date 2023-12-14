from fastapi.testclient import TestClient
from Chashnikov_fastAPI import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "programm start"}

def test_predict_translate1():
    response = client.post("/predict/", json={"text": "Where are you from?"})
    json_data = response.json()
    #print(json_data)
    assert response.status_code == 200
    assert json_data['translation_text'] == 'Откуда ты?'

def test_predict_translate2():
    response = client.post("/predict/", json={"text": "I will be an excellent engineer."})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == "Я буду отличным инженером."

