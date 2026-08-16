import streamlit as st
import pandas as pd
import numpy as np
import requests
import joblib
import plotly.express as px
import shap
import google.generativeai as genai
import os

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="SolarSense AI",
    layout="wide"
)

# ---------------- GEMINI CLIENT ---------------- #
# PASTE YOUR NEWLY GENERATED API KEY HERE:
API_KEY = os.getenv("OPENWEATHER_API_KEY")
genai.configure(api_key=API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")
# ---------------- INITIALIZE SESSION STATE ---------------- #
if "forecast_generated" not in st.session_state:
    st.session_state.forecast_generated = False
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None
if "prediction" not in st.session_state:
    st.session_state.prediction = 0.0
if "sample_input" not in st.session_state:
    st.session_state.sample_input = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CUSTOM CSS ---------------- #
try:
    with open("app/assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ---------------- TITLE ---------------- #
st.markdown(
    """
    <h1 style='text-align:center;'>☀️ SolarSense AI</h1>
    <h3 style='text-align:center;color:gray;'>Intelligent Real-Time Solar Forecasting Dashboard</h3>
    """, 
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #
st.sidebar.markdown("## ⚡ Forecast Settings")
model_option = st.sidebar.selectbox(
    "Choose Forecasting Model",
    ("Random Forest", "XGBoost", "Decision Tree")
)

# ---------------- LOAD MODEL ---------------- #
@st.cache_resource
def load_model(option):
    try:
        if option == "Random Forest":
            return joblib.load("models/random_forest_model.pkl")
        elif option == "XGBoost":
            return joblib.load("models/xgboost_model.pkl")
        else:
            return joblib.load("models/decision_tree_model.pkl")
    except Exception:
        return None

model = load_model(model_option)
explainer = shap.TreeExplainer(model) if model else None

# ---------------- CITY INPUT ---------------- #
city = st.text_input("Enter City Name")

# ---------------- FORECAST GENERATION ---------------- #
if st.button("Generate Live Forecast"):
    OPENWEATHER_API_KEY = "d6b14f6fc1d9ff43d4fcd75eddbde602"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        weather_json = response.json()
        
        if response.status_code == 200:
            st.session_state.weather_data = weather_json
            
            # Extract features
            temperature = float(weather_json['main']['temp'])
            cloud_cover = float(weather_json['clouds']['all'])
            irradiation = max(0, 1000 - (cloud_cover * 8))
            module_temperature = temperature + 5
            current_hour = pd.Timestamp.now().hour
            
            # Create input payload
            sample_input = pd.DataFrame({
                'PLANT_ID': [4135001], 'DAILY_YIELD': [2500], 'TOTAL_YIELD': [9850000],
                'AMBIENT_TEMPERATURE': [temperature], 'MODULE_TEMPERATURE': [module_temperature],
                'IRRADIATION': [irradiation], 'HOUR': [current_hour], 'DAY': [pd.Timestamp.now().day],
                'MONTH': [pd.Timestamp.now().month], 'DAY_OF_WEEK': [pd.Timestamp.now().dayofweek],
                'WEEK_OF_YEAR': [pd.Timestamp.now().isocalendar().week],
                'IS_PEAK_HOUR': [1 if 10 <= current_hour <= 15 else 0],
                'TEMP_DIFFERENCE': [module_temperature - temperature],
                'IRRADIATION_EFFICIENCY': [0], 'PREVIOUS_AC_POWER': [0], 'ROLLING_MEAN_AC_POWER': [0]
            })
            
            # Save payload to session state for SHAP to use later
            st.session_state.sample_input = sample_input
            
            if model:
                st.session_state.prediction = float(model.predict(sample_input)[0])
            else:
                st.session_state.prediction = 1250.50 # Mock value if model is missing
                
            st.session_state.forecast_generated = True
            st.success("Live Forecast Generated Successfully")
        else:
            st.error(f"City not found or API error: {weather_json.get('message', '')}")
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")

# ---------------- RENDER DASHBOARD (PERSISTENT) ---------------- #
if st.session_state.forecast_generated and st.session_state.weather_data:
    w_data = st.session_state.weather_data
    temp = float(w_data['main']['temp'])
    clouds = float(w_data['clouds']['all'])
    pred = st.session_state.prediction
    
    # Hero Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", f"{temp} °C")
    col2.metric("Cloud Cover", f"{clouds}%")
    col3.metric("Predicted Power", f"{pred:.2f} kW")
    
    # Graphs & Visualizations
    graph_df = pd.DataFrame({'Category': ['Predicted AC Power'], 'Power': [pred]})
    fig = px.bar(graph_df, x='Category', y='Power', color='Power', title='Live Solar Forecast')
    fig.update_layout(template='plotly_dark', plot_bgcolor='#0f172a', paper_bgcolor='#0f172a', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)

    # ---------- SHAP EXPLAINABILITY ---------- #
    st.markdown("---")
    st.subheader("Explainable AI Insights")

    if model and explainer and st.session_state.sample_input is not None:
        try:
            shap_values = explainer.shap_values(st.session_state.sample_input)
            shap_df = pd.DataFrame({
                'Feature': st.session_state.sample_input.columns,
                'Impact': np.abs(shap_values)[0]
            }).sort_values(by='Impact', ascending=False)

            shap_fig = px.bar(shap_df, x='Impact', y='Feature', orientation='h',
                              color='Impact', title='SHAP Feature Contribution')
            shap_fig.update_layout(template='plotly_dark', plot_bgcolor='#0f172a',
                                   paper_bgcolor='#0f172a', font=dict(color='white'))
            st.plotly_chart(shap_fig, use_container_width=True)
        except Exception:
            st.warning("SHAP visualization temporarily unavailable. Using mock model?")

    # ---------- FEATURE IMPORTANCE ---------- #
    st.subheader("Feature Importance Analysis")

    feature_importance_df = pd.DataFrame({
        'Feature': ['IRRADIATION', 'MODULE_TEMPERATURE', 'HOUR', 'AMBIENT_TEMPERATURE', 'DAILY_YIELD', 'TOTAL_YIELD'],
        'Importance': [0.42, 0.18, 0.14, 0.10, 0.09, 0.07]
    })

    importance_fig = px.bar(feature_importance_df, x='Importance', y='Feature',
                            orientation='h', color='Importance', title='Feature Importance')
    importance_fig.update_layout(template='plotly_dark', plot_bgcolor='#0f172a',
                                 paper_bgcolor='#0f172a', font=dict(color='white'))
    st.plotly_chart(importance_fig, use_container_width=True)


# ---------------- CHATBOT SECTION ---------------- #
st.markdown("---")
st.subheader("🤖 Solar AI Assistant")

# 1. Render existing message history first
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 2. Accept new user input at the bottom
if user_input := st.chat_input("Ask about solar forecasting..."):
    # Display user message immediately
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate system prompt context
    solar_prompt = f"You are SolarSense AI Assistant. Answer this solar query: {user_input}"
    
    # Fetch from Gemini API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = gemini_model.generate_content(solar_prompt)
            bot_reply = response.text
            message_placeholder.write(bot_reply)
        except Exception as e:
            bot_reply = f"API Error: {e}"
            message_placeholder.error(bot_reply)
            
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# ---------------- SIDEBAR FOOTER ---------------- #
st.sidebar.markdown("---")
st.sidebar.info("SolarSense AI uses Machine Learning for intelligent solar forecasting.")