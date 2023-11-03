import streamlit as st
import pickle
import pandas as pd

st.markdown("<h1 style='text-align: center;'>House Price Prediction</h1>", unsafe_allow_html=True)

# Center the input features under the title using HTML and CSS
st.markdown(
    """
    <style>
    .input-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create input fields for user input in a centered container
with st.container() as input_container:
    st.header('Input Features')
    age = st.number_input("Age")
    bmi = st.number_input("BMI")
    glucose = st.number_input("Glucose")
    insulin = st.number_input("Insulin")
    homa = st.number_input("HOMA")
    leptin = st.number_input("Leptin")
    adiponectin = st.number_input("Adiponectin")
    resistin = st.number_input("Resistin")
    mcp1 = st.number_input("MCP.1")

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

# Center the prediction under the input features using HTML and CSS
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Predict"):
    # Make the prediction
    predicted_class = model.predict(input_data)[0]
    st.write(f"Prediction: {predicted_class}")
st.markdown("</div>", unsafe_allow_html=True)
