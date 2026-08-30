# 🚀 Predictive Maintenance System

An end-to-end **Machine Learning + MLOps application** that predicts whether industrial equipment is at risk of failure based on sensor readings.

The project covers the complete workflow from **data processing and model training to API serving, testing, containerization, and cloud deployment**.

---

## 📌 Project Overview

Predictive maintenance uses machine-learning models to identify equipment that may require maintenance before an actual failure occurs.

This project uses machine sensor data such as:

* Air temperature
* Process temperature
* Rotational speed
* Torque
* Tool wear
* Machine type

The trained model predicts the probability of equipment failure and provides a maintenance recommendation through a REST API.

---

## 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │      GitHub      │
                         │   Source Code    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ GitHub Actions   │
                         │       CI         │
                         └────────┬─────────┘
                                  │
                         Install dependencies
                                  │
                         Configure DVC
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ DVC / DagsHub    │
                         │  Model Storage   │
                         └────────┬─────────┘
                                  │
                              dvc pull
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     pytest       │
                         │      Tests       │
                         └────────┬─────────┘
                                  │
                              Tests pass
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ GitHub Actions   │
                         │       CD         │
                         └────────┬─────────┘
                                  │
                         Install and Configure DVC  
                                  │
                                  ▼   
                         ┌──────────────────┐
                         │ DVC / DagsHub    │
                         │  Model Storage   │
                         └────────┬─────────┘
                                  │
                              dvc pull
                                  │
                                  ▼                       
                         ┌──────────────────┐
                         │      Docker      │
                         │   Build Image    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Docker Hub     │
                         │  Image Registry  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      Render      │
                         │    Deployment    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    FastAPI       │
                         │    REST API      │
                         └────────┬─────────┘
                                  │
                         ┌────────┴─────────┐
                         ▼                  ▼
                  ┌──────────────┐   ┌──────────────┐
                  │ PostgreSQL   │   │ ML Model     │
                  │   Database   │   │  Prediction  │
                  └──────────────┘   └──────────────┘
```

---

## ✨ Features

* Machine failure prediction using Machine Learning
* Scikit-learn preprocessing pipeline
* Random Forest classification model
* Model versioning using DVC
* DagsHub for remote model storage
* FastAPI REST API
* PostgreSQL database
* User authentication
* Prediction history
* Automated unit/integration testing with pytest
* Docker containerization
* GitHub Actions CI/CD
* Docker Hub image registry
* Cloud deployment with Render
* Environment-based configuration

---

## 🧠 Machine Learning

### Model

The project uses a **Random Forest Classifier** with preprocessing integrated into a Scikit-learn pipeline.

### Input Features

| Feature        | Description         |
| -------------- | ------------------- |
| `type`         | Machine type        |
| `air_temp`     | Air temperature     |
| `process_temp` | Process temperature |
| `rot_speed`    | Rotational speed    |
| `torque`       | Torque              |
| `tool_wear`    | Tool wear           |

### Prediction

The API returns:

* Failure probability
* Prediction
* Whether maintenance is required
* Recommendation message

Example:

```json
{
  "prediction": "failure",
  "maintenance_required": true,
  "failure_probability": 0.72,
  "message": "Equipment failure risk detected. Maintenance is recommended."
}
```

---

## 🔄 ML Pipeline

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Preprocessing
     │
     ▼
Model Training
     │
     ▼
Hyperparameter Tuning
     │
     ▼
Model Evaluation
     │
     ▼
model.joblib
     │
     ▼
DVC Versioning
     │
     ▼
DagsHub
```

---

## 📦 Project Structure

```text
Predictive-Maintenance-System/
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── services/
│
├── data/
│
├── models/
│   └── model.joblib.dvc
│
├── notebooks/
│
├── reports/
│
├── src/
│   ├── config.py
│   ├── logger.py
│   ├── train.py
│   └── ...
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_inference.py
│   └── test_model.py
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── Dockerfile
├── dvc.yaml
├── dvc.lock
├── params.yaml
├── requirements.txt
└── README.md
```

---

## 🌐 API

The backend is built using **FastAPI**.

### API Documentation

After starting the application, interactive API documentation is available at:

```text
/docs
```

FastAPI also provides an OpenAPI specification at:

```text
/openapi.json
```

---

## 🔮 Prediction API

### `POST /inference`

Example request:

```json
{
  "type": "M",
  "air_temp": 298.1,
  "process_temp": 308.6,
  "rot_speed": 1551,
  "torque": 42.8,
  "tool_wear": 0
}
```

