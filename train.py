import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def main():
    print("=== Training Loan Approval Model ===")
    df = pd.read_csv('data/loan_data.csv')
    print(f"Loaded {len(df)} records")

    X = df[['age', 'income', 'loan_amount', 'credit_score', 'employed']]
    y = df['approved']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Training complete.")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")

    joblib.dump(model, 'model.pkl')
    print("Model saved as model.pkl")

if __name__ == "__main__":
    main()