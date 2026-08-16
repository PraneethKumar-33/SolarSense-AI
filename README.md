<div align="center">

# ☀️ SolarSense AI

### AI-Powered Solar Energy Forecasting & Analytics Platform

Predict solar power generation using Machine Learning, weather intelligence, and interactive visual analytics.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-success?style=for-the-badge)

</div>

---

# 🌍 About the Project

SolarSense AI is an intelligent Machine Learning application that forecasts solar energy generation using historical plant data and weather information.

The platform combines data preprocessing, feature engineering, predictive machine learning models, and an interactive Streamlit dashboard to provide accurate solar power predictions and insightful visual analytics.

The goal is to assist in understanding and forecasting solar power generation using data-driven techniques.

---

# ✨ Features

- ☀️ Solar Power Prediction
- 🤖 Machine Learning Forecasting
- 🌤️ Real-Time Weather Integration
- 📊 Interactive Dashboard
- 📈 Historical Trend Analysis
- ⚡ Advanced Feature Engineering
- 📉 Model Comparison
- 🎯 High Accuracy Prediction
- 📱 Easy-to-use Interface

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| ML Libraries | Scikit-Learn, XGBoost |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Frontend | Streamlit |
| API | OpenWeather API |

---

# 📂 Project Structure

```text
SolarSense-AI
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/
│
├── src/
│
├── notebooks/
│
├── data/
│
├── outputs/
│
└── models/
```

---

# 🔄 Workflow

```text
Solar Plant Dataset
          │
          ▼
Data Cleaning
          │
          ▼
Feature Engineering
          │
          ▼
Train-Test Split
          │
          ▼
Machine Learning Models
          │
          ▼
Model Evaluation
          │
          ▼
Solar Power Prediction
          │
          ▼
Interactive Dashboard
```

---

# 🏗 System Architecture

```text
                +--------------------------+
                | Historical Solar Dataset |
                +--------------------------+
                           │
                           ▼
                +--------------------------+
                | Data Preprocessing       |
                +--------------------------+
                           │
                           ▼
                +--------------------------+
                | Feature Engineering      |
                +--------------------------+
                           │
                           ▼
        +------------------------------------------+
        | Machine Learning Models                  |
        |------------------------------------------|
        | Linear Regression                        |
        | Decision Tree                            |
        | Random Forest                            |
        | XGBoost                                  |
        +------------------------------------------+
                           │
                           ▼
                +--------------------------+
                | Weather Information      |
                +--------------------------+
                           │
                           ▼
                +--------------------------+
                | Prediction Engine        |
                +--------------------------+
                           │
                           ▼
                +--------------------------+
                | Streamlit Dashboard      |
                +--------------------------+
```

---

# 📊 Dataset

The project uses historical solar plant generation data together with weather sensor measurements.

### Dataset Attributes

- AC Power
- DC Power
- Module Temperature
- Ambient Temperature
- Irradiation
- Daily Yield
- Total Yield
- Timestamp

---

# 🤖 Machine Learning Models

The following regression models were implemented and evaluated.

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# ⚙ Feature Engineering

Several engineered features were created to improve prediction performance.

- Hour
- Day
- Month
- Day of Week
- Week of Year
- Lag Features
- Rolling Mean
- Previous AC Power
- Peak Hour Indicator
- Temperature Difference
- Irradiation Efficiency

---

# 🌤 Weather Integration

Real-time weather information is obtained using the OpenWeather API.

Parameters used include:

- Temperature
- Humidity
- Cloud Cover
- Weather Conditions

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/PraneethKumar-33/SolarSense-AI.git
```

Go into the project

```bash
cd SolarSense-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

The actual API key is intentionally excluded from the repository.

---

# 📈 Future Enhancements

- LSTM-based Deep Learning Forecasting
- Explainable AI using SHAP
- Cloud Deployment
- Live Solar Plant Monitoring
- Multi-Plant Forecasting
- Automated Model Retraining

---

# 📚 Learning Outcomes

This project strengthened practical knowledge in:

- Data Cleaning
- Feature Engineering
- Machine Learning
- Hyperparameter Tuning
- Model Evaluation
- Streamlit Development
- API Integration
- Git & GitHub

---

# 👨‍💻 Author

## Pamu Praneeth Kumar

Computer Science and Engineering (Artificial Intelligence)

**GitHub**

https://github.com/PraneethKumar-33

**LinkedIn**

https://www.linkedin.com/in/praneeth-kumar-5013aa325/

---

# ⭐ If you like this project

Please consider giving it a **Star ⭐** on GitHub.

It motivates further improvements and supports the project.

---

# 📄 License

This project is intended for educational and research purposes.
