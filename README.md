```text
# Webhook test
# Email notification test
```

# Loan Approval ML — DevOps Pipeline Project

A complete end-to-end DevOps project built on a Machine Learning Loan Approval system, covering CI/CD pipelines, containerization, and container orchestration across Experiments 3–10 of the Agile Product Development lab manual.

---

## 📁 Project Structure

```text
loan-approval-devops/ 
├── data/ 
│   └── loan_data.csv       # Dataset — 30 loan records 
├── app.py                  # Main entry point — trains, saves, and predicts 
├── train.py                # Model training script 
├── predict.py              # Standalone prediction script 
├── test_app.py             # Pytest test suite (4 tests) 
├── requirements.txt        # Python dependencies 
├── Jenkinsfile             # Declarative Jenkins pipeline (6 stages) 
├── Dockerfile              # Docker image definition (python:3.9-slim) 
├── .dockerignore           # Files excluded from Docker build context 
├── deploy.sh               # Shell script to build and deploy 
├── deployment.yaml         # Kubernetes Deployment manifest 
├── service.yaml            # Kubernetes Service manifest (NodePort) 
└── job.yaml                # Kubernetes Job manifest (batch run) 
```

---

## 🧠 The ML Application

The core application (`app.py`) is a **Loan Approval Prediction System** built using scikit-learn's `DecisionTreeClassifier`.

### How it Works
1. Loads a dataset of 30 loan records with features:
   * **Age** — Applicant's age
   * **Income** — Annual income
   * **Loan Amount** — Requested loan amount
   * **Credit Score** — Applicant's credit score
   * **Approval Status** — Target label (Approved / Denied)
2. Trains a `DecisionTreeClassifier` on 80% of the data.
3. Evaluates accuracy on the remaining 20%.
4. Saves the trained model to `model.pkl` using `joblib`.
5. Makes a sample prediction:
   > **Sample Prediction** (Age: 35, Income: 60000, Loan: 20000, Score: 700): `Approved`

### Model Performance
* **Dataset:** 30 records 
* **Train/Test Split:** 80/20 
* **Accuracy:** 83.33%

### Dependencies
```text
scikit-learn>=1.4.0 
pandas>=2.0.0 
numpy>=1.26.0 
joblib>=1.3.0 
pytest>=7.4.0
```

---

## 🧪 Test Suite

Four pytest tests are defined in `test_app.py`:

| Test | Description |
|------|-------------|
| `test_data_loads` | Verifies dataset loads with correct shape |
| `test_model_trains` | Confirms model trains and returns accuracy > 0 |
| `test_prediction_approved` | Checks strong profile gets `Approved` |
| `test_prediction_denied` | Checks weak profile gets `Denied` |

**Run locally:**
```bash
python3 -m pytest test_app.py -v
```

---

## ⚙️ Experiments Overview

### Experiment 3 — Git & GitHub
* Initialised local Git repository.
* Connected to remote GitHub repo.
* Established branching strategy on `main`.
* All project files version-controlled throughout.

```bash
git init
git remote add origin https://github.com/neel-911/Basic-ML-LoanApproval-Devops.git
git push -u origin main
```

### Experiment 4 — Jenkins Setup
* Installed and configured Jenkins locally at `http://localhost:8080`.
* Created a freestyle job (`loan-approval-build`) connected to the GitHub repo.
* Verified Jenkins can pull source code and execute shell build steps.

### Experiment 5 — GitHub Webhooks with ngrok
* Used ngrok to expose the local Jenkins server to the internet.
* Configured a GitHub webhook pointing to the ngrok URL.
* Any `git push` to `main` automatically triggers the Jenkins pipeline.
* **Webhook URL format:** `https://<ngrok-id>.ngrok.io/github-webhook/`

### Experiment 6 — Email Notifications
* Configured Jenkins Extended E-mail Notification plugin.
* Pipeline sends email alerts on build success and failure.
* SMTP configured via Gmail with App Password.

### Experiment 7 — Chained Freestyle Jobs
* Created two freestyle jobs:
  1. `loan-approval-build` — installs dependencies and runs `app.py`.
  2. `loan-approval-test` — runs the pytest test suite.
* `loan-approval-build` triggers `loan-approval-test` on success.
* Demonstrates sequential job chaining in Jenkins.

