# Translator from RU to ENG
# Imports
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")


@app.get("/")
def root():
    return {"message": "programm start, input your text"}


@app.post("/predict/")
def predict(item: Item):
    return translator(item.text)[0]
