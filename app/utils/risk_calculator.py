# app/utils/risk_calculator.py

def calculate_credit_risk(age: int, income: float, credit_history_score: float, existing_loans: int) -> str:
    """
    Calculate credit risk based on simple rules.
    Returns: 'Low', 'Medium', or 'High'
    """
    risk_score = 0

    # Rule 1: Credit history score
    if credit_history_score < 50:
        risk_score += 3
    elif credit_history_score < 75:
        risk_score += 2
    else:
        risk_score += 1

    # Rule 2: Existing loans
    if existing_loans >= 3:
        risk_score += 3
    elif existing_loans == 2:
        risk_score += 2
    else:
        risk_score += 1

    # Rule 3: Income
    if income < 30000:
        risk_score += 3
    elif income < 60000:
        risk_score += 2
    else:
        risk_score += 1

    # Rule 4: Age (optional)
    if age < 25:
        risk_score += 2
    elif age > 60:
        risk_score += 2
    else:
        risk_score += 1

    # Convert score to risk category
    if risk_score >= 9:
        return "High"
    elif risk_score >= 6:
        return "Medium"
    else:
        return "Low"
