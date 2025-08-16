from fastapi import FastAPI
from app.models.customer import CustomerData
from app.utils.risk_calculator import calculate_credit_risk
from app.models.db_models import SessionLocal, PredictionLog
from typing import List


app = FastAPI(title="Credit Risk API")


@app.get("/health")
def health_check():
    return {"status": "API is running smoothly!"}


@app.post("/predict-risk")
def predict_risk(customer: CustomerData):

    # Risk ka logic
    risk = calculate_credit_risk(
        age=customer.age,
        income=customer.income,
        credit_history_score=customer.credit_history_score,
        existing_loans=customer.existing_loans
    )

    # Log prediction to db
    db = SessionLocal()
    log_entry = PredictionLog(
        name=customer.name,
        age=customer.age,
        income=customer.income,
        credit_history_score=customer.credit_history_score,
        existing_loans=customer.existing_loans,
        risk=risk
    )
    db.add(log_entry)
    db.commit()
    db.close()

    return {
        "name": customer.name,
        "risk": risk
    }


@app.get("/prediction-history")
def get_prediction_history():
    db = SessionLocal()
    logs = db.query(PredictionLog).all()
    db.close()

    # Convert ORM objects to dicts
    history = []
    for log in logs:
        history.append({
            "id": log.id,
            "name": log.name,
            "age": log.age,
            "income": log.income,
            "credit_history_score": log.credit_history_score,
            "existing_loans": log.existing_loans,
            "risk": log.risk
        })

    return {"history": history}
