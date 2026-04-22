# webhook test
# email notification test
# email notification test

# 🏦 Loan Approval ML — DevOps Pipeline Project

A complete end-to-end DevOps project built on a Machine Learning Loan Approval system,
covering CI/CD pipelines, containerization, and container orchestration across
Experiments 3–10 of the lab manual.

---

## 📁 Project Structure

loan-approval-devops/ 
├── data/ 
│ └── loan_data.csv # Dataset — 30 loan records 
├── app.py # Main entry point — trains, saves, and predicts 
├── train.py # Model training script 
├── predict.py # Standalone prediction script 
├── test_app.py # Pytest test suite (4 tests) 
├── requirements.txt # Python dependencies 
├── Jenkinsfile # Declarative Jenkins pipeline (6 stages) 
├── Dockerfile # Docker image definition (python:3.9-slim) 
├── .dockerignore # Files excluded from Docker build context 
├── deploy.sh # Shell script to build and deploy 
├── deployment.yaml # Kubernetes Deployment manifest 
├── service.yaml # Kubernetes Service manifest (NodePort) 
├── job.yaml # Kubernetes Job manifest (batch run) 

---

## 🤖 The ML Application

The core application (`app.py`) is a **Loan Approval Prediction System** built using
scikit-learn's `DecisionTreeClassifier`.

### How it works
1. Loads a dataset of 30 loan records with features:
   - **Age** — applicant's age
   - **Income** — annual income
   - **Loan Amount** — requested loan amount
   - **Credit Score** — applicant's credit score
   - **Approval Status** — target label (Approved / Denied)

2. Trains a `DecisionTreeClassifier` on 80% of the data

3. Evaluates accuracy on the remaining 20%

4. Saves the trained model to `model.pkl` using `joblib`

5. Makes a sample prediction:
Sample Prediction (Age:35, Income:60000, Loan:20000, Score:700): Approved


### Model Performance
Dataset: 30 records Train/Test Split: 80/20 Accuracy: 83.33%


### Dependencies
scikit-learn>=1.4.0 pandas>=2.0.0 numpy>=1.26.0 joblib>=1.3.0 pytest>=7.4.0


---

## 🧪 Test Suite

Four pytest tests in `test_app.py`:

| Test | Description |
|------|-------------|
| `test_data_loads` | Verifies dataset loads with correct shape |
| `test_model_trains` | Confirms model trains and returns accuracy > 0 |
| `test_prediction_approved` | Checks strong profile gets `Approved` |
| `test_prediction_denied` | Checks weak profile gets `Denied` |

Run locally:
```bash
python3 -m pytest test_app.py -v