import streamlit as st
import joblib
import pandas as pd

model = joblib.load("laptop_price_model.pkl")

st.title("Laptop Price Prediction")

Company = st.number_input("Company")
Product = st.number_input("Product")
TypeName = st.number_input("TypeName")
Inches = st.number_input("Inches")
ScreenResolution = st.number_input("ScreenResolution")
Cpu = st.number_input("Cpu")
Ram = st.number_input("Ram")
Memory = st.number_input("Memory")
Gpu = st.number_input("Gpu")
OpSys = st.number_input("Operating System")
Weight = st.number_input("Weight")

if st.button("Predict"):

    input_data = pd.DataFrame([[Company, Product, TypeName, Inches,
                                ScreenResolution, Cpu, Ram, Memory,
                                Gpu, OpSys, Weight]],
                              columns=['Company','Product','TypeName','Inches',
                                       'ScreenResolution','Cpu','Ram','Memory',
                                       'Gpu','OpSys','Weight'])

    prediction = model.predict(input_data)

    st.success(f"Predicted Laptop Price: €{prediction[0]:.2f}")
