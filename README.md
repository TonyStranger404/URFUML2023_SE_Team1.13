# URFUML2023_SE_Team1.13

Created by:  
Kravtsov A.V.  
ilin v.  
Salov A.S.  
Chashnikov S.

---

Инструкция Kravtsov_main.py:

1. Установить зависимости transformers и streamlit
2. Запустить скрипт из терминала командой streamlit run Kravtsov_main.py

Приложение предназначено для определения доминирующей эмоции в тексте. Создано на основе модели "seara/rubert-tiny2-ru-go-emotions".

---

Инструкция ilin_vik_web_hw2.py

Это преложение предназначена для перевода тескта с русского на английский.
Даное приложение запускается с помощью Streamlit фреймворк для создания веб-приложений
Для запуска вам потребуется установить библиотеки
Вы можете установить все библиотеки с файла requirements.txt
командой: pip install -r requirements.txt

Либо по отдельности
pip install transformers
pip install sacremoses
pip install streamlit
pip install torch
pip install watchdog - отслеживает изменение в коде и автоматически перезапускает его(Не обязательно ни как не влияет на работу приложения)

запуск приложение можно из терминала командой: streamlit run ilin_vik_web_hw.py

---

Инструкция Chashnikov.py

Приложение предназначено для перевода текста с английского на русский. Создано на основе модели 'Helsinki-NLP/opus-mt-en-ru'.
Для запуска требуется установка transformers и streamlit
