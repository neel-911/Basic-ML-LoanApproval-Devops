import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def load_data():
    df = pd.read_csv('data/loan_data.csv')
    return df

def train_model(df):
    X = df[['age', 'income', 'loan_amount', 'credit_score', 'employed']]
    y = df['approved']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

def save_model(model, path='model.pkl'):
    joblib.dump(model, path)
    print(f"Model saved to {path}")

def predict(model, age, income, loan_amount, credit_score, employed):
    features = pd.DataFrame([[age, income, loan_amount, credit_score, employed]],
                            columns=['age', 'income', 'loan_amount', 'credit_score', 'employed'])
    prediction = model.predict(features)[0]
    return "Approved" if prediction == 1 else "Rejected"


if __name__ == "__main__":
    print("=== Loan Approval Prediction System ===")
    df = load_data()
    print(f"Dataset loaded: {len(df)} records")
    model, accuracy = train_model(df)
    print(f"Model trained. Accuracy: {accuracy * 100:.2f}%")
    save_model(model)
    result = predict(model, age=35, income=60000, loan_amount=20000, credit_score=700, employed=1)
    print(f"Sample Prediction (Age:35, Income:60000, Loan:20000, Score:700): {result}")
    print("Build Success")this is broken code !!!
