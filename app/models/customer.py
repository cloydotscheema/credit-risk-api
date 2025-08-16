# app/models/customer.py
from pydantic import BaseModel

class CustomerData(BaseModel):
    name: str
    age: int
    income: float
    credit_history_score: float
    existing_loans: int
