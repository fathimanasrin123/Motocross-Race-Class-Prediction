
import streamlit as st
import joblib

# Load the trained machine learning model
model = joblib.load("motocross_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Motocross Engine Class Prediction",
    page_icon="🏁",
    layout="centered"
)

# Application heading
st.title("🏁 Motocross Engine Class Prediction")

st.write(
    "Enter your motocross bike model to predict its engine capacity class."
)

st.info("Currently supported classes: 125cc, 250cc and 450cc.")

# Input field
bike_name = st.text_input(
    "Enter Bike Model",
    placeholder="Example: Honda CRF250R"
)

# Prediction button
if st.button("Predict Engine Class"):

    if bike_name.strip():

        prediction = model.predict([bike_name.strip()])[0]

        st.success("Prediction Completed!")

        st.subheader("Predicted Engine Capacity")
        st.header(f"🏍️ {prediction}")

    else:
        st.warning("Please enter a bike model.")

st.divider()

st.caption("Machine Learning Project | Motocross Race Class Prediction")

st.caption(
    "Educational prototype. Verify engine capacity using manufacturer specifications."
)
