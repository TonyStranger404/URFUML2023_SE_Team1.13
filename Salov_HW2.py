import io
import streamlit as st
from transformers import pipeline

st.title(' Переводчик с русского на английский ')

res = st.text_input('Пожалуйста введите текст')

en_ru_translator = pipeline("translation_en_to_ru", 'Helsinki-NLP/opus-mt-ru-en')
trans = en_ru_translator(res)
st.write('Перевод')
for i in trans:
    st.write(i['translation_text'])
