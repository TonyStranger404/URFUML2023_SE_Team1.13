!pip install transformers
from transformers import pipeline

classifier = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

classifier("Привет, ты мне нравишься!")