import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('sonar_model.pkl')

st.title("Rock vs Mine Prediction")

st.write("Enter 60 features (comma separated):")
user_input = st.text_area("Input Data", "")

if st.button("Predict"):
    try:
        # Convert input string to a numpy array
        input_data = np.array([float(x) for x in user_input.split(",") if x.strip() != ""])
        if input_data.shape[0] != 60:
            st.error("Please enter exactly 60 values.")
        else:
            input_data_reshaped = input_data.reshape(1, -1)
            prediction = model.predict(input_data_reshaped)
            if prediction[0] == 'R':
                st.success("The object is a Rock")
            else:
                st.success("The object is a Mine")
    except Exception as e:
        st.error(f"Invalid input: {e}")