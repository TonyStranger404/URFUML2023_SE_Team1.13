# Программа переводчик с англ. на русский
# Импортируем библиотеки
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

# Создаем класс с полем текста, который будем переводить
class Item(BaseModel):
    text: str

# Создаем объект FastAPI и переводчик на основе пайплайна с названием модели
app = FastAPI()
translator = pipeline("translation_en_to_ru", "Helsinki-NLP/opus-mt-en-ru")

# Декоратор, который указывает при каком запросе нужно вызывать функцию
@app.get("/")
def root():
    return {"message": "programm start"}

# Декоратор метода и его функция переводчика
@app.post("/predict/")
def predict(item: Item):
    return translator(item.text)[0]

