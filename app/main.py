from fastapi import FastAPI
from app.models.customer import CustomerData

app = FastAPI(title="Credit Risk API")

@app.get("/health")
def health_check():
    return {"status": "API is running smoothly!"}

@app.post("/predict-risk")
def predict_risk(customer: CustomerData):
    """
    Dummy endpoint to predict credit risk.
    """
    # Simple dummy logic for now
    if customer.credit_history_score < 50 or customer.existing_loans > 2:
        risk = "High"
    elif customer.credit_history_score < 75:
        risk = "Medium"
    else:
        risk = "Low"
    
    return {
        "name": customer.name,
        "risk": risk
    }
