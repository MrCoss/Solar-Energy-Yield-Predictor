import os
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Load dataset
print("📊 Loading dataset...")
df = pd.read_csv("preprocessed_plant1.csv", parse_dates=["DATE_TIME"])
print(f"✅ Loaded data → Shape: {df.shape}")

# Drop leakage-prone columns
df = df.drop(columns=["PLANT_ID", "TOTAL_YIELD"], errors='ignore')

# Feature engineering: extract hour and day
df["HOUR"] = df["DATE_TIME"].dt.hour
df["DAY"] = df["DATE_TIME"].dt.dayofyear

# Drop original DATE_TIME
df = df.drop(columns=["DATE_TIME"])

# Define features and target
X = df.drop(columns=["DAILY_YIELD"])
y = df["DAILY_YIELD"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data (80% train, 20% test)
split_index = int(len(X_scaled) * 0.8)
X_train, X_test = X_scaled[:split_index], X_scaled[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)
test_mse = mean_squared_error(y_test, y_pred_test)

print(f"\n📈 Train R²: {train_r2:.4f}")
print(f"📉 Test R²: {test_r2:.4f}")
print(f"📉 Test MSE: {test_mse:,.2f}")

# TimeSeries cross-validation
tscv = TimeSeriesSplit(n_splits=5)
cv_scores = cross_val_score(model, X_scaled, y, cv=tscv, scoring='r2')
print(f"🔁 Avg TimeSeries CV R²: {cv_scores.mean():.4f}")

# Save feature names
feature_names = list(X.columns)
joblib.dump(feature_names, "model/feature_names.pkl")
print("✅ Feature names saved successfully!")
print("📋 Features used for training:")
for i, name in enumerate(feature_names, 1):
    print(f"  {i}. {name}")

# Save model and scaler
joblib.dump(model, "model/model_daily_yield.pkl")
joblib.dump(scaler, "model/scaler_daily_yield.pkl")
print("✅ Model and Scaler saved successfully in 'model/' folder!")
