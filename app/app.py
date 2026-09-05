import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Wellness Tourism Predictor", page_icon="✈️")
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "wellness_tourism_model.joblib"
model = joblib.load(MODEL_PATH)

st.title("✈️ Wellness Tourism Package Predictor")
st.write("Enter customer and interaction details to estimate purchase probability.")

with st.form("prediction_form"):
    age = st.number_input("Age", 18, 100, 35)
    type_contact = st.selectbox("Type of Contact", ["Company Invited", "Self Inquiry"])
    city_tier = st.selectbox("City Tier", [1, 2, 3], index=2)
    occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Large Business", "Free Lancer"])
    gender = st.selectbox("Gender", ["Male", "Female", "Fe Male"])
    people = st.number_input("Number of People Visiting", 1, 20, 2)
    property_star = st.number_input("Preferred Property Star", 1.0, 5.0, 3.0)
    marital = st.selectbox("Marital Status", ["Married", "Single", "Divorced", "Unmarried"])
    trips = st.number_input("Number of Trips", 0.0, 30.0, 3.0)
    passport = st.selectbox("Passport", [0, 1], format_func=lambda x: "Yes" if x else "No")
    own_car = st.selectbox("Own Car", [0, 1], format_func=lambda x: "Yes" if x else "No")
    children = st.number_input("Number of Children Visiting", 0.0, 10.0, 1.0)
    designation = st.selectbox("Designation", ["Manager", "Executive", "Senior Manager", "AVP", "VP"])
    income = st.number_input("Monthly Income", 0.0, 200000.0, 20000.0)
    pitch_score = st.number_input("Pitch Satisfaction Score", 1, 5, 3)
    product = st.selectbox("Product Pitched", ["Basic", "Deluxe", "Standard", "Super Deluxe", "King"])
    followups = st.number_input("Number of Followups", 0.0, 20.0, 3.0)
    duration = st.number_input("Duration of Pitch", 0.0, 200.0, 15.0)
    submitted = st.form_submit_button("Predict Purchase Probability")

if submitted:
    input_df = pd.DataFrame([{
        "Age": age, "TypeofContact": type_contact, "CityTier": city_tier,
        "Occupation": occupation, "Gender": gender, "NumberOfPersonVisiting": people,
        "PreferredPropertyStar": property_star, "MaritalStatus": marital,
        "NumberOfTrips": trips, "Passport": passport, "OwnCar": own_car,
        "NumberOfChildrenVisiting": children, "Designation": designation,
        "MonthlyIncome": income, "PitchSatisfactionScore": pitch_score,
        "ProductPitched": product, "NumberOfFollowups": followups,
        "DurationOfPitch": duration
    }])
    probability = float(model.predict_proba(input_df)[0, 1])
    prediction = int(probability >= 0.50)
    st.metric("Purchase probability", f"{probability:.1%}")
    if prediction:
        st.success("High-priority prospect: model predicts a likely purchase.")
    else:
        st.info("Lower-priority prospect: model predicts a less likely purchase.")
