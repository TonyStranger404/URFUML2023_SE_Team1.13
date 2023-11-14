import streamlit as st
from transformers import pipeline

classifier = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

st.title('Нахождение эмоции в тексте')

txt = st.text_area("Введите текст для анализа:")

button = st.button('Найти эмоцию!')

if button:
    result = classifier(txt)
    st.write(f'Эмоция: {result[0]["label"]}')
    st.write(f'Точность: {result[0]["score"]}')

# Запускать из терминала командой streamlit run Kravtsov_main.py
