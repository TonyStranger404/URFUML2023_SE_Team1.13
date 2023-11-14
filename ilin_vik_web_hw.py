# pip install transformers
# pip install sacremoses
# pip install streamlit
# conda install pytorch torchvision torchaudio -c pytorch / данная библиотека предварительно собрана для Mac(M1/M2) на Arme64
# Необходимо, чтоб conda была установлена уже
# pip install watchdog - отслеживает изменение в коде и автоматически перезапускает его

import streamlit as st
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

# Загрузка модели и токенизатора
mname = "facebook/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(mname)
model = FSMTForConditionalGeneration.from_pretrained(mname)


# Определение функции для генерации перевода
def generate_translation(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded


# Веб-приложение с использованием Streamlit
st.title("Перевод текста с Русского на Английский")

# Получение входного текста от пользователя
input_text = st.text_input("Введите текст для перевода:", "Это твоя первая программа?")

# Генерация перевода при нажатии кнопки
if st.button("Перевести"):
    translation_result = generate_translation(input_text)
    st.text("Результат перевода:")
    st.write(translation_result)

# Запускаем из командной строки
# streamlit run ilin_vik_web_hw.py
