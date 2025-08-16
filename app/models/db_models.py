from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    income = Column(Float, nullable=False)
    credit_history_score = Column(Float, nullable=False)
    existing_loans = Column(Integer, nullable=False)
    risk = Column(String, nullable=False)


engine = create_engine("sqlite:///credit_risk.db")
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)
