import pytest
from app import train_model, predict, load_data

def test_data_loads():
    df = load_data()
    assert df is not None
    assert len(df) > 0

def test_model_trains():
    df = load_data()
    model, accuracy = train_model(df)
    assert model is not None
    assert 0.0 <= accuracy <= 1.0

def test_prediction_approved():
    df = load_data()
    model, _ = train_model(df)
    result = predict(model, age=35, income=60000, loan_amount=20000, credit_score=700, employed=1)
    assert result in ["Approved", "Denied"]

def test_prediction_denied():
    df = load_data()
    model, _ = train_model(df)
    result = predict(model, age=22, income=10000, loan_amount=50000, credit_score=500, employed=0)
    assert result in ["Approved", "Denied"]
