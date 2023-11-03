import streamlit as st
import pickle
import pandas as pd

st.title("Classification")

# Create input fields for user input
#st.sidebar.title('Input Features')
age = st.sidebar.number_input("Age")
bmi = st.sidebar.number_input("BMI")
glucose = st.sidebar.number_input("Glucose")
insulin = st.sidebar.number_input("Insulin")
homa = st.sidebar.number_input("HOMA")
leptin = st.sidebar.number_input("Leptin")
adiponectin = st.sidebar.number_input("Adiponectin")
resistin = st.sidebar.number_input("Resistin")
mcp1 = st.sidebar.number_input("MCP.1")

# Load your pre-trained classification model using pickle
with open('Classification_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a DataFrame with the input data
input_data = pd.DataFrame({
    'Age': [age],
    'BMI': [bmi],
    'Glucose': [glucose],
    'Insulin': [insulin],
    'HOMA': [homa],
    'Leptin': [leptin],
    'Adiponectin': [adiponectin],
    'Resistin': [resistin],
    'MCP.1': [mcp1]
})

if st.sidebar.button("Predict"):
    # Make the prediction
    predicted_class = model.predict(input_data)[0]
    st.write(f"Prediction: {predicted_class}")
