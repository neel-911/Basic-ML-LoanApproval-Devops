import pytest
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import load_data, train_model, predict, save_model

class TestDataLoading:
    def test_data_loads_successfully(self):
        df = load_data()
        assert df is not None
        assert len(df) > 0

    def test_data_has_required_columns(self):
        df = load_data()
        required_cols = ['age', 'income', 'loan_amount', 'credit_score', 'employed', 'approved']
        for col in required_cols:
            assert col in df.columns, f"Missing column: {col}"

    def test_no_missing_values(self):
        df = load_data()
        assert df.isnull().sum().sum() == 0

class TestModelTraining:
    def test_model_trains_successfully(self):
        df = load_data()
        model, accuracy = train_model(df)
        assert model is not None

    def test_model_accuracy_above_threshold(self):
        df = load_data()
        model, accuracy = train_model(df)
        assert accuracy >= 0.7, f"Accuracy too low: {accuracy}"

    def test_model_saves_successfully(self, tmp_path):
        df = load_data()
        model, _ = train_model(df)
        model_path = str(tmp_path / "test_model.pkl")
        save_model(model, model_path)
        assert os.path.exists(model_path)

class TestPredictions:
    def test_prediction_returns_valid_output(self):
        df = load_data()
        model, _ = train_model(df)
        result = predict(model, age=40, income=80000, loan_amount=25000, credit_score=740, employed=1)
        assert result in ["Approved", "Rejected"]

    def test_prediction_output_is_string(self):
        df = load_data()
        model, _ = train_model(df)
        result = predict(model, age=35, income=60000, loan_amount=20000, credit_score=700, employed=1)
        assert isinstance(result, str)

    def test_low_profile_applicant(self):
        df = load_data()
        model, _ = train_model(df)
        result = predict(model, age=21, income=12000, loan_amount=8000, credit_score=520, employed=0)
        assert result in ["Approved", "Rejected"]