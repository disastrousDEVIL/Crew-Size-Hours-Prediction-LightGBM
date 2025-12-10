# 🚚 Crew Size & Hours Prediction

A regression-based machine learning project that predicts **how many crew members** and **how many hours** are required for a given moving job.  
This model forms one of the three intelligent components of the **MSP Optimization System**, alongside the **MSP Ranking Model** and the **Order Acceptance Predictor**.

---

## 🧠 Project Overview

This system helps logistics and moving service providers **optimize labor allocation, improve scheduling accuracy, and enhance pricing decisions** using data-driven insights.

### 🎯 Core Objectives
- Predict the optimal **crew size** for each job.
- Estimate the **hours required** to complete the move.
- Enable real-time prediction through a **FastAPI REST endpoint**.

---

## ⚙️ Tech Stack

**Languages & Libraries**
- Python 3.10+
- Pandas, NumPy, Scikit-learn, LightGBM
- Joblib for model serialization

**Serving Layer**
- FastAPI (for inference API)
- Uvicorn (for local deployment and testing)

**Environment**
- Developed and tested in Google Colab + VSCode (Cursor)
- Reproducible through `.pkl` model files

---

## 📁 Project Structure

```

crew-size-hours-prediction/
│
├── app/
│   ├── main.py               # FastAPI entry point
│   ├── predict.py            # Loads models and handles inference
│   └── schemas.py            # Pydantic models for request/response
│
├── data/
│   └── crew_hours_synthetic.csv     # Simulated dataset
│
├── models/
│   ├── model_hours.pkl       # Trained LightGBM model (hours)
│   └── model_crew.pkl        # Trained LightGBM model (crew size)
│
├── notebooks/
│   ├── 01_model_training.ipynb     # Data simulation + training + model saving
│   └── 03_inference_tests.ipynb    # Model and API inference tests
│
├── utils/
│   └── features.py            # Centralized feature engineering logic
│
├── .gitignore
└── README.md

````

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
````

*(or manually install)*

```bash
pip install pandas numpy lightgbm scikit-learn fastapi uvicorn joblib
```

### 2️⃣ Train models (optional)

Open and run:

```
notebooks/01_model_training.ipynb
```

This will generate:

```
models/model_hours.pkl
models/model_crew.pkl
```

### 3️⃣ Start FastAPI server

```bash
uvicorn app.main:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

### 4️⃣ Example JSON input

```json
{
  "job_size_sqft": 1500,
  "num_rooms": 4,
  "num_heavy_items": 6,
  "num_light_items": 35,
  "distance_km": 15,
  "floor_number": 2,
  "has_elevator": true,
  "past_avg_hours": 6.5,
  "past_avg_crew_size": 3.0
}
```

### ✅ Example Response

```json
{
  "predicted_crew_size": 3,
  "predicted_hours_required": 6.7
}
```

---

## 📊 Model Performance

| Target         | MAE  | RMSE |
| -------------- | ---- | ---- |
| Hours Required | 0.49 | 0.67 |
| Crew Size      | 0.14 | 0.28 |

*(On synthetic dataset with realistic job complexity correlations.)*

---

## 🧩 Related Projects

* 🧠 **MSP Ranking System** – Learning-to-Rank model using XGBoostRanker
* ⚡ **Order Acceptance Predictor** – Classification model for MSP job acceptance
  Together, these models create a complete **AI-driven logistics optimization framework**.

---

## 👤 Author

**Krish Batra**
AI/ML Engineer | Developer of the MSP Optimization Suite
🔗 [GitHub](https://github.com/disastrousDEVIL) • [LinkedIn](https://www.linkedin.com/in/krish-batra) • [Website](https://vybecode.in)

---

## 🧩 License

This project is released under the **MIT License**.

---

## 🪄 Future Improvements

* Integrate real operational datasets via BigQuery ML.
* Deploy on Vertex AI or Render with GPU optimization.
* Add time-based and weather-aware features for richer predictions.
