<div align="center">

# ☀️ SolarSense AI
### Intelligent Real-Time Solar Forecasting & Generative AI Dashboard

Predict solar power generation using Machine Learning, weather intelligence, and conversational AI analytics.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-success?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google%20Gemini-Generative%20AI-blue?style=for-the-badge&logo=google)

</div>

---

## 🌍 About the Project

**SolarSense AI** is an intelligent, full-stack Machine Learning application designed to forecast solar energy generation. By combining historical solar plant data with real-time weather API integration, it provides accurate, day-ahead power predictions. 

Beyond predictive modeling, SolarSense AI features a **Generative AI Assistant** powered by Google Gemini, allowing users to query solar data, understand forecasting metrics, and get explainable AI insights interactively.

---

## ✨ Key Features

- ☀️ **Real-Time Solar Power Prediction:** Forecast AC/DC power output based on live atmospheric conditions.
- 🤖 **Multiple ML Models:** Compare predictions across Random Forest, Decision Tree, and XGBoost models.
- 💬 **Generative AI Assistant:** Integrated conversational chatbot powered by Google Gemini 2.5 Flash for natural language querying.
- 🌤️ **Live Weather Integration:** Dynamically fetches real-time meteorological data via the OpenWeather API.
- 📊 **Explainable AI (XAI):** Visualizes feature importance and SHAP (SHapley Additive exPlanations) values to interpret model decisions.
- 📈 **Interactive Dashboard:** Built with Streamlit and Plotly for a seamless, dark-mode visual analytics experience.

---

## 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Programming** | Python 3 |
| **Machine Learning** | Scikit-Learn, XGBoost, SHAP |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib |
| **Frontend/UI** | Streamlit |
| **APIs / LLMs** | OpenWeather API, Google Gemini API |

---

## 📂 Project Structure

```text
SolarSense-AI/
├── app.py                   # Main Streamlit Application (Frontend & AI Assistant)
├── requirements.txt         # Project Dependencies
├── .env.example             # Template for Environment Variables
├── models/                  # Pickled ML Models (.pkl) - Ignored in Git
├── data/                    # Raw and Processed Datasets
├── notebooks/               # Jupyter Notebooks for EDA & Model Training
├── outputs/                 # Exported Graphs and Forecasts
└── src/                     # Helper scripts and utilities
```

---

## 🚀 Setup & Installation

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/PraneethKumar-33/SolarSense-AI.git
cd SolarSense-AI
```

### 2. Install Dependencies
Make sure you have Python 3 installed. Install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:
```bash
OPENWEATHER_API_KEY=your_openweather_api_key_here
GEMINI_API_KEY=your_google_gemini_api_key_here
```
*(Note: You can get a free OpenWeather API key [here](https://openweathermap.org/api) and a Google Gemini API key [here](https://aistudio.google.com/).)*

### 4. Run the Application
```bash
streamlit run app.py
```

---

## 🏗 System Architecture & Workflow

1. **Data Ingestion:** Historical solar data is cleaned and feature-engineered (lag features, rolling means).
2. **Model Training:** Regression models (RF, XGBoost, Decision Tree) are trained and serialized using `joblib`.
3. **Live Inference:** The Streamlit app takes a city name, fetches live weather data, applies the same feature engineering, and feeds it to the pre-trained models.
4. **AI Generation:** The Gemini LLM acts as an interactive layer on top of the dashboard for contextual Q&A.

---

## 👨‍💻 Author
**Pamu Praneeth Kumar**  
B.Tech in Computer Science and Engineering (Artificial Intelligence)  
🔗 [LinkedIn](https://www.linkedin.com/in/praneeth-kumar-5013aa325/) | 🐙 [GitHub](https://github.com/PraneethKumar-33)

---

⭐ *If you found this project helpful, please consider giving it a Star!*
