
import streamlit as st
from modules.model import load_model
import numpy as np

st.title("🏦 Loan Eligibility Checker")

model = load_model("models/loan_model.pkl")

gender = st.selectbox("Gender", ["Male", "Female"])
income = st.number_input("Applicant Income", 0, 100000, 5000)

if st.button("Check Eligibility"):
    input_data = np.array([[1 if gender == "Male" else 0, income]])
    prediction = model.predict(input_data)
    result = "Eligible" if prediction[0] == 1 else "Not Eligible"
    st.success(f"Loan Status: {result}")