Example response:

```json
{
  "prediction": "working",
  "maintenance_required": false,
  "failure_probability": 0.12,
  "message": "Equipment is operating normally. No maintenance required."
}
```

---

## 🔐 Authentication

The API provides user authentication and protected endpoints.

Authentication includes:

* User registration
* User login
* Session/token-based authentication
* Protected API endpoints
* Password hashing using Argon2

---

## 🗄️ Database

The application uses **PostgreSQL** to store application data and prediction records.

Prediction records contain information such as:

* User
* Machine type
* Temperature
* Rotational speed
* Torque
* Tool wear
* Prediction result

---

## 🧪 Testing

Tests are written using **pytest**.

The test suite covers areas including:

```text
Authentication
      │
      ├── Registration
      └── Login

Model
      │
      └── Model loading

Inference
      │
      └── Prediction endpoint
```

Run tests locally:

```bash
pytest
```

---

## 🔄 CI/CD Pipeline

GitHub Actions is used to automate testing and deployment.

### Continuous Integration

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ├── Install Python
   │
   ├── Install dependencies
   │
   ├── Configure DVC
   │
   ├── Download model
   │
   └── Run pytest
```

If tests fail, deployment is stopped.

### Continuous Deployment

After successful CI:

```text
CI Success
    │
    ▼
Build Docker Image
    │
    ▼
Install and Configure DVC
    │
    ▼
Push to Docker Hub
    │
    ▼
Deploy to Render via Deploy Hook
```

This ensures that only code that passes the test suite is deployed.

---

## 🐳 Docker

The application is containerized using Docker.

Build the image:

```bash
docker build -t <username>/predictive-maintenance .
```

Run the container:

```bash
docker run -d -p 8000:8000 <username>/predictive-maintenance
```

The API can then be accessed at:

```text
http://localhost:8000
```

---

## 📊 MLOps

This project implements several MLOps practices:

| Component                  | Technology     |
| -------------------------- | -------------- |
| Version Control            | Git / GitHub   |
| Dataset & Model Versioning | DVC            |
| Remote Storage             | DagsHub        |
| ML Framework               | Scikit-learn   |
| API                        | FastAPI        |
| Database                   | PostgreSQL     |
| Testing                    | pytest         |
| Containerization           | Docker         |
| CI/CD                      | GitHub Actions |
| Container Registry         | Docker Hub     |
| Deployment                 | Render         |

---

## ⚙️ Environment Variables

Create a `.env` file for local development.

Example:

```env
DATABASE_URL=your_database_url
SECRET=your_secret
ALGORITHM=your_algorithm
MODEL_PATH=model_path
MLFLOW_TRACKING_USERNAME=your_mlflow_tracking_username
DAGSHUB_URL=your_dagshub_url
MODEL_NAME=your_registered_model_name
MLFLOW_TRACKING_PASSWORD=your_mlflow_tracking_password

```

Do not commit secrets or `.env` files to Git.

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Krishna72user/Predictive-Maintenance-System.git

cd Predictive-Maintenance-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull the model

```bash
dvc pull models/model.joblib
```

### 5. Configure environment variables

Create your `.env` file.

### 6. Start the API

```bash
uvicorn app.main:app --reload
```

### 7. Run tests

```bash
pytest
```

---

## ☁️ Deployment

The application uses:

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Docker Hub
   │
   ▼
Render
```

The ML model is maintained separately using DVC/DagsHub.

This allows the application code and ML artifacts to be versioned independently.

---

## 🔒 Security

Sensitive configuration is stored using environment variables and GitHub Actions secrets.

Examples include:

* Database credentials
* Authentication secrets
* DVC storage credentials
* Docker Hub credentials

Credentials are never committed to the repository.

---

## 🎯 Future Improvements

Possible future improvements include:

* Model monitoring
* Data drift detection
* Automated model retraining
* ML experiment tracking with MLflow
* Model performance monitoring
* API load testing
* Automated post-deployment API testing
* Monitoring with Prometheus/Grafana
* Improved model evaluation and threshold optimization

---

## 👨‍💻 Author

**Krishna Laha**

BCA Student | Machine Learning | MLOps | Backend Development

---

## ⭐ Project Goal

This project demonstrates how a machine-learning model can be transformed from a training experiment into a **production-oriented ML application** with:

**Versioning → Testing → API Serving → Containerization → CI/CD → Cloud Deployment**
