from transformers import MarianMTModel, MarianTokenizer

# Инициализация предобученной модели и токенизатора
model_name = "Helsinki-NLP/opus-mt-ru-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Текст для перевода
text_ru = "Привет, как дела?"

# Получение перевода
translated_text = model.generate(**tokenizer(text_ru, return_tensors="pt"))
translated_text = tokenizer.decode(translated_text[0], skip_special_tokens=True)

print("Перевод на английский:", translated_text)
