import joblib
import streamlit as st
import pandas as pd

model = joblib.load('/home/hgidea/Desktop/Coding/Python/hackthon/intel/best_random_forest_model (2).pkl')

# Function to determine AQI category based on AQI value
def get_aqi_category(aqi_value):
    if aqi_value >= 0 and aqi_value <= 50:
        return "Good (Green)"
    elif aqi_value <= 100:
        return "Moderate (Yellow)"
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive Groups (Orange)"
    elif aqi_value <= 200:
        return "Unhealthy (Red)"
    elif aqi_value <= 300:
        return "Very Unhealthy (Purple)"
    else:
        return "Hazardous (Maroon)"

st.title("Air Quality Prediction App")

st.write("Enter values for the following pollutants (in the same units as your training data):")
pm25 = st.number_input("PM2.5 (μg/m³)", min_value=0.0)
ozone = st.number_input("Ozone (ppb)", min_value=0.0)
co = st.number_input("CO (ppm)", min_value=0.0)
no2 = st.number_input("NO2 (ppb)", min_value=0.0)

# You might want to adjust these dummy values based on the actual range of your encoded labels
default_aqi_category = 0
default_co_aqi_category = 0
default_ozone_aqi_category = 0
default_no2_aqi_category = 0
default_pm25_aqi_category = 0

# Prepare user input as a DataFrame with all features
user_data = pd.DataFrame({'PM2.5 AQI Value': [pm25],
                          'Ozone AQI Value': [ozone],
                          'CO AQI Value': [co],
                          'NO2 AQI Value': [no2],
                          'AQI Category': [default_aqi_category],
                          'CO AQI Category': [default_co_aqi_category],
                          'Ozone AQI Category': [default_ozone_aqi_category],
                          'NO2 AQI Category': [default_no2_aqi_category],
                          'PM2.5 AQI Category': [default_pm25_aqi_category]})

# Predict AQI using the model
predicted_aqi = model.predict(user_data)[0]

# Get the AQI category
predicted_aqi_category = get_aqi_category(predicted_aqi)

# Display predicted AQI and AQI category
st.write(f"Predicted AQI: {predicted_aqi}")
st.write(f"AQI Category: {predicted_aqi_category}")
