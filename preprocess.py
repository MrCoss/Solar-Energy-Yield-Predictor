# preprocess_plant1.py

import pandas as pd
import os

# Paths
gen_path = os.path.join("datasets", "Plant_1_Generation_Data.csv")
weather_path = os.path.join("datasets", "Plant_1_Weather_Sensor_Data.csv")

print("🔍 Loading generation and weather data...")

# Load and parse date
gen = pd.read_csv(gen_path)
gen['DATE_TIME'] = pd.to_datetime(gen['DATE_TIME'], format='%d-%m-%Y %H:%M', errors='coerce')

weather = pd.read_csv(weather_path)
weather['DATE_TIME'] = pd.to_datetime(weather['DATE_TIME'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Drop problematic SOURCE_KEY before merge (not joinable)
gen = gen.drop(columns=['SOURCE_KEY'], errors='ignore')
weather = weather.drop(columns=['SOURCE_KEY'], errors='ignore')

# Merge on DATE_TIME and PLANT_ID
merged = pd.merge(gen, weather, on=['DATE_TIME', 'PLANT_ID'], how='inner')

print(f"✅ Merged rows: {merged.shape[0]}")

# Filter out rows with missing or zero DC_POWER
merged = merged[merged['DC_POWER'] > 0]

# Save preprocessed CSV
output_path = "preprocessed_plant1.csv"
merged.to_csv(output_path, index=False)

print(f"💾 Preprocessed data saved to {output_path} → Shape: {merged.shape}")
# Display first few rows
print("📊 Sample data:")