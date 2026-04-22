import argparse
import joblib
import os
import sys

def predict_loan(age, income, loan_amount, credit_score, employed):
    if not os.path.exists('model.pkl'):
        print("model.pkl not found. Please run app.py or train.py first.")
        sys.exit(1)

    model = joblib.load('model.pkl')
    features = [[age, income, loan_amount, credit_score, employed]]
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]

    result = "APPROVED" if prediction == 1 else "REJECTED"
    confidence = max(probability) * 100

    print("=== Loan Approval Prediction ===")
    print(f"Age:          {age}")
    print(f"Income:       ${income:,}")
    print(f"Loan Amount:  ${loan_amount:,}")
    print(f"Credit Score: {credit_score}")
    print(f"Employed:     {'Yes' if employed else 'No'}")
    print(f"Decision:     {result}")
    print(f"Confidence:   {confidence:.1f}%")

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Loan Approval Predictor')
    parser.add_argument('--age',          type=int, default=35)
    parser.add_argument('--income',       type=int, default=60000)
    parser.add_argument('--loan_amount',  type=int, default=20000)
    parser.add_argument('--credit_score', type=int, default=700)
    parser.add_argument('--employed',     type=int, default=1)

    args = parser.parse_args()
    predict_loan(args.age, args.income, args.loan_amount, args.credit_score, args.employed)