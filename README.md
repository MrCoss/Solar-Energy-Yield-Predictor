# 🔆 Solar Energy Yield Predictor

[](https://shields.io/)
[](https://www.python.org/)
[](https://streamlit.io/)
[](https://scikit-learn.org/)

An interactive machine learning application built with **Streamlit** to forecast the daily energy yield of a solar power plant. The app uses a pre-trained regression model to provide accurate estimates based on environmental and time-based inputs.

**Author:** Costas Pinto | **GitHub:** [@MrCoss](https://github.com/MrCoss)

-----

## Table of Contents

  - [1. Project Rationale & Business Value](https://www.google.com/search?q=%231-project-rationale--business-value)
  - [2. The Prediction Pipeline: How It Works](https://www.google.com/search?q=%232-the-prediction-pipeline-how-it-works)
  - [3. Core Features & Functionality](https://www.google.com/search?q=%233-core-features--functionality)
  - [4. Machine Learning Model & Features](https://www.google.com/search?q=%234-machine-learning-model--features)
  - [5. Project Structure Explained](https://www.google.com/search?q=%235-project-structure-explained)
  - [6. Technical Stack](https://www.google.com/search?q=%236-technical-stack)
  - [7. Local Setup & Usage Guide](https://www.google.com/search?q=%237-local-setup--usage-guide)
  - [8. Acknowledgements](https://www.google.com/search?q=%238-acknowledgements)

-----

## 1\. Project Rationale & Business Value

As the world transitions to renewable energy, accurate forecasting of solar power generation is becoming increasingly critical. Reliable predictions help grid operators maintain stability, enable energy traders to make informed decisions, and allow plant operators to optimize maintenance schedules.

This project aims to demonstrate how machine learning can be applied to solve this real-world problem. By building an accessible and interactive tool, it demystifies the process of energy forecasting and serves as a practical example of deploying a trained model as a web application.

-----

## 2\. The Prediction Pipeline: How It Works

The application uses a pre-trained model and a simple, efficient workflow to deliver predictions in real-time.

### Step 1: User Input Collection

  - The user interacts with the **Streamlit** interface to provide key input parameters, including location, date, time, ambient temperature, module temperature, and solar irradiation (W/m²).

### Step 2: Feature Engineering

  - The application processes the raw inputs to create a feature vector that matches the format the model was trained on.
  - It derives time-based features like **Day of the Year** and **Hour of the Day** from the user's date/time selection, which are crucial for capturing daily and seasonal patterns.

### Step 3: Data Scaling

  - The engineered feature vector is then transformed using a pre-fitted **`StandardScaler`** object (`scaler_daily_yield.pkl`).
  - This step is essential because it normalizes the input data to the same scale as the data used to train the model, ensuring accurate predictions.

### Step 4: Prediction

  - The scaled feature vector is passed to the pre-trained regression model (`model_daily_yield.pkl`).
  - The model's `.predict()` method is called to compute the estimated daily energy yield in kilowatt-hours (kWh).

### Step 5: Displaying Results

  - The final predicted yield is presented to the user in a clear, easy-to-understand format within the Streamlit app.

-----

## 3\. Core Features & Functionality

  - **Interactive Controls:** Users can adjust sliders and input fields for temperature and irradiation to see the immediate impact on the predicted energy yield.
  - **Time-Aware Predictions:** The model incorporates the day of the year and the hour of the day, allowing it to account for seasonal and diurnal variations in solar energy generation.
  - **Fully Offline Operation:** The primary mode of the app relies on manual inputs, meaning it can be run anywhere without requiring an internet connection or external API keys.
  - **Modular and Saved Model:** The application loads a pre-trained model, scaler, and feature list, demonstrating a key MLOps principle of separating model training from inference.
  - **Extensible Design:** The codebase is designed to optionally integrate with the OpenWeatherMap API for fetching live weather data (requires a `.env` file with an API key).

-----

## 4\. Machine Learning Model & Features

The predictive power of the app comes from a regression model trained on a historical dataset of solar power generation.

  - **Model Type:** A regression algorithm (e.g., RandomForestRegressor, GradientBoostingRegressor) saved as `model_daily_yield.pkl`.
  - **Key Features Used:** The model was trained on a set of highly relevant features:
      - `AMBIENT_TEMPERATURE`: Air temperature affects panel efficiency.
      - `MODULE_TEMPERATURE`: The temperature of the solar panels themselves.
      - `IRRADIATION`: The amount of solar radiation hitting the panels, the most critical factor for power generation.
      - `DAY` & `HOUR`: Temporal features to capture daily and seasonal cycles.
      - `DC_POWER` & `AC_POWER`: Historical power generation data used during training.
  - **Persistence:** The model, scaler, and feature names are saved using `joblib`, allowing for quick loading and consistent predictions.

-----

## 5\. Project Structure Explained

```
.
├── app.py                      # Main Streamlit application script.
├── model/
│   ├── model_daily_yield.pkl   # The serialized, pre-trained ML model.
│   ├── scaler_daily_yield.pkl  # The saved StandardScaler object.
│   └── feature_names.pkl       # A list of feature names in the correct order for the model.
├── requirements.txt            # A list of all Python dependencies.
├── .env.example                # Example file for optional API key integration.
└── README.md                   # This detailed project documentation.
```

-----

## 6\. Technical Stack

  - **Core Language:** Python
  - **Web Framework:** Streamlit
  - **Machine Learning:** Scikit-learn
  - **Data Manipulation:** Pandas
  - **Model Persistence:** Joblib
  - **Environment Variables:** python-dotenv (for optional API integration)

-----

## 7\. Local Setup & Usage Guide

To run this application on your local machine, please follow these steps.

### Step 1: Clone the Repository

```bash
git clone https://github.com/MrCoss/solar-energy-predictor.git
cd solar-energy-predictor
```

### Step 2: Create and Activate a Virtual Environment (Recommended)

```bash
# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

Your web browser will automatically open with the running application.

-----

## 8\. Acknowledgements

  - This application was built using the powerful and easy-to-use **Streamlit** framework.
  - The machine learning model was developed with the robust and comprehensive **Scikit-learn** library.

This project uses a pre-trained machine learning model to predict solar energy yield. Users can input weather data manually (like temperature and irradiation), and the model provides an estimated daily yield in **kWh**.

---

## Features

- Input location (city)
- Manual input for ambient/module temperature
- Irradiation control (W/m²)
- Date & time selection
- ML-based prediction (using trained `.pkl` model)
- Detailed input display
- Fully offline mode — no API needed

---

## Requirements

Install dependencies via pip:

```bash
pip install -r requirements.txt
````

**Requirements include:**

* streamlit
* pandas
* scikit-learn
* joblib
* python-dotenv (optional, if using API)

---

## How to Run

```bash
streamlit run app.py
```

---

## Model Info

* Trained with features like:

  * DC\_POWER, AC\_POWER
  * AMBIENT\_TEMPERATURE
  * MODULE\_TEMPERATURE
  * IRRADIATION
  * DAY of year
  * HOUR of day

* Model: `model/model_daily_yield.pkl`

* Scaler: `model/scaler_daily_yield.pkl`

* Feature list: `model/feature_names.pkl`

---

## Notes

* This version uses **manual weather input**.
* Optional integration with OpenWeatherMap can be added using `.env` and API key.

## ScreenShots
![image](https://github.com/user-attachments/assets/d9227bef-a1f4-42eb-b239-363bc80938a0)




---

## Acknowledgements

* Built using [Streamlit](https://streamlit.io/)
* Machine learning powered by [scikit-learn](https://scikit-learn.org/)

---

> *“Solar energy is bound to be in our future. We just need to make it easier to predict.”*

