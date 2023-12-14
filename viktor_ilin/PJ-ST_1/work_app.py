import streamlit as st
from mtranslate import translate

# Веб-приложение с использованием Streamlit
st.title("Перевод текста с Русского на Английский")

# Получение входного текста от пользователя
input_text = st.text_input("Введите текст для перевода:", "Это твоя первая программа?")

# Генерация перевода при нажатии кнопки
if st.button("Перевести"):
    translation_result = translate(input_text, "en")
    st.text("Результат перевода:")
    st.write(translation_result)
