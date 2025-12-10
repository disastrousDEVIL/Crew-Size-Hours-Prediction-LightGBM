from fastapi import FastAPI
from app.schemas import JobFeatures, PredictionResponse
from app.predict import predict_requirements

app = FastAPI(title="Crew Size & Hours Prediction API")

@app.get("/")
def root():
    return {"message": "Crew Size and Hours Prediction API is live!"}

@app.post("/predict", response_model=PredictionResponse)
def predict_job(data: JobFeatures):
    result = predict_requirements(data.dict())
    return result
