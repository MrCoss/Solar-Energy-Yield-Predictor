import pandas as pd
import joblib
from datetime import datetime

# === Load saved model, scaler, and feature names ===
model = joblib.load("model/model_daily_yield.pkl")
scaler = joblib.load("model/scaler_daily_yield.pkl")
feature_names = joblib.load("model/feature_names.pkl")

# === Example datetime input ===
datetime_input = datetime(2025, 6, 26, 14, 30)  # June 26, 2025, 2:30 PM
hour = datetime_input.hour
day = datetime_input.timetuple().tm_yday

# === Input feature values (match the training order) ===
input_values = {
    "DC_POWER": 4700,                 # in watts
    "AC_POWER": 4500,                 # in watts
    "AMBIENT_TEMPERATURE": 32.0,     # in °C
    "MODULE_TEMPERATURE": 38.0,      # in °C
    "IRRADIATION": 800.0,            # in W/m²
    "HOUR": hour,
    "DAY": day
}

# === Convert to DataFrame with correct column order ===
input_df = pd.DataFrame([input_values])[feature_names]

# === Scale and Predict ===
input_scaled = scaler.transform(input_df)
prediction = model.predict(input_scaled)

# === Output ===
print("📍 Input values:")
for key, value in input_values.items():
    print(f"  {key}: {value}")

print(f"\n🔮 Predicted DAILY_YIELD: {prediction[0]:,.2f}")