### Experiment 8 — Declarative Jenkinsfile Pipeline
* Replaced freestyle jobs with a single `Jenkinsfile` at the repo root.
* Created pipeline job `loan-approval-pipeline` in Jenkins (SCM-based).
* All stages defined as code — pipeline is version-controlled alongside the app.

### Experiment 9 — Docker Containerisation
* Wrote a `Dockerfile` using `python:3.9-slim` as the base image.
* Built and ran the image locally.
* Rebuilt as `loan-approval-app:v2` after a code change.
* Saved image as a `.tar` archive.
* Jenkins pipeline updated with Docker PATH fix:
  ```groovy
  environment {
      PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
  }
  ```

```bash
docker build -t loan-approval-app .
docker run loan-approval-app
docker build -t loan-approval-app:v2 .
docker save -o loan-approval-app.tar loan-approval-app
```

### Experiment 10 — Kubernetes Deployment
* Installed Minikube for a local single-node Kubernetes cluster.
* Loaded the Docker image directly into Minikube (no registry needed).
* Deployed using a Kubernetes Job (correct resource type for a batch ML script).
* Job completed in 4 seconds with 0 failures.

```bash
minikube start
minikube image load loan-approval-app:latest
kubectl apply -f job.yaml
kubectl get jobs
kubectl logs <pod-name>
```

---

## 🔁 Jenkins Pipeline — Full Stages

Defined in `Jenkinsfile`, triggered automatically on every `git push` via GitHub webhook.

```text
┌─────────────────────────┐
│    GitHub push (main)   │
└────────────┬────────────┘
             │ webhook
             ▼
┌─────────────────────────┐
│  Stage 1: Checkout      │  Clone repo from GitHub
├─────────────────────────┤
│  Stage 2: Install Deps  │  pip3 install -r requirements.txt
├─────────────────────────┤
│  Stage 3: Build         │  python3 app.py → trains model, saves pkl
├─────────────────────────┤
│  Stage 4: Test          │  pytest test_app.py -v → 4/4 passed
├─────────────────────────┤
│  Stage 5: Docker Build  │  docker build -t loan-approval-app .
├─────────────────────────┤
│  Stage 6: Docker Run    │  docker run --rm loan-approval-app
└─────────────────────────┘
             │
             ▼
      ✅ SUCCESS → Email Notification sent
```

### Jenkinsfile Snippet
```groovy
pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
    }
    stages {
        stage('Checkout')             { ... }
        stage('Install Dependencies') { ... }
        stage('Build')                { ... }
        stage('Test')                 { ... }
        stage('Docker Build')         { ... }
        stage('Docker Run')           { ... }
    }
    post {
        success { echo '=== Pipeline completed successfully! ===' }
    }
}
```

---

## 🐳 Docker

### Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "app.py"]
```

### Commands
```bash
# Build
docker build -t loan-approval-app .

# Run
docker run --rm loan-approval-app

# Version 2
docker build -t loan-approval-app:v2 .

# List images
docker images | grep loan-approval-app
```

---

## ☸️ Kubernetes

### Job Manifest (`job.yaml`)
Batch workload — correct for ML scripts.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: loan-approval-job
spec:
  template:
    spec:
      containers:
      - name: loan-approval
        image: loan-approval-app:latest
        imagePullPolicy: Never
      restartPolicy: Never
  backoffLimit: 2
```

### Result
```text
NAME                STATUS     COMPLETIONS   DURATION
loan-approval-job   Complete   1/1           4s

Pods Statuses: 0 Active / 1 Succeeded / 0 Failed
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **ML** | scikit-learn, pandas, numpy |
| **Testing** | pytest |
| **Version Control** | Git, GitHub |
| **CI/CD** | Jenkins (declarative pipeline) |
| **Webhook Tunnel** | ngrok |
| **Containerisation** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **Language** | Python 3.9 |
| **Platform** | macOS (Apple M-series) |

---

## 🚀 Run Locally

```bash
# Clone
git clone https://github.com/neel-911/Basic-ML-LoanApproval-Devops.git
cd Basic-ML-LoanApproval-Devops

# Install dependencies
pip3 install -r requirements.txt

# Run the app
python3 app.py

# Run tests
python3 -m pytest test_app.py -v

# Docker
docker build -t loan-approval-app .
docker run --rm loan-approval-app
```

---

## 👤 Author
**Neel Jaiswal** *DevOps Lab Project — Experiments 3 to 10*
