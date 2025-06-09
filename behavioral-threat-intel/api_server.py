from fastapi import FastAPI
from pydantic import BaseModel
from ai_social_engineering_detector import train_model, DATA_PATH

app = FastAPI(title="AI Social Engineering Detector")
model = train_model(DATA_PATH)

class Email(BaseModel):
    text: str

@app.post("/detect")
def detect_email(email: Email):
    prediction = model.predict([email.text])[0]
    return {"prediction": prediction}

