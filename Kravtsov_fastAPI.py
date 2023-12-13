from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()

classifier = pipeline(model="seara/rubert-tiny2-ru-go-emotions")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)

# Запускать командой из терминала uvicorn Kravtsov_fastAPI:app
#
# Запрос: curl -X POST http://127.0.0.1:8000/predict/ -H 'Content-Type: application/json' -d '{"text": "I hate machine learning engineering!"}'
#