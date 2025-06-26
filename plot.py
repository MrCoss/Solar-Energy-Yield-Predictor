import streamlit as st

def main():
    st.set_page_config(page_title="Solar Energy Estimator", layout="centered")
    
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌞 Solar Energy Estimator</h1>", unsafe_allow_html=True)
    st.markdown("---")

    city = st.text_input("Enter city name", "Sample City")
    weather_desc = st.text_input("Enter weather description", "Clear sky")
    temp_c = st.number_input("Enter temperature (°C)", min_value=-50.0, max_value=60.0, value=25.0, step=0.1)

    if st.button("Submit"):
        st.success(f"Manual Weather for **{city}**:")
        st.write(f"**Description:** {weather_desc}")
        st.write(f"**Temperature:** {temp_c:.2f} °C")

        # Optional: Estimate solar energy logic here
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("Using manual weather data input.")

    else:
        st.info("Fill in the fields and click 'Submit'.")

if __name__ == "__main__":
    main()
