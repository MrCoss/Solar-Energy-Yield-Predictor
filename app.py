import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# === Load model, scaler, and features ===
@st.cache_resource
def load_model_components():
    try:
        model = joblib.load("model/model_daily_yield.pkl")
        scaler = joblib.load("model/scaler_daily_yield.pkl")
        feature_names = joblib.load("model/feature_names.pkl")
        return model, scaler, feature_names
    except Exception as e:
        st.error(f"⚠️ Failed to load model or scaler: {e}")
        return None, None, None

model, scaler, feature_names = load_model_components()
if model is None:
    st.stop()

# === Page UI ===
st.set_page_config(page_title="☀️ Solar Yield Predictor", layout="wide")
st.markdown("<h1 style='text-align: center;'>🔆 Solar Energy Yield Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Estimate daily solar energy output using manual weather data and ML.</p>", unsafe_allow_html=True)
st.markdown("---")

# === Sidebar Inputs ===
st.sidebar.header("🌍 Enter Inputs")
city = st.sidebar.text_input("📍 City", value="Jaipur")
dc_power = st.sidebar.number_input("🔌 DC Power (W)", min_value=0, value=4700)
ac_power = st.sidebar.number_input("⚡ AC Power (W)", min_value=0, value=4500)
ambient_temp = st.sidebar.slider("🌡️ Ambient Temp (°C)", 0, 60, 32)
feels_like = st.sidebar.slider("🤒 Feels Like Temp (°C)", 0, 60, 35)
irradiation = st.sidebar.slider("☀️ Irradiation (W/m²)", 0, 1200, 800)
module_temp = st.sidebar.slider("🔋 Module Temp (°C)", 0, 100, 38)
date = st.sidebar.date_input("📅 Date", datetime.now().date())
time = st.sidebar.time_input("🕒 Time", datetime.now().time())

# === Date & Time Breakdown ===
selected_datetime = datetime.combine(date, time)
hour = selected_datetime.hour
day = selected_datetime.timetuple().tm_yday

# === Prepare input ===
input_data = {
    "DC_POWER": dc_power,
    "AC_POWER": ac_power,
    "AMBIENT_TEMPERATURE": ambient_temp,
    "MODULE_TEMPERATURE": module_temp,
    "IRRADIATION": irradiation,
    "HOUR": hour,
    "DAY": day
}

# === Predict ===
try:
    input_df = pd.DataFrame([input_data])[feature_names]
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
except Exception as e:
    st.error(f"⚠️ Prediction failed: {e}")
    st.stop()

# === Display Prediction ===
st.markdown("## 🔮 Predicted Output")
st.metric("DAILY_YIELD (kWh)", f"{prediction:,.2f}")

with st.expander("📋 Full Input Details"):
    st.write(f"**City:** {city}")
    st.write(f"**Ambient Temp:** {ambient_temp} °C, **Feels Like:** {feels_like} °C")
    st.write(f"**Manual Irradiation:** {irradiation:.2f} W/m²")
    st.dataframe(pd.DataFrame([input_data]).T.rename(columns={0: "Value"}), use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>🔐 Secure | ✅ Robust | ⚡ Built by Costas</p>", unsafe_allow_html=True)
