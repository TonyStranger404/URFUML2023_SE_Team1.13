from transformers import pipeline

classifier = pipeline("sentiment-analysis",
                      "blanchefort/rubert-base-cased-sentiment")

print("\t\t\tPROGRAMM START")
classifier("Я обожаю инженерию машинного обучения!")
print("\n\t\t\tPROGRAMM END")
