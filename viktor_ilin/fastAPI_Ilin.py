from fastapi import FastAPI
from pydantic import BaseModel
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

app = FastAPI()


class Item(BaseModel):
    text: str


mname = "facebook/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(mname)
model = FSMTForConditionalGeneration.from_pretrained(mname)


@app.post("/predict/")
async def interpreter(item: Item):
    input_ids = tokenizer.encode(item.text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"result": decoded}
