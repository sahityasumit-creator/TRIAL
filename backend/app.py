from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")
def predict(data: Input):
    # placeholder logic
    return {"prediction": data.feature1 + data.feature2}
