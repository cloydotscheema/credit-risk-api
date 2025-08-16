from fastapi import FastAPI
from app.models.customer import CustomerData
from app.utils.risk_calculator import calculate_credit_risk

app = FastAPI(title="Credit Risk API")

@app.get("/health")
def health_check():
    return {"status": "API is running smoothly!"}

@app.post("/predict-risk")
def predict_risk(customer: CustomerData):
    """
    Real logic.
    """
    risk = calculate_credit_risk(
        age=customer.age,
        income=customer.income,
        credit_history_score=customer.credit_history_score,
        existing_loans=customer.existing_loans
    )
    
    return {
        "name": customer.name,
        "risk": risk
    }
