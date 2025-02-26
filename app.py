from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Define FastAPI app
app = FastAPI()

# Request body model
class PredictionRequest(BaseModel):
    instances: list

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictionRequest):
    response = requests.post(
        "http://127.0.0.1:1234/invocations", 
        json={"instances": request.instances}
    )
    return response.json()

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}
