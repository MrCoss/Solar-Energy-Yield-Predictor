🔆 Solar Energy Yield Predictor

A **Streamlit-powered machine learning app** that estimates daily solar energy output based on environmental inputs and power ratings.

![Streamlit UI](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)  
**Author:** Costas Pinto | [@MrCoss](https://github.com/MrCoss)

---

## ⚡ Overview

This project uses a pre-trained machine learning model to predict solar energy yield. Users can input weather data manually (like temperature and irradiation), and the model provides an estimated daily yield in **kWh**.

---

## 🛠 Features

- 📍 Input location (city)
- 🌡️ Manual input for ambient/module temperature
- ☀️ Irradiation control (W/m²)
- ⏰ Date & time selection
- 🤖 ML-based prediction (using trained `.pkl` model)
- 📊 Detailed input display
- ✅ Fully offline mode — no API needed

---

## 📦 Requirements

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

## 🚀 How to Run

```bash
streamlit run app.py
```

---

## 🧠 Model Info

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

## 📁 Folder Structure

```
Solar-Energy-Yield-Predictor/
├── app.py
├── model/
│   ├── model_daily_yield.pkl
│   ├── scaler_daily_yield.pkl
│   └── feature_names.pkl
├── .gitignore
└── README.md
```

---

## 🔐 Notes

* This version uses **manual weather input**.
* Optional integration with OpenWeatherMap can be added using `.env` and API key.

---

## 🙌 Acknowledgements

* Built using [Streamlit](https://streamlit.io/)
* Machine learning powered by [scikit-learn](https://scikit-learn.org/)

---

> *“Solar energy is bound to be in our future. We just need to make it easier to predict.”*

